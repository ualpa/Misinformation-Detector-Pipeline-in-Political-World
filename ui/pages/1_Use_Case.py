import streamlit as st

st.set_page_config(page_title="Use Case · TruthLens", page_icon="📌", layout="wide")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  .page-header {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    border-radius: 20px;
    padding: 56px 48px 48px;
    margin-bottom: 48px;
    position: relative;
    overflow: hidden;
  }
  .page-header::before {
    content: "";
    position: absolute;
    top: -80px; right: -60px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(130,80,255,0.2) 0%, transparent 70%);
    border-radius: 50%;
  }
  .page-header .badge {
    display: inline-block;
    background: rgba(239,68,68,0.2);
    border: 1px solid rgba(239,68,68,0.4);
    color: #fca5a5;
    font-size: 11px; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
    padding: 5px 16px; border-radius: 100px;
    margin-bottom: 20px;
  }
  .page-header h1 { color:#fff; font-size:40px; font-weight:800; margin:0 0 14px; line-height:1.2; }
  .page-header p  { color:rgba(255,255,255,0.6); font-size:16px; max-width:640px; line-height:1.8; margin:0; }

  /* ── big stat grid ── */
  .stat-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 40px;
  }
  .stat-card {
    background: #1a1a2e;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 28px 22px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .stat-card::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
  }
  .stat-card.red::after   { background: linear-gradient(90deg,#ef4444,#f97316); }
  .stat-card.purple::after{ background: linear-gradient(90deg,#7c3aed,#a78bfa); }
  .stat-card.blue::after  { background: linear-gradient(90deg,#0ea5e9,#38bdf8); }
  .stat-card.amber::after { background: linear-gradient(90deg,#f59e0b,#fbbf24); }

  .stat-number {
    font-size: 44px; font-weight: 800; line-height: 1;
    margin-bottom: 8px;
  }
  .stat-card.red    .stat-number { color: #f87171; }
  .stat-card.purple .stat-number { color: #c4b5fd; }
  .stat-card.blue   .stat-number { color: #7dd3fc; }
  .stat-card.amber  .stat-number { color: #fcd34d; }

  .stat-label {
    font-size: 13px; color: rgba(255,255,255,0.55);
    line-height: 1.5; margin-bottom: 6px;
  }
  .stat-source {
    font-size: 10px; color: rgba(255,255,255,0.25);
    letter-spacing: 0.5px; text-transform: uppercase;
  }

  /* ── section title ── */
  .section-title {
    font-size: 24px; font-weight: 800; color: #f1f5f9;
    margin: 48px 0 20px;
    display: flex; align-items: center; gap: 12px;
  }
  .section-title span {
    width: 4px; height: 28px;
    background: linear-gradient(180deg,#7c3aed,#38bdf8);
    border-radius: 4px; display: inline-block;
  }

  /* ── narrative cards ── */
  .narrative-card {
    background: #1a1a2e;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 32px 36px;
    margin-bottom: 16px;
    color: rgba(255,255,255,0.65);
    font-size: 15px;
    line-height: 1.85;
  }
  .narrative-card h3 {
    color: #f1f5f9; font-size: 18px; font-weight: 700;
    margin: 0 0 14px;
    display: flex; align-items: center; gap: 10px;
  }
  .narrative-card strong { color: #e2e8f0; }
  .narrative-card .highlight {
    background: rgba(124,58,237,0.12);
    border-left: 3px solid #7c3aed;
    border-radius: 0 8px 8px 0;
    padding: 14px 20px;
    margin: 18px 0 0;
    font-size: 14px;
    color: rgba(255,255,255,0.7);
    font-style: italic;
  }

  /* ── quote block ── */
  .quote-block {
    background: linear-gradient(135deg, rgba(124,58,237,0.1), rgba(56,189,248,0.08));
    border: 1px solid rgba(124,58,237,0.25);
    border-radius: 16px;
    padding: 32px 36px;
    margin: 16px 0;
    position: relative;
  }
  .quote-block::before {
    content: '"';
    font-size: 80px; font-weight: 800;
    color: rgba(124,58,237,0.3);
    position: absolute; top: -10px; left: 24px;
    line-height: 1;
  }
  .quote-block p {
    font-size: 16px; color: rgba(255,255,255,0.75);
    line-height: 1.8; margin: 0 0 12px; padding-top: 28px;
    font-style: italic;
  }
  .quote-block .attribution {
    font-size: 12px; color: rgba(255,255,255,0.35);
    letter-spacing: 0.5px; text-transform: uppercase; font-style: normal;
  }

  /* ── two-col ── */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }

  /* ── instagram spotlight ── */
  .ig-spotlight {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid rgba(225,48,108,0.3);
    border-radius: 16px;
    padding: 36px;
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
  }
  .ig-spotlight::before {
    content: "";
    position: absolute; top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(225,48,108,0.15) 0%, transparent 70%);
    border-radius: 50%;
  }
  .ig-spotlight h3 { color:#f1f5f9; font-size:20px; font-weight:700; margin:0 0 14px; }
  .ig-spotlight p  { color:rgba(255,255,255,0.6); font-size:14px; line-height:1.8; margin:0 0 10px; }
  .ig-big-stat {
    font-size: 56px; font-weight: 800;
    background: linear-gradient(90deg,#f472b6,#e1306c);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1; margin: 16px 0 6px;
  }

  /* ── call-to-action banner ── */
  .cta-banner {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 100%);
    border: 1px solid rgba(167,139,250,0.3);
    border-radius: 20px;
    padding: 44px 48px;
    text-align: center;
    margin-top: 48px;
  }
  .cta-banner h2 { color:#fff; font-size:28px; font-weight:800; margin:0 0 12px; }
  .cta-banner p  { color:rgba(255,255,255,0.55); font-size:15px; max-width:540px; margin:0 auto; line-height:1.7; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <div class="badge">⚠ Why This Matters</div>
  <h1>Political misinformation is<br>the defining threat of our era</h1>
  <p>
    Across 25 nations, billions of people are exposed daily to false political narratives online.
    The damage is measurable — to elections, to trust, to democracy itself.
    Here is what the data says.
  </p>
</div>
""", unsafe_allow_html=True)

# ── STAT GRID ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
  <div class="stat-card red">
    <div class="stat-number">72%</div>
    <div class="stat-label">of people across 25 nations consider online misinformation a <strong>major threat</strong></div>
    <div class="stat-source">Pew Research · 2025</div>
  </div>
  <div class="stat-card purple">
    <div class="stat-number">64%</div>
    <div class="stat-label">worry AI-generated content could directly <strong>influence elections</strong></div>
    <div class="stat-source">Statista · 2025</div>
  </div>
  <div class="stat-card blue">
    <div class="stat-number">42.8%</div>
    <div class="stat-label">of news sharers admit to <strong>spreading false information</strong> at least once</div>
    <div class="stat-source">University of Derby · 2024</div>
  </div>
  <div class="stat-card amber">
    <div class="stat-number">2%</div>
    <div class="stat-label">of misleading posts on Instagram & Facebook received any <strong>fact-check label</strong></div>
    <div class="stat-source">Statista · 2025</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — THE SCALE ─────────────────────────────────────────────────────
st.markdown('<div class="section-title"><span></span>The Scale of the Problem</div>', unsafe_allow_html=True)

st.markdown("""
<div class="narrative-card">
  <h3>🌍 A global crisis with no borders</h3>
  <p>
    In the spring of 2025, Pew Research surveyed adults across 25 countries spanning five continents.
    The finding was unambiguous: <strong>24 out of 25 nations</strong> had clear majorities who viewed
    false information online as a <strong>major threat</strong> — not a minor annoyance, not a distant problem,
    but an active danger to their society.
  </p>
  <p>
    Concern is also accelerating. In Poland, the share of adults calling it a major threat rose by
    <strong>20 percentage points</strong> between 2022 and 2025. Sweden saw a <strong>+10 point</strong> rise,
    France and Germany each <strong>+6 points</strong>. The trend is not levelling off — it is intensifying.
  </p>
  <div class="highlight">
    "72% median across 25 nations view false information online as a major threat to their country."
    — Pew Research Global, August 2025
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="two-col">
  <div class="narrative-card">
    <h3>📉 Trust is collapsing</h3>
    <p>
      Only <strong>38% of people</strong> trust most news most of the time — a figure that fell
      4 percentage points in a single year. Less than half trust even the news sources they
      personally choose to follow. Meanwhile, <strong>42% of the global population</strong> ranks
      social media as the <em>least trusted</em> news source worldwide — and yet it remains
      where most people encounter political content daily.
    </p>
  </div>
  <div class="narrative-card">
    <h3>📲 45% see it every single day</h3>
    <p>
      Nearly half of UK adults report encountering fake news <strong>every day</strong>.
      During the COVID-19 crisis, the UK government alone identified <strong>up to 70 incidents
      weekly</strong> of false narratives actively spreading online. The volume is too high for
      any human moderation system — or for the average reader — to keep up with.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — WHY IT SPREADS ────────────────────────────────────────────────
st.markdown('<div class="section-title"><span></span>Why It Spreads So Fast</div>', unsafe_allow_html=True)

st.markdown("""
<div class="quote-block">
  <p>Nowadays everyone is an editor and everyone can publish news — especially on social media.</p>
  <div class="attribution">— Richard Bowyer, Senior Lecturer in Journalism, University of Derby</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-card">
  <h3>🔁 We are all unknowing amplifiers</h3>
  <p>
    The problem is not just bad actors creating misinformation — it is ordinary people spreading it.
    <strong>42.8% of news sharers</strong> admit they have knowingly or unknowingly shared inaccurate
    information. The most common motivation? Not malice — but a desire to <em>inform others</em> and
    <em>express their feelings</em>. Emotion drives engagement, and misinformation is engineered to provoke it.
  </p>
  <p>
    The term "fake news" itself exploded in use by <strong>365%</strong> between 2016 and 2017 —
    tracking almost exactly with the rise of politically weaponised social media. The Oxford English
    Dictionary formally added the term in 2019. What was once a fringe phenomenon became a defining
    feature of the information landscape.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-card">
  <h3>🤖 AI is making it dramatically worse</h3>
  <p>
    A new and accelerating threat has emerged: AI-generated content that is indistinguishable from
    real information. <strong>70% of adults</strong> now say they struggle to trust online information
    because they cannot tell what was made by a person and what was generated by a machine.
    <strong>60% of U.S. adults</strong> are specifically concerned about deepfake videos and audio
    being used to spread political lies. The barrier to creating convincing misinformation has dropped
    to near zero — while the barrier to detecting it has never been higher.
  </p>
  <div class="highlight">
    "64% of global participants worry AI-generated content could influence elections."
    — Statista, 2025
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 3 — INSTAGRAM SPOTLIGHT ──────────────────────────────────────────
st.markdown('<div class="section-title"><span></span>Why Instagram Is Ground Zero</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ig-spotlight">
  <h3>📸 The platform built for virality</h3>
  <p>
    Instagram's visual-first, share-first design makes it uniquely dangerous for political misinformation.
    A false claim embedded in an infographic, a screenshot, or a short video reaches millions before
    any fact-checker can respond. And the platforms themselves are not doing nearly enough.
  </p>
  <div class="ig-big-stat">2%</div>
  <p style="font-size:15px; color:rgba(255,255,255,0.75); margin-bottom:16px;">
    <strong>Only 2% of misleading posts on Facebook and Instagram received any fact-check label.</strong>
    That means <strong>98 out of every 100 false posts</strong> circulate completely unchecked.
  </p>
  <p>
    By contrast, on X (formerly Twitter), 99% of false extreme weather claims were at least debunked
    or labelled. YouTube applied <strong>zero</strong> fact-checking labels to misleading weather content.
    Moderation at scale is broken — and Instagram's political content sits in the widest gap.
  </p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — POLITICAL CONSEQUENCES ───────────────────────────────────────
st.markdown('<div class="section-title"><span></span>The Political Consequences</div>', unsafe_allow_html=True)

st.markdown("""
<div class="narrative-card">
  <h3>🗳️ Democracy at risk</h3>
  <p>
    Misinformation does not merely mislead — it <strong>polarises</strong>. Pew Research found that
    in Germany and the U.S., the gap in concern about misinformation between left-leaning and
    right-leaning populations is <strong>22 percentage points</strong> (82% vs. 60% in the U.S.).
    When people disagree not just on values but on basic facts, the common ground for democratic
    debate disappears.
  </p>
  <p>
    Supporters of right-wing populist parties show systematically lower concern about online
    misinformation — with a <strong>34-point gap</strong> between AfD supporters (55%) and
    non-supporters (89%) in Germany alone. This is not coincidence. Political actors have a direct
    interest in keeping populations unable to distinguish truth from fiction.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="two-col">
  <div class="narrative-card">
    <h3>⚡ Real-world violence</h3>
    <p>
      During the UK riots of July–August 2024, <strong>46% of British adults</strong> believed
      social media platforms handled misinformation poorly. False narratives about the identity and
      religion of a murder suspect spread unchecked, triggering real-world attacks on mosques
      and asylum seeker hotels. <strong>28 individuals</strong> were charged with online offences
      across England and Wales — a direct link between digital misinformation and physical harm.
    </p>
  </div>
  <div class="narrative-card">
    <h3>🧠 The psychological toll</h3>
    <p>
      Living in a misinformation-saturated environment has measurable psychological effects.
      <strong>82% of U.S. consumers</strong> are actively concerned about the spread of false
      information — a constant background anxiety about whether what they are reading is real.
      Dr William Van Gordon of the University of Derby recommends deliberate "perceptual distance"
      from news — a coping strategy that shouldn't be necessary in a functioning information ecosystem.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-banner">
  <h2>This is the problem TruthLens is built to solve</h2>
  <p>
    When 98% of misleading posts go unlabelled, when AI lowers the cost of fabrication to zero,
    and when half the population spreads false information without realising it —
    automated, accessible fact-checking is no longer a nice-to-have. It is a necessity.
  </p>
</div>
""", unsafe_allow_html=True)
