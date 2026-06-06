import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PlantNutri - Kalkulator Pupuk Sayuran",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI chrome
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --green-900: #1a3a22; --green-800: #1e4d2a; --green-700: #1a5c2a;
    --green-600: #2d8a45; --green-500: #3aab55; --green-400: #4caf50;
    --green-100: #e8f5e9; --green-50: #f0fdf4;
    --sidebar-w: 240px; --radius: 14px;
    --shadow: 0 2px 16px rgba(0,0,0,0.07);
    --shadow-md: 0 4px 24px rgba(0,0,0,0.10);
    --font: 'Plus Jakarta Sans', sans-serif;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; overflow: hidden; }
  body { font-family: var(--font); background: #f5f7f5; color: #1a2e1c; display: flex; }

  /* SIDEBAR */
  .sidebar {
    width: var(--sidebar-w); background: #fff;
    border-right: 1px solid #e6ede7;
    display: flex; flex-direction: column;
    height: 100vh; overflow-y: auto;
    box-shadow: 2px 0 12px rgba(0,0,0,0.04); flex-shrink: 0;
  }
  .sidebar-logo {
    display: flex; align-items: center; gap: 10px;
    padding: 20px 18px 16px; border-bottom: 1px solid #eef2ef;
  }
  .logo-icon {
    width: 38px; height: 38px; border-radius: 10px;
    background: linear-gradient(135deg, #1a5c2a, #4caf50);
    display: flex; align-items: center; justify-content: center; font-size: 17px;
  }
  .logo-text { font-size: 1.1rem; font-weight: 800; color: #1a2e1c; }
  .sidebar-collapse {
    margin-left: auto; background: #f0f4f0; border: none;
    border-radius: 8px; padding: 4px 8px; cursor: pointer; color: #7a9a7e;
  }
  .sidebar-section-label {
    font-size: 0.62rem; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: #9db8a0; padding: 16px 18px 6px;
  }
  .nav-item {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 16px; margin: 2px 10px;
    border-radius: 10px; cursor: pointer;
    font-size: 0.85rem; font-weight: 500; color: #5a7a5e;
    transition: all 0.15s; border: none; background: transparent;
    width: calc(100% - 20px); text-align: left; font-family: var(--font);
  }
  .nav-item:hover { background: var(--green-50); color: var(--green-700); }
  .nav-item.active { background: var(--green-100); color: var(--green-700); font-weight: 700; }
  .nav-icon { font-size: 0.95rem; width: 20px; text-align: center; }
  .sidebar-footer { margin-top: auto; padding: 14px 14px 16px; border-top: 1px solid #eef2ef; }
  .sidebar-footer-card {
    background: var(--green-50); border-radius: 10px;
    padding: 11px 13px; display: flex; align-items: center; gap: 9px;
  }
  .sidebar-footer-text { font-size: 0.73rem; color: var(--green-700); font-weight: 600; line-height: 1.4; }
  .sidebar-year { display: flex; align-items: center; gap: 7px; padding: 8px 16px 2px; font-size: 0.75rem; color: #9db8a0; }

  /* MAIN */
  .main { flex: 1; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }
  .topbar {
    background: #fff; border-bottom: 1px solid #e6ede7;
    padding: 12px 24px; display: flex; align-items: center;
    justify-content: flex-end; gap: 12px; flex-shrink: 0;
    box-shadow: 0 1px 6px rgba(0,0,0,0.04);
  }
  .topbar-bell { background: none; border: none; cursor: pointer; font-size: 1.1rem; color: #7a9a7e; padding: 5px; border-radius: 7px; }
  .topbar-bell:hover { background: var(--green-50); }
  .deploy-btn {
    background: var(--green-600); color: white; border: none;
    border-radius: 22px; padding: 7px 20px; font-size: 0.82rem;
    font-weight: 700; cursor: pointer; font-family: var(--font);
  }
  .deploy-btn:hover { background: var(--green-700); }
  .topbar-dots { background: none; border: none; cursor: pointer; font-size: 1.1rem; color: #7a9a7e; }
  .content { padding: 22px 28px; flex: 1; overflow-y: auto; }

  /* HERO */
  .hero-banner {
    background: linear-gradient(120deg, #1a3a22 0%, #1e5c30 45%, #2d8a45 100%);
    border-radius: var(--radius); padding: 32px 36px;
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 20px; position: relative; overflow: hidden; min-height: 175px;
  }
  .hero-left { z-index: 2; }
  .hero-icon-wrap {
    display: inline-flex; align-items: center; justify-content: center;
    width: 48px; height: 48px; border-radius: 13px;
    background: rgba(255,255,255,0.13); font-size: 1.5rem; margin-bottom: 10px;
    border: 1px solid rgba(255,255,255,0.18);
  }
  .hero-title { font-size: 2rem; font-weight: 800; letter-spacing: -0.02em; line-height: 1; margin-bottom: 8px; }
  .hero-title .white { color: white; }
  .hero-title .accent { color: #7ddb8a; }
  .hero-sub { color: rgba(255,255,255,0.82); font-size: 0.88rem; font-weight: 500; max-width: 360px; line-height: 1.5; }
  .hero-ref { display: flex; align-items: center; gap: 5px; margin-top: 9px; color: rgba(255,255,255,0.45); font-size: 0.72rem; }
  .hero-img-placeholder {
    position: absolute; right: 0; top: 0; bottom: 0; width: 280px;
    display: flex; align-items: center; justify-content: flex-end; padding-right: 28px;
  }
  .hero-plant-emoji { font-size: 6rem; opacity: 0.22; }

  /* STATS */
  .stats-row { display: grid; grid-template-columns: repeat(3,1fr); gap: 14px; margin-bottom: 20px; }
  .stat-card {
    background: white; border-radius: var(--radius); padding: 18px 20px;
    box-shadow: var(--shadow); display: flex; align-items: center; gap: 14px; transition: box-shadow 0.2s;
  }
  .stat-card:hover { box-shadow: var(--shadow-md); }
  .stat-icon-wrap {
    width: 40px; height: 40px; border-radius: 11px; background: var(--green-50);
    display: flex; align-items: center; justify-content: center; font-size: 1.2rem; flex-shrink: 0;
  }
  .stat-value { font-size: 1.55rem; font-weight: 800; color: var(--green-700); line-height: 1; }
  .stat-label { font-size: 0.75rem; color: #7a9a7e; margin-top: 3px; font-weight: 500; }
  .stat-dots { margin-left: auto; opacity: 0.18; display: grid; grid-template-columns: repeat(4,5px); gap: 3px; }
  .stat-dots span { width: 4px; height: 4px; background: #4caf50; border-radius: 50%; display: block; }

  /* CARDS */
  .cards-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px; }
  .feature-card { background: white; border-radius: var(--radius); padding: 20px 22px; box-shadow: var(--shadow); position: relative; overflow: hidden; }
  .feature-card-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
  .feature-card-icon {
    width: 34px; height: 34px; border-radius: 9px;
    background: linear-gradient(135deg, #1a5c2a, #4caf50);
    display: flex; align-items: center; justify-content: center; font-size: 0.9rem; color: white;
  }
  .feature-card-title { font-size: 0.92rem; font-weight: 700; color: #1a2e1c; }
  .feature-list { list-style: none; display: flex; flex-direction: column; gap: 8px; }
  .feature-list li { display: flex; align-items: flex-start; gap: 8px; font-size: 0.8rem; color: #4a6a4e; line-height: 1.4; }
  .check-icon {
    width: 17px; height: 17px; border-radius: 50%; background: var(--green-100);
    color: var(--green-700); display: flex; align-items: center;
    justify-content: center; font-size: 0.58rem; flex-shrink: 0; margin-top: 1px;
  }
  .plant-tags { display: flex; flex-wrap: wrap; gap: 7px; }
  .plant-tag {
    display: flex; align-items: center; gap: 4px;
    background: #f3f7f3; border: 1px solid #d8e8d8;
    border-radius: 18px; padding: 4px 11px;
    font-size: 0.77rem; color: #3a6a3e; font-weight: 500;
  }
  .validated-row {
    display: flex; align-items: center; gap: 6px;
    margin-top: 12px; font-size: 0.75rem; color: #7a9a7e;
    border-top: 1px solid #eef2ef; padding-top: 11px;
  }
  .mini-chart { position: absolute; bottom: 10px; right: 14px; opacity: 0.12; pointer-events: none; }

  /* PAGES */
  .page { display: none; }
  .page.active { display: block; }
  .page-title { font-size: 1.1rem; font-weight: 800; margin-bottom: 18px; color: #1a2e1c; }

  /* FORM */
  .calc-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: 18px; }
  .jadwal-grid { display: grid; grid-template-columns: 1fr 1.6fr; gap: 18px; }
  .form-card { background: white; border-radius: var(--radius); padding: 22px; box-shadow: var(--shadow); }
  .form-card h3 { font-size: 0.92rem; font-weight: 700; margin-bottom: 16px; color: #1a2e1c; }
  .form-group { margin-bottom: 14px; }
  .form-label { display: block; font-size: 0.78rem; font-weight: 600; color: #4a6a4e; margin-bottom: 5px; }
  .form-select, .form-input {
    width: 100%; padding: 9px 13px; border-radius: 8px;
    border: 1.5px solid #d8e8d8; background: #f9fdf9;
    font-size: 0.84rem; font-family: var(--font); color: #1a2e1c; outline: none;
    transition: border-color 0.15s;
  }
  .form-select:focus, .form-input:focus { border-color: var(--green-500); }
  .calc-btn {
    width: 100%; padding: 11px; border-radius: 9px;
    background: linear-gradient(135deg, #1a5c2a, #2d8a45);
    color: white; border: none; font-size: 0.88rem; font-weight: 700;
    cursor: pointer; font-family: var(--font); margin-top: 4px;
  }
  .calc-btn:hover { opacity: 0.9; }
  .result-placeholder {
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; height: 100%; min-height: 240px;
    color: #b0cbb4; text-align: center;
  }
  .result-placeholder .big-emoji { font-size: 3rem; margin-bottom: 10px; }
  .result-box {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    border: 2px solid #86efac; border-radius: var(--radius); padding: 20px; display: none;
  }
  .result-box.show { display: block; }
  .result-title { font-size: 0.96rem; font-weight: 700; margin-bottom: 12px; color: var(--green-700); }
  .result-metrics { display: grid; grid-template-columns: repeat(3,1fr); gap: 9px; margin-bottom: 12px; }
  .result-metric { background: white; border-radius: 9px; padding: 9px; text-align: center; box-shadow: 0 1px 5px rgba(0,0,0,0.05); }
  .result-metric .val { font-size: 1.15rem; font-weight: 800; color: var(--green-700); }
  .result-metric .lbl { font-size: 0.68rem; color: #7a9a7e; margin-top: 2px; }
  .result-dose-card { background: white; border-radius: 9px; padding: 13px 15px; margin-bottom: 11px; }
  .result-dose-label { font-size: 0.76rem; font-weight: 700; color: #4a6a4e; margin-bottom: 3px; }
  .result-dose-value { font-size: 1.7rem; font-weight: 800; color: var(--green-700); line-height: 1; }
  .result-dose-sub { font-size: 0.7rem; color: #9db8a0; margin-top: 2px; }
  .warn-box { background: #fffbeb; border: 1px solid #fcd34d; border-radius: 8px; padding: 9px 13px; font-size: 0.78rem; color: #78590a; }

  /* SCHEDULE */
  .schedule-timeline { display: flex; flex-direction: column; gap: 0; }
  .schedule-step { display: flex; gap: 13px; padding: 0 0 16px 0; position: relative; }
  .schedule-step::before { content:''; position:absolute; left:14px; top:26px; bottom:0; width:2px; background:#d1e8d4; }
  .schedule-step:last-child::before { display: none; }
  .step-dot {
    width: 28px; height: 28px; border-radius: 50%; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center; font-size: 0.75rem; z-index: 1;
  }
  .step-dot.start { background: #dcfce7; color: var(--green-700); }
  .step-dot.mid { background: #bbf7d0; color: var(--green-700); }
  .step-dot.harvest { background: var(--green-600); color: white; }
  .step-week { font-size: 0.68rem; font-weight: 700; color: var(--green-600); text-transform: uppercase; letter-spacing: 0.05em; }
  .step-phase { font-size: 0.8rem; font-weight: 700; color: #1a2e1c; margin: 2px 0; }
  .step-desc { font-size: 0.76rem; color: #5a7a5e; line-height: 1.5; }
  .info-box-green { background: var(--green-50); border: 1px solid #bbf7d0; border-radius: 9px; padding: 12px 15px; font-size: 0.8rem; color: #2a5a2e; line-height: 1.6; }

  /* CHART */
  .chart-section { background: white; border-radius: var(--radius); padding: 20px; box-shadow: var(--shadow); margin-bottom: 16px; }
  .chart-title { font-size: 0.88rem; font-weight: 700; margin-bottom: 14px; color: #1a2e1c; }
  .bar-chart { display: flex; flex-direction: column; gap: 10px; }
  .bar-row { display: flex; align-items: center; gap: 11px; }
  .bar-label { font-size: 0.76rem; color: #4a6a4e; width: 110px; flex-shrink: 0; font-weight: 500; }
  .bar-wrap { flex: 1; background: #f0fdf4; border-radius: 5px; height: 26px; overflow: hidden; }
  .bar-fill {
    height: 100%; border-radius: 5px;
    background: linear-gradient(90deg, #2d8a45, #4caf50);
    display: flex; align-items: center; padding-left: 9px;
    font-size: 0.7rem; font-weight: 700; color: white;
    transition: width 0.8s cubic-bezier(0.4,0,0.2,1);
  }
  .tabs { display: flex; gap: 7px; margin-bottom: 16px; }
  .tab-btn {
    padding: 6px 16px; border-radius: 7px; border: 1.5px solid #d8e8d8;
    background: white; font-size: 0.8rem; font-weight: 600;
    cursor: pointer; color: #5a7a5e; font-family: var(--font); transition: all 0.15s;
  }
  .tab-btn.active { background: var(--green-700); color: white; border-color: var(--green-700); }
  .tab-content { display: none; }
  .tab-content.active { display: block; }
  .data-table { width: 100%; border-collapse: collapse; font-size: 0.8rem; }
  .data-table th { background: var(--green-50); color: var(--green-700); padding: 9px 13px; text-align: left; font-weight: 700; border-bottom: 2px solid #d1e8d4; }
  .data-table td { padding: 9px 13px; border-bottom: 1px solid #f0f4f0; color: #3a5a3e; }
  .data-table tr:last-child td { border-bottom: none; }
  .data-table tr:hover td { background: #f9fdf9; }

  /* ACCORDION */
  .accordion { display: flex; flex-direction: column; gap: 10px; }
  .acc-item { background: white; border-radius: var(--radius); box-shadow: var(--shadow); overflow: hidden; }
  .acc-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 18px; cursor: pointer; font-size: 0.88rem;
    font-weight: 700; color: #1a2e1c; user-select: none; transition: background 0.15s;
  }
  .acc-header:hover { background: var(--green-50); }
  .acc-arrow { transition: transform 0.22s; font-size: 0.75rem; color: var(--green-600); }
  .acc-item.open .acc-arrow { transform: rotate(180deg); }
  .acc-body { display: none; padding: 0 18px 16px; font-size: 0.81rem; color: #4a6a4e; line-height: 1.7; }
  .acc-item.open .acc-body { display: block; }
  .acc-body ul, .acc-body ol { padding-left: 17px; }
  .acc-body li { margin-bottom: 4px; }
  .acc-body blockquote {
    border-left: 3px solid var(--green-400); padding: 7px 13px;
    background: var(--green-50); border-radius: 0 7px 7px 0;
    font-style: italic; color: #3a6a3e; margin: 7px 0;
  }
</style>
</head>
<body>

<aside class="sidebar">
  <div class="sidebar-logo">
    <div class="logo-icon">🌱</div>
    <span class="logo-text">PlantNutri</span>
    <button class="sidebar-collapse">&#x276E;&#x276E;</button>
  </div>
  <div class="sidebar-section-label">Menu Navigasi</div>
  <button class="nav-item active" onclick="switchPage('beranda',this)"><span class="nav-icon">🏠</span> Beranda</button>
  <button class="nav-item" onclick="switchPage('kalkulator',this)"><span class="nav-icon">🧮</span> Kalkulator Pupuk</button>
  <button class="nav-item" onclick="switchPage('jadwal',this)"><span class="nav-icon">📅</span> Jadwal Pemupukan</button>
  <button class="nav-item" onclick="switchPage('perbandingan',this)"><span class="nav-icon">📊</span> Perbandingan Dosis</button>
  <button class="nav-item" onclick="switchPage('panduan',this)"><span class="nav-icon">📚</span> Panduan & Referensi</button>
  <div class="sidebar-footer">
    <div class="sidebar-footer-card">
      <span style="font-size:1.3rem">🌱</span>
      <span class="sidebar-footer-text">Nutrisi Tepat<br>Untuk Tanaman Sehat</span>
    </div>
    <div class="sidebar-year"><span>📅</span><span>2026</span></div>
  </div>
</aside>

<div class="main">
  <header class="topbar">
    <button class="topbar-bell">🔔</button>
    <button class="deploy-btn">Deploy</button>
    <button class="topbar-dots">⋮</button>
  </header>

  <div class="content">

    <!-- BERANDA -->
    <div class="page active" id="page-beranda">
      <div class="hero-banner">
        <div class="hero-left">
          <div class="hero-icon-wrap">🌱</div>
          <div class="hero-title"><span class="white">Plant</span><span class="accent">Nutri</span></div>
          <div class="hero-sub">Aplikasi Kalkulator Kebutuhan Pupuk Tanaman Sayuran Berbasis Pertanian Presisi</div>
          <div class="hero-ref">📖 Referensi: Wahyudi & Hasibuan (2024) — JPatin Vol.1 No.1</div>
        </div>
        <div class="hero-img-placeholder"><span class="hero-plant-emoji">🌿</span></div>
      </div>
      <div class="stats-row">
        <div class="stat-card">
          <div class="stat-icon-wrap">🌿</div>
          <div><div class="stat-value">8+</div><div class="stat-label">Jenis Tanaman Sayuran</div></div>
          <div class="stat-dots"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
        </div>
        <div class="stat-card">
          <div class="stat-icon-wrap">💰</div>
          <div><div class="stat-value">3</div><div class="stat-label">Jenis Pupuk Tersedia</div></div>
          <div class="stat-dots"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
        </div>
        <div class="stat-card">
          <div class="stat-icon-wrap">✅</div>
          <div><div class="stat-value">100%</div><div class="stat-label">Berbasis Jurnal Ilmiah</div></div>
          <div class="stat-dots"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
        </div>
      </div>
      <div class="cards-row">
        <div class="feature-card">
          <div class="feature-card-header">
            <div class="feature-card-icon">🎯</div>
            <span class="feature-card-title">Fitur Utama</span>
          </div>
          <ul class="feature-list">
            <li><div class="check-icon">✓</div> Kalkulator kebutuhan pupuk presisi</li>
            <li><div class="check-icon">✓</div> Rekomendasi dosis optimal</li>
            <li><div class="check-icon">✓</div> Jadwal pemupukan terencana</li>
            <li><div class="check-icon">✓</div> Perbandingan dosis pupuk</li>
          </ul>
          <svg class="mini-chart" width="110" height="65" viewBox="0 0 110 65">
            <rect x="8" y="38" width="13" height="27" fill="#4caf50" rx="3" opacity="0.5"/>
            <rect x="32" y="24" width="13" height="41" fill="#4caf50" rx="3" opacity="0.7"/>
            <rect x="56" y="12" width="13" height="53" fill="#4caf50" rx="3" opacity="0.9"/>
            <rect x="80" y="4" width="13" height="61" fill="#2d8a45" rx="3"/>
            <polyline points="0,58 22,42 46,28 70,15 95,5" fill="none" stroke="#4caf50" stroke-width="2.5"/>
          </svg>
        </div>
        <div class="feature-card">
          <div class="feature-card-header">
            <div class="feature-card-icon">🌿</div>
            <span class="feature-card-title">Tanaman yang Didukung</span>
          </div>
          <div class="plant-tags">
            <span class="plant-tag">🥬 Sawi</span>
            <span class="plant-tag">🌿 Kangkung</span>
            <span class="plant-tag">🥬 Bayam</span>
            <span class="plant-tag">🥗 Selada</span>
            <span class="plant-tag">🍅 Tomat</span>
            <span class="plant-tag">🌶️ Cabai</span>
            <span class="plant-tag">🥒 Mentimun</span>
            <span class="plant-tag">+ Lainnya</span>
          </div>
          <div class="validated-row">🛡️ Data berbasis penelitian & validasi lapangan</div>
        </div>
      </div>
    </div>

    <!-- KALKULATOR -->
    <div class="page" id="page-kalkulator">
      <div class="page-title">🧮 Kalkulator Kebutuhan Pupuk</div>
      <div class="calc-grid">
        <div class="form-card">
          <h3>📝 Input Data Lahan</h3>
          <div class="form-group">
            <label class="form-label">🌿 Pilih Jenis Tanaman</label>
            <select class="form-select" id="calc-tanaman">
              <option>Ketimun / Timun</option><option>Tomat</option><option>Cabai</option>
              <option>Bayam</option><option>Kangkung</option><option>Bawang Merah</option>
              <option>Terong</option><option>Wortel</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">📐 Luas Lahan (m²)</label>
            <input class="form-input" type="number" id="calc-luas" value="100" min="1" step="10">
          </div>
          <div class="form-group">
            <label class="form-label">🧪 Jenis Pupuk</label>
            <select class="form-select" id="calc-pupuk">
              <option>Pupuk Organik (Pupuk Kandang)</option>
              <option>Pupuk NPK (Anorganik)</option>
              <option>Semi Organik (Kandang + NPK)</option>
            </select>
          </div>
          <button class="calc-btn" onclick="hitungPupuk()">🔍 Hitung Kebutuhan Pupuk</button>
        </div>
        <div>
          <div class="result-placeholder" id="result-placeholder">
            <div class="big-emoji">🌿</div>
            <p style="font-size:0.85rem;">Isi form di kiri lalu klik<br><b>Hitung Kebutuhan Pupuk</b></p>
          </div>
          <div class="result-box" id="result-box">
            <div class="result-title" id="result-title"></div>
            <div class="result-metrics" id="result-metrics"></div>
            <div id="result-dose"></div>
            <div class="warn-box" id="result-warn"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- JADWAL -->
    <div class="page" id="page-jadwal">
      <div class="page-title">📅 Jadwal Pemupukan Otomatis</div>
      <div class="jadwal-grid">
        <div class="form-card">
          <h3>🌿 Pilih Tanaman</h3>
          <div class="form-group">
            <label class="form-label">Tanaman</label>
            <select class="form-select" id="jadwal-tanaman">
              <option>Ketimun / Timun</option><option>Tomat</option><option>Cabai</option>
              <option>Bayam</option><option>Kangkung</option><option>Bawang Merah</option>
              <option>Terong</option><option>Wortel</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">📆 Tanggal Tanam</label>
            <input class="form-input" type="date" id="jadwal-tgl">
          </div>
          <button class="calc-btn" onclick="tampilkanJadwal()">📅 Tampilkan Jadwal</button>
        </div>
        <div class="form-card" id="jadwal-result">
          <div class="result-placeholder" id="jadwal-placeholder">
            <div class="big-emoji">📅</div>
            <p style="font-size:0.85rem;">Pilih tanaman & tanggal tanam,<br>lalu klik <b>Tampilkan Jadwal</b></p>
          </div>
          <div id="jadwal-content" style="display:none;">
            <div id="jadwal-header" style="margin-bottom:14px;"></div>
            <div class="schedule-timeline" id="jadwal-timeline"></div>
            <div class="info-box-green" style="margin-top:12px;">💧 <b>Penyiraman:</b> Disarankan setiap 3 hari sekali untuk hasil optimal (Wahyudi & Hasibuan, 2024).</div>
          </div>
        </div>
      </div>
    </div>

    <!-- PERBANDINGAN -->
    <div class="page" id="page-perbandingan">
      <div class="page-title">📊 Perbandingan Dosis & Hasil Tanaman</div>
      <p style="font-size:0.8rem;color:#7a9a7e;margin-bottom:16px;">Data berdasarkan penelitian Wahyudi & Hasibuan (2024) — Tanaman Ketimun</p>
      <div class="tabs">
        <button class="tab-btn active" onclick="switchTab('tab-tinggi',this)">📏 Tinggi Tanaman</button>
        <button class="tab-btn" onclick="switchTab('tab-buah',this)">🥒 Hasil Buah</button>
      </div>
      <div class="tab-content active" id="tab-tinggi">
        <div class="chart-section">
          <div class="chart-title">Rerata Tinggi Tanaman (cm)</div>
          <div class="bar-chart">
            <div class="bar-row"><div class="bar-label">Tanpa Pupuk</div><div class="bar-wrap"><div class="bar-fill" style="width:81.5%">174.33</div></div></div>
            <div class="bar-row"><div class="bar-label">Organik 50g</div><div class="bar-wrap"><div class="bar-fill" style="width:91.4%">195.55</div></div></div>
            <div class="bar-row"><div class="bar-label">NPK 1.5g</div><div class="bar-wrap"><div class="bar-fill" style="width:100%">214.00</div></div></div>
            <div class="bar-row"><div class="bar-label">Semi Organik</div><div class="bar-wrap"><div class="bar-fill" style="width:95.3%">203.88</div></div></div>
          </div>
        </div>
        <div class="chart-section">
          <table class="data-table">
            <thead><tr><th>Dosis Pupuk</th><th>Rerata Tinggi (cm)</th></tr></thead>
            <tbody>
              <tr><td>Tanpa Pupuk</td><td>174.33</td></tr>
              <tr><td>Organik 50g</td><td>195.55</td></tr>
              <tr><td>NPK 1.5g</td><td>214.00</td></tr>
              <tr><td>Semi Organik</td><td>203.88</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="tab-content" id="tab-buah">
        <div class="chart-section">
          <div class="chart-title">Berat Segar Buah (g)</div>
          <div class="bar-chart">
            <div class="bar-row"><div class="bar-label">Tanpa Pupuk</div><div class="bar-wrap"><div class="bar-fill" style="width:46.8%">737.93</div></div></div>
            <div class="bar-row"><div class="bar-label">Organik 50g</div><div class="bar-wrap"><div class="bar-fill" style="width:100%">1577.07</div></div></div>
            <div class="bar-row"><div class="bar-label">NPK 1.5g</div><div class="bar-wrap"><div class="bar-fill" style="width:89.9%">1418.13</div></div></div>
            <div class="bar-row"><div class="bar-label">Semi Organik</div><div class="bar-wrap"><div class="bar-fill" style="width:69%">1088.76</div></div></div>
          </div>
        </div>
        <div class="chart-section">
          <table class="data-table">
            <thead><tr><th>Dosis Pupuk</th><th>Jumlah Buah</th><th>Berat Segar (g)</th><th>Diameter (cm)</th></tr></thead>
            <tbody>
              <tr><td>Tanpa Pupuk</td><td>2.44</td><td>737.93</td><td>4.71</td></tr>
              <tr><td>Organik 50g</td><td>4.88</td><td>1577.07</td><td>5.02</td></tr>
              <tr><td>NPK 1.5g</td><td>4.22</td><td>1418.13</td><td>5.13</td></tr>
              <tr><td>Semi Organik</td><td>3.22</td><td>1088.76</td><td>5.18</td></tr>
            </tbody>
          </table>
        </div>
        <div class="info-box-green">
          💡 <b>Kesimpulan:</b><br>
          • <b>Organik 50g/tanaman</b> → jumlah buah & berat segar tertinggi<br>
          • <b>NPK 1.5g</b> → tinggi tanaman & diameter buah terbaik<br>
          • <b>Semi Organik</b> → keseimbangan pertumbuhan dan hasil<br>
          • Penyiraman <b>3 hari sekali</b> memberikan hasil paling optimal
        </div>
      </div>
    </div>

    <!-- PANDUAN -->
    <div class="page" id="page-panduan">
      <div class="page-title">📚 Panduan & Referensi Ilmiah</div>
      <div class="accordion">
        <div class="acc-item open">
          <div class="acc-header" onclick="toggleAcc(this)">📖 Cara Menggunakan Aplikasi <span class="acc-arrow">▼</span></div>
          <div class="acc-body"><ol>
            <li><b>Kalkulator Pupuk</b> → Pilih tanaman, luas lahan, jenis pupuk → klik Hitung</li>
            <li><b>Jadwal Pemupukan</b> → Pilih tanaman, tanggal tanam → klik Tampilkan Jadwal</li>
            <li><b>Perbandingan Dosis</b> → Lihat grafik efektivitas berbagai pupuk</li>
          </ol></div>
        </div>
        <div class="acc-item">
          <div class="acc-header" onclick="toggleAcc(this)">🌿 Penjelasan Jenis Pupuk <span class="acc-arrow">▼</span></div>
          <div class="acc-body">
            <b>Pupuk Organik (Pupuk Kandang)</b><br>Memperbaiki struktur tanah & melepas hara perlahan. Dosis optimal ketimun: <b>50 g/tanaman</b> (10 ton/ha)<br><br>
            <b>Pupuk NPK (Anorganik)</b><br>Kandungan hara tinggi, cepat tersedia. Dosis optimal ketimun: <b>1,5 g/tanaman</b> (300 kg/ha)<br><br>
            <b>Semi Organik (Kombinasi)</b><br>Menggabungkan keunggulan organik & anorganik. Dosis: <b>25 g kandang + 0,75 g NPK</b> per tanaman
          </div>
        </div>
        <div class="acc-item">
          <div class="acc-header" onclick="toggleAcc(this)">📄 Referensi Ilmiah <span class="acc-arrow">▼</span></div>
          <div class="acc-body">
            <blockquote>Wahyudi, R.U. & Hasibuan, I. (2024). Pengaruh Dosis Pemupukan (Organik dan Anorganik) dan Frekuensi Penyiraman Terhadap Pertumbuhan dan Hasil Ketimun (<i>Cucumis sativus</i> L.). <i>JPatin</i>, Vol. 1, No. 1, Juni 2024, hal. 12-20.</blockquote>
            <ul>
              <li>BPS. (2016). Produksi Tanaman Hortikultura. Jakarta.</li>
              <li>Lingga, P. & Marsono. (2006). Petunjuk Penggunaan Pupuk. Penebar Swadaya.</li>
              <li>Samadi, B. (2002). Teknik Budi Daya Timun Hibrida. Kanisius.</li>
              <li>Sutanto, R. (2002). Pertanian Organik. Kanisius.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>

<script>
const dataTanaman = {
  "Ketimun / Timun": {jx:50,jy:100,npk:1.5,organik:50,semiKandang:25,semiNpk:0.75,panen:"55-65 hari"},
  "Tomat":           {jx:60,jy:70, npk:2.1,organik:90,semiKandang:45,semiNpk:1.05,panen:"75-90 hari"},
  "Cabai":           {jx:60,jy:70, npk:2.4,organik:120,semiKandang:60,semiNpk:1.2,panen:"90-120 hari"},
  "Bayam":           {jx:20,jy:20, npk:0.06,organik:2,semiKandang:1,semiNpk:0.03,panen:"25-35 hari"},
  "Kangkung":        {jx:20,jy:25, npk:0.06,organik:2,semiKandang:1,semiNpk:0.03,panen:"20-30 hari"},
  "Bawang Merah":    {jx:15,jy:20, npk:0.15,organik:4.5,semiKandang:2.25,semiNpk:0.075,panen:"60-70 hari"},
  "Terong":          {jx:70,jy:70, npk:1.715,organik:73.5,semiKandang:36.75,semiNpk:0.858,panen:"70-90 hari"},
  "Wortel":          {jx:20,jy:10, npk:0.05,organik:2,semiKandang:1,semiNpk:0.025,panen:"90-120 hari"},
};
const jadwalData = {
  "Ketimun / Timun": [
    {w:"Minggu 1",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 50 g/tanaman. Campurkan ke lubang tanam.",type:"start"},
    {w:"Minggu 2-3",fase:"🌱 Vegetatif",desc:"Pupuk susulan 1: NPK 0,5 g/tanaman. Larikan di sekitar tanaman.",type:"mid"},
    {w:"Minggu 4-5",fase:"🌸 Pembungaan",desc:"Pupuk susulan 2: NPK 0,5 g/tanaman. Masa pembungaan.",type:"mid"},
    {w:"Minggu 6-7",fase:"🥒 Pembuahan",desc:"Pupuk susulan 3: NPK 0,5 g/tanaman. Dukung pembentukan buah.",type:"mid"},
    {w:"Minggu 8",fase:"🌾 Panen",desc:"Stop pemupukan, persiapkan panen.",type:"harvest"},
  ],
  "Tomat": [
    {w:"Minggu 1",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 90 g/tanaman di lubang tanam.",type:"start"},
    {w:"Minggu 2-4",fase:"🌱 Vegetatif",desc:"Pupuk susulan 1: NPK 0,7 g/tanaman. Fase vegetatif aktif.",type:"mid"},
    {w:"Minggu 5-6",fase:"🌸 Pembungaan",desc:"Pupuk susulan 2: NPK 0,7 g/tanaman saat bunga mulai muncul.",type:"mid"},
    {w:"Minggu 7-10",fase:"🍅 Pembuahan",desc:"Pupuk susulan 3: NPK 0,7 g/tanaman untuk pembentukan buah.",type:"mid"},
    {w:"Minggu 11-12",fase:"🌾 Panen",desc:"Stop pemupukan, tunggu panen.",type:"harvest"},
  ],
  "Cabai": [
    {w:"Minggu 1-2",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 120 g/tanaman di bedengan.",type:"start"},
    {w:"Minggu 3-5",fase:"🌱 Vegetatif",desc:"Pupuk susulan 1: NPK 0,8 g/tanaman.",type:"mid"},
    {w:"Minggu 6-8",fase:"🌸 Pembungaan",desc:"Pupuk susulan 2: NPK 0,8 g/tanaman saat bunga keluar.",type:"mid"},
    {w:"Minggu 9-14",fase:"🌶️ Pembuahan",desc:"Pupuk susulan 3: NPK 0,8 g/tanaman selama pembuahan.",type:"mid"},
    {w:"Minggu 15+",fase:"🌾 Panen",desc:"Panen bertahap.",type:"harvest"},
  ],
  "Bayam": [
    {w:"Hari 1",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 2 g/tanaman.",type:"start"},
    {w:"Minggu 2",fase:"🌱 Vegetatif",desc:"Pupuk susulan: NPK 0,03 g/tanaman.",type:"mid"},
    {w:"Minggu 3-4",fase:"🌾 Panen",desc:"Siap panen.",type:"harvest"},
  ],
  "Kangkung": [
    {w:"Hari 1",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 2 g/tanaman.",type:"start"},
    {w:"Minggu 1-2",fase:"🌱 Vegetatif",desc:"Pupuk susulan: NPK 0,03 g/tanaman.",type:"mid"},
    {w:"Minggu 3",fase:"🌾 Panen",desc:"Panen.",type:"harvest"},
  ],
  "Bawang Merah": [
    {w:"Minggu 1",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 4,5 g/tanaman.",type:"start"},
    {w:"Minggu 2-3",fase:"🌱 Vegetatif",desc:"Pupuk susulan 1: NPK 0,05 g/tanaman.",type:"mid"},
    {w:"Minggu 4-6",fase:"🧅 Umbi",desc:"Pupuk susulan 2: NPK 0,05 g/tanaman. Pembentukan umbi.",type:"mid"},
    {w:"Minggu 7-9",fase:"🌾 Panen",desc:"Stop pemupukan, panen.",type:"harvest"},
  ],
  "Terong": [
    {w:"Minggu 1",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 73,5 g/tanaman.",type:"start"},
    {w:"Minggu 2-4",fase:"🌱 Vegetatif",desc:"Pupuk susulan 1: NPK 0,57 g/tanaman.",type:"mid"},
    {w:"Minggu 5-6",fase:"🌸 Pembungaan",desc:"Pupuk susulan 2: NPK 0,57 g/tanaman.",type:"mid"},
    {w:"Minggu 7-12",fase:"🍆 Pembuahan",desc:"Pupuk susulan 3: NPK 0,57 g/tanaman.",type:"mid"},
    {w:"Minggu 13+",fase:"🌾 Panen",desc:"Panen bertahap.",type:"harvest"},
  ],
  "Wortel": [
    {w:"Minggu 1",fase:"🟢 Awal Tanam",desc:"Pupuk dasar: Pupuk kandang 2 g/tanaman.",type:"start"},
    {w:"Minggu 3-4",fase:"🌱 Vegetatif",desc:"Pupuk susulan 1: NPK 0,025 g/tanaman.",type:"mid"},
    {w:"Minggu 7-12",fase:"🥕 Umbi",desc:"Pupuk susulan 2: NPK 0,025 g/tanaman. Pembentukan umbi.",type:"mid"},
    {w:"Minggu 13-16",fase:"🌾 Panen",desc:"Stop pemupukan, panen.",type:"harvest"},
  ],
};
function switchPage(id,el){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  el.classList.add('active');
}
function hitungPupuk(){
  const tn=document.getElementById('calc-tanaman').value;
  const luas=parseFloat(document.getElementById('calc-luas').value)||100;
  const pupuk=document.getElementById('calc-pupuk').value;
  const d=dataTanaman[tn];
  const jml=Math.floor(luas/((d.jx/100)*(d.jy/100)));
  const ha=(luas/10000).toFixed(4);
  document.getElementById('result-placeholder').style.display='none';
  const box=document.getElementById('result-box');
  box.classList.add('show');
  document.getElementById('result-title').textContent='✅ Hasil — '+tn;
  document.getElementById('result-metrics').innerHTML=`
    <div class="result-metric"><div class="val">${jml.toLocaleString()}</div><div class="lbl">Jumlah Tanaman</div></div>
    <div class="result-metric"><div class="val">${ha}</div><div class="lbl">Luas (ha)</div></div>
    <div class="result-metric"><div class="val">${d.jx}×${d.jy}</div><div class="lbl">Jarak Tanam (cm)</div></div>`;
  let dose='';
  if(pupuk.includes('Organik (')){
    const t=(d.organik*jml/1000).toFixed(2);
    dose=`<div class="result-dose-card"><div class="result-dose-label">🌿 Pupuk Kandang</div><div class="result-dose-value">${t} kg</div><div class="result-dose-sub">(${d.organik} g/tanaman × ${jml.toLocaleString()} tanaman)</div></div>`;
  } else if(pupuk.includes('NPK')){
    const t=(d.npk*jml/1000).toFixed(2);
    dose=`<div class="result-dose-card"><div class="result-dose-label">🧪 Pupuk NPK</div><div class="result-dose-value">${t} kg</div><div class="result-dose-sub">(${d.npk} g/tanaman × ${jml.toLocaleString()} tanaman)</div></div>`;
  } else {
    const k=(d.semiKandang*jml/1000).toFixed(2),n=(d.semiNpk*jml/1000).toFixed(2);
    dose=`<div class="result-dose-card"><div class="result-dose-label">🌿 Semi Organik</div><div style="margin-top:5px">Pupuk Kandang: <span style="font-size:1.3rem;font-weight:800;color:#1a5c2a">${k} kg</span> <span style="font-size:0.7rem;color:#9db8a0">(${d.semiKandang} g/tanaman)</span></div><div style="margin-top:4px">Pupuk NPK: <span style="font-size:1.3rem;font-weight:800;color:#2d8a45">${n} kg</span> <span style="font-size:0.7rem;color:#9db8a0">(${d.semiNpk} g/tanaman)</span></div></div>`;
  }
  document.getElementById('result-dose').innerHTML=dose;
  document.getElementById('result-warn').innerHTML=`⏱️ <b>Umur Panen:</b> ${d.panen}<br>💡 Berikan pupuk bertahap sesuai fase pertumbuhan.`;
}
function tampilkanJadwal(){
  const tn=document.getElementById('jadwal-tanaman').value;
  const tgl=document.getElementById('jadwal-tgl').value;
  const steps=jadwalData[tn];
  document.getElementById('jadwal-placeholder').style.display='none';
  document.getElementById('jadwal-content').style.display='block';
  const tglStr=tgl?new Date(tgl).toLocaleDateString('id-ID',{day:'2-digit',month:'long',year:'numeric'}):'';
  document.getElementById('jadwal-header').innerHTML=`<div style="font-size:0.96rem;font-weight:700;color:#1a2e1c;margin-bottom:3px">📋 Jadwal — ${tn}</div>${tglStr?`<div style="font-size:0.78rem;color:#7a9a7e">Mulai tanam: ${tglStr}</div>`:''}`;
  document.getElementById('jadwal-timeline').innerHTML=steps.map(s=>`
    <div class="schedule-step">
      <div class="step-dot ${s.type}">${s.type==='harvest'?'🌾':s.type==='start'?'🌱':'🪴'}</div>
      <div class="step-content">
        <div class="step-week">${s.w}</div>
        <div class="step-phase">${s.fase}</div>
        <div class="step-desc">${s.desc}</div>
      </div>
    </div>`).join('');
}
function switchTab(id,el){
  document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  el.classList.add('active');
}
function toggleAcc(h){h.parentElement.classList.toggle('open');}
document.getElementById('jadwal-tgl').valueAsDate=new Date();
</script>
</body>
</html>
"""

components.html(html_code, height=800, scrolling=False)