import os
import json
import re
import spacy
from groq import Groq
from transformers import pipeline as hf_pipeline
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

_nlp = None
_sentiment_pipe = None
_groq_client = None

SENTIMENT_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
LLM_MODEL = "llama-3.3-70b-versatile"
ENTITY_TYPES = {"PERSON", "ORG", "GPE", "EVENT", "NORP"}

SYSTEM_PROMPT = """\
You are a fact-checking assistant specialising in political misinformation in social media and news.
You receive a post/article snippet and NLP metadata, and assess its credibility.

Respond ONLY with a valid JSON object — no markdown fences, no preamble — in this schema:
{
  "credibility_score": <integer 0-10>,
  "misinformation_risk": <"low" | "medium" | "high">,
  "red_flags": [<string>, ...],
  "reasoning": <one concise sentence>
}

Scoring guide:
8-10 → Factual, verifiable, balanced reporting
5-7  → Mostly accurate but missing sources, slightly exaggerated, or one-sided
2-4  → Misleading framing, unverified claims, cherry-picked data
0-1  → Fabricated quotes, conspiracy rhetoric, clear misinformation
"""


def _load_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp


def _load_sentiment():
    global _sentiment_pipe
    if _sentiment_pipe is None:
        _sentiment_pipe = hf_pipeline(
            task="sentiment-analysis",
            model=SENTIMENT_MODEL,
            tokenizer=SENTIMENT_MODEL,
            top_k=None,
            truncation=True,
            max_length=512,
        )
    return _sentiment_pipe


def _load_groq():
    global _groq_client
    if _groq_client is None:
        _groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    return _groq_client


def run_ner(text: str) -> dict:
    nlp = _load_nlp()
    doc = nlp(text[:1000])
    by_type = {t: [] for t in ENTITY_TYPES}
    for ent in doc.ents:
        if ent.label_ in ENTITY_TYPES:
            clean = ent.text.strip()
            if clean:
                by_type[ent.label_].append(clean)
    for k in by_type:
        by_type[k] = list(dict.fromkeys(by_type[k]))
    all_ents = [e for lst in by_type.values() for e in lst]
    return {
        "persons": by_type["PERSON"],
        "orgs": by_type["ORG"],
        "locations": by_type["GPE"],
        "events": by_type["EVENT"],
        "groups": by_type["NORP"],
        "all": all_ents,
        "count": len(all_ents),
    }


def run_sentiment(text: str) -> dict:
    pipe = _load_sentiment()
    results = pipe(text[:512])[0]
    scores = {r["label"]: round(r["score"], 4) for r in results}
    best = max(results, key=lambda x: x["score"])
    return {
        "label": best["label"],
        "score": round(best["score"], 4),
        "positive": scores.get("Positive", 0.0),
        "neutral": scores.get("Neutral", 0.0),
        "negative": scores.get("Negative", 0.0),
    }


def run_llm(text: str, ner: dict, sentiment: dict) -> dict:
    client = _load_groq()
    prompt = f"""\
TEXT    : {text[:800]}

NLP METADATA:
  Sentiment     : {sentiment['label']} (confidence {sentiment['score']})
  Persons       : {ner['persons'] or 'none detected'}
  Organisations : {ner['orgs'] or 'none detected'}
  Locations     : {ner['locations'] or 'none detected'}
  Pol. groups   : {ner['groups'] or 'none detected'}
  Total entities: {ner['count']}

Assess the credibility and misinformation risk of this content.
"""
    resp = client.chat.completions.create(
        model=LLM_MODEL,
        max_tokens=512,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    raw = resp.choices[0].message.content.strip()
    raw = re.sub(r"```json\s*", "", raw)
    raw = re.sub(r"```\s*", "", raw)
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        raw = match.group(0)
    parsed = json.loads(raw)
    return {
        "credibility_score": parsed.get("credibility_score"),
        "misinfo_risk": parsed.get("misinformation_risk"),
        "red_flags": parsed.get("red_flags", []),
        "reasoning": parsed.get("reasoning", ""),
    }


def analyze(text: str) -> dict:
    ner = run_ner(text)
    sentiment = run_sentiment(text)
    llm = run_llm(text, ner, sentiment)
    return {"ner": ner, "sentiment": sentiment, "llm": llm}
