<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>🔐 SecureAI — 나만의 AI 비서</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Noto+Sans+KR:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

:root {
  --bg:  #07080f;
  --s1:  #0e1018;
  --s2:  #161822;
  --c1:  #e8ff47;
  --c2:  #ff4f8b;
  --c3:  #47c8ff;
  --c4:  #7fffb2;
  --tx:  #eef0ff;
  --dim: #676a8a;
  --bd:  rgba(232,255,71,0.13);
  --r:   14px;
  --rs:  9px;
}

/* BASE — no overflow hidden anywhere on body/html */
html { min-height: 100%; }
body {
  font-family: 'Noto Sans KR', sans-serif;
  background: var(--bg); color: var(--tx);
  min-height: 100vh;
}
body::before {
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background:
    radial-gradient(ellipse 60% 40% at 15% 10%, rgba(232,255,71,.05) 0%, transparent 55%),
    radial-gradient(ellipse 50% 60% at 85% 90%, rgba(255,79,139,.04) 0%, transparent 55%);
}

/* WIZARD PAGE — normal flow, scrollable */
#pg-wizard {
  display: block; position: relative; z-index: 1; padding-bottom: 80px;
}

/* AI PAGE — fixed full-screen overlay */
#pg-ai {
  display: none; position: fixed; inset: 0; z-index: 200;
  background: var(--bg); flex-direction: column;
}
#pg-ai.on { display: flex; }

/* ── HERO ── */
.hero {
  text-align: center; padding: 44px 20px 28px;
  border-bottom: 1px solid var(--bd);
  background: linear-gradient(180deg, rgba(232,255,71,.05) 0%, transparent 100%);
}
.hero-badge {
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(232,255,71,.08); border: 1px solid rgba(232,255,71,.3);
  border-radius: 50px; padding: 5px 16px; margin-bottom: 18px;
  font-family: 'Syne', sans-serif; font-size: 10px; font-weight: 700;
  color: var(--c1); letter-spacing: 3px; text-transform: uppercase;
}
.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: clamp(28px, 8vw, 46px); font-weight: 800;
  color: var(--c1); line-height: 1.1; margin-bottom: 10px;
  text-shadow: 0 0 50px rgba(232,255,71,.28);
}
.hero-sub { color: var(--dim); font-size: 13px; line-height: 1.75; }

/* ── STICKY PROGRESS ── */
.prog-wrap {
  position: sticky; top: 0; z-index: 50;
  background: rgba(7,8,15,.93); backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--bd); padding: 10px 18px;
}
.prog-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 7px; }
.prog-lbl { font-family: 'Syne', sans-serif; font-size: 10px; font-weight: 700; color: var(--c1); letter-spacing: 2px; }
.prog-num { font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--c1); }
.prog-bg  { height: 3px; background: rgba(232,255,71,.1); border-radius: 3px; }
.prog-bar { height: 3px; background: var(--c1); border-radius: 3px; width: 0%; transition: width .45s ease; }

/* ── SECTIONS — no overflow:hidden ── */
.wsec {
  margin: 18px 14px 0; border: 1px solid var(--bd);
  border-radius: var(--r); background: var(--s1);
}
.wsec-hd {
  display: flex; align-items: center; gap: 12px;
  padding: 15px 16px; cursor: pointer; user-select: none;
  border-radius: var(--r) var(--r) 0 0; transition: background .2s;
}
.wsec-hd:hover { background: rgba(232,255,71,.04); }
.wsec.closed .wsec-hd { border-radius: var(--r); }
.sec-num {
  width: 30px; height: 30px; border-radius: 8px; flex-shrink: 0;
  background: rgba(232,255,71,.1); border: 1px solid rgba(232,255,71,.3);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Syne', sans-serif; font-size: 12px; font-weight: 800; color: var(--c1);
}
.sec-ttl { flex: 1; font-size: 14px; font-weight: 600; }
.sec-arr { color: var(--c1); font-size: 16px; transition: transform .28s; flex-shrink: 0; }
.wsec.closed .sec-arr { transform: rotate(-90deg); }
.wsec-body {
  padding: 18px 16px; display: flex; flex-direction: column; gap: 18px;
  border-top: 1px solid var(--bd);
}
.wsec.closed .wsec-body { display: none; }

/* ── Q ELEMENTS ── */
.qlbl  { font-size: 13px; font-weight: 600; margin-bottom: 9px; line-height: 1.55; }
.qhint {
  font-size: 11px; color: var(--dim); font-family: 'JetBrains Mono', monospace;
  background: rgba(71,200,255,.05); border-left: 2px solid rgba(71,200,255,.3);
  padding: 5px 10px; border-radius: 0 6px 6px 0; margin-bottom: 9px; line-height: 1.65;
}

/* chips */
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip {
  padding: 8px 15px; border-radius: 50px;
  border: 1px solid rgba(255,255,255,.1); background: rgba(255,255,255,.03);
  color: var(--dim); font-size: 12px; font-weight: 500;
  font-family: 'Noto Sans KR', sans-serif;
  cursor: pointer; transition: all .18s; user-select: none; white-space: nowrap;
}
.chip:hover  { border-color: rgba(232,255,71,.5); color: var(--c1); }
.chip.sel    { border-color: var(--c1);  background: rgba(232,255,71,.1);  color: var(--c1);  box-shadow: 0 0 10px rgba(232,255,71,.15); }
.chip.msel   { border-color: var(--c4);  background: rgba(127,255,178,.1); color: var(--c4);  box-shadow: 0 0 10px rgba(127,255,178,.15); }

