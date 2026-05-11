import streamlit as st

st.set_page_config(page_title="How We Identify · TruthLens", page_icon="🔬", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.page-header { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); border-radius: 20px; padding: 56px 48px 48px; margin-bottom: 48px; position: relative; overflow: hidden; }
.page-header::before { content: ""; position: absolute; top: -60px; right: -60px; width: 280px; height: 280px; background: radial-gradient(circle, rgba(56,189,248,0.18) 0%, transparent 70%); border-radius: 50%; }
.page-header .badge { display: inline-block; background: rgba(56,189,248,0.15); border: 1px solid rgba(56,189,248,0.35); color: #7dd3fc; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; padding: 5px 16px; border-radius: 100px; margin-bottom: 20px; }
.page-header h1 { color:#fff; font-size:40px; font-weight:800; margin:0 0 14px; line-height:1.2; }
.page-header h1 span { background: linear-gradient(90deg,#a78bfa,#38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.page-header p { color:rgba(255,255,255,0.58); font-size:16px; max-width:620px; line-height:1.8; margin:0; }
.pipeline-flow { display: flex; align-items: center; justify-content: center; gap: 0; margin: 0 0 52px; flex-wrap: wrap; }
.flow-node { background: #1a1a2e; border: 1px solid rgba(255,255,255,0.09); border-radius: 14px; padding: 18px 26px; text-align: center; min-width: 150px; }
.flow-node .fn-icon { font-size: 28px; margin-bottom: 6px; }
.flow-node .fn-label { font-size: 13px; font-weight: 700; color: #f1f5f9; }
.flow-node .fn-sub { font-size: 11px; color: rgba(255,255,255,0.35); margin-top: 2px; }
.flow-arrow { font-size: 22px; color: rgba(255,255,255,0.2); margin: 0 6px; flex-shrink: 0; }
.flow-node.active-1 { border-color: rgba(167,139,250,0.5); box-shadow: 0 0 24px rgba(124,58,237,0.2); }
.flow-node.active-2 { border-color: rgba(56,189,248,0.5); box-shadow: 0 0 24px rgba(56,189,248,0.15); }
.flow-node.active-3 { border-color: rgba(34,197,94,0.5); box-shadow: 0 0 24px rgba(34,197,94,0.15); }
.step-header { display: flex; align-items: center; gap: 20px; margin-bottom: 16px; }
.step-badge { display: flex; flex-direction: column; align-items: center; justify-content: center; width: 64px; height: 64px; border-radius: 18px; font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; flex-shrink: 0; }
.step-badge.s1 { background: linear-gradient(135deg,#4c1d95,#7c3aed); color:#e9d5ff; }
.step-badge.s2 { background: linear-gradient(135deg,#0c4a6e,#0ea5e9); color:#bae6fd; }
.step-badge.s3 { background: linear-gradient(135deg,#14532d,#16a34a); color:#bbf7d0; }
.step-badge .sn { font-size: 22px; font-weight: 800; line-height: 1; }
.step-badge .sl { font-size: 9px; letter-spacing: 1.5px; margin-top: 2px; opacity: 0.8; }
.step-meta h2 { color:#f1f5f9; font-size:22px; font-weight:800; margin:0 0 4px; }
.step-lib { display: inline-block; font-size: 12px; font-weight: 600; color: #a78bfa; background: rgba(124,58,237,0.12); border: 1px solid rgba(124,58,237,0.25); padding: 2px 10px; border-radius: 100px; margin-right: 6px; }
.step-lib.blue { color:#7dd3fc; background:rgba(56,189,248,0.1); border-color:rgba(56,189,248,0.2); }
.step-lib.green { color:#86efac; background:rgba(34,197,94,0.1); border-color:rgba(34,197,94,0.2); }
.step-body { background: #1a1a2e; border: 1px solid rgba(255,255,255,0.07); border-radius: 18px; padding: 32px 36px; color: rgba(255,255,255,0.65); font-size: 14.5px; line-height: 1.85; margin-bottom: 8px; }
.step-body strong { color: #e2e8f0; }
.step-body p { margin: 0 0 14px; }
.why-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; padding: 18px 22px; margin-top: 20px; font-size: 13.5px; color: rgba(255,255,255,0.5); }
.why-box strong { color: rgba(255,255,255,0.75); font-size: 12px; letter-spacing: 1px; text-transform: uppercase; }
.entity-grid { display: grid; grid-template-columns: repeat(5,1fr); gap: 10px; margin-top: 20px; }
.entity-chip { border-radius: 12px; padding: 14px 10px; text-align: center; }
.entity-chip .ec-label { font-size: 13px; font-weight: 800; margin-bottom: 4px; }
.entity-chip .ec-desc { font-size: 10px; color: rgba(255,255,255,0.4); margin-bottom: 6px; line-height:1.4; }
.entity-chip .ec-ex { font-size: 11px; font-style: italic; }
.ec-person { background:rgba(167,139,250,0.1); border:1px solid rgba(167,139,250,0.25); }
.ec-person .ec-label { color:#c4b5fd; } .ec-person .ec-ex { color:#a78bfa; }
.ec-org { background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.2); }
.ec-org .ec-label { color:#7dd3fc; } .ec-org .ec-ex { color:#38bdf8; }
.ec-gpe { background:rgba(34,197,94,0.08); border:1px solid rgba(34,197,94,0.2); }
.ec-gpe .ec-label { color:#86efac; } .ec-gpe .ec-ex { color:#4ade80; }
.ec-event { background:rgba(251,191,36,0.08); border:1px solid rgba(251,191,36,0.2); }
.ec-event .ec-label { color:#fcd34d; } .ec-event .ec-ex { color:#fbbf24; }
.ec-norp { background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.2); }
.ec-norp .ec-label { color:#fca5a5; } .ec-norp .ec-ex { color:#f87171; }
.sentiment-row { display: grid; grid-template-columns: repeat(3,1fr); gap: 12px; margin-top: 20px; }
.sentiment-pill { border-radius: 14px; padding: 18px 16px; text-align: center; }
.sentiment-pill .sp-icon { font-size: 28px; margin-bottom: 8px; }
.sentiment-pill .sp-label { font-size: 14px; font-weight: 800; margin-bottom: 4px; }
.sentiment-pill .sp-desc { font-size: 12px; color: rgba(255,255,255,0.4); line-height:1.4; }
.sp-pos { background:rgba(34,197,94,0.1); border:1px solid rgba(34,197,94,0.25); }
.sp-pos .sp-label { color:#86efac; }
.sp-neu { background:rgba(148,163,184,0.1); border:1px solid rgba(148,163,184,0.2); }
.sp-neu .sp-label { color:#cbd5e1; }
.sp-neg { background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.25); }
.sp-neg .sp-label { color:#fca5a5; }
.json-box { background: #0d1117; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 24px 28px; margin-top: 20px; font-family: 'Courier New', monospace; font-size: 13.5px; line-height: 1.8; }
.jk { color: #a78bfa; } .jn { color: #fcd34d; } .js { color: #86efac; } .jl { color: #f87171; } .jp { color: rgba(255,255,255,0.25); }
.score-guide { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-top: 20px; }
.sg-card { border-radius: 12px; padding: 16px 14px; text-align: center; }
.sg-card .sg-range { font-size: 22px; font-weight: 800; margin-bottom: 4px; }
.sg-card .sg-label { font-size: 11px; color: rgba(255,255,255,0.45); line-height:1.4; }
.sg-10 { background:rgba(34,197,94,0.1); border:1px solid rgba(34,197,94,0.2); } .sg-10 .sg-range { color:#86efac; }
.sg-7 { background:rgba(251,191,36,0.08); border:1px solid rgba(251,191,36,0.2); } .sg-7 .sg-range { color:#fcd34d; }
.sg-4 { background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.2); } .sg-4 .sg-range { color:#fdba74; }
.sg-1 { background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.2); } .sg-1 .sg-range { color:#fca5a5; }
.connector { display: flex; align-items: center; justify-content: center; margin: 4px 0; color: rgba(255,255,255,0.15); font-size: 13px; letter-spacing: 1px; gap: 10px; }
.connector::before, .connector::after { content: ""; flex: 1; height: 1px; background: rgba(255,255,255,0.06); }
</style>
""", unsafe_allow_html=True)

# ── HERO
st.markdown('<div class="page-header"><div class="badge">🔬 Under the Hood</div><h1>Three stages. One <span>verdict.</span></h1><p>Every post you submit travels through a sequential NLP pipeline — Named Entity Recognition, Sentiment Analysis, and LLM Credibility Scoring. Here is exactly how each stage works and why the combination is more powerful than any single technique alone.</p></div>', unsafe_allow_html=True)

# ── PIPELINE FLOW
st.markdown('<div class="pipeline-flow"><div class="flow-node active-1"><div class="fn-icon">🏷️</div><div class="fn-label">NER</div><div class="fn-sub">spaCy · en_core_web_sm</div></div><div class="flow-arrow">→</div><div class="flow-node active-2"><div class="fn-icon">🎭</div><div class="fn-label">Sentiment</div><div class="fn-sub">RoBERTa · Cardiff NLP</div></div><div class="flow-arrow">→</div><div class="flow-node active-3"><div class="fn-icon">🤖</div><div class="fn-label">LLM Scoring</div><div class="fn-sub">Llama 3.3 70B · Groq</div></div><div class="flow-arrow">→</div><div class="flow-node"><div class="fn-icon">✅</div><div class="fn-label">Verdict</div><div class="fn-sub">score · risk · flags</div></div></div>', unsafe_allow_html=True)

# ── STEP 1 HEADER
st.markdown('<div class="step-header"><div class="step-badge s1"><div class="sn">01</div><div class="sl">Stage</div></div><div class="step-meta"><h2>Named Entity Recognition</h2><span class="step-lib">spaCy</span><span class="step-lib">en_core_web_sm</span></div></div>', unsafe_allow_html=True)

# ── STEP 1 BODY
st.markdown('<div class="step-body"><p>Before any opinion is formed about a post\'s truthfulness, we need to know <strong>who and what it is talking about</strong>. NER is a sequence-labelling technique that scans every word and assigns it a semantic category — person, organisation, location, event, or political group.</p><p>We run NER on the <strong>original, uncleaned text</strong> — capitalisation preserved — because spaCy relies on casing to distinguish <em>trump</em> (a verb) from <em>Trump</em> (a person). The model processes up to 1,000 characters and deduplicates repeated mentions automatically.</p><div class="entity-grid"><div class="entity-chip ec-person"><div class="ec-label">PERSON</div><div class="ec-desc">Politicians &amp; public figures</div><div class="ec-ex">Joe Biden</div></div><div class="entity-chip ec-org"><div class="ec-label">ORG</div><div class="ec-desc">Parties, media, institutions</div><div class="ec-ex">NATO · FBI · CNN</div></div><div class="entity-chip ec-gpe"><div class="ec-label">GPE</div><div class="ec-desc">Countries, cities, states</div><div class="ec-ex">Russia · Washington</div></div><div class="entity-chip ec-event"><div class="ec-label">EVENT</div><div class="ec-desc">Named historical events</div><div class="ec-ex">2026 Election</div></div><div class="entity-chip ec-norp"><div class="ec-label">NORP</div><div class="ec-desc">Nationalities &amp; pol. groups</div><div class="ec-ex">Republican · Democrat</div></div></div><div class="why-box"><strong>Why it matters</strong><br>Misinformation posts tend to pack in a high density of named political figures and institutions to manufacture an air of authority — often citing people who never said what is attributed to them. High entity counts combined with low source credibility is one of the strongest signals the LLM uses.</div></div>', unsafe_allow_html=True)

st.markdown('<div class="connector">feeds into</div>', unsafe_allow_html=True)

# ── STEP 2 HEADER
st.markdown('<div class="step-header"><div class="step-badge s2"><div class="sn">02</div><div class="sl">Stage</div></div><div class="step-meta"><h2>Sentiment Analysis</h2><span class="step-lib blue">RoBERTa</span><span class="step-lib blue">cardiffnlp/twitter-roberta-base-sentiment-latest</span></div></div>', unsafe_allow_html=True)

# ── STEP 2 BODY
st.markdown('<div class="step-body"><p>Misinformation is engineered to make you feel something — outrage, fear, urgency — because <strong>emotion is what drives shares</strong>. Our second stage measures exactly that: the emotional polarity of the text, and how confident the model is in its reading.</p><p>We use a <strong>RoBERTa model fine-tuned on 124 million tweets</strong>, published by Cardiff NLP. It was chosen specifically because Instagram captions share the same short, punchy, often punctuation-free register as social media text — the same domain the model was trained on. The input is capped at 512 tokens to match the model\'s context window.</p><div class="sentiment-row"><div class="sentiment-pill sp-pos"><div class="sp-icon">😊</div><div class="sp-label">Positive</div><div class="sp-desc">Uplifting, celebratory, or optimistic framing. Low standalone risk.</div></div><div class="sentiment-pill sp-neu"><div class="sp-icon">😐</div><div class="sp-label">Neutral</div><div class="sp-desc">Factual, measured tone. Often found in credible reporting.</div></div><div class="sentiment-pill sp-neg"><div class="sp-icon">😠</div><div class="sp-label">Negative</div><div class="sp-desc">Fear, anger, outrage. Strongest correlate of misinformation spread.</div></div></div><div class="why-box"><strong>Why it matters</strong><br>Both the label and the confidence score are passed to the LLM in stage 3. A post that is <em>Negative at 95% confidence</em> is treated very differently from one that is <em>Negative at 52%</em>. The model uses this gradient — not just the category — when assessing risk.</div></div>', unsafe_allow_html=True)

st.markdown('<div class="connector">feeds into</div>', unsafe_allow_html=True)

# ── STEP 3 HEADER
st.markdown('<div class="step-header"><div class="step-badge s3"><div class="sn">03</div><div class="sl">Stage</div></div><div class="step-meta"><h2>LLM Credibility Scoring</h2><span class="step-lib green">Llama 3.3 70B</span><span class="step-lib green">Groq API</span></div></div>', unsafe_allow_html=True)

# ── STEP 3 BODY
st.markdown('<div class="step-body"><p>The final stage synthesises everything. <strong>Llama 3.3 70B</strong> — a 70-billion parameter instruction-tuned model — receives the original text <em>plus</em> the structured NLP metadata from stages 1 and 2 in a single prompt. It reasons over all of it and returns a structured JSON verdict.</p><p>Sending the NLP metadata alongside the raw text is the key design decision here. The LLM does not just read the post — it reads the post <em>knowing</em> how many entities were detected, what the sentiment confidence was, and which political groups were mentioned. This grounds its reasoning in measurable signals rather than intuition alone.</p><div class="json-box"><span class="jp">{</span><br>&nbsp;&nbsp;<span class="jk">"credibility_score"</span><span class="jp">:</span> <span class="jn">3</span><span class="jp">,</span><br>&nbsp;&nbsp;<span class="jk">"misinformation_risk"</span><span class="jp">:</span> <span class="js">"high"</span><span class="jp">,</span><br>&nbsp;&nbsp;<span class="jk">"red_flags"</span><span class="jp">: [</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="jl">"no primary source cited"</span><span class="jp">,</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="jl">"emotionally charged language"</span><span class="jp">,</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="jl">"unverified statistic"</span><br>&nbsp;&nbsp;<span class="jp">],</span><br>&nbsp;&nbsp;<span class="jk">"reasoning"</span><span class="jp">:</span> <span class="js">"The post uses alarming language with no attributed source and cites a figure not found in any official record."</span><br><span class="jp">}</span></div><div class="score-guide"><div class="sg-card sg-10"><div class="sg-range">8 – 10</div><div class="sg-label">Factual, verifiable, balanced reporting</div></div><div class="sg-card sg-7"><div class="sg-range">5 – 7</div><div class="sg-label">Mostly accurate but one-sided or missing sources</div></div><div class="sg-card sg-4"><div class="sg-range">2 – 4</div><div class="sg-label">Misleading framing or unverified claims</div></div><div class="sg-card sg-1"><div class="sg-range">0 – 1</div><div class="sg-label">Fabricated quotes or clear misinformation</div></div></div><div class="why-box"><strong>Why it matters</strong><br>Rules-based fact-checking breaks on language variation and novel narratives. A large language model generalises — it can reason about implication, tone, and missing context the way a human fact-checker would, at a speed and scale no human team can match.</div></div>', unsafe_allow_html=True)
