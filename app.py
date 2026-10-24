
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudOps Studio",
        "time": datetime.now().isoformat()
    })


@app.route("/")
def dashboard():
    return r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CloudOps Studio | Deployment Center</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #080d19;
    --panel: #111827;
    --panel2: #151e30;
    --border: rgba(148,163,184,.15);
    --text: #f1f5f9;
    --muted: #91a0b8;
    --blue: #6487ff;
    --cyan: #45d6e9;
    --green: #48d7a0;
}
* { box-sizing: border-box; }
body {
    margin: 0;
    background:
      radial-gradient(ellipse at 80% 0%, rgba(70,90,220,.17), transparent 38%),
      radial-gradient(ellipse at 5% 70%, rgba(20,184,166,.08), transparent 35%),
      var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
}
button { font: inherit; cursor: pointer; }
.layout { display: flex; min-height: 100vh; }
.sidebar {
    width: 248px;
    flex-shrink: 0;
    border-right: 1px solid var(--border);
    background: rgba(9,15,29,.83);
    padding: 27px 17px;
    display: flex;
    flex-direction: column;
}
.brand { display:flex; align-items:center; gap:12px; padding: 0 10px 35px; }
.brand-icon {
    width: 42px; height: 42px; display:grid; place-items:center;
    border-radius: 13px; font-size:22px;
    background: linear-gradient(135deg,#6487ff,#8258e8);
    box-shadow: 0 7px 25px #647aff35;
}
.brand-name { font:700 19px 'Space Grotesk',sans-serif; }
.brand-sub { color:var(--muted); font-size:10px; margin-top:3px; letter-spacing:1.5px; }
.section-label { font-size:10px; color:#697991; letter-spacing:1.8px; padding:0 12px; margin:14px 0 10px; }
.nav {
    display:flex; align-items:center; gap:12px; padding:12px;
    color:var(--muted); border-radius:10px; margin:3px 0;
    font-size:13px; transition:.2s;
}
.nav:hover, .nav.active { background:#657fff19; color:#a9bcff; }
.nav.active { border:1px solid #7088ff30; }
.nav .symbol { font-size:17px; width:20px; text-align:center; }
.sidebar-bottom { margin-top:auto; }
.profile {
    display:flex; align-items:center; gap:10px; padding:15px 8px 0;
    border-top:1px solid var(--border); margin-top:25px;
}
.avatar {
    width:36px;height:36px;border-radius:12px;display:grid;place-items:center;
    background:linear-gradient(135deg,#38bdf8,#6366f1);font-weight:700;
}
.profile small { display:block; color:var(--muted); font-size:11px; margin-top:3px; }
.main { min-width:0; flex:1; padding:31px clamp(18px,4vw,48px) 35px; }
.topbar { display:flex; justify-content:space-between; align-items:center; gap:15px; margin-bottom:38px; }
.eyebrow { color:#8ea4ff; text-transform:uppercase; letter-spacing:2px; font-size:10px; font-weight:700; }
h1,h2,h3,p { margin-top:0; }
h1 { font:600 clamp(25px,3vw,35px) 'Space Grotesk',sans-serif; letter-spacing:-1.1px; margin:9px 0; }
.subtitle { color:var(--muted); font-size:13px; line-height:1.7; }
.top-actions { display:flex; gap:10px; align-items:center; }
.clock {
    border:1px solid var(--border); border-radius:11px; padding:10px 13px;
    font-size:12px; color:#bdc8db; background:#ffffff05;
}
.btn {
    border:1px solid var(--border); border-radius:10px; padding:11px 15px;
    color:var(--text); background:#ffffff07; font-size:12px;
    transition:.2s;
}
.btn:hover { transform:translateY(-2px); border-color:#8297ff80; }
.btn.primary { background:linear-gradient(120deg,#5577f5,#795be8); border:0; font-weight:700; }
.hero {
    border:1px solid #8796ff30; border-radius:19px; padding:27px;
    display:flex; align-items:center; justify-content:space-between; gap:20px;
    background:linear-gradient(115deg,#18264aee,#171a32dd 55%,#112c3aee);
    position:relative; overflow:hidden; margin-bottom:22px;
}
.hero:after {
    content:""; position:absolute; width:230px;height:230px;border-radius:50%;
    right:12%;top:-160px; border:1px solid #a2b5ff23;
    box-shadow:0 0 0 30px #a2b5ff08,0 0 0 60px #a2b5ff05;
}
.hero-content { position:relative; z-index:1; }
.hero h2 { font:600 23px 'Space Grotesk',sans-serif; margin:11px 0 8px; }
.hero p { color:#b0bdd5; font-size:12px; line-height:1.8; max-width:520px; margin-bottom:17px; }
.pill {
    display:inline-flex; align-items:center; gap:7px; font-size:10px;
    color:#9ce9c8; background:#37d99a14; border:1px solid #37d99a38;
    border-radius:50px; padding:7px 10px;
}
.dot { width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 10px #48d7a0; }
.hero-art { position:relative;z-index:1; width:125px;height:125px; flex-shrink:0; display:grid;place-items:center; }
.orbit { position:absolute; inset:0; border:1px solid #8ca3ff4a; border-radius:50%; animation:spin 18s linear infinite; }
.orbit:before { content:"";position:absolute;top:13px;left:13px;width:8px;height:8px;border-radius:50%;background:#65e5ee;box-shadow:0 0 15px #65e5ee; }
.orbit.two { inset:16px; border-color:#61c7ff4a; animation-direction:reverse; }
.cube { font-size:48px;filter:drop-shadow(0 0 20px #6c8bff80); }
@keyframes spin { to {transform:rotate(360deg)} }
.grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; margin-bottom:25px; }
.card {
    background:linear-gradient(145deg,#151e30e8,#101827e8);
    border:1px solid var(--border); border-radius:15px; padding:19px;
    transition:transform .22s,border-color .22s; min-width:0;
}
.card:hover { transform:translateY(-3px); border-color:#879aff50; }
.metric-head { display:flex; align-items:center; justify-content:space-between; gap:8px; }
.metric-icon { width:38px;height:38px;display:grid;place-items:center;border-radius:11px;font-size:19px; }
.blue { background:#6487ff18; color:#90a7ff; }
.teal { background:#45d6e918; color:#6be1ec; }
.green { background:#48d7a018; color:#69e6b4; }
.purple { background:#a78bfa18; color:#b9a5ff; }
.metric-label { color:var(--muted);font-size:11px;margin-top:17px; }
.metric-value { font:600 27px 'Space Grotesk',sans-serif; margin-top:5px; }
.metric-note { font-size:10px;color:#8090aa;margin-top:7px; line-height:1.5; }
.section-head { display:flex; align-items:end; justify-content:space-between; gap:15px; margin:27px 0 15px; }
.section-head h2 { font:600 18px 'Space Grotesk',sans-serif; margin:0 0 5px; }
.section-head p { color:var(--muted);font-size:11px;margin:0; }
.tools { display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px; }
.tool-top { display:flex;align-items:center;gap:12px; }
.tool-logo {
    width:43px;height:43px;border-radius:12px;display:grid;place-items:center;
    background:#ffffff08;border:1px solid var(--border);font-size:22px;
}
.tool-title { font-weight:700;font-size:13px; }
.tool-category { font-size:10px;color:var(--muted);margin-top:4px; }
.tool-desc { color:#a0aec2;font-size:11px;line-height:1.8;margin:17px 0;min-height:39px; }
.tool-foot { border-top:1px solid var(--border);padding-top:12px;display:flex;justify-content:space-between;gap:8px;align-items:center; }
.tag { font-size:9px;border:1px solid var(--border);padding:5px 8px;border-radius:6px;color:#b6c3d7; }
.small-link { color:#9eafff;font-size:10px;cursor:pointer;background:none;border:0; }
.lower { display:grid;grid-template-columns:1.4fr 1fr;gap:14px;margin-top:25px; }
.pipeline-step { display:flex;align-items:center;gap:12px;padding:13px 0; }
.step-icon {
    width:35px;height:35px;border:1px solid #8295ff35;border-radius:10px;
    display:grid;place-items:center;background:#7389ff10;flex-shrink:0;
}
.step-info { flex:1;min-width:0; }
.step-info strong { font-size:12px;font-weight:600; }
.step-info p { font-size:10px;color:var(--muted);margin:4px 0 0; }
.step-state { font-size:9px;color:#aebcce;border:1px solid var(--border);padding:5px 7px;border-radius:6px; }
.note { color:#8c9bb2;font-size:10px;line-height:1.8;margin-top:10px; }
.activity { display:flex;gap:11px;padding:13px 0;border-bottom:1px solid var(--border); }
.activity:last-child { border-bottom:0; }
.activity-icon { width:30px;height:30px;display:grid;place-items:center;border-radius:9px;background:#ffffff08;flex-shrink:0; }
.activity strong { font-size:11px; }
.activity p { font-size:10px;color:var(--muted);line-height:1.6;margin:5px 0 0; }
footer { border-top:1px solid var(--border);margin-top:28px;padding-top:19px;display:flex;justify-content:space-between;gap:12px;color:#74839c;font-size:10px; }
footer span { color:#a6b4ce; }
.toast {
    position:fixed;right:22px;bottom:22px;max-width:320px;padding:14px 18px;
    border:1px solid #6e8cff65;border-radius:12px;background:#17223a;
    color:#eef2ff;font-size:12px;box-shadow:0 12px 40px #0005;
    opacity:0;transform:translateY(12px);pointer-events:none;transition:.25s;
}
.toast.show { opacity:1;transform:translateY(0); }
@media(max-width:1050px) {
    .grid { grid-template-columns:repeat(2,minmax(0,1fr)); }
    .tools { grid-template-columns:repeat(2,minmax(0,1fr)); }
}
@media(max-width:700px) {
    .sidebar { width:65px;padding:22px 8px; }
    .brand { padding:0 3px 30px; }
    .brand-text,.nav-text,.section-label,.profile-text { display:none; }
    .nav { justify-content:center;padding:13px 5px; }
    .profile { justify-content:center;padding:15px 0 0; }
    .main { padding:22px 14px; }
    .topbar { align-items:flex-start;flex-direction:column;margin-bottom:25px; }
    .top-actions { width:100%;flex-wrap:wrap; }
    .hero { padding:21px; }
    .hero-art { width:70px;height:70px; }
    .cube { font-size:32px; }
    .lower { grid-template-columns:1fr; }
    .tools { grid-template-columns:1fr; }
    footer { flex-direction:column; }
}
@media(max-width:400px) {
    .grid { grid-template-columns:1fr; }
    .hero-art { display:none; }
}
</style>
</head>
<body>
<div class="layout">
<aside class="sidebar">
    <div class="brand">
        <div class="brand-icon">⌘</div>
        <div class="brand-text">
            <div class="brand-name">CloudOps</div>
            <div class="brand-sub">STUDIO / 001</div>
        </div>
    </div>

    <div class="section-label">WORKSPACE</div>
    <div class="nav active"><span class="symbol">▦</span><span class="nav-text">Overview</span></div>
    <div class="nav" onclick="goTo('toolkit')"><span class="symbol">◇</span><span class="nav-text">Technology Stack</span></div>
    <div class="nav" onclick="goTo('pipeline')"><span class="symbol">⌘</span><span class="nav-text">CI/CD Pipeline</span></div>
    <div class="nav" onclick="showToast('Deployment integration will be configured in a future stage.')"><span class="symbol">⇧</span><span class="nav-text">Deployments</span></div>

    <div class="section-label">PROJECT</div>
    <div class="nav" onclick="showToast('This dashboard currently uses demonstration data.')"><span class="symbol">◷</span><span class="nav-text">Activity Log</span></div>
    <div class="nav" onclick="window.open('/health','_blank')"><span class="symbol">♥</span><span class="nav-text">Health Check</span></div>

    <div class="sidebar-bottom">
        <div class="nav" onclick="showToast('CloudOps Studio | Flask learning project')"><span class="symbol">ⓘ</span><span class="nav-text">About Project</span></div>
        <div class="profile">
            <div class="avatar">C</div>
            <div class="profile-text">
                <div style="font-size:12px;font-weight:700">Cloud Learner</div>
                <small>DevOps Portfolio</small>
            </div>
        </div>
    </div>
</aside>

<main class="main">
    <div class="topbar">
        <div>
            <div class="eyebrow">CLOUD INFRASTRUCTURE / OVERVIEW</div>
            <h1>Deployment Center<span style="color:#8298ff">.</span></h1>
            <div class="subtitle">One workspace to explore your cloud and DevOps learning journey.</div>
        </div>
        <div class="top-actions">
            <div class="clock" id="clock">Loading time...</div>
            <button class="btn" onclick="refreshDashboard()">↻ Refresh</button>
            <button class="btn primary" onclick="window.open('/health','_blank')">Check Health ↗</button>
        </div>
    </div>

    <section class="hero">
        <div class="hero-content">
            <div class="pill"><span class="dot"></span> APPLICATION RUNNING LOCALLY</div>
            <h2>Build. Ship. Scale.</h2>
            <p>
                Welcome to your CloudOps workspace. Explore the tools behind
                modern application delivery, from version control to containers
                and automated deployment.
            </p>
            <button class="btn primary" onclick="goTo('toolkit')">Explore technology stack &nbsp; →</button>
        </div>
        <div class="hero-art">
            <div class="orbit"></div><div class="orbit two"></div>
            <div class="cube">☁</div>
        </div>
    </section>

    <div class="grid">
        <div class="card">
            <div class="metric-head"><div class="metric-icon blue">☁</div><span class="tag">CLOUD</span></div>
            <div class="metric-label">Cloud Platform</div>
            <div class="metric-value">AWS</div>
            <div class="metric-note">S3 storage · EC2 compute</div>
        </div>
        <div class="card">
            <div class="metric-head"><div class="metric-icon teal">◈</div><span class="tag">SOURCE</span></div>
            <div class="metric-label">Version Control</div>
            <div class="metric-value">Git</div>
            <div class="metric-note">Track and manage code changes</div>
        </div>
        <div class="card">
            <div class="metric-head"><div class="metric-icon green">▣</div><span class="tag">CONTAINERS</span></div>
            <div class="metric-label">Container Platform</div>
            <div class="metric-value">Docker</div>
            <div class="metric-note">Package apps consistently</div>
        </div>
        <div class="card">
            <div class="metric-head"><div class="metric-icon purple">⟳</div><span class="tag">AUTOMATION</span></div>
            <div class="metric-label">CI/CD Tool</div>
            <div class="metric-value">Jenkins</div>
            <div class="metric-note">Automate build and test tasks</div>
        </div>
    </div>

    <section id="toolkit">
        <div class="section-head">
            <div><h2>Technology Stack</h2><p>The tools in your Cloud & DevOps learning journey</p></div>
            <span class="tag">6 TECHNOLOGIES</span>
        </div>
        <div class="tools">
            <div class="card">
                <div class="tool-top"><div class="tool-logo">☁</div><div><div class="tool-title">Amazon Web Services</div><div class="tool-category">CLOUD INFRASTRUCTURE</div></div></div>
                <div class="tool-desc">Cloud storage with S3 and virtual computing resources with EC2.</div>
                <div class="tool-foot"><span class="tag">AWS S3 · EC2</span><button class="small-link" onclick="showToast('AWS integration is not connected yet.')">Explore ↗</button></div>
            </div>
            <div class="card">
                <div class="tool-top"><div class="tool-logo">⑂</div><div><div class="tool-title">Git & GitHub</div><div class="tool-category">VERSION CONTROL</div></div></div>
                <div class="tool-desc">Track source code changes, maintain project history and collaborate.</div>
                <div class="tool-foot"><span class="tag">SOURCE CODE</span><button class="small-link" onclick="showToast('GitHub integration can be added after repository setup.')">Explore ↗</button></div>
            </div>
            <div class="card">
                <div class="tool-top"><div class="tool-logo">🐳</div><div><div class="tool-title">Docker</div><div class="tool-category">CONTAINERIZATION</div></div></div>
                <div class="tool-desc">Package your Flask application and its dependencies into a container.</div>
                <div class="tool-foot"><span class="tag">CONTAINERS</span><button class="small-link" onclick="showToast('Docker will be configured in the next project stage.')">Explore ↗</button></div>
            </div>
            <div class="card">
                <div class="tool-top"><div class="tool-logo">♧</div><div><div class="tool-title">Jenkins</div><div class="tool-category">CI/CD AUTOMATION</div></div></div>
                <div class="tool-desc">Create an automated pipeline to build and test your application.</div>
                <div class="tool-foot"><span class="tag">AUTOMATION</span><button class="small-link" onclick="showToast('Jenkins pipeline is planned, not connected yet.')">Explore ↗</button></div>
            </div>
            <div class="card">
                <div class="tool-top"><div class="tool-logo">⚙</div><div><div class="tool-title">Kubernetes</div><div class="tool-category">CONTAINER ORCHESTRATION</div></div></div>
                <div class="tool-desc">Learn to orchestrate containers, scale workloads and manage deployments.</div>
                <div class="tool-foot"><span class="tag">NEXT TO LEARN</span><button class="small-link" onclick="showToast('Kubernetes is a future learning goal.')">Explore ↗</button></div>
            </div>
            <div class="card">
                <div class="tool-top"><div class="tool-logo">⌘</div><div><div class="tool-title">Termius & SSH</div><div class="tool-category">REMOTE ACCESS</div></div></div>
                <div class="tool-desc">Connect securely to remote servers and use command-line tools.</div>
                <div class="tool-foot"><span class="tag">SERVER ACCESS</span><button class="small-link" onclick="showToast('Remote server access is not configured in this dashboard.')">Explore ↗</button></div>
            </div>
        </div>
    </section>

    <div class="lower">
        <section class="card" id="pipeline">
            <div class="section-head" style="margin-top:0">
                <div><h2>CI/CD Pipeline</h2><p>Planned application delivery workflow</p></div>
                <span class="tag">DEMO</span>
            </div>
            <div class="pipeline-step"><div class="step-icon">⑂</div><div class="step-info"><strong>01 · Source</strong><p>Push code to GitHub</p></div><span class="step-state">Planned</span></div>
            <div class="pipeline-step"><div class="step-icon">⟳</div><div class="step-info"><strong>02 · Build & Test</strong><p>Run a Jenkins pipeline</p></div><span class="step-state">Planned</span></div>
            <div class="pipeline-step"><div class="step-icon">🐳</div><div class="step-info"><strong>03 · Package</strong><p>Build a Docker image</p></div><span class="step-state">Planned</span></div>
            <div class="pipeline-step"><div class="step-icon">☁</div><div class="step-info"><strong>04 · Deploy</strong><p>Deploy to a cloud server</p></div><span class="step-state">Planned</span></div>
            <div class="note">These are planned stages, not actual deployment results. We will connect each stage as the project develops.</div>
        </section>

        <section class="card">
            <div class="section-head" style="margin-top:0">
                <div><h2>Project Activity</h2><p>Your current project milestones</p></div>
            </div>
            <div class="activity"><div class="activity-icon">✦</div><div><strong>Flask dashboard created</strong><p>A web interface built with Python and HTML/CSS.</p></div></div>
            <div class="activity"><div class="activity-icon">⑂</div><div><strong>GitHub setup</strong><p>Next milestone: publish your source code.</p></div></div>
            <div class="activity"><div class="activity-icon">▣</div><div><strong>Docker containerization</strong><p>Upcoming milestone: package the application.</p></div></div>
            <div class="activity"><div class="activity-icon">⟳</div><div><strong>CI/CD automation</strong><p>Upcoming milestone: configure Jenkins.</p></div></div>
        </section>
    </div>

    <footer><div>© 2026 <span>CloudOps Studio</span> · Student Portfolio Project</div><div>Built with Python + Flask · <span id="health-label">Local demo</span></div></footer>
</main>
</div>

<div class="toast" id="toast"></div>
<script>
function updateClock() {
    document.getElementById('clock').textContent =
        new Date().toLocaleString(undefined, {
            month:'short', day:'numeric', hour:'2-digit', minute:'2-digit', second:'2-digit'
        });
}
updateClock();
setInterval(updateClock, 1000);

function showToast(message) {
    const el = document.getElementById('toast');
    el.textContent = message;
    el.classList.add('show');
    clearTimeout(window.toastTimer);
    window.toastTimer = setTimeout(() => el.classList.remove('show'), 3000);
}
function goTo(id) {
    document.getElementById(id).scrollIntoView({behavior:'smooth', block:'start'});
}
async function refreshDashboard() {
    const label = document.getElementById('health-label');
    try {
        const response = await fetch('/health');
        if (!response.ok) throw new Error('Health check failed');
        const data = await response.json();
        label.textContent = 'Flask API healthy';
        showToast('Application health check passed.');
    } catch (error) {
        label.textContent = 'Check unavailable';
        showToast('Could not reach the health endpoint.');
    }
}
</script>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