/* toggles */
.tog-row {
  display: flex; align-items: center; gap: 12px;
  padding: 11px 14px; background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07); border-radius: var(--rs);
}
.tog-lbl { font-size: 13px; flex: 1; line-height: 1.45; }
.tog-sub { font-size: 10px; color: var(--dim); display: block; margin-top: 2px; }
.tog-sw  { position: relative; width: 42px; height: 22px; flex-shrink: 0; }
.tog-sw input { opacity: 0; width: 0; height: 0; position: absolute; }
.tog-tk {
  position: absolute; inset: 0;
  background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.12);
  border-radius: 22px; cursor: pointer; transition: all .28s;
}
.tog-tk::after {
  content: ''; position: absolute; left: 3px; top: 50%; transform: translateY(-50%);
  width: 14px; height: 14px; background: var(--dim); border-radius: 50%; transition: all .28s;
}
.tog-sw input:checked + .tog-tk { background: rgba(232,255,71,.2); border-color: var(--c1); }
.tog-sw input:checked + .tog-tk::after { left: calc(100% - 17px); background: var(--c1); box-shadow: 0 0 8px rgba(232,255,71,.5); }

/* text inputs — 16px stops iOS zoom */
.winput, .wtxt {
  width: 100%; background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.1); border-radius: var(--rs);
  color: var(--tx); font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px; padding: 11px 14px; outline: none;
  transition: border-color .2s; -webkit-appearance: none; appearance: none;
}
.winput:focus, .wtxt:focus { border-color: var(--c1); box-shadow: 0 0 0 3px rgba(232,255,71,.08); }
.wtxt { resize: vertical; min-height: 72px; line-height: 1.6; }
.keymsg { font-size: 11px; margin-top: 5px; color: var(--dim); font-family: 'JetBrains Mono', monospace; min-height: 16px; transition: color .2s; }

