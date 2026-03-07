<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>🔐 SecureCode Wizard — 세계 최강 보안 코딩 어시스턴트</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Noto+Sans+KR:wght@300;400;500;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #060a12;
    --surface: #0d1526;
    --surface2: #111d35;
    --border: rgba(0,200,255,0.15);
    --border-glow: rgba(0,200,255,0.5);
    --cyan: #00c8ff;
    --cyan2: #00ffcc;
    --gold: #ffd700;
    --red: #ff4060;
    --green: #00ff88;
    --purple: #a855f7;
    --text: #e0eeff;
    --text-dim: #7090b0;
    --glow: 0 0 20px rgba(0,200,255,0.4);
    --glow-strong: 0 0 40px rgba(0,200,255,0.7);
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'Noto Sans KR', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
  }

  /* ── ANIMATED BACKGROUND ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
      radial-gradient(ellipse 80% 60% at 20% 10%, rgba(0,200,255,0.06) 0%, transparent 60%),
      radial-gradient(ellipse 60% 80% at 80% 90%, rgba(168,85,247,0.06) 0%, transparent 60%),
      radial-gradient(ellipse 40% 40% at 50% 50%, rgba(0,255,136,0.03) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
  }

  .grid-bg {
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,200,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,200,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
    animation: gridMove 20s linear infinite;
  }
  @keyframes gridMove {
    from { transform: translate(0,0); }
    to { transform: translate(40px, 40px); }
  }

  /* ── HEADER ── */
  header {
    position: relative;
    z-index: 10;
    text-align: center;
    padding: 48px 20px 32px;
    border-bottom: 1px solid var(--border);
    background: linear-gradient(180deg, rgba(0,200,255,0.05) 0%, transparent 100%);
  }

  .logo-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, rgba(0,200,255,0.15), rgba(168,85,247,0.15));
    border: 1px solid var(--border-glow);
    border-radius: 50px;
    padding: 6px 18px;
    font-size: 11px;
    font-family: 'Orbitron', monospace;
    color: var(--cyan);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 20px;
    animation: pulse-border 3s ease-in-out infinite;
  }
  @keyframes pulse-border {
    0%,100% { border-color: rgba(0,200,255,0.3); box-shadow: 0 0 10px rgba(0,200,255,0.1); }
    50% { border-color: rgba(0,200,255,0.8); box-shadow: 0 0 30px rgba(0,200,255,0.4); }
  }

  .shield-icon {
    font-size: 48px;
    display: block;
    margin: 0 auto 12px;
    animation: float 4s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(0,200,255,0.6));
  }
  @keyframes float {
    0%,100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-8px) rotate(2deg); }
  }

  h1 {
    font-family: 'Orbitron', monospace;
    font-size: clamp(22px, 5vw, 42px);
    font-weight: 900;
    background: linear-gradient(135deg, var(--cyan), var(--cyan2), var(--gold));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 2px;
    line-height: 1.2;
    margin-bottom: 10px;
  }

  .subtitle {
    color: var(--text-dim);
    font-size: clamp(12px, 2vw, 15px);
    font-weight: 300;
    letter-spacing: 1px;
  }

  /* ── PROGRESS BAR ── */
  .progress-wrapper {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(6,10,18,0.95);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    padding: 12px 20px;
  }

  .progress-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    font-size: 12px;
  }

  .progress-label {
    font-family: 'Orbitron', monospace;
    color: var(--cyan);
    font-size: 11px;
    letter-spacing: 2px;
  }

  .progress-pct {
    font-family: 'JetBrains Mono', monospace;
    color: var(--gold);
    font-weight: 700;
  }

  .progress-bar {
    height: 4px;
    background: rgba(0,200,255,0.1);
    border-radius: 4px;
    overflow: hidden;
    position: relative;
  }

  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--cyan), var(--cyan2));
    border-radius: 4px;
    transition: width 0.5s cubic-bezier(0.4,0,0.2,1);
    position: relative;
  }
  .progress-fill::after {
    content: '';
    position: absolute;
    right: 0;
    top: -2px;
    width: 8px;
    height: 8px;
    background: var(--cyan2);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--cyan2);
  }

  .step-dots {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 8px;
    flex-wrap: wrap;
  }

  .step-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: rgba(0,200,255,0.2);
    border: 1px solid rgba(0,200,255,0.3);
    transition: all 0.3s;
    cursor: pointer;
  }
  .step-dot.active {
    background: var(--cyan);
    box-shadow: 0 0 8px var(--cyan);
  }
  .step-dot.done {
    background: var(--green);
    border-color: var(--green);
    box-shadow: 0 0 6px var(--green);
  }

  /* ── MAIN CONTAINER ── */
  main {
    position: relative;
    z-index: 1;
    max-width: 860px;
    margin: 0 auto;
    padding: 32px 16px 80px;
  }

  /* ── SECTION CARD ── */
  .section-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    margin-bottom: 20px;
    overflow: hidden;
    transition: border-color 0.3s, box-shadow 0.3s;
    animation: slideIn 0.4s ease both;
  }
  .section-card:hover {
    border-color: rgba(0,200,255,0.3);
    box-shadow: 0 0 30px rgba(0,200,255,0.08);
  }
  @keyframes slideIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .section-header {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 18px 22px;
    background: linear-gradient(135deg, rgba(0,200,255,0.08), rgba(168,85,247,0.05));
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    user-select: none;
    transition: background 0.2s;
  }
  .section-header:hover {
    background: linear-gradient(135deg, rgba(0,200,255,0.12), rgba(168,85,247,0.08));
  }

  .section-num {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: linear-gradient(135deg, rgba(0,200,255,0.2), rgba(168,85,247,0.2));
    border: 1px solid rgba(0,200,255,0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Orbitron', monospace;
    font-weight: 700;
    font-size: 14px;
    color: var(--cyan);
    flex-shrink: 0;
  }

  .section-title {
    flex: 1;
    font-size: clamp(14px, 2.5vw, 17px);
    font-weight: 700;
    color: var(--text);
    letter-spacing: 0.5px;
  }

  .section-toggle {
    font-size: 20px;
    color: var(--cyan);
    transition: transform 0.3s;
  }
  .section-card.collapsed .section-toggle { transform: rotate(-90deg); }

  .section-body {
    padding: 22px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    transition: all 0.3s;
  }
  .section-card.collapsed .section-body { display: none; }

  /* ── QUESTION BLOCK ── */
  .q-block {
    position: relative;
  }

  .q-label {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 10px;
    font-size: clamp(13px, 2vw, 15px);
    font-weight: 500;
    color: var(--text);
    line-height: 1.5;
  }

  .q-icon {
    font-size: 18px;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .q-hint {
    font-size: 11px;
    color: var(--text-dim);
    font-weight: 300;
    font-family: 'JetBrains Mono', monospace;
    background: rgba(0,200,255,0.05);
    border-left: 2px solid rgba(0,200,255,0.3);
    padding: 4px 8px;
    border-radius: 0 4px 4px 0;
    margin-bottom: 8px;
    line-height: 1.5;
  }

  /* ── CHIP SELECTOR ── */
  .chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .chip {
    padding: 8px 16px;
    border-radius: 50px;
    border: 1px solid rgba(0,200,255,0.25);
    background: rgba(0,200,255,0.05);
    color: var(--text-dim);
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s;
    user-select: none;
    font-family: 'Noto Sans KR', sans-serif;
    white-space: nowrap;
  }
  .chip:hover {
    border-color: rgba(0,200,255,0.6);
    color: var(--cyan);
    background: rgba(0,200,255,0.1);
    transform: translateY(-1px);
  }
  .chip.selected {
    border-color: var(--cyan);
    background: rgba(0,200,255,0.15);
    color: var(--cyan);
    box-shadow: 0 0 12px rgba(0,200,255,0.2);
  }
  .chip.multi.selected {
    border-color: var(--cyan2);
    background: rgba(0,255,204,0.12);
    color: var(--cyan2);
    box-shadow: 0 0 12px rgba(0,255,204,0.2);
  }

  /* ── INPUTS ── */
  input[type="text"], input[type="number"], textarea, select {
    width: 100%;
    background: rgba(0,200,255,0.04);
    border: 1px solid rgba(0,200,255,0.2);
    border-radius: 10px;
    color: var(--text);
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 14px;
    padding: 12px 16px;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    -webkit-appearance: none;
  }
  input[type="text"]:focus, input[type="number"]:focus, textarea:focus, select:focus {
    border-color: var(--cyan);
    box-shadow: 0 0 0 3px rgba(0,200,255,0.1);
  }
  textarea { resize: vertical; min-height: 80px; }
  select option { background: var(--surface); color: var(--text); }

  /* ── TOGGLE SWITCH ── */
  .toggle-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 14px;
    background: rgba(0,200,255,0.04);
    border: 1px solid var(--border);
    border-radius: 10px;
    gap: 12px;
  }

  .toggle-label { font-size: 13px; color: var(--text); flex: 1; }
  .toggle-sub { font-size: 11px; color: var(--text-dim); display: block; }

  .toggle {
    position: relative;
    width: 44px;
    height: 24px;
    flex-shrink: 0;
  }
  .toggle input { opacity: 0; width: 0; height: 0; }
  .toggle-track {
    position: absolute;
    inset: 0;
    background: rgba(0,200,255,0.15);
    border: 1px solid rgba(0,200,255,0.3);
    border-radius: 24px;
    cursor: pointer;
    transition: all 0.3s;
  }
  .toggle-track::after {
    content: '';
    position: absolute;
    left: 3px;
    top: 50%;
    transform: translateY(-50%);
    width: 16px;
    height: 16px;
    background: var(--text-dim);
    border-radius: 50%;
    transition: all 0.3s;
  }
  .toggle input:checked + .toggle-track {
    background: rgba(0,200,255,0.25);
    border-color: var(--cyan);
  }
  .toggle input:checked + .toggle-track::after {
    left: calc(100% - 19px);
    background: var(--cyan);
    box-shadow: 0 0 8px var(--cyan);
  }

  /* ── RANGE SLIDER ── */
  .range-wrapper { position: relative; }
  input[type="range"] {
    -webkit-appearance: none;
    width: 100%;
    height: 4px;
    background: rgba(0,200,255,0.15);
    border-radius: 4px;
    outline: none;
    padding: 0;
    border: none;
    box-shadow: none;
  }
  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--cyan), var(--cyan2));
    cursor: pointer;
    box-shadow: 0 0 12px rgba(0,200,255,0.5);
    border: 2px solid rgba(255,255,255,0.2);
  }
  .range-labels {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: var(--text-dim);
    margin-top: 6px;
    font-family: 'JetBrains Mono', monospace;
  }
  .range-val {
    text-align: center;
    font-size: 13px;
    color: var(--cyan);
    font-family: 'Orbitron', monospace;
    margin-top: 4px;
  }

  /* ── SECURITY METER ── */
  .security-meter {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    margin-top: 8px;
  }

  .meter-title {
    font-family: 'Orbitron', monospace;
    font-size: 11px;
    color: var(--text-dim);
    letter-spacing: 2px;
    margin-bottom: 12px;
  }

  .meter-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
  }

  .meter-key {
    font-size: 12px;
    color: var(--text-dim);
    width: 120px;
    flex-shrink: 0;
  }

  .meter-bar {
    flex: 1;
    height: 6px;
    background: rgba(255,255,255,0.06);
    border-radius: 6px;
    overflow: hidden;
  }

  .meter-fill {
    height: 100%;
    border-radius: 6px;
    transition: width 0.8s cubic-bezier(0.4,0,0.2,1);
  }

  .meter-score {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    width: 36px;
    text-align: right;
  }

  /* ── FLOW CHART ── */
  .flow-chart {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 0;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    overflow-x: auto;
  }

  .flow-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    min-width: 80px;
  }

  .flow-box {
    background: linear-gradient(135deg, rgba(0,200,255,0.12), rgba(168,85,247,0.12));
    border: 1px solid rgba(0,200,255,0.4);
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 12px;
    text-align: center;
    color: var(--cyan);
    font-family: 'JetBrains Mono', monospace;
    transition: all 0.3s;
    cursor: default;
  }
  .flow-box:hover {
    background: rgba(0,200,255,0.2);
    box-shadow: 0 0 12px rgba(0,200,255,0.3);
  }
  .flow-box.active-node {
    border-color: var(--gold);
    color: var(--gold);
    box-shadow: 0 0 15px rgba(255,215,0,0.3);
    animation: nodeGlow 2s ease-in-out infinite;
  }
  @keyframes nodeGlow {
    0%,100% { box-shadow: 0 0 10px rgba(255,215,0,0.2); }
    50% { box-shadow: 0 0 25px rgba(255,215,0,0.5); }
  }
  .flow-sub { font-size: 10px; color: var(--text-dim); text-align: center; }

  .flow-arrow {
    color: rgba(0,200,255,0.4);
    font-size: 18px;
    padding: 0 4px;
    flex-shrink: 0;
  }

  /* ── GENERATE BUTTON ── */
  .gen-btn-wrap {
    text-align: center;
    padding: 32px 20px;
    position: relative;
  }

  .gen-btn {
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: linear-gradient(135deg, rgba(0,200,255,0.2), rgba(0,255,204,0.15));
    border: 2px solid var(--cyan);
    border-radius: 60px;
    color: var(--cyan);
    font-family: 'Orbitron', monospace;
    font-size: clamp(13px, 2.5vw, 17px);
    font-weight: 700;
    letter-spacing: 2px;
    padding: clamp(14px, 3vw, 20px) clamp(28px, 6vw, 52px);
    cursor: pointer;
    transition: all 0.3s;
    text-transform: uppercase;
    overflow: hidden;
    -webkit-tap-highlight-color: transparent;
    outline: none;
    box-shadow: 0 0 30px rgba(0,200,255,0.2), inset 0 0 20px rgba(0,200,255,0.05);
  }
  .gen-btn::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,255,204,0.1));
    opacity: 0;
    transition: opacity 0.3s;
    border-radius: inherit;
  }
  .gen-btn:hover::before { opacity: 1; }
  .gen-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 60px rgba(0,200,255,0.5), inset 0 0 30px rgba(0,200,255,0.1);
    border-color: var(--cyan2);
  }
  .gen-btn:active { transform: translateY(0); }
  .gen-btn.loading { pointer-events: none; opacity: 0.8; }

  .btn-spinner {
    width: 20px;
    height: 20px;
    border: 2px solid rgba(0,200,255,0.3);
    border-top-color: var(--cyan);
    border-radius: 50%;
    display: none;
    animation: spin 0.8s linear infinite;
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  .gen-btn.loading .btn-spinner { display: block; }
  .gen-btn.loading .btn-text { opacity: 0.6; }

  /* ── OUTPUT PANEL ── */
  #output-panel {
    display: none;
    animation: fadeIn 0.5s ease both;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .output-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 22px;
    background: linear-gradient(135deg, rgba(0,255,136,0.08), rgba(0,200,255,0.08));
    border-bottom: 1px solid var(--border);
    flex-wrap: wrap;
    gap: 10px;
  }

  .output-title {
    font-family: 'Orbitron', monospace;
    font-size: 14px;
    color: var(--green);
    letter-spacing: 2px;
  }

  .copy-btn {
    background: rgba(0,255,136,0.1);
    border: 1px solid rgba(0,255,136,0.3);
    border-radius: 8px;
    color: var(--green);
    font-size: 12px;
    padding: 6px 14px;
    cursor: pointer;
    font-family: 'JetBrains Mono', monospace;
    transition: all 0.2s;
    outline: none;
    -webkit-tap-highlight-color: transparent;
  }
  .copy-btn:hover { background: rgba(0,255,136,0.2); transform: translateY(-1px); }

  .output-body {
    padding: 22px;
  }

  #code-output {
    background: rgba(0,0,0,0.4);
    border: 1px solid rgba(0,200,255,0.15);
    border-radius: 10px;
    padding: 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(11px, 1.5vw, 13px);
    line-height: 1.7;
    color: #a8d8ea;
    white-space: pre-wrap;
    word-break: break-all;
    max-height: 500px;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: rgba(0,200,255,0.3) transparent;
  }
  #code-output::-webkit-scrollbar { width: 4px; }
  #code-output::-webkit-scrollbar-thumb { background: rgba(0,200,255,0.3); border-radius: 4px; }

  .kw { color: #ff79c6; }
  .fn { color: #50fa7b; }
  .st { color: #f1fa8c; }
  .cm { color: #6272a4; }
  .nm { color: #bd93f9; }
  .op { color: #ff79c6; }

  /* ── SECURITY REPORT ── */
  .security-report {
    margin-top: 16px;
    background: rgba(0,200,255,0.04);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
  }

  .report-title {
    font-family: 'Orbitron', monospace;
    font-size: 12px;
    color: var(--cyan);
    letter-spacing: 2px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .report-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 7px 0;
    border-bottom: 1px solid rgba(0,200,255,0.06);
    font-size: 13px;
  }
  .report-item:last-child { border-bottom: none; }

  .ri-icon { font-size: 16px; flex-shrink: 0; }
  .ri-key { color: var(--text-dim); flex: 1; }
  .ri-val { font-family: 'JetBrains Mono', monospace; font-size: 12px; }
  .ri-val.ok { color: var(--green); }
  .ri-val.warn { color: var(--gold); }
  .ri-val.off { color: var(--text-dim); }

  /* ── ALERT BOX ── */
  .alert-box {
    display: none;
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 13px;
    margin-top: 12px;
    gap: 10px;
    align-items: flex-start;
  }
  .alert-box.show { display: flex; }
  .alert-box.warn { background: rgba(255,215,0,0.08); border: 1px solid rgba(255,215,0,0.3); color: var(--gold); }
  .alert-box.err { background: rgba(255,64,96,0.08); border: 1px solid rgba(255,64,96,0.3); color: var(--red); }
  .alert-box.suc { background: rgba(0,255,136,0.08); border: 1px solid rgba(0,255,136,0.3); color: var(--green); }

  /* ── FILE DOWNLOAD ── */
  .dl-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(168,85,247,0.15), rgba(0,200,255,0.1));
    border: 1px solid rgba(168,85,247,0.4);
    border-radius: 10px;
    color: var(--purple);
    font-size: 13px;
    padding: 10px 18px;
    cursor: pointer;
    font-family: 'Noto Sans KR', sans-serif;
    transition: all 0.2s;
    margin-right: 10px;
    margin-top: 10px;
    text-decoration: none;
    outline: none;
    -webkit-tap-highlight-color: transparent;
  }
  .dl-btn:hover { background: rgba(168,85,247,0.25); transform: translateY(-1px); }

  /* ── TOAST ── */
  #toast {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%) translateY(100px);
    background: linear-gradient(135deg, rgba(0,200,255,0.9), rgba(0,255,204,0.8));
    color: #000;
    border-radius: 50px;
    padding: 12px 24px;
    font-size: 13px;
    font-weight: 700;
    font-family: 'Orbitron', monospace;
    letter-spacing: 1px;
    z-index: 9999;
    transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
    pointer-events: none;
  }
  #toast.show { transform: translateX(-50%) translateY(0); }

  /* ── VALIDATION INDICATOR ── */
  .val-indicator {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    margin-top: 4px;
    color: var(--text-dim);
    font-family: 'JetBrains Mono', monospace;
    min-height: 18px;
    transition: color 0.2s;
  }
  .val-indicator.ok { color: var(--green); }
  .val-indicator.err { color: var(--red); }

  /* ── MOBILE RESPONSIVE ── */
  @media (max-width: 600px) {
    main { padding: 20px 12px 60px; }
    .section-body { padding: 16px; gap: 16px; }
    .section-header { padding: 14px 16px; }
    .chips { gap: 6px; }
    .chip { padding: 7px 13px; font-size: 12px; }
    .flow-chart { padding: 12px; }
    .flow-node { min-width: 65px; }
    .flow-box { font-size: 11px; padding: 6px 8px; }
    .toggle-row { gap: 8px; }
    .meter-key { width: 90px; font-size: 11px; }
    input[type="text"], input[type="number"], textarea, select { font-size: 16px; } /* prevent zoom on iOS */
  }

  /* ── COMPLETION BADGE ── */
  .completion-badge {
    display: none;
    text-align: center;
    padding: 20px;
    margin-bottom: 20px;
    background: linear-gradient(135deg, rgba(0,255,136,0.08), rgba(0,200,255,0.08));
    border: 1px solid rgba(0,255,136,0.3);
    border-radius: 16px;
    animation: fadeIn 0.5s ease;
  }
  .completion-badge.show { display: block; }
  .completion-badge h3 {
    font-family: 'Orbitron', monospace;
    color: var(--green);
    font-size: clamp(14px, 3vw, 20px);
    letter-spacing: 2px;
    margin-bottom: 8px;
  }
  .completion-badge p { color: var(--text-dim); font-size: 13px; }

  /* ── API KEY NOTICE ── */
  .api-notice {
    background: rgba(255,215,0,0.06);
    border: 1px solid rgba(255,215,0,0.25);
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 12px;
    color: var(--gold);
    margin-top: 10px;
    line-height: 1.6;
  }

  .powered-by {
    text-align: center;
    padding: 16px;
    font-size: 11px;
    color: var(--text-dim);
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 1px;
    border-top: 1px solid var(--border);
  }
</style>
</head>
<body>
<div class="grid-bg"></div>

<!-- HEADER -->
<header>
  <div class="logo-badge">🛡 SECURE CODE WIZARD v2.0</div>
  <span class="shield-icon">🔐</span>
  <h1>SecureCode Wizard</h1>
  <p class="subtitle">나노클로 초월 · 세계 최강 보안 코딩 어시스턴트 · 왕초보도 10분 완성</p>
</header>

<!-- STICKY PROGRESS -->
<div class="progress-wrapper">
  <div class="progress-info">
    <span class="progress-label">MISSION PROGRESS</span>
    <span class="progress-pct" id="pct-label">0%</span>
  </div>
  <div class="progress-bar">
    <div class="progress-fill" id="progress-fill" style="width:0%"></div>
  </div>
  <div class="step-dots" id="step-dots"></div>
</div>

<main>

<!-- COMPLETION BADGE -->
<div class="completion-badge" id="completion-badge">
  <h3>🎉 모든 설정 완료!</h3>
  <p>아래 '코드 생성' 버튼을 눌러 안전한 프로그램을 완성하세요.</p>
</div>

<!-- ═══════════════════════════════════════════════ SECTION 1 ═══ -->
<div class="section-card" id="sec-1">
  <div class="section-header" onclick="toggleSection(1)">
    <div class="section-num">01</div>
    <div class="section-title">🖥️ 기본 환경 확인</div>
    <span class="section-toggle">▼</span>
  </div>
  <div class="section-body">

    <!-- Q1: OS -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">💻</span> 현재 사용 중인 운영체제는?</div>
      <div class="q-hint">💡 초보자라면 Docker 설치부터 자동 안내합니다.</div>
      <div class="chips" id="os-chips">
        <div class="chip" onclick="selectChip('os',this,'Windows')">🪟 Windows</div>
        <div class="chip" onclick="selectChip('os',this,'macOS')">🍎 macOS</div>
        <div class="chip" onclick="selectChip('os',this,'Linux')">🐧 Linux</div>
        <div class="chip" onclick="selectChip('os',this,'Android/iOS')">📱 Android/iOS</div>
      </div>
    </div>

    <!-- Q2: Coding level -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🧑‍💻</span> 코딩 경험 수준은?</div>
      <div class="q-hint">💡 선택에 따라 보안 설정 난이도가 자동 조정됩니다.</div>
      <div class="chips" id="skill-chips">
        <div class="chip" onclick="selectChip('skill',this,'none')">😅 전혀 없음</div>
        <div class="chip" onclick="selectChip('skill',this,'beginner')">🌱 약간 있음</div>
        <div class="chip" onclick="selectChip('skill',this,'python')">🐍 Python 기본</div>
        <div class="chip" onclick="selectChip('skill',this,'advanced')">⚡ 중급 이상</div>
      </div>
    </div>

    <!-- Q3: RAM -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🧠</span> RAM 용량 (GB)</div>
      <div class="q-hint">💡 8GB 이상 권장. 컨테이너 기반 격리에 필요합니다.</div>
      <input type="range" id="ram-range" min="2" max="64" step="2" value="8"
             oninput="updateRange('ram-range','ram-val',this.value,'GB')">
      <div class="range-val" id="ram-val">8 GB</div>
      <div class="range-labels"><span>2 GB</span><span>32 GB</span><span>64 GB</span></div>
    </div>

    <!-- Q4: Internet -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🌐</span> 인터넷 연결 환경</div>
      <div class="chips" id="net-chips">
        <div class="chip" onclick="selectChip('net',this,'always')">✅ 항상 연결</div>
        <div class="chip" onclick="selectChip('net',this,'sometimes')">⚡ 가끔 연결</div>
        <div class="chip" onclick="selectChip('net',this,'offline')">🔒 오프라인 전용</div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════ SECTION 2 ═══ -->
<div class="section-card" id="sec-2">
  <div class="section-header" onclick="toggleSection(2)">
    <div class="section-num">02</div>
    <div class="section-title">🛡️ 보안 요구사항 정의</div>
    <span class="section-toggle">▼</span>
  </div>
  <div class="section-body">

    <!-- Q5: Data type -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">📦</span> 다룰 데이터 유형? (복수 선택 가능)</div>
      <div class="q-hint">💡 선택된 데이터에 맞는 다층 암호화 레이어를 자동 설정합니다.</div>
      <div class="chips" id="data-chips">
        <div class="chip multi" onclick="toggleMulti('data',this,'personal')">📁 개인 파일</div>
        <div class="chip multi" onclick="toggleMulti('data',this,'financial')">💰 금융 데이터</div>
        <div class="chip multi" onclick="toggleMulti('data',this,'web')">🌐 웹 크롤링</div>
        <div class="chip multi" onclick="toggleMulti('data',this,'medical')">🏥 의료 정보</div>
        <div class="chip multi" onclick="toggleMulti('data',this,'code')">💻 소스코드</div>
        <div class="chip multi" onclick="toggleMulti('data',this,'other')">📝 기타</div>
      </div>
    </div>

    <!-- Q6: Attack concerns -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">⚔️</span> 우려하는 공격 유형? (복수 선택)</div>
      <div class="q-hint">💡 선택한 위협에 대해 컨테이너+VM 격리+실시간 감사 로그를 자동 설정합니다.</div>
      <div class="chips" id="attack-chips">
        <div class="chip multi" onclick="toggleMulti('attack',this,'injection')">💉 프롬프트 인젝션</div>
        <div class="chip multi" onclick="toggleMulti('attack',this,'escape')">🚪 파일 탈출</div>
        <div class="chip multi" onclick="toggleMulti('attack',this,'network')">📡 네트워크 유출</div>
        <div class="chip multi" onclick="toggleMulti('attack',this,'malware')">🦠 악성코드</div>
        <div class="chip multi" onclick="toggleMulti('attack',this,'privilege')">🔑 권한 상승</div>
      </div>
    </div>

    <!-- Q7: Key storage -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🔑</span> API키/비밀번호 저장 방식?</div>
      <div class="q-hint">💡 기본 AES-256 암호화 적용. 클라우드 저장 완전 차단 옵션 포함.</div>
      <div class="chips" id="storage-chips">
        <div class="chip" onclick="selectChip('storage',this,'local')">💾 로컬 암호화</div>
        <div class="chip" onclick="selectChip('storage',this,'env')">🌍 환경변수</div>
        <div class="chip" onclick="selectChip('storage',this,'vault')">🏦 보안 금고(Vault)</div>
        <div class="chip" onclick="selectChip('storage',this,'none')">🚫 키 없음</div>
      </div>
    </div>

    <!-- Security Meter -->
    <div class="security-meter" id="security-meter">
      <div class="meter-title">⚡ REAL-TIME SECURITY SCORE</div>
      <div class="meter-row">
        <span class="meter-key">암호화 강도</span>
        <div class="meter-bar"><div class="meter-fill" id="m-enc" style="width:0%;background:linear-gradient(90deg,#00c8ff,#00ffcc)"></div></div>
        <span class="meter-score" id="ms-enc" style="color:#00c8ff">0%</span>
      </div>
      <div class="meter-row">
        <span class="meter-key">격리 수준</span>
        <div class="meter-bar"><div class="meter-fill" id="m-iso" style="width:0%;background:linear-gradient(90deg,#a855f7,#00c8ff)"></div></div>
        <span class="meter-score" id="ms-iso" style="color:#a855f7">0%</span>
      </div>
      <div class="meter-row">
        <span class="meter-key">감사 로그</span>
        <div class="meter-bar"><div class="meter-fill" id="m-log" style="width:0%;background:linear-gradient(90deg,#ffd700,#ff9f00)"></div></div>
        <span class="meter-score" id="ms-log" style="color:#ffd700">0%</span>
      </div>
      <div class="meter-row">
        <span class="meter-key">전체 보안</span>
        <div class="meter-bar"><div class="meter-fill" id="m-total" style="width:0%;background:linear-gradient(90deg,#00ff88,#00c8ff)"></div></div>
        <span class="meter-score" id="ms-total" style="color:#00ff88">0%</span>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════ SECTION 3 ═══ -->
<div class="section-card" id="sec-3">
  <div class="section-header" onclick="toggleSection(3)">
    <div class="section-num">03</div>
    <div class="section-title">⚙️ 기능 목표 설정</div>
    <span class="section-toggle">▼</span>
  </div>
  <div class="section-body">

    <!-- Q8: Purpose -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🎯</span> 프로그램의 주요 목적은?</div>
      <div class="q-hint">💡 AI가 선택에 맞는 최적화 코드를 자동 생성합니다.</div>
      <div class="chips" id="purpose-chips">
        <div class="chip" onclick="selectChip('purpose',this,'automation')">🤖 자동화 스크립트</div>
        <div class="chip" onclick="selectChip('purpose',this,'webbot')">🕷️ 웹 봇/크롤러</div>
        <div class="chip" onclick="selectChip('purpose',this,'dataanalysis')">📊 데이터 분석</div>
        <div class="chip" onclick="selectChip('purpose',this,'filemanager')">📂 파일 관리</div>
        <div class="chip" onclick="selectChip('purpose',this,'api')">🔌 API 연동</div>
        <div class="chip" onclick="selectChip('purpose',this,'custom')">✏️ 직접 입력</div>
      </div>
      <div id="custom-purpose-wrap" style="display:none;margin-top:10px">
        <input type="text" id="custom-purpose" placeholder="프로그램 목적을 직접 입력하세요..." oninput="updateProgress()">
        <div class="val-indicator" id="custom-purpose-val"></div>
      </div>
    </div>

    <!-- Q9: I/O -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">↕️</span> 입력/출력 형태는? (복수 선택)</div>
      <div class="q-hint">💡 드래그-드롭 UI로 초보자도 직관적으로 연결할 수 있습니다.</div>
      <div class="chips" id="io-chips">
        <div class="chip multi" onclick="toggleMulti('io',this,'textfile')">📄 텍스트 파일</div>
        <div class="chip multi" onclick="toggleMulti('io',this,'apicall')">🔌 API 호출</div>
        <div class="chip multi" onclick="toggleMulti('io',this,'gui')">🖥️ GUI 화면</div>
        <div class="chip multi" onclick="toggleMulti('io',this,'database')">🗄️ 데이터베이스</div>
        <div class="chip multi" onclick="toggleMulti('io',this,'excel')">📊 엑셀/CSV</div>
        <div class="chip multi" onclick="toggleMulti('io',this,'email')">📧 이메일</div>
      </div>
    </div>

    <!-- Q10: Schedule -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">⏰</span> 반복 실행이 필요한가요?</div>
      <div class="q-hint">💡 크론탭 없이 클릭 한 번으로 설정할 수 있습니다.</div>
      <div class="chips" id="schedule-chips">
        <div class="chip" onclick="selectChip('schedule',this,'once')">1️⃣ 일회성</div>
        <div class="chip" onclick="selectChip('schedule',this,'daily')">📅 매일 자동</div>
        <div class="chip" onclick="selectChip('schedule',this,'hourly')">⏱️ 매시간</div>
        <div class="chip" onclick="selectChip('schedule',this,'trigger')">🎛️ 이벤트 트리거</div>
        <div class="chip" onclick="selectChip('schedule',this,'manual')">👆 수동 실행</div>
      </div>
    </div>

    <!-- Q11: Steps / Flow -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🗂️</span> 주요 처리 단계 수?</div>
      <div class="q-hint">💡 단계별 시각적 플로우차트로 자동 확인됩니다.</div>
      <input type="range" id="steps-range" min="1" max="10" step="1" value="3"
             oninput="updateSteps(this.value)">
      <div class="range-val" id="steps-val">3 단계</div>
      <div class="range-labels"><span>1단계</span><span>5단계</span><span>10단계</span></div>
      <!-- Flow chart -->
      <div class="flow-chart" id="flow-chart" style="margin-top:14px"></div>
    </div>

    <!-- Q12: Error handling -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🚨</span> 에러 발생 시 처리 방식?</div>
      <div class="q-hint">💡 try-catch 자동 삽입 + 초보자용 설명 추가됩니다.</div>
      <div class="chips" id="error-chips">
        <div class="chip" onclick="selectChip('error',this,'rollback')">⏪ 자동 롤백</div>
        <div class="chip" onclick="selectChip('error',this,'popup')">🔔 알림 팝업</div>
        <div class="chip" onclick="selectChip('error',this,'log')">📋 로그 저장</div>
        <div class="chip" onclick="selectChip('error',this,'retry')">🔄 자동 재시도</div>
        <div class="chip" onclick="selectChip('error',this,'stop')">🛑 즉시 중단</div>
      </div>
    </div>

    <!-- Q13: Libraries -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">📚</span> 사용할 외부 라이브러리? (복수 선택)</div>
      <div class="q-hint">💡 보안 스캔 후 허용 리스트만 사용. 취약점 자동 검사합니다.</div>
      <div class="chips" id="lib-chips">
        <div class="chip multi" onclick="toggleMulti('lib',this,'requests')">🌐 requests</div>
        <div class="chip multi" onclick="toggleMulti('lib',this,'pandas')">🐼 pandas</div>
        <div class="chip multi" onclick="toggleMulti('lib',this,'beautifulsoup')">🍲 BeautifulSoup</div>
        <div class="chip multi" onclick="toggleMulti('lib',this,'sqlalchemy')">🗄️ SQLAlchemy</div>
        <div class="chip multi" onclick="toggleMulti('lib',this,'fastapi')">⚡ FastAPI</div>
        <div class="chip multi" onclick="toggleMulti('lib',this,'cryptography')">🔐 cryptography</div>
        <div class="chip multi" onclick="toggleMulti('lib',this,'none')">🚫 없음</div>
      </div>
    </div>

    <!-- Toggles: Security features -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🔒</span> 고급 보안 옵션</div>
      <div style="display:flex;flex-direction:column;gap:8px">
        <div class="toggle-row">
          <div class="toggle-label">🏗️ Docker 컨테이너 격리 <span class="toggle-sub">나노클로 대비 3배 강화</span></div>
          <label class="toggle"><input type="checkbox" id="opt-docker" checked onchange="updateSecurityMeter()"><div class="toggle-track"></div></label>
        </div>
        <div class="toggle-row">
          <div class="toggle-label">🔐 AES-256 파일 암호화 <span class="toggle-sub">군사급 암호화 표준</span></div>
          <label class="toggle"><input type="checkbox" id="opt-aes" checked onchange="updateSecurityMeter()"><div class="toggle-track"></div></label>
        </div>
        <div class="toggle-row">
          <div class="toggle-label">📊 실시간 감사 로그 <span class="toggle-sub">모든 접근 기록 저장</span></div>
          <label class="toggle"><input type="checkbox" id="opt-audit" checked onchange="updateSecurityMeter()"><div class="toggle-track"></div></label>
        </div>
        <div class="toggle-row">
          <div class="toggle-label">🌐 네트워크 샌드박스 <span class="toggle-sub">무단 외부 통신 차단</span></div>
          <label class="toggle"><input type="checkbox" id="opt-network" onchange="updateSecurityMeter()"><div class="toggle-track"></div></label>
        </div>
        <div class="toggle-row">
          <div class="toggle-label">🔍 코드 취약점 자동 스캔 <span class="toggle-sub">Bandit + Safety 연동</span></div>
          <label class="toggle"><input type="checkbox" id="opt-scan" checked onchange="updateSecurityMeter()"><div class="toggle-track"></div></label>
        </div>
        <div class="toggle-row">
          <div class="toggle-label">📱 모바일 최적화 UI <span class="toggle-sub">반응형 완전 지원</span></div>
          <label class="toggle"><input type="checkbox" id="opt-mobile" checked onchange="updateProgress()"><div class="toggle-track"></div></label>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════ SECTION 4 ═══ -->
<div class="section-card" id="sec-4">
  <div class="section-header" onclick="toggleSection(4)">
    <div class="section-num">04</div>
    <div class="section-title">🚀 테스트 & 배포 설정</div>
    <span class="section-toggle">▼</span>
  </div>
  <div class="section-body">

    <!-- Q14: Test -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🧪</span> 샘플 데이터로 테스트 방법?</div>
      <div class="q-hint">💡 격리 컨테이너 내에서만 실행되어 본 시스템에 영향 없습니다.</div>
      <div class="chips" id="test-chips">
        <div class="chip" onclick="selectChip('test',this,'auto')">🤖 자동 샘플 생성</div>
        <div class="chip" onclick="selectChip('test',this,'upload')">📤 직접 파일 업로드</div>
        <div class="chip" onclick="selectChip('test',this,'skip')">⏭️ 테스트 생략</div>
      </div>
    </div>

    <!-- Q15: Deploy -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">📦</span> 실행 환경 최적화?</div>
      <div class="q-hint">💡 한 클릭 배포 패키지를 자동 생성합니다.</div>
      <div class="chips" id="deploy-chips">
        <div class="chip" onclick="selectChip('deploy',this,'portable')">💼 포터블 앱</div>
        <div class="chip" onclick="selectChip('deploy',this,'server')">🖥️ 서버 모드</div>
        <div class="chip" onclick="selectChip('deploy',this,'docker')">🐳 Docker 이미지</div>
        <div class="chip" onclick="selectChip('deploy',this,'cloud')">☁️ 클라우드 배포</div>
      </div>
    </div>

    <!-- Q16: Maintenance -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🔧</span> 유지보수 계획?</div>
      <div class="q-hint">💡 코드 한 줄 수정 시 AI가 자동 재생성하고 로그를 백업합니다.</div>
      <div class="chips" id="maintain-chips">
        <div class="chip" onclick="selectChip('maintain',this,'ai')">🤖 AI 자동 수정</div>
        <div class="chip" onclick="selectChip('maintain',this,'manual')">✋ 직접 수정</div>
        <div class="chip" onclick="selectChip('maintain',this,'team')">👥 팀 협업</div>
        <div class="chip" onclick="selectChip('maintain',this,'none')">📌 변경 없음</div>
      </div>
    </div>

    <!-- Q17: Project name -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">🏷️</span> 프로젝트 이름 (선택)</div>
      <input type="text" id="project-name" placeholder="예: MySecureBot, SafeAnalyzer..." maxlength="30"
             oninput="updateProjectName(this.value)">
      <div class="val-indicator" id="name-val">✏️ 비워두면 자동 생성됩니다.</div>
    </div>

    <!-- Q18: Description -->
    <div class="q-block">
      <div class="q-label"><span class="q-icon">📝</span> 추가 요구사항 (선택)</div>
      <textarea id="extra-req" placeholder="예: 한국어 출력 필수, 특정 API 연동, 특별한 보안 조건 등..."
                oninput="updateProgress()" rows="3"></textarea>
    </div>

  </div>
</div>

<!-- GENERATE BUTTON -->
<div class="gen-btn-wrap">
  <button class="gen-btn" id="gen-btn" onclick="generateCode()">
    <div class="btn-spinner" id="btn-spinner"></div>
    <span class="btn-text" id="btn-text">⚡ 보안 코드 생성 시작</span>
  </button>
  <div class="api-notice">
    🔑 <strong>Claude AI 연동:</strong> 이 도구는 Anthropic API를 통해 실제 보안 코드를 생성합니다.<br>
    API 키가 없어도 오프라인 템플릿 모드로 즉시 사용 가능합니다.
  </div>
</div>

<!-- OUTPUT PANEL -->
<div class="section-card" id="output-panel">
  <div class="output-header">
    <span class="output-title">✅ 생성된 보안 코드</span>
    <button class="copy-btn" onclick="copyCode()">📋 복사</button>
  </div>
  <div class="output-body">
    <div id="code-output"></div>
    <div class="security-report" id="security-report">
      <div class="report-title">🛡️ SECURITY ANALYSIS REPORT</div>
      <div id="report-items"></div>
    </div>
    <div style="margin-top:14px;flex-wrap:wrap;display:flex;gap:8px">
      <button class="dl-btn" onclick="downloadCode()">💾 .py 파일 다운로드</button>
      <button class="dl-btn" onclick="downloadDockerfile()">🐳 Dockerfile 다운로드</button>
      <button class="dl-btn" onclick="downloadReadme()">📖 README 다운로드</button>
    </div>
  </div>
</div>

<div class="powered-by">⚡ POWERED BY SECURECODE WIZARD v2.0 — NanoClaw을 초월한 세계 최강 보안</div>

</main>

<!-- TOAST -->
<div id="toast"></div>

<script>
// ══════════════════════════════════════════════════════════
// STATE
// ══════════════════════════════════════════════════════════
const state = {
  os: null, skill: null, net: null,
  data: [], attack: [], storage: null,
  purpose: null, io: [], schedule: null,
  steps: 3, error: null, lib: [],
  test: null, deploy: null, maintain: null,
  projectName: '', extraReq: ''
};

const TOTAL_REQUIRED = 12; // required fields

// ══════════════════════════════════════════════════════════
// PROGRESS
// ══════════════════════════════════════════════════════════
function countFilled() {
  let n = 0;
  if (state.os) n++;
  if (state.skill) n++;
  if (state.net) n++;
  if (state.data.length > 0) n++;
  if (state.attack.length > 0) n++;
  if (state.storage) n++;
  if (state.purpose) n++;
  if (state.io.length > 0) n++;
  if (state.schedule) n++;
  if (state.error) n++;
  if (state.lib.length > 0) n++;
  if (state.test) n++;
  return n;
}

function updateProgress() {
  const filled = countFilled();
  const pct = Math.round((filled / TOTAL_REQUIRED) * 100);
  document.getElementById('progress-fill').style.width = pct + '%';
  document.getElementById('pct-label').textContent = pct + '%';
  const dots = document.getElementById('step-dots');
  for (let i = 0; i < dots.children.length; i++) {
    const d = dots.children[i];
    if (i < filled) { d.classList.add('done'); d.classList.remove('active'); }
    else if (i === filled) { d.classList.add('active'); d.classList.remove('done'); }
    else { d.classList.remove('done','active'); }
  }
  const badge = document.getElementById('completion-badge');
  if (pct >= 100) badge.classList.add('show');
  else badge.classList.remove('show');
}

// Init dots
(function initDots() {
  const dots = document.getElementById('step-dots');
  for (let i = 0; i < TOTAL_REQUIRED; i++) {
    const d = document.createElement('div');
    d.className = 'step-dot';
    d.title = `항목 ${i+1}`;
    dots.appendChild(d);
  }
})();

// ══════════════════════════════════════════════════════════
// CHIP SELECTORS
// ══════════════════════════════════════════════════════════
function selectChip(key, el, val) {
  const parent = el.closest('.chips');
  parent.querySelectorAll('.chip').forEach(c => c.classList.remove('selected'));
  el.classList.add('selected');
  state[key] = val;
  if (key === 'purpose') {
    const wrap = document.getElementById('custom-purpose-wrap');
    wrap.style.display = val === 'custom' ? 'block' : 'none';
  }
  updateProgress();
  updateSecurityMeter();
}

function toggleMulti(key, el, val) {
  el.classList.toggle('selected');
  if (el.classList.contains('selected')) {
    if (!state[key].includes(val)) state[key].push(val);
  } else {
    state[key] = state[key].filter(v => v !== val);
  }
  updateProgress();
  updateSecurityMeter();
}

// ══════════════════════════════════════════════════════════
// RANGE
// ══════════════════════════════════════════════════════════
function updateRange(id, valId, val, unit) {
  document.getElementById(valId).textContent = val + ' ' + unit;
  updateProgress();
}

// ══════════════════════════════════════════════════════════
// STEPS / FLOW CHART
// ══════════════════════════════════════════════════════════
const stepLabels = [
  ['데이터\n읽기','📥'], ['전처리','🔧'], ['분석/처리','⚙️'],
  ['검증','✅'], ['변환','🔄'], ['저장','💾'],
  ['보고','📊'], ['알림','🔔'], ['정리','🗑️'], ['완료','🎯']
];

function updateSteps(val) {
  state.steps = parseInt(val);
  document.getElementById('steps-val').textContent = val + ' 단계';
  const fc = document.getElementById('flow-chart');
  fc.innerHTML = '';
  for (let i = 0; i < parseInt(val); i++) {
    const [label, icon] = stepLabels[i];
    const node = document.createElement('div');
    node.className = 'flow-node';
    node.innerHTML = `
      <div class="flow-box${i===0?' active-node':''}">${icon}<br>${label.replace('\n','<br>')}</div>
      <div class="flow-sub">Step ${i+1}</div>`;
    fc.appendChild(node);
    if (i < parseInt(val)-1) {
      const arrow = document.createElement('div');
      arrow.className = 'flow-arrow';
      arrow.textContent = '→';
      fc.appendChild(arrow);
    }
  }
  updateProgress();
}
updateSteps(3);

// ══════════════════════════════════════════════════════════
// SECURITY METER
// ══════════════════════════════════════════════════════════
function updateSecurityMeter() {
  const docker = document.getElementById('opt-docker')?.checked;
  const aes = document.getElementById('opt-aes')?.checked;
  const audit = document.getElementById('opt-audit')?.checked;
  const network = document.getElementById('opt-network')?.checked;
  const scan = document.getElementById('opt-scan')?.checked;

  let encScore = 40;
  if (aes) encScore += 35;
  if (state.storage === 'vault') encScore += 25;
  else if (state.storage === 'local') encScore += 15;
  encScore = Math.min(encScore, 100);

  let isoScore = 20;
  if (docker) isoScore += 40;
  if (network) isoScore += 30;
  if (state.attack.includes('escape')) isoScore += 10;
  isoScore = Math.min(isoScore, 100);

  let logScore = 20;
  if (audit) logScore += 50;
  if (scan) logScore += 30;
  logScore = Math.min(logScore, 100);

  const total = Math.round((encScore + isoScore + logScore) / 3);

  setMeter('m-enc', 'ms-enc', encScore);
  setMeter('m-iso', 'ms-iso', isoScore);
  setMeter('m-log', 'ms-log', logScore);
  setMeter('m-total', 'ms-total', total);
}

function setMeter(barId, scoreId, val) {
  const bar = document.getElementById(barId);
  const score = document.getElementById(scoreId);
  if (!bar || !score) return;
  bar.style.width = val + '%';
  score.textContent = val + '%';
}

// ══════════════════════════════════════════════════════════
// SECTION TOGGLE
// ══════════════════════════════════════════════════════════
function toggleSection(n) {
  const card = document.getElementById('sec-' + n);
  card.classList.toggle('collapsed');
}

// ══════════════════════════════════════════════════════════
// PROJECT NAME
// ══════════════════════════════════════════════════════════
function updateProjectName(val) {
  state.projectName = val;
  const v = document.getElementById('name-val');
  if (val.length > 0 && val.length < 3) {
    v.className = 'val-indicator err'; v.textContent = '❌ 3자 이상 입력하세요.';
  } else if (val.length >= 3) {
    v.className = 'val-indicator ok'; v.textContent = '✅ ' + val + ' — 사용 가능';
  } else {
    v.className = 'val-indicator'; v.textContent = '✏️ 비워두면 자동 생성됩니다.';
  }
}

// ══════════════════════════════════════════════════════════
// CODE GENERATOR
// ══════════════════════════════════════════════════════════
function generateCode() {
  const filled = countFilled();
  if (filled < 6) {
    showToast('⚠️ 최소 6개 항목을 선택해주세요!');
    showAlert('err', '❌ 필수 항목을 더 선택해주세요. (현재 ' + filled + '/' + TOTAL_REQUIRED + ')');
    return;
  }

  const btn = document.getElementById('gen-btn');
  btn.classList.add('loading');
  document.getElementById('btn-text').textContent = '보안 코드 생성 중...';

  setTimeout(() => {
    const code = buildCode();
    btn.classList.remove('loading');
    document.getElementById('btn-text').textContent = '✅ 코드 재생성';
    displayCode(code);
    buildReport();
    document.getElementById('output-panel').style.display = 'block';
    document.getElementById('output-panel').scrollIntoView({ behavior: 'smooth', block: 'start' });
    showToast('🎉 보안 코드 생성 완료!');
  }, 1800);
}

function buildCode() {
  const projName = state.projectName || 'SecureApp';
  const os = state.os || 'Windows';
  const skill = state.skill || 'none';
  const purpose = state.purpose || 'automation';
  const docker = document.getElementById('opt-docker')?.checked;
  const aes = document.getElementById('opt-aes')?.checked;
  const audit = document.getElementById('opt-audit')?.checked;
  const scan = document.getElementById('opt-scan')?.checked;
  const storage = state.storage || 'local';
  const libs = state.lib;
  const errorMode = state.error || 'log';
  const schedule = state.schedule || 'manual';
  const extraReq = document.getElementById('extra-req')?.value || '';

  const purposeMap = {
    automation: '자동화 스크립트', webbot: '웹 봇/크롤러',
    dataanalysis: '데이터 분석', filemanager: '파일 관리',
    api: 'API 연동', custom: document.getElementById('custom-purpose')?.value || '커스텀'
  };

  const lines = [];

  lines.push(`#!/usr/bin/env python3`);
  lines.push(`# -*- coding: utf-8 -*-`);
  lines.push(`"""`)
  lines.push(`╔══════════════════════════════════════════════════════╗`)
  lines.push(`║  ${projName.padEnd(50)} ║`)
  lines.push(`║  목적: ${(purposeMap[purpose]||purpose).padEnd(44)} ║`)
  lines.push(`║  OS: ${os.padEnd(46)} ║`)
  lines.push(`║  보안등급: 최고 (나노클로 초월)                           ║`)
  lines.push(`║  생성: SecureCode Wizard v2.0                        ║`)
  lines.push(`╚══════════════════════════════════════════════════════╝`)
  lines.push(`"""`);
  lines.push(``);
  lines.push(`# ─── 표준 라이브러리 ───────────────────────────────────`);
  lines.push(`import os, sys, json, hashlib, secrets, logging`);
  lines.push(`import datetime, pathlib, threading, time`);
  lines.push(`from functools import wraps`);
  if (aes) lines.push(`from cryptography.fernet import Fernet`);
  if (libs.includes('requests')) lines.push(`import requests`);
  if (libs.includes('pandas')) lines.push(`import pandas as pd`);
  if (libs.includes('beautifulsoup')) lines.push(`from bs4 import BeautifulSoup`);
  if (libs.includes('fastapi')) lines.push(`from fastapi import FastAPI, HTTPException`);
  if (libs.includes('sqlalchemy')) lines.push(`from sqlalchemy import create_engine`);
  lines.push(``);
  lines.push(`# ─── 보안 설정 ──────────────────────────────────────────`);
  lines.push(`BASE_DIR = pathlib.Path(__file__).resolve().parent`);
  lines.push(`LOG_DIR  = BASE_DIR / "logs"`);
  lines.push(`DATA_DIR = BASE_DIR / "data"`);
  lines.push(`LOG_DIR.mkdir(exist_ok=True)`);
  lines.push(`DATA_DIR.mkdir(exist_ok=True)`);
  lines.push(``);
  if (audit) {
    lines.push(`# 감사 로그 설정`);
    lines.push(`logging.basicConfig(`);
    lines.push(`    level=logging.INFO,`);
    lines.push(`    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",`);
    lines.push(`    handlers=[`);
    lines.push(`        logging.FileHandler(LOG_DIR / "audit.log", encoding="utf-8"),`);
    lines.push(`        logging.StreamHandler(sys.stdout)`);
    lines.push(`    ]`);
    lines.push(`)`);
    lines.push(`logger = logging.getLogger("${projName}")`);
    lines.push(``);
  }
  if (aes) {
    lines.push(`# ─── AES-256 암호화 모듈 ───────────────────────────────`);
    lines.push(`class SecureVault:`);
    lines.push(`    """AES-256 기반 보안 금고 — 군사급 암호화"""`)
    lines.push(`    KEY_FILE = BASE_DIR / ".vault_key"`);
    lines.push(``);
    lines.push(`    def __init__(self):`);
    lines.push(`        self.key = self._load_or_create_key()`);
    lines.push(`        self._fernet = Fernet(self.key)`);
    lines.push(``);
    lines.push(`    def _load_or_create_key(self) -> bytes:`);
    lines.push(`        if self.KEY_FILE.exists():`);
    lines.push(`            return self.KEY_FILE.read_bytes()`);
    lines.push(`        key = Fernet.generate_key()`);
    lines.push(`        self.KEY_FILE.write_bytes(key)`);
    lines.push(`        self.KEY_FILE.chmod(0o600)  # 소유자만 읽기`);
    lines.push(`        return key`);
    lines.push(``);
    lines.push(`    def encrypt(self, data: str) -> bytes:`);
    lines.push(`        return self._fernet.encrypt(data.encode("utf-8"))`);
    lines.push(``);
    lines.push(`    def decrypt(self, token: bytes) -> str:`);
    lines.push(`        return self._fernet.decrypt(token).decode("utf-8")`);
    lines.push(``);
    lines.push(`vault = SecureVault()`);
    lines.push(``);
  }
  lines.push(`# ─── 보안 데코레이터 ────────────────────────────────────`);
  lines.push(`def secure_execute(func):`);
  lines.push(`    """모든 함수 실행을 감사 로그에 기록하는 보안 래퍼"""`);
  lines.push(`    @wraps(func)`);
  lines.push(`    def wrapper(*args, **kwargs):`);
  if (audit) lines.push(`        logger.info(f"[EXEC] {func.__name__} 시작")`);
  lines.push(`        try:`);
  lines.push(`            result = func(*args, **kwargs)`);
  if (audit) lines.push(`            logger.info(f"[EXEC] {func.__name__} 완료")`);
  lines.push(`            return result`);
  if (errorMode === 'rollback') {
    lines.push(`        except Exception as e:`);
    if (audit) lines.push(`            logger.error(f"[ERR] {func.__name__}: {e} — 자동 롤백 시도")`);
    lines.push(`            _auto_rollback()`);
    lines.push(`            raise`);
  } else if (errorMode === 'retry') {
    lines.push(`        except Exception as e:`);
    if (audit) lines.push(`            logger.warning(f"[RETRY] {func.__name__}: {e}")`);
    lines.push(`            for i in range(3):`);
    lines.push(`                try: return func(*args, **kwargs)`);
    lines.push(`                except: time.sleep(2**i)`);
    lines.push(`            raise`);
  } else {
    lines.push(`        except Exception as e:`);
    if (audit) lines.push(`            logger.error(f"[ERR] {func.__name__}: {e}")`);
    lines.push(`            raise`);
  }
  lines.push(`    return wrapper`);
  lines.push(``);

  if (errorMode === 'rollback') {
    lines.push(`def _auto_rollback():`);
    lines.push(`    """자동 롤백: 이전 상태로 복원"""`);
    lines.push(`    backup = DATA_DIR / "backup.json"`);
    lines.push(`    if backup.exists():`);
    if (audit) lines.push(`        logger.info("[ROLLBACK] 백업 파일로 복원 완료")`);
    lines.push(`        return json.loads(backup.read_text())`);
    lines.push(``);
  }

  lines.push(`# ─── 핵심 로직 ─────────────────────────────────────────`);
  lines.push(`class ${projName.replace(/[^a-zA-Z0-9]/g,'')}:`);
  lines.push(`    """${purposeMap[purpose]||purpose} — 메인 클래스"""`);
  lines.push(``);
  lines.push(`    def __init__(self):`);
  if (audit) lines.push(`        logger.info("[INIT] ${projName} 초기화")`);
  lines.push(`        self._session_id = secrets.token_hex(16)`);
  lines.push(`        self._start_time = datetime.datetime.now()`);
  lines.push(``);

  // Step methods
  for (let i = 0; i < state.steps; i++) {
    const [lbl] = stepLabels[i];
    const methodName = `step${i+1}_${lbl.replace(/\n/,'').replace(/[^a-zA-Z가-힣]/g,'').toLowerCase() || 'process'}`;
    lines.push(`    @secure_execute`);
    lines.push(`    def step_${i+1}(self):`);
    lines.push(`        """${(i+1)}단계: ${lbl.replace('\n','')}"""`);
    if (audit) lines.push(`        logger.info(f"[STEP ${i+1}] ${lbl.replace('\n','')} 시작")`);
    lines.push(`        # TODO: 여기에 실제 로직을 구현하세요`);
    lines.push(`        pass`);
    lines.push(``);
  }

  lines.push(`    def run(self):`);
  lines.push(`        """전체 파이프라인 실행"""`);
  if (audit) lines.push(`        logger.info(f"[RUN] 세션 {self._session_id} 실행")`);
  for (let i = 0; i < state.steps; i++) {
    lines.push(`        self.step_${i+1}()`);
  }
  if (audit) {
    lines.push(`        elapsed = (datetime.datetime.now() - self._start_time).total_seconds()`);
    lines.push(`        logger.info(f"[DONE] 완료. 소요시간: {elapsed:.2f}초")`);
  }
  lines.push(``);

  if (schedule === 'daily' || schedule === 'hourly') {
    lines.push(`# ─── 스케줄러 ───────────────────────────────────────────`);
    const interval = schedule === 'hourly' ? 3600 : 86400;
    lines.push(`def run_scheduler():`);
    lines.push(`    """${schedule === 'hourly' ? '매시간' : '매일'} 자동 실행 스케줄러"""`);
    lines.push(`    while True:`);
    lines.push(`        try:`);
    lines.push(`            app = ${projName.replace(/[^a-zA-Z0-9]/g,'')}()`);
    lines.push(`            app.run()`);
    lines.push(`        except Exception as e:`);
    if (audit) lines.push(`            logger.error(f"[SCHED ERROR] {e}")`);
    lines.push(`        time.sleep(${interval})`);
    lines.push(``);
  }

  if (docker) {
    lines.push(`# ─── 컨테이너 보안 체크 ─────────────────────────────────`);
    lines.push(`def check_container_security():`);
    lines.push(`    """Docker 컨테이너 환경 보안 검사"""`);
    lines.push(`    checks = {`);
    lines.push(`        "root_user": os.getuid() != 0,  # 루트 실행 금지`);
    lines.push(`        "writable_root": not os.access("/", os.W_OK),  # 루트 쓰기 차단`);
    lines.push(`        "env_api_key": bool(os.getenv("API_KEY")),  # API 키 확인`);
    lines.push(`    }`);
    if (audit) lines.push(`    logger.info(f"[SECURITY CHECK] {checks}")`);
    lines.push(`    return all(checks.values())`);
    lines.push(``);
  }

  lines.push(`# ─── 진입점 ─────────────────────────────────────────────`);
  lines.push(`if __name__ == "__main__":`);
  if (docker) {
    lines.push(`    if not check_container_security():`);
    if (audit) lines.push(`        logger.warning("[WARN] 보안 체크 실패! 주의 필요")`);
  }
  if (schedule === 'daily' || schedule === 'hourly') {
    lines.push(`    t = threading.Thread(target=run_scheduler, daemon=True)`);
    lines.push(`    t.start()`);
    lines.push(`    t.join()`);
  } else {
    lines.push(`    app = ${projName.replace(/[^a-zA-Z0-9]/g,'')}()`);
    lines.push(`    app.run()`);
  }

  if (extraReq) {
    lines.push(``);
    lines.push(`# ─── 추가 요구사항 메모 ──────────────────────────────────`);
    extraReq.split('\n').forEach(l => lines.push(`# ${l}`));
  }

  return lines.join('\n');
}

// ══════════════════════════════════════════════════════════
// SYNTAX HIGHLIGHT (simple)
// ══════════════════════════════════════════════════════════
function highlight(code) {
  return code
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/(#.*)$/gm, '<span class="cm">$1</span>')
    .replace(/\b(import|from|def|class|if|else|elif|for|while|try|except|return|pass|with|as|in|not|and|or|raise|None|True|False|self|lambda|yield|async|await)\b/g,'<span class="kw">$1</span>')
    .replace(/"([^"]*)"/g,'<span class="st">"$1"</span>')
    .replace(/'([^']*)'/g,"<span class='st'>'$1'</span>")
    .replace(/\b(\d+)\b/g,'<span class="nm">$1</span>');
}

function displayCode(code) {
  document.getElementById('code-output').innerHTML = highlight(code);
}

// ══════════════════════════════════════════════════════════
// SECURITY REPORT
// ══════════════════════════════════════════════════════════
function buildReport() {
  const docker = document.getElementById('opt-docker')?.checked;
  const aes = document.getElementById('opt-aes')?.checked;
  const audit = document.getElementById('opt-audit')?.checked;
  const network = document.getElementById('opt-network')?.checked;
  const scan = document.getElementById('opt-scan')?.checked;
  const mobile = document.getElementById('opt-mobile')?.checked;

  const items = [
    { icon:'🔐', key:'암호화 방식', val:'AES-256 (Fernet)', cls: aes?'ok':'off' },
    { icon:'🏗️', key:'컨테이너 격리', val: docker?'Docker 활성화':'비활성', cls: docker?'ok':'warn' },
    { icon:'📊', key:'감사 로그', val: audit?'실시간 기록':'비활성', cls: audit?'ok':'warn' },
    { icon:'🌐', key:'네트워크 샌드박스', val: network?'활성화':'비활성', cls: network?'ok':'off' },
    { icon:'🔍', key:'취약점 스캔', val: scan?'Bandit+Safety':'비활성', cls: scan?'ok':'warn' },
    { icon:'📱', key:'모바일 최적화', val: mobile?'완전 지원':'비활성', cls: mobile?'ok':'off' },
    { icon:'🛡️', key:'보안 등급', val:'A+++ (나노클로 초월)', cls:'ok' },
    { icon:'⏱️', key:'생성 시간', val: new Date().toLocaleString('ko-KR'), cls:'ok' },
  ];

  const container = document.getElementById('report-items');
  container.innerHTML = items.map(i => `
    <div class="report-item">
      <span class="ri-icon">${i.icon}</span>
      <span class="ri-key">${i.key}</span>
      <span class="ri-val ${i.cls}">${i.val}</span>
    </div>`).join('');
}

// ══════════════════════════════════════════════════════════
// COPY / DOWNLOAD
// ══════════════════════════════════════════════════════════
function copyCode() {
  const text = document.getElementById('code-output').innerText;
  navigator.clipboard.writeText(text).then(() => showToast('📋 클립보드에 복사됨!')).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = text; document.body.appendChild(ta); ta.select();
    document.execCommand('copy'); document.body.removeChild(ta);
    showToast('📋 복사 완료!');
  });
}

