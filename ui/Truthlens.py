import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st

st.set_page_config(
    page_title="TruthLens",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
div[data-testid="stSidebar"] { background: #080818; border-right: 1px solid rgba(255,255,255,0.05); }
div[data-testid="stSidebar"] * { color: rgba(255,255,255,0.6) !important; }
.stTextArea textarea { background: #0a0a1a !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 14px !important; color: #f1f5f9 !important; font-size: 15px !important; line-height: 1.7 !important; }
.stTextArea textarea:focus { border-color: rgba(124,58,237,0.5) !important; box-shadow: 0 0 0 3px rgba(124,58,237,0.1) !important; }
.stButton > button[kind="primary"] { background: linear-gradient(135deg,#7c3aed,#4f46e5) !important; border: none !important; border-radius: 12px !important; font-weight: 700 !important; font-size: 15px !important; padding: 14px 28px !important; letter-spacing: 0.3px !important; transition: all 0.2s !important; }
.stButton > button[kind="primary"]:hover { transform: translateY(-1px) !important; box-shadow: 0 8px 24px rgba(124,58,237,0.4) !important; }
.hero { background: linear-gradient(135deg, #080818 0%, #0f0c29 30%, #1a0533 60%, #0a1628 100%); border-radius: 28px; padding: 80px 48px 72px; text-align: center; margin-bottom: 48px; position: relative; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); }
.hero::before { content: ""; position: absolute; top: -100px; right: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(124,58,237,0.2) 0%, transparent 65%); border-radius: 50%; }
.hero::after { content: ""; position: absolute; bottom: -120px; left: -80px; width: 450px; height: 450px; background: radial-gradient(circle, rgba(14,165,233,0.12) 0%, transparent 65%); border-radius: 50%; }
.hero-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(124,58,237,0.15); border: 1px solid rgba(124,58,237,0.35); color: #c4b5fd; font-size: 11px; font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; padding: 7px 20px; border-radius: 100px; margin-bottom: 32px; }
.hero-badge::before { content: "●"; color: #a78bfa; font-size: 8px; }
.hero h1 { font-size: 58px; font-weight: 900; color: #ffffff; line-height: 1.1; margin: 0 0 20px; letter-spacing: -1.5px; }
.hero h1 span { background: linear-gradient(90deg, #a78bfa 0%, #60a5fa 50%, #34d399 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero p { font-size: 18px; color: rgba(255,255,255,0.55); max-width: 520px; margin: 0 auto 0; line-height: 1.75; }
.stats-strip { display: grid; grid-template-columns: repeat(3,1fr); gap: 14px; margin-bottom: 40px; }
.stat-pill { background: #0f0f1f; border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 22px 20px; text-align: center; }
.stat-pill .sp-num { font-size: 34px; font-weight: 800; margin-bottom: 4px; }
.stat-pill .sp-desc { font-size: 12px; color: rgba(255,255,255,0.4); line-height: 1.5; }
.stat-pill .sp-src { font-size: 10px; color: rgba(255,255,255,0.2); margin-top: 4px; letter-spacing: 0.5px; }
.sp-red .sp-num { color: #f87171; }
.sp-purple .sp-num { color: #c4b5fd; }
.sp-amber .sp-num { color: #fcd34d; }
.checker-wrap { background: #0d0d1f; border: 1px solid rgba(255,255,255,0.07); border-radius: 24px; padding: 44px 48px; max-width: 820px; margin: 0 auto 16px; box-shadow: 0 32px 80px rgba(0,0,0,0.5); }
.checker-wrap h2 { font-size: 22px; font-weight: 800; color: #f1f5f9; margin: 0 0 6px; }
.checker-wrap .sub { font-size: 13px; color: rgba(255,255,255,0.35); margin-bottom: 20px; }
.tech-strip { display: flex; align-items: center; justify-content: center; gap: 8px; flex-wrap: wrap; max-width: 820px; margin: 0 auto 56px; }
.tech-pill { display: inline-flex; align-items: center; gap: 6px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); border-radius: 100px; padding: 5px 14px; font-size: 11px; color: rgba(255,255,255,0.35); font-weight: 600; }
.tech-pill .tp-dot { width: 6px; height: 6px; border-radius: 50%; }
.verdict-banner { border-radius: 20px; padding: 32px 36px; margin-bottom: 16px; border: 1px solid; }
.vb-low { background: linear-gradient(135deg, rgba(22,163,74,0.1), rgba(21,128,61,0.05)); border-color: rgba(34,197,94,0.25); }
.vb-medium { background: linear-gradient(135deg, rgba(217,119,6,0.1), rgba(180,83,9,0.05)); border-color: rgba(245,158,11,0.25); }
.vb-high { background: linear-gradient(135deg, rgba(220,38,38,0.1), rgba(185,28,28,0.05)); border-color: rgba(239,68,68,0.25); }
.vb-inner { display: flex; align-items: center; gap: 28px; flex-wrap: wrap; }
.score-ring { width: 80px; height: 80px; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; }
.sr-low { background: conic-gradient(#22c55e, #16a34a, #22c55e); box-shadow: 0 0 24px rgba(34,197,94,0.3); }
.sr-medium { background: conic-gradient(#f59e0b, #d97706, #f59e0b); box-shadow: 0 0 24px rgba(245,158,11,0.3); }
.sr-high { background: conic-gradient(#ef4444, #dc2626, #ef4444); box-shadow: 0 0 24px rgba(239,68,68,0.3); }
.score-ring .ring-num { font-size: 28px; font-weight: 900; color: white; line-height: 1; }
.score-ring .ring-sub { font-size: 9px; color: rgba(255,255,255,0.6); letter-spacing: 0.5px; }
.vb-text { flex: 1; min-width: 200px; }
.vb-risk-label { font-size: 22px; font-weight: 800; color: #f1f5f9; margin-bottom: 8px; }
.vb-reasoning { font-size: 14px; color: rgba(255,255,255,0.6); line-height: 1.7; }
.results-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 14px; margin-bottom: 40px; }
.rg-card { background: #0d0d1f; border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; padding: 24px 22px; }
.rg-card h4 { font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,0.3); margin: 0 0 14px; }
.tag { display: inline-block; padding: 4px 12px; border-radius: 100px; font-size: 12px; font-weight: 600; margin: 3px 3px 3px 0; }
.tag-red    { background: rgba(239,68,68,0.12);  color: #fca5a5; border: 1px solid rgba(239,68,68,0.25); }
.tag-blue   { background: rgba(56,189,248,0.1);  color: #7dd3fc; border: 1px solid rgba(56,189,248,0.2); }
.tag-purple { background: rgba(167,139,250,0.1); color: #c4b5fd; border: 1px solid rgba(167,139,250,0.2); }
.tag-green  { background: rgba(34,197,94,0.1);   color: #86efac; border: 1px solid rgba(34,197,94,0.2); }
.tag-amber  { background: rgba(251,191,36,0.1);  color: #fcd34d; border: 1px solid rgba(251,191,36,0.2); }
.sentiment-big { display: flex; align-items: center; gap: 12px; }
.sent-icon { font-size: 36px; }
.sent-label { font-size: 20px; font-weight: 800; }
.sent-conf { font-size: 12px; color: rgba(255,255,255,0.35); margin-top: 2px; }
.ent-row { margin-bottom: 8px; font-size: 13px; color: rgba(255,255,255,0.35); }
.ent-row span { margin-right: 4px; }
.how-section { margin: 0 0 16px; }
.how-title { text-align: center; margin-bottom: 32px; }
.how-title h2 { font-size: 30px; font-weight: 800; color: #f1f5f9; margin: 0 0 8px; }
.how-title p { font-size: 14px; color: rgba(255,255,255,0.4); margin: 0; }
.how-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; }
.how-card { background: #0d0d1f; border: 1px solid rgba(255,255,255,0.07); border-radius: 20px; padding: 32px 28px; position: relative; overflow: hidden; }
.how-card::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px; }
.how-card.hc1::before { background: linear-gradient(90deg,#7c3aed,#a78bfa); }
.how-card.hc2::before { background: linear-gradient(90deg,#0ea5e9,#38bdf8); }
.how-card.hc3::before { background: linear-gradient(90deg,#16a34a,#4ade80); }
.how-card .hc-num { font-size: 11px; font-weight: 800; letter-spacing: 2px; color: rgba(255,255,255,0.2); text-transform: uppercase; margin-bottom: 14px; }
.how-card .hc-icon { font-size: 36px; margin-bottom: 14px; }
.how-card h3 { font-size: 17px; font-weight: 800; color: #f1f5f9; margin: 0 0 10px; }
.how-card p { font-size: 13px; color: rgba(255,255,255,0.45); line-height: 1.7; margin: 0; }
.how-card .hc-lib { display: inline-block; margin-top: 14px; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 100px; }
.hc1 .hc-lib { background: rgba(124,58,237,0.15); color: #c4b5fd; border: 1px solid rgba(124,58,237,0.25); }
.hc2 .hc-lib { background: rgba(14,165,233,0.12); color: #7dd3fc; border: 1px solid rgba(14,165,233,0.2); }
.hc3 .hc-lib { background: rgba(22,163,74,0.12);  color: #86efac; border: 1px solid rgba(22,163,74,0.2); }
</style>
""", unsafe_allow_html=True)

# ── HERO
st.markdown('<div class="hero"><div class="hero-badge">AI-Powered Fact Checker</div><h1>Is this Instagram post<br><span>real or fake?</span></h1><p>Paste any political caption or post below. Our three-stage NLP pipeline analyses it for misinformation signals, credibility, and red flags — in seconds.</p></div>', unsafe_allow_html=True)

# ── STATS STRIP
st.markdown('<div class="stats-strip"><div class="stat-pill sp-red"><div class="sp-num">72%</div><div class="sp-desc">of people globally see online misinformation as a major threat</div><div class="sp-src">Pew Research · 2025</div></div><div class="stat-pill sp-purple"><div class="sp-num">2%</div><div class="sp-desc">of misleading Instagram posts ever receive a fact-check label</div><div class="sp-src">Statista · 2025</div></div><div class="stat-pill sp-amber"><div class="sp-num">42.8%</div><div class="sp-desc">of news sharers admit to spreading false information unknowingly</div><div class="sp-src">University of Derby · 2024</div></div></div>', unsafe_allow_html=True)

# ── CHECKER CARD (wrapper opened, Streamlit widgets inside, wrapper closed)
st.markdown('<div class="checker-wrap"><h2>Paste the post content</h2><div class="sub">Works best with Instagram captions, political headlines, or short statements</div></div>', unsafe_allow_html=True)

# Native Streamlit widgets (must be outside HTML)
post_text = st.text_area(
    label="post_input",
    label_visibility="collapsed",
    placeholder='e.g. "BREAKING: Government secretly approved vaccine mandates for ALL citizens starting next month. Share before they delete this! 🚨"',
    height=150,
    key="post_input",
)
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    analyze_btn = st.button("🔍  Analyse Post", use_container_width=True, type="primary")

# ── TECH PILLS
st.markdown('<div class="tech-strip"><span class="tech-pill"><span class="tp-dot" style="background:#a78bfa"></span>spaCy NER</span><span class="tech-pill"><span class="tp-dot" style="background:#38bdf8"></span>RoBERTa Sentiment</span><span class="tech-pill"><span class="tp-dot" style="background:#4ade80"></span>Llama 3.3 70B</span><span class="tech-pill"><span class="tp-dot" style="background:#fb923c"></span>Groq API</span></div>', unsafe_allow_html=True)

# ── RESULTS
if analyze_btn:
    if not post_text.strip():
        st.warning("Please paste some text before analysing.")
    else:
        with st.spinner("Running NER · Sentiment · LLM credibility scoring…"):
            try:
                from utils.pipeline import analyze
                result = analyze(post_text)
                ner       = result["ner"]
                sentiment = result["sentiment"]
                llm       = result["llm"]

                risk        = (llm.get("misinfo_risk") or "medium").lower()
                score       = llm.get("credibility_score", "?")
                risk_label  = {"low": "Low Risk of Misinformation", "medium": "Medium Risk of Misinformation", "high": "High Risk of Misinformation"}.get(risk, "Unknown Risk")
                ring_class  = {"low": "sr-low", "medium": "sr-medium", "high": "sr-high"}.get(risk, "sr-medium")
                banner_class = f"vb-{risk}"
                sent_icon   = {"Positive": "😊", "Neutral": "😐", "Negative": "😠"}.get(sentiment["label"], "😐")
                sent_color  = {"Positive": "#86efac", "Neutral": "#cbd5e1", "Negative": "#fca5a5"}.get(sentiment["label"], "#cbd5e1")

                # verdict banner
                flags      = llm.get("red_flags", [])
                flags_html = " ".join(f'<span class="tag tag-red">{f}</span>' for f in flags) if flags else '<span class="tag tag-green">No red flags detected</span>'

                st.markdown(f'<div class="verdict-banner {banner_class}"><div class="vb-inner"><div class="score-ring {ring_class}"><div class="ring-num">{score}</div><div class="ring-sub">/ 10</div></div><div class="vb-text"><div class="vb-risk-label">{risk_label}</div><div class="vb-reasoning">{llm.get("reasoning", "")}</div></div></div></div>', unsafe_allow_html=True)

                # 3-col breakdown
                persons_html  = " ".join(f'<span class="tag tag-purple">{p}</span>' for p in ner["persons"]) if ner["persons"] else ""
                orgs_html     = " ".join(f'<span class="tag tag-blue">{o}</span>'   for o in ner["orgs"])    if ner["orgs"]    else ""
                locs_html     = " ".join(f'<span class="tag tag-green">{l}</span>'  for l in ner["locations"]) if ner["locations"] else ""
                groups_html   = " ".join(f'<span class="tag tag-red">{g}</span>'   for g in ner["groups"])   if ner["groups"]   else ""
                no_ents       = '<span style="font-size:13px;color:rgba(255,255,255,0.25);">None detected</span>'
                ents_block    = ""
                if persons_html: ents_block += f'<div class="ent-row"><span style="color:rgba(255,255,255,0.2);font-size:11px;text-transform:uppercase;letter-spacing:1px;">People</span><br>{persons_html}</div>'
                if orgs_html:    ents_block += f'<div class="ent-row"><span style="color:rgba(255,255,255,0.2);font-size:11px;text-transform:uppercase;letter-spacing:1px;">Orgs</span><br>{orgs_html}</div>'
                if locs_html:    ents_block += f'<div class="ent-row"><span style="color:rgba(255,255,255,0.2);font-size:11px;text-transform:uppercase;letter-spacing:1px;">Places</span><br>{locs_html}</div>'
                if groups_html:  ents_block += f'<div class="ent-row"><span style="color:rgba(255,255,255,0.2);font-size:11px;text-transform:uppercase;letter-spacing:1px;">Groups</span><br>{groups_html}</div>'
                if not ents_block: ents_block = no_ents

                st.markdown(f'<div class="results-grid"><div class="rg-card"><h4>🚩 Red Flags</h4>{flags_html}</div><div class="rg-card"><h4>🎭 Sentiment</h4><div class="sentiment-big"><div class="sent-icon">{sent_icon}</div><div><div class="sent-label" style="color:{sent_color}">{sentiment["label"]}</div><div class="sent-conf">Confidence: {sentiment["score"]:.0%}</div></div></div></div><div class="rg-card"><h4>🏷️ Named Entities</h4>{ents_block}</div></div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Analysis failed: {e}")

# ── HOW IT WORKS
st.markdown('<div class="how-section"><div class="how-title"><h2>How TruthLens works</h2><p>Three NLP stages run in sequence on every piece of content you submit.</p></div><div class="how-grid"><div class="how-card hc1"><div class="hc-num">Stage 01</div><div class="hc-icon">🏷️</div><h3>Named Entity Recognition</h3><p>spaCy scans the original text and extracts every person, organisation, location, event, and political group — signals of politically loaded content.</p><span class="hc-lib">spaCy · en_core_web_sm</span></div><div class="how-card hc2"><div class="hc-num">Stage 02</div><div class="hc-icon">🎭</div><h3>Sentiment Analysis</h3><p>A RoBERTa model fine-tuned on 124M tweets classifies the emotional tone as Positive, Neutral, or Negative with a precise confidence score.</p><span class="hc-lib">cardiffnlp · RoBERTa</span></div><div class="how-card hc3"><div class="hc-num">Stage 03</div><div class="hc-icon">🤖</div><h3>LLM Credibility Scoring</h3><p>Llama 3.3 70B receives the text plus NLP metadata and returns a 0–10 credibility score, risk level, specific red flags, and a plain-English verdict.</p><span class="hc-lib">Llama 3.3 70B · Groq</span></div></div></div>', unsafe_allow_html=True)