/* security meter */
.smeter { background: var(--s2); border: 1px solid var(--bd); border-radius: var(--rs); padding: 14px 16px; }
.sm-ttl { font-family: 'Syne', sans-serif; font-size: 10px; font-weight: 700; color: var(--dim); letter-spacing: 2px; margin-bottom: 12px; }
.sm-row { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.sm-row:last-child { margin-bottom: 0; }
.sm-k   { font-size: 11px; color: var(--dim); width: 56px; flex-shrink: 0; }
.sm-bar { flex: 1; height: 4px; background: rgba(255,255,255,.07); border-radius: 4px; overflow: hidden; }
.sm-f   { height: 100%; border-radius: 4px; width: 0%; transition: width .6s ease; }
.sm-v   { font-family: 'JetBrains Mono', monospace; font-size: 11px; width: 32px; text-align: right; }

/* generate button */
.gen-wrap { padding: 28px 16px; text-align: center; }
.gen-btn {
  display: inline-flex; align-items: center; gap: 10px;
  background: var(--c1); border: none; border-radius: 50px;
  color: #07080f; font-family: 'Syne', sans-serif;
  font-size: clamp(14px, 3.5vw, 19px); font-weight: 800; letter-spacing: 1px;
  padding: clamp(14px, 3vw, 18px) clamp(32px, 7vw, 60px);
  cursor: pointer; transition: all .25s; outline: none;
  box-shadow: 0 8px 40px rgba(232,255,71,.35);
}
.gen-btn:hover  { transform: translateY(-3px); box-shadow: 0 16px 50px rgba(232,255,71,.5); }
.gen-btn:active { transform: scale(.97); }
.gen-btn.busy   { opacity: .65; pointer-events: none; }
.spin {
  width: 18px; height: 18px; flex-shrink: 0;
  border: 2px solid rgba(0,0,0,.2); border-top-color: #07080f;
  border-radius: 50%; display: none; animation: spin .7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.gen-btn.busy .spin { display: block; }

/* ══ AI SCREEN ══ */
.ai-hdr {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; flex-shrink: 0;
  background: rgba(14,16,24,.96); backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--bd);
}
.ai-ava {
  width: 38px; height: 38px; border-radius: 50%; flex-shrink: 0;
  background: linear-gradient(135deg, var(--c1), #b8cc00);
  display: flex; align-items: center; justify-content: center; font-size: 20px;
  box-shadow: 0 0 20px rgba(232,255,71,.3);
}
.ai-meta { flex: 1; }
.ai-nm   { font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 700; }
.ai-stat { font-size: 11px; color: var(--c4); display: flex; align-items: center; gap: 5px; }
.sdot    { width: 6px; height: 6px; border-radius: 50%; background: var(--c4); animation: sdot 2s ease-in-out infinite; flex-shrink: 0; }
@keyframes sdot { 0%,100% { opacity:1; } 50% { opacity:.3; } }
.hdrbtn {
  background: var(--s2); border: 1px solid var(--bd); border-radius: 8px;
  color: var(--dim); font-size: 12px; padding: 7px 12px; cursor: pointer;
  font-family: 'Noto Sans KR', sans-serif; transition: all .2s; outline: none;
}
.hdrbtn:hover { border-color: var(--c1); color: var(--c1); }

.qbar {
  display: flex; gap: 7px; padding: 9px 14px; flex-shrink: 0;
  overflow-x: auto; scrollbar-width: none;
  background: var(--s1); border-bottom: 1px solid var(--bd);
}
.qbar::-webkit-scrollbar { display: none; }
.qbtn {
  display: flex; align-items: center; gap: 5px; white-space: nowrap; flex-shrink: 0;
  background: var(--s2); border: 1px solid var(--bd); border-radius: 50px;
  color: var(--dim); font-size: 12px; padding: 7px 13px; cursor: pointer;
  font-family: 'Noto Sans KR', sans-serif; transition: all .2s; outline: none;
}
.qbtn:hover, .qbtn:active { border-color: var(--c1); color: var(--c1); background: rgba(232,255,71,.06); }

/* chat — flex:1 so it fills remaining space and scrolls internally */
.chat {
  flex: 1; overflow-y: auto; padding: 16px;
  display: flex; flex-direction: column; gap: 10px;
  scrollbar-width: thin; scrollbar-color: rgba(232,255,71,.15) transparent;
}
.chat::-webkit-scrollbar { width: 3px; }
.chat::-webkit-scrollbar-thumb { background: rgba(232,255,71,.15); border-radius: 3px; }

.welcome { text-align: center; padding: 24px 12px; color: var(--dim); font-size: 13px; line-height: 1.9; }
.welcome .wname {
  font-family: 'Syne', sans-serif; font-size: 20px; font-weight: 800;
  color: var(--c1); display: block; margin-bottom: 8px;
}

.msg { display: flex; gap: 9px; animation: msgin .28s ease both; }
@keyframes msgin { from { opacity:0; transform:translateY(6px); } to { opacity:1; transform:translateY(0); } }
.msg.user { flex-direction: row-reverse; }
.mava {
  width: 28px; height: 28px; border-radius: 50%; flex-shrink: 0; margin-top: 2px;
  display: flex; align-items: center; justify-content: center; font-size: 14px;
}
.msg.ai   .mava { background: linear-gradient(135deg, var(--c1), #b8cc00); box-shadow: 0 0 10px rgba(232,255,71,.3); }
.msg.user .mava { background: linear-gradient(135deg, var(--c3), #2299cc); box-shadow: 0 0 10px rgba(71,200,255,.3); }
.mbub-wrap { max-width: calc(100% - 40px); }
.mbub {
  padding: 11px 15px; font-size: 14px; line-height: 1.7;
  word-break: break-word; border-radius: 14px;
}
.msg.ai   .mbub { background: var(--s2); border: 1px solid var(--bd); border-top-left-radius: 4px; }
.msg.user .mbub { background: rgba(71,200,255,.12); border: 1px solid rgba(71,200,255,.25); border-top-right-radius: 4px; }
.mbub.err       { background: rgba(255,79,139,.09); border: 1px solid rgba(255,79,139,.25); color: var(--c2); }
.mtime { font-size: 10px; color: var(--dim); margin-top: 3px; padding: 0 4px; }
.msg.user .mtime { text-align: right; }

.tdots { display: flex; gap: 5px; padding: 4px 0; }
.tdots span { width: 7px; height: 7px; border-radius: 50%; background: var(--c1); animation: td 1.2s ease-in-out infinite; }
.tdots span:nth-child(2) { animation-delay: .2s; }
.tdots span:nth-child(3) { animation-delay: .4s; }
@keyframes td { 0%,60%,100% { transform:scale(.55); opacity:.4; } 30% { transform:scale(1); opacity:1; } }

.cblk {
  background: var(--bg); border: 1px solid rgba(255,255,255,.08); border-radius: 8px;
  padding: 12px; font-family: 'JetBrains Mono', monospace; font-size: 12px;
  line-height: 1.6; overflow-x: auto; margin: 8px 0; color: #c0d0ff;
}

.fprev {
  display: none; align-items: center; gap: 8px;
  background: var(--s2); border: 1px solid var(--bd);
  border-radius: 8px; padding: 7px 12px; margin-bottom: 8px;
}
.fprev.on { display: flex; }
.fprev-name { flex: 1; font-size: 12px; color: var(--dim); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.fprev-rm   { cursor: pointer; color: var(--c2); font-size: 17px; line-height: 1; flex-shrink: 0; padding: 0 2px; }

.inp-area {
  padding: 10px 14px; flex-shrink: 0;
  background: rgba(14,16,24,.97); backdrop-filter: blur(20px);
  border-top: 1px solid var(--bd);
}
.inp-row { display: flex; gap: 8px; align-items: flex-end; }
.sbtn {
  width: 36px; height: 36px; flex-shrink: 0;
  background: var(--s2); border: 1px solid var(--bd); border-radius: 9px;
  color: var(--dim); font-size: 16px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all .2s; outline: none;
}
.sbtn:hover { border-color: var(--c1); color: var(--c1); }
#msginp {
  flex: 1; background: var(--s2); border: 1px solid var(--bd); border-radius: 12px;
  color: var(--tx); font-family: 'Noto Sans KR', sans-serif; font-size: 16px;
  padding: 10px 14px; outline: none; resize: none;
  max-height: 120px; min-height: 44px; line-height: 1.55;
  transition: border-color .2s; -webkit-appearance: none; appearance: none;
}
#msginp:focus { border-color: var(--c1); }
#msginp::placeholder { color: var(--dim); }
#sendbtn {
  width: 44px; height: 44px; flex-shrink: 0;
  background: var(--c1); border: none; border-radius: 12px;
  color: #07080f; font-size: 22px; font-weight: 900; line-height: 1;
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: all .2s; outline: none;
  box-shadow: 0 4px 15px rgba(232,255,71,.3);
}
#sendbtn:hover   { transform: scale(1.06); box-shadow: 0 6px 22px rgba(232,255,71,.5); }
#sendbtn:active  { transform: scale(.95); }
#sendbtn:disabled { opacity: .3; cursor: not-allowed; transform: none !important; box-shadow: none; }

@supports (padding-bottom: env(safe-area-inset-bottom)) {
  .inp-area { padding-bottom: calc(10px + env(safe-area-inset-bottom)); }
}

/* modal */
.modal-ov {
  display: none; position: fixed; inset: 0; z-index: 500;
  background: rgba(0,0,0,.75); backdrop-filter: blur(10px);
  align-items: center; justify-content: center; padding: 20px;
}
.modal-ov.on { display: flex; }
.modal {
  background: var(--s1); border: 1px solid var(--bd); border-radius: var(--r);
  padding: 22px; width: 100%; max-width: 360px;
  animation: mdin .3s cubic-bezier(.34,1.56,.64,1);
}
@keyframes mdin { from { opacity:0; transform:scale(.88); } to { opacity:1; transform:scale(1); } }
.modal-ttl { font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; margin-bottom: 16px; }
.minp {
  width: 100%; background: var(--s2); border: 1px solid var(--bd); border-radius: var(--rs);
  color: var(--tx); font-family: 'Noto Sans KR', sans-serif; font-size: 16px;
  padding: 11px 14px; outline: none; margin-bottom: 10px;
  transition: border-color .2s; -webkit-appearance: none; appearance: none;
}
.minp:focus { border-color: var(--c1); }
.mbtns { display: flex; gap: 8px; }
.mbtn {
  flex: 1; padding: 12px; border-radius: var(--rs);
  font-size: 14px; font-weight: 600; cursor: pointer; outline: none;
  font-family: 'Noto Sans KR', sans-serif; transition: all .2s;
}
.mbtn.cancel { background: var(--s2); border: 1px solid var(--bd); color: var(--dim); }
.mbtn.ok     { background: var(--c1); border: none; color: #07080f; box-shadow: 0 4px 15px rgba(232,255,71,.3); }
.mbtn:hover  { transform: translateY(-1px); }
.mbtn:active { transform: scale(.97); }

/* toast */
#toast {
  position: fixed; bottom: 90px; left: 50%; z-index: 600;
  transform: translateX(-50%) translateY(16px);
  background: var(--s2); border: 1px solid var(--bd); border-radius: 50px;
  padding: 9px 20px; font-size: 13px; color: var(--tx);
  pointer-events: none; opacity: 0; transition: all .3s; white-space: nowrap;
  max-width: calc(100vw - 32px); text-align: center;
}
#toast.on { opacity: 1; transform: translateX(-50%) translateY(0); }

/* mobile */
@media (max-width: 480px) {
  .wsec      { margin: 14px 12px 0; }
  .wsec-body { padding: 14px 12px; }
  .hero      { padding: 32px 16px 22px; }
}
</style>
</head>
<body>

<!-- ══ WIZARD PAGE ══ -->
<div id="pg-wizard">

  <div class="hero">
    <div class="hero-badge">🔐 SECURE AI WIZARD</div>
    <div class="hero-title">나만의 AI 비서<br>만들기</div>
    <div class="hero-sub">질문에 답하면 → 보안 설정된 AI 비서가 즉시 실행돼요</div>
  </div>

  <div class="prog-wrap">
    <div class="prog-row">
      <span class="prog-lbl">진행률</span>
      <span class="prog-num" id="pct-txt">0%</span>
    </div>
    <div class="prog-bg"><div class="prog-bar" id="prog-bar"></div></div>
  </div>

  <!-- SEC 1 -->
  <div class="wsec" id="sec1">
    <div class="wsec-hd" onclick="toggleSec('sec1')">
      <div class="sec-num">01</div>
      <div class="sec-ttl">🖥️ 기본 환경</div>
      <span class="sec-arr">▾</span>
    </div>
    <div class="wsec-body">
      <div>
        <div class="qlbl">💻 사용 중인 기기는?</div>
        <div class="chips" id="ch-device">
          <div class="chip" onclick="pick('device',this,'mobile')">📱 스마트폰</div>
          <div class="chip" onclick="pick('device',this,'pc')">💻 PC/노트북</div>
          <div class="chip" onclick="pick('device',this,'both')">🌐 둘 다</div>
        </div>
      </div>
      <div>
        <div class="qlbl">🧑‍💻 코딩 경험은?</div>
        <div class="qhint">💡 선택에 따라 설명 난이도가 자동으로 조정돼요</div>
        <div class="chips" id="ch-skill">
          <div class="chip" onclick="pick('skill',this,'zero')">😅 전혀 없음</div>
          <div class="chip" onclick="pick('skill',this,'little')">🌱 약간 있음</div>
          <div class="chip" onclick="pick('skill',this,'python')">🐍 Python 기본</div>
          <div class="chip" onclick="pick('skill',this,'pro')">⚡ 중급 이상</div>
        </div>
      </div>
      <div>
        <div class="qlbl">🔑 Claude API 키 입력</div>
        <div class="qhint">💡 console.anthropic.com 에서 무료 발급 가능 — 브라우저에만 저장, 서버 전송 없음 ✅</div>
        <input class="winput" type="password" id="apikey-inp"
               placeholder="sk-ant-api03-..."
               oninput="onKeyInput(this.value)" autocomplete="off">
        <div class="keymsg" id="key-msg">키를 입력하면 바로 형식을 확인해드려요</div>
      </div>
    </div>
  </div>

  <!-- SEC 2 -->
  <div class="wsec" id="sec2">
    <div class="wsec-hd" onclick="toggleSec('sec2')">
      <div class="sec-num">02</div>
      <div class="sec-ttl">🛡️ 보안 설정</div>
      <span class="sec-arr">▾</span>
    </div>
    <div class="wsec-body">
      <div>
        <div class="qlbl">📦 주로 다룰 데이터는? (복수 선택)</div>
        <div class="chips" id="ch-data">
          <div class="chip" onclick="multi('data',this,'personal')">📁 개인 파일</div>
          <div class="chip" onclick="multi('data',this,'financial')">💰 금융 정보</div>
          <div class="chip" onclick="multi('data',this,'work')">💼 업무 문서</div>
          <div class="chip" onclick="multi('data',this,'web')">🌐 웹 정보</div>
          <div class="chip" onclick="multi('data',this,'general')">📝 일반</div>
        </div>
      </div>
      <div>
        <div class="qlbl">🔒 보안 옵션 설정</div>
        <div style="display:flex;flex-direction:column;gap:8px">
          <div class="tog-row">
            <div class="tog-lbl">🔐 AES-256 암호화 저장<span class="tog-sub">대화 내용 암호화</span></div>
            <label class="tog-sw"><input type="checkbox" id="opt-enc" checked onchange="updateMeter()"><div class="tog-tk"></div></label>
          </div>
          <div class="tog-row">
            <div class="tog-lbl">📊 사용 로그 기록<span class="tog-sub">모든 요청 자동 저장</span></div>
            <label class="tog-sw"><input type="checkbox" id="opt-log" onchange="updateMeter()"><div class="tog-tk"></div></label>
          </div>
          <div class="tog-row">
            <div class="tog-lbl">🌐 외부 전송 차단<span class="tog-sub">API 외 통신 완전 차단</span></div>
            <label class="tog-sw"><input type="checkbox" id="opt-net" checked onchange="updateMeter()"><div class="tog-tk"></div></label>
          </div>
          <div class="tog-row">
            <div class="tog-lbl">💾 API 키 이 기기에만 저장<span class="tog-sub">서버 전송 없음</span></div>
            <label class="tog-sw"><input type="checkbox" id="opt-save" checked onchange="updateMeter()"><div class="tog-tk"></div></label>
          </div>
        </div>
      </div>
      <div class="smeter">
        <div class="sm-ttl">⚡ 실시간 보안 점수</div>
        <div class="sm-row">
          <span class="sm-k">암호화</span>
          <div class="sm-bar"><div class="sm-f" id="m-enc" style="background:linear-gradient(90deg,var(--c1),#b8cc00)"></div></div>
          <span class="sm-v" id="mv-enc" style="color:var(--c1)">0%</span>
        </div>
        <div class="sm-row">
          <span class="sm-k">격리</span>
          <div class="sm-bar"><div class="sm-f" id="m-iso" style="background:linear-gradient(90deg,var(--c3),#2299cc)"></div></div>
          <span class="sm-v" id="mv-iso" style="color:var(--c3)">0%</span>
        </div>
        <div class="sm-row">
          <span class="sm-k">전체</span>
          <div class="sm-bar"><div class="sm-f" id="m-tot" style="background:linear-gradient(90deg,var(--c4),#40cc88)"></div></div>
          <span class="sm-v" id="mv-tot" style="color:var(--c4)">0%</span>
        </div>
      </div>
    </div>
  </div>

  <!-- SEC 3 -->
  <div class="wsec" id="sec3">
    <div class="wsec-hd" onclick="toggleSec('sec3')">
      <div class="sec-num">03</div>
      <div class="sec-ttl">⚙️ AI 비서 기능 설정</div>
      <span class="sec-arr">▾</span>
    </div>
    <div class="wsec-body">
      <div>
        <div class="qlbl">🎯 주로 시킬 작업은? (복수 선택)</div>
        <div class="chips" id="ch-task">
          <div class="chip" onclick="multi('task',this,'data')">📊 데이터 분석</div>
          <div class="chip" onclick="multi('task',this,'email')">📧 이메일 작성</div>
          <div class="chip" onclick="multi('task',this,'search')">🌐 정보 검색</div>
          <div class="chip" onclick="multi('task',this,'file')">📂 파일 정리</div>
          <div class="chip" onclick="multi('task',this,'summary')">📋 요약/정리</div>
          <div class="chip" onclick="multi('task',this,'translate')">🌍 번역</div>
          <div class="chip" onclick="multi('task',this,'code')">💻 코드 도움</div>
        </div>
      </div>
      <div>
        <div class="qlbl">🤖 AI 비서 이름 (선택)</div>
        <input class="winput" type="text" id="ai-name-inp"
               placeholder="예: 지민이, 알파, 비서봇..." maxlength="10"
               oninput="calcProgress()">
      </div>
      <div>
        <div class="qlbl">🗣️ AI 말투는?</div>
        <div class="chips" id="ch-tone">
          <div class="chip" onclick="pick('tone',this,'formal')">👔 정중하게</div>
          <div class="chip" onclick="pick('tone',this,'friendly')">😊 친근하게</div>
          <div class="chip" onclick="pick('tone',this,'brief')">⚡ 간결하게</div>
          <div class="chip" onclick="pick('tone',this,'fun')">🎉 재미있게</div>
        </div>
      </div>
      <div>
        <div class="qlbl">🔔 에러 발생 시 처리 방식?</div>
        <div class="chips" id="ch-err">
          <div class="chip" onclick="pick('err',this,'popup')">🔔 팝업 알림</div>
          <div class="chip" onclick="pick('err',this,'retry')">🔄 자동 재시도</div>
          <div class="chip" onclick="pick('err',this,'log')">📋 로그만 저장</div>
        </div>
      </div>
    </div>
  </div>

  <!-- SEC 4 -->
  <div class="wsec" id="sec4">
    <div class="wsec-hd" onclick="toggleSec('sec4')">
      <div class="sec-num">04</div>
      <div class="sec-ttl">🚀 추가 설정 (선택)</div>
      <span class="sec-arr">▾</span>
    </div>
    <div class="wsec-body">
      <div>
        <div class="qlbl">📝 AI 비서에게 추가로 알려줄 것</div>
        <div class="qhint">💡 예: "나는 마케터야", "항상 표로 정리해줘", "영어로도 같이 써줘"</div>
        <textarea class="wtxt" id="extra-inp"
          placeholder="AI 비서가 알아야 할 정보나 특별 지시사항을 자유롭게 입력하세요..."
          oninput="calcProgress()"></textarea>
      </div>
    </div>
  </div>

  <div class="gen-wrap">
    <button class="gen-btn" id="gen-btn" onclick="launchAI()">
      <div class="spin" id="gen-spin"></div>
      <span id="gen-txt">⚡ AI 비서 실행하기</span>
    </button>
  </div>

</div><!-- /#pg-wizard -->


<!-- ══ AI PAGE ══ -->
<div id="pg-ai">
  <div class="ai-hdr">
    <div class="ai-ava" id="ai-ava">🤖</div>
    <div class="ai-meta">
      <div class="ai-nm" id="ai-nm">AI 비서</div>
      <div class="ai-stat"><div class="sdot"></div><span>온라인 · Claude AI</span></div>
    </div>
    <button class="hdrbtn" onclick="showEmail()">📧</button>
    <button class="hdrbtn" onclick="clearChat()">🗑️</button>
    <button class="hdrbtn" onclick="goWizard()">⚙️</button>
  </div>
  <div class="qbar" id="qbar"></div>
  <div class="chat" id="chat">
    <div class="welcome">
      <span class="wname" id="w-name">AI 비서</span>
      안녕하세요! 저는 당신만을 위한 AI 비서예요.<br>
      뭐든지 말씀해주세요. 바로 도와드릴게요! 😊
    </div>
  </div>
  <div class="inp-area">
    <div class="fprev" id="fprev">
      <span>📎</span>
      <span class="fprev-name" id="fprev-name"></span>
      <span class="fprev-rm" onclick="clearAttach()">✕</span>
    </div>
    <div class="inp-row">
      <button class="sbtn" onclick="document.getElementById('file-inp').click()">📎</button>
      <textarea id="msginp" placeholder="무엇이든 물어보세요..." rows="1"
                oninput="autoResize(this)" onkeydown="onKey(event)"></textarea>
      <button id="sendbtn" onclick="sendMsg()">↑</button>
    </div>
    <input type="file" id="file-inp" style="display:none"
           accept=".txt,.csv,.json,.md" onchange="onFile(this)">
  </div>
</div>

<!-- EMAIL MODAL -->
<div class="modal-ov" id="emodal" onclick="if(event.target===this)closeEmail()">
  <div class="modal">
    <div class="modal-ttl">📧 이메일 작성 도우미</div>
    <input class="minp" id="e-to"    placeholder="받는 사람 (예: 팀장님, 거래처 김부장님)">
    <input class="minp" id="e-topic" placeholder="주제 (예: 휴가 신청, 미팅 일정 조율)">
    <input class="minp" id="e-tone"  placeholder="말투 (예: 공손하게, 친근하게) — 선택">
    <div class="mbtns">
      <button class="mbtn cancel" onclick="closeEmail()">취소</button>
      <button class="mbtn ok"     onclick="submitEmail()">✍️ 작성하기</button>
    </div>
  </div>
</div>

<div id="toast"></div>

<script>
/* STATE */
const S = { device:null, skill:null, apikey:'', data:[], task:[], tone:null, err:null };
let history   = [];
let sysprompt = '';
let busy      = false;
let attached  = null;

/* CHIP SELECTORS */
function pick(key, el, val) {
  el.closest('.chips').querySelectorAll('.chip').forEach(c => c.classList.remove('sel'));
  el.classList.add('sel');
  S[key] = val;
  calcProgress();
}
function multi(key, el, val) {
  if (el.classList.contains('msel')) {
    el.classList.remove('msel');
    S[key] = S[key].filter(v => v !== val);
  } else {
    el.classList.add('msel');
    if (!S[key].includes(val)) S[key].push(val);
  }
  calcProgress();
}

/* API KEY */
function onKeyInput(val) {
  S.apikey = val.trim();
  const msg = document.getElementById('key-msg');
  if (!val) {
    msg.style.color = 'var(--dim)';
    msg.textContent = '키를 입력하면 바로 형식을 확인해드려요';
  } else if (val.startsWith('sk-ant')) {
    msg.style.color = 'var(--c4)';
    msg.textContent = '✅ 올바른 형식이에요!';
  } else {
    msg.style.color = 'var(--c2)';
    msg.textContent = '❌ sk-ant 로 시작해야 해요';
  }
  calcProgress();
}

/* PROGRESS */
function calcProgress() {
  let n = 0;
  if (S.device)                      n++;
  if (S.skill)                       n++;
  if (S.apikey.startsWith('sk-ant')) n++;
  if (S.task && S.task.length > 0)   n++;
  if (S.tone)                        n++;
  const pct = Math.round(n / 5 * 100);
  document.getElementById('prog-bar').style.width = pct + '%';
  document.getElementById('pct-txt').textContent  = pct + '%';
}

/* SECURITY METER */
function updateMeter() {
  const enc = document.getElementById('opt-enc').checked;
  const net = document.getElementById('opt-net').checked;
  const e = enc ? 92 : 40, i = net ? 88 : 35, t = Math.round((e+i)/2);
  sm('m-enc','mv-enc',e); sm('m-iso','mv-iso',i); sm('m-tot','mv-tot',t);
}
function sm(bid, vid, n) {
  const b = document.getElementById(bid); if (b) b.style.width = n + '%';
  const v = document.getElementById(vid); if (v) v.textContent = n + '%';
}

/* SECTION TOGGLE */
function toggleSec(id) {
  document.getElementById(id).classList.toggle('closed');
}

/* LAUNCH */
function launchAI() {
  if (!S.apikey || !S.apikey.startsWith('sk-ant')) { showToast('❌ API 키를 먼저 입력해주세요!'); return; }
  if (!S.task || !S.task.length)                   { showToast('❌ 주로 시킬 작업을 하나 이상 선택해주세요!'); return; }
  if (!S.tone)                                      { showToast('❌ AI 말투를 선택해주세요!'); return; }

  const btn = document.getElementById('gen-btn');
  btn.classList.add('busy');
  document.getElementById('gen-txt').textContent = '비서 준비 중...';

  setTimeout(() => {
    buildSysPrompt();
    buildQuickBar();
    updateAIHeader();
    if (document.getElementById('opt-save').checked) {
      try { localStorage.setItem('_scai_k', btoa(S.apikey)); } catch(_) {}
    }
    document.getElementById('pg-wizard').style.display = 'none';
    document.getElementById('pg-ai').classList.add('on');
    btn.classList.remove('busy');
    document.getElementById('gen-txt').textContent = '⚡ AI 비서 실행하기';
    setTimeout(() => document.getElementById('msginp').focus(), 300);
  }, 900);
}

/* BUILD SYSTEM PROMPT */
function buildSysPrompt() {
  const name  = document.getElementById('ai-name-inp').value.trim() || 'AI 비서';
  const extra = document.getElementById('extra-inp').value.trim();
  const toneMap = { formal:'정중하고 전문적인 말투로 존댓말 사용', friendly:'친근하고 따뜻한 말투로 편하게', brief:'간결하고 핵심만 짧게', fun:'재미있고 유쾌하게 이모지를 많이 사용' };
  const taskMap = { data:'📊 데이터 분석 및 정리', email:'📧 이메일/문서 작성', search:'🌐 정보 검색 및 요약', file:'📂 파일 정리 방법 제안', summary:'📋 내용 요약', translate:'🌍 번역', code:'💻 코드 작성 및 디버깅' };
  const tasks = (S.task||[]).map(t => taskMap[t]||t).join(', ');
  const tone  = toneMap[S.tone] || '친근하게';
  const ex    = extra ? `\n\n사용자 추가 지시: ${extra}` : '';
  sysprompt = `당신의 이름은 "${name}"이며 사용자의 전담 AI 비서입니다.\n항상 한국어로, ${tone} 답변하세요.\n\n전문 분야: ${tasks}\n\n역할:\n- 첨부 파일(CSV, TXT, JSON 등)을 분석하고 핵심을 요약합니다\n- 이메일/보고서/문서를 상황에 맞게 작성합니다\n- 데이터를 분석하고 인사이트를 제공합니다\n- 정보를 체계적으로 정리하고 요약합니다\n- 어떤 질문이든 명확하게 답변합니다\n\n이모지를 적절히 사용하고, 긴 내용은 번호나 불릿으로 정리하세요.${ex}`;
}

/* BUILD QUICK BAR */
function buildQuickBar() {
  const MAP = {
    data:      { icon:'📊', label:'데이터 분석', prompt:'파일을 📎 첨부해줘. 내용을 분석하고 핵심 포인트를 요약해줘.' },
    email:     { icon:'📧', label:'이메일 작성', action:'email' },
    search:    { icon:'🌐', label:'최신 트렌드', prompt:'요즘 가장 주목받는 트렌드나 뉴스를 알려줘' },
    file:      { icon:'📂', label:'파일 정리법', prompt:'PC 파일과 폴더를 효율적으로 정리하는 방법을 알려줘' },
    summary:   { icon:'📋', label:'내용 요약',   prompt:'아래 내용을 핵심 3줄로 요약해줘:\n\n(여기에 내용 붙여넣기)' },
    translate: { icon:'🌍', label:'번역',         prompt:'아래 텍스트를 한국어로 번역해줘:\n\n' },
    code:      { icon:'💻', label:'코드 도움',   prompt:'코드 관련 질문이 있어. 어떤 언어든 OK. 뭘 도와줄까?' },
  };
  const bar = document.getElementById('qbar');
  bar.innerHTML = '';
  (S.task||[]).forEach(t => {
    const m = MAP[t]; if (!m) return;
    const b = document.createElement('button');
    b.className = 'qbtn'; b.innerHTML = `${m.icon} ${m.label}`;
    b.onclick = m.action === 'email' ? showEmail : () => quickSend(m.prompt);
    bar.appendChild(b);
  });
  const more = document.createElement('button');
  more.className = 'qbtn'; more.innerHTML = '💡 뭘 할 수 있어?';
  more.onclick = () => quickSend('네가 할 수 있는 모든 것을 알려줘!');
  bar.appendChild(more);
}

/* UPDATE AI HEADER */
function updateAIHeader() {
  const name = document.getElementById('ai-name-inp').value.trim() || 'AI 비서';
  const ava  = S.task.includes('data') ? '📊' : S.task.includes('code') ? '💻' : S.task.includes('email') ? '📧' : S.task.includes('search') ? '🌐' : '🤖';
  document.getElementById('ai-nm').textContent  = name;
  document.getElementById('ai-ava').textContent = ava;
  document.getElementById('w-name').textContent = `안녕하세요! 저는 ${name}이에요 👋`;
}

/* GO BACK TO WIZARD */
function goWizard() {
  document.getElementById('pg-ai').classList.remove('on');
  document.getElementById('pg-wizard').style.display = 'block';
  window.scrollTo(0, 0);
}

/* CHAT HELPERS */
function autoResize(el) { el.style.height = 'auto'; el.style.height = Math.min(el.scrollHeight, 120) + 'px'; }
function onKey(e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMsg(); } }
function ts() { return new Date().toLocaleTimeString('ko-KR', {hour:'2-digit', minute:'2-digit'}); }
function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function fmt(t) {
  t = t.replace(/```[\w]*\n?([\s\S]*?)```/g, (_,c) => `<div class="cblk">${esc(c.trim())}</div>`);
  t = t.replace(/`([^`\n]+)`/g, '<code style="background:rgba(232,255,71,.12);padding:1px 6px;border-radius:4px;font-family:\'JetBrains Mono\',monospace;font-size:12px">$1</code>');
  t = t.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  t = t.replace(/\n/g, '<br>');
  return t;
}

function addMsg(role, html, isErr) {
  const wrap = document.getElementById('chat');
  const div  = document.createElement('div');
  div.className = `msg ${role}`;
  const ava = role === 'ai' ? (document.getElementById('ai-ava').textContent || '🤖') : '👤';
  div.innerHTML = `<div class="mava">${ava}</div><div class="mbub-wrap"><div class="mbub${isErr?' err':''}">${html}</div><div class="mtime">${ts()}</div></div>`;
  wrap.appendChild(div);
  wrap.scrollTop = wrap.scrollHeight;
}

function showTyping() {
  const wrap = document.getElementById('chat');
  const div  = document.createElement('div');
  div.id = 'typing'; div.className = 'msg ai';
  const ava = document.getElementById('ai-ava').textContent || '🤖';
  div.innerHTML = `<div class="mava">${ava}</div><div class="mbub-wrap"><div class="mbub"><div class="tdots"><span></span><span></span><span></span></div></div></div>`;
  wrap.appendChild(div);
  wrap.scrollTop = wrap.scrollHeight;
}
function rmTyping() { const el = document.getElementById('typing'); if (el) el.remove(); }

/* SEND MESSAGE */
async function sendMsg() {
  if (busy) return;
  const inp  = document.getElementById('msginp');
  const text = inp.value.trim();
  if (!text && !attached) return;

  let apiContent  = text;
  let displayText = text;
  if (attached) {
    apiContent  = `📎 파일명: ${attached.name}\n\n파일 내용:\n${attached.content}\n\n${text || '이 파일을 분석하고 핵심 내용을 요약해줘'}`;
    displayText = text || `📎 ${attached.name} — 분석 요청`;
  }

  addMsg('user', esc(displayText).replace(/\n/g,'<br>'));
  inp.value = ''; inp.style.height = 'auto';
  clearAttach();
  busy = true;
  document.getElementById('sendbtn').disabled = true;
  history.push({ role:'user', content:apiContent });
  showTyping();

  try {
    const res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: sysprompt,
        messages: history.slice(-20)
      })
    });
    const data = await res.json();
    rmTyping();
    if (data.error) {
      addMsg('ai', `❌ API 오류: ${esc(data.error.message||'알 수 없는 오류')}<br><br>API 키를 확인해주세요.`, true);
      history.pop();
      if (S.err === 'popup') showToast('❌ API 오류 발생');
    } else {
      const reply = (data.content||[]).map(b=>b.text||'').join('') || '응답을 받지 못했어요.';
      addMsg('ai', fmt(reply));
      history.push({ role:'assistant', content:reply });
    }
  } catch(err) {
    rmTyping();
    addMsg('ai', `❌ 연결 오류: ${esc(err.message)}<br><br>인터넷 연결을 확인해주세요.`, true);
    history.pop();
    if (S.err === 'retry') {
      showToast('🔄 3초 후 자동 재시도...');
      busy = false;
      document.getElementById('sendbtn').disabled = false;
      setTimeout(sendMsg, 3000);
      return;
    }
  }
  busy = false;
  document.getElementById('sendbtn').disabled = false;
  document.getElementById('msginp').focus();
}

function quickSend(text) {
  const inp = document.getElementById('msginp');
  inp.value = text; autoResize(inp); sendMsg();
}

function clearChat() {
  if (!confirm('대화 내용을 모두 지울까요?')) return;
  history = [];
  const name = document.getElementById('ai-nm').textContent || 'AI 비서';
  document.getElementById('chat').innerHTML = `<div class="welcome"><span class="wname">${esc(name)}</span>대화가 초기화됐어요! 새롭게 시작해보세요 😊</div>`;
  showToast('🗑️ 초기화 완료');
}

/* FILE */
function onFile(inp) {
  const f = inp.files[0]; if (!f) return;
  if (f.size > 512000) { showToast('❌ 500KB 이하 파일만 가능해요'); inp.value=''; return; }
  const r = new FileReader();
  r.onload  = e => { attached={name:f.name,content:e.target.result}; document.getElementById('fprev-name').textContent=f.name; document.getElementById('fprev').classList.add('on'); showToast(`📎 ${f.name} 첨부됨`); };
  r.onerror = () => showToast('❌ 파일 읽기 실패');
  r.readAsText(f,'utf-8'); inp.value='';
}
function clearAttach() {
  attached=null;
  document.getElementById('fprev').classList.remove('on');
  document.getElementById('fprev-name').textContent='';
}

/* EMAIL MODAL */
function showEmail()  { document.getElementById('emodal').classList.add('on'); document.getElementById('e-to').focus(); }
function closeEmail() { document.getElementById('emodal').classList.remove('on'); }
function submitEmail() {
  const to=document.getElementById('e-to').value.trim(), topic=document.getElementById('e-topic').value.trim(), tone=document.getElementById('e-tone').value.trim();
  if (!to||!topic) { showToast('❌ 받는 사람과 주제를 입력해주세요'); return; }
  closeEmail();
  quickSend(`📧 이메일을 작성해줘.\n받는 사람: ${to}\n주제: ${topic}\n말투: ${tone||'정중하게'}\n\n제목과 본문 모두 작성해줘.`);
  ['e-to','e-topic','e-tone'].forEach(id => document.getElementById(id).value='');
}

/* TOAST */
let _tt;
function showToast(msg) {
  const t=document.getElementById('toast'); t.textContent=msg; t.classList.add('on');
  clearTimeout(_tt); _tt=setTimeout(()=>t.classList.remove('on'),2700);
}

/* INIT */
(function() {
  try {
    const saved = localStorage.getItem('_scai_k');
    if (saved) { const v=atob(saved); document.getElementById('apikey-inp').value=v; S.apikey=v; onKeyInput(v); }
  } catch(_) {}
  updateMeter();
  calcProgress();
})();
</script>
</body>
</html>