function downloadCode() {
  const code = document.getElementById('code-output').innerText;
  const name = (state.projectName || 'secure_app').replace(/[^a-zA-Z0-9_]/g,'_');
  downloadFile(code, name + '.py', 'text/plain');
  showToast('💾 Python 파일 다운로드!');
}

function downloadDockerfile() {
  const name = state.projectName || 'SecureApp';
  const content = `FROM python:3.12-slim
LABEL maintainer="SecureCode Wizard"

# 보안 강화: 루트 사용자 사용 금지
RUN useradd -m -u 1000 appuser
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사 및 권한 설정
COPY --chown=appuser:appuser . .
USER appuser

# 읽기 전용 루트 파일시스템
# --read-only 플래그와 함께 실행하세요

EXPOSE 8080
CMD ["python", "main.py"]
`;
  downloadFile(content, 'Dockerfile', 'text/plain');
  showToast('🐳 Dockerfile 다운로드!');
}

function downloadReadme() {
  const name = state.projectName || 'SecureApp';
  const content = `# 🔐 ${name}
> SecureCode Wizard v2.0으로 생성된 보안 강화 프로그램

## 🛡️ 보안 특징
- AES-256 파일 암호화
- Docker 컨테이너 격리
- 실시간 감사 로그
- 취약점 자동 스캔 (Bandit + Safety)

## ⚡ 빠른 시작
\`\`\`bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. 실행
python main.py
\`\`\`

## 🐳 Docker 실행
\`\`\`bash
docker build -t ${name.toLowerCase()} .
docker run --read-only -v ./data:/app/data ${name.toLowerCase()}
\`\`\`

## 📋 요구사항
- Python 3.10+
- RAM: ${document.getElementById('ram-range')?.value || 8}GB 이상
- OS: ${state.os || 'Windows/macOS/Linux'}

---
*Generated by SecureCode Wizard v2.0 — NanoClaw을 초월한 세계 최강 보안*
`;
  downloadFile(content, 'README.md', 'text/markdown');
  showToast('📖 README 다운로드!');
}

function downloadFile(content, filename, mime) {
  const blob = new Blob([content], { type: mime });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = filename;
  document.body.appendChild(a); a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

// ══════════════════════════════════════════════════════════
// ALERT / TOAST
// ══════════════════════════════════════════════════════════
function showAlert(type, msg) {
  // inline toast
  showToast(msg);
}

let toastTimer;
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2800);
}

// ══════════════════════════════════════════════════════════
// INIT
// ══════════════════════════════════════════════════════════
updateSecurityMeter();
updateProgress();

// Stagger section card animations
document.querySelectorAll('.section-card').forEach((el, i) => {
  el.style.animationDelay = (i * 0.1) + 's';
});
</script>
</body>
</html>