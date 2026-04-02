import streamlit as st
import base64
from pathlib import Path

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Siddant Ojha | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

ADMIN_PASSWORD = "siddant2025"

# ── SESSION STATE INIT ────────────────────────────────────────────────────────
for key, val in {
    "admin": False,
    "nav": "🏠  Home",
    "selected_cert": None,
    "cert_tag": "All",
    "show_admin_login": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ── CERTIFICATE DATA ──────────────────────────────────────────────────────────
CERTIFICATES = [
    {"file":"cert_ai_expert.png","title":"AI Expert","issuer":"Codingal · STEM Accredited","grade":"Grade 9","date":"Jun 14, 2025","desc":"Completed the AI Expert: Hands-On AI, LLMs & Python Course with exceptional dedication and achievement.","tag":"🤖 AI","color":"#e91e8c","featured":True},
    {"file":"cert_ai_programmer.png","title":"Young AI Programmer","issuer":"Codingal · STEM Accredited","grade":"Grade 6","date":"—","desc":"Completed the Artificial Intelligence Course and earned the title of Young AI Programmer.","tag":"🤖 AI","color":"#e91e8c","featured":True},
    {"file":"cert_coding_grandmaster.png","title":"Coding Grandmaster","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Jul 28, 2023","desc":"For mastering the art of coding and learning to solve real-world problems.","tag":"💻 Coding","color":"#d63384","featured":True},
    {"file":"cert_coding_prodigy.png","title":"Coding Prodigy","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Jul 28, 2023","desc":"For gaining skills in analytical and advanced algorithmic thinking.","tag":"💻 Coding","color":"#d63384","featured":False},
    {"file":"cert_coding_champion.png","title":"Coding Champion","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Jul 28, 2023","desc":"For gaining advanced coding skills and building deeper understanding of complex coding concepts.","tag":"💻 Coding","color":"#d63384","featured":False},
    {"file":"cert_rising_star.png","title":"Rising Coding Star","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Jul 28, 2023","desc":"For quickly grasping coding principles and acquiring strong logic-building skills.","tag":"💻 Coding","color":"#d63384","featured":False},
    {"file":"cert_adv_python.png","title":"Advance Python Developer","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Jun 11, 2023","desc":"Completed Advance Python modules and earned the title of Advance Python Developer.","tag":"🐍 Python","color":"#c2185b","featured":True},
    {"file":"cert_python_game.png","title":"Python Game Developer","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Jul 13, 2023","desc":"Completed Python game development modules and earned the title of Python Game Developer.","tag":"🐍 Python","color":"#c2185b","featured":False},
    {"file":"cert_java.png","title":"Java Developer","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Sep 25, 2023","desc":"Successfully completed Java modules and earned the title of Java Developer.","tag":"☕ Java","color":"#ad1457","featured":False},
    {"file":"cert_adv_animation.png","title":"Advance Animation & Game Dev","issuer":"Codingal · STEM Accredited","grade":"Grade 6","date":"—","desc":"Completed Advance Scratch modules and earned the title of Advance Animation and Game Developer.","tag":"🎮 Game Dev","color":"#880e4f","featured":False},
    {"file":"cert_adv_android.png","title":"Advance Android App Developer","issuer":"Codingal · STEM Accredited","grade":"Grade 6","date":"—","desc":"Completed Advance Thunkable modules and earned the title of Advance Android Application Developer.","tag":"📱 Android","color":"#e91e8c","featured":False},
    {"file":"cert_pro_android_app_dev.png","title":"Pro Android Application Dev","issuer":"Codingal · STEM Accredited","grade":"Grade 6","date":"—","desc":"Completed the Thunkable course and earned the title of Pro Android Application Developer.","tag":"📱 Android","color":"#e91e8c","featured":False},
    {"file":"cert_pro_android_app.png","title":"Pro Android App Developer","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Dec 06, 2023","desc":"Completed Advanced Android App Development Modules and earned Pro Android App Developer title.","tag":"📱 Android","color":"#e91e8c","featured":False},
    {"file":"cert_app_dev.png","title":"Young App Developer","issuer":"Codingal · STEM Accredited","grade":"Grade 7","date":"Oct 18, 2023","desc":"Completed the App Development module and earned the title of Young App Developer.","tag":"📱 Android","color":"#e91e8c","featured":False},
]

VIDEOS = [
    {"title": "My Project Showcase", "youtube_id": "Qlsa9zmz6Yo"},
]

NAV_PAGES = ["🏠  Home", "👤  About Me", "🏆  Certificates", "🎬  Videos"]

# ── HELPERS ───────────────────────────────────────────────────────────────────
def img_to_b64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

def img_html(path, css="", alt=""):
    b64 = img_to_b64(path)
    if not b64: return ""
    ext = Path(path).suffix.lstrip(".").replace("jpg","jpeg")
    return f'<img src="data:image/{ext};base64,{b64}" class="{css}" alt="{alt}">'

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Nunito:wght@300;400;600;700;800&display=swap');

:root {
    --pink1: #fff0f5;
    --pink2: #ffd6e7;
    --pink3: #ffadc9;
    --pink4: #e91e8c;
    --pink5: #c2185b;
    --rose:  #ff6b9d;
    --blush: #ffe4ef;
    --dark:  #2d1a24;
    --mid:   #6b3d52;
    --soft:  #b07090;
    --white: #ffffff;
    --card:  rgba(255,255,255,0.78);
    --radius: 20px;
    --rsm:   12px;
    --shadow: 0 8px 30px rgba(200,60,120,0.12);
    --shadow-lg: 0 16px 50px rgba(200,60,120,0.22);
}

/* ── Base ── */
.stApp {
    background: linear-gradient(145deg, #fff0f5 0%, #ffe4ef 50%, #fff5f8 100%) !important;
    font-family: 'Nunito', sans-serif;
    color: var(--dark);
}
#MainMenu, footer, header { visibility: hidden !important; }
.block-container {
    padding: 1.5rem 2rem 3rem !important;
    max-width: 1100px !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #ffd6e7 0%, #ffe4ef 100%) !important;
    border-right: 1.5px solid var(--pink2) !important;
    min-width: 220px !important;
    max-width: 260px !important;
}
[data-testid="stSidebar"] > div:first-child { 
    padding-top: 0 !important; 
}
[data-testid="stSidebarCollapseButton"] {
    display: block !important;
}

/* ── PROFILE SECTION ── */
.sb-profile {
    text-align: center;
    padding: 2rem 1rem 1.4rem;
    border-bottom: 1px solid rgba(233,30,140,0.18);
    margin-bottom: 0.6rem;
}
.sb-avatar {
    width: 100px; height: 100px;
    border-radius: 50%;
    object-fit: cover; object-position: top;
    border: 3px solid white;
    box-shadow: 0 4px 18px rgba(200,60,120,0.28);
    display: block; margin: 0 auto 0.8rem;
}
.sb-name {
    font-family: 'Playfair Display', serif;
    font-size: 1rem; font-weight: 700; color: var(--dark); margin: 0;
}
.sb-tag {
    font-size: 0.68rem; font-weight: 700; color: var(--pink4);
    letter-spacing: 0.07em; text-transform: uppercase; margin: 0.25rem 0 0;
}

/* ── TOP NAVBAR ── */
.nav-container {
    background: linear-gradient(135deg, #fff0f5 0%, #ffe4ef 100%);
    border-bottom: 1.5px solid #ffd6e7;
    padding: 1rem 2rem;
    margin: -1.5rem -2rem 1.8rem -2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1.5rem;
    box-shadow: 0 2px 8px rgba(200,60,120,0.08);
}

.nav-profile {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    min-width: 200px;
}

.nav-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    object-position: top;
    border: 2px solid white;
    box-shadow: 0 2px 10px rgba(200,60,120,0.2);
}

.nav-profile-text h3 {
    font-family: 'Playfair Display', serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--dark);
    margin: 0;
}

.nav-profile-text p {
    font-size: 0.65rem;
    font-weight: 700;
    color: var(--pink4);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0.1rem 0 0;
}

.nav-links {
    display: flex;
    gap: 0.5rem;
    flex: 1;
    justify-content: center;
    flex-wrap: wrap;
}

.nav-btn {
    padding: 0.6rem 1.2rem !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    border-radius: var(--rsm) !important;
    background: rgba(255, 255, 255, 0.7) !important;
    color: var(--mid) !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

.nav-btn:hover {
    background: white !important;
    color: var(--pink4) !important;
    box-shadow: 0 2px 8px rgba(200,60,120,0.15) !important;
}

.nav-btn.active {
    background: white !important;
    color: var(--pink4) !important;
    box-shadow: 0 2px 12px rgba(200,60,120,0.2) !important;
}

.nav-admin {
    display: flex;
    gap: 0.5rem;
}

/* ── DROPDOWN (Hidden on Desktop) ── */
.nav-dropdown {
    display: none;
}

.nav-dropdown-btn {
    padding: 0.6rem 1rem !important;
    background: rgba(255, 255, 255, 0.7) !important;
    border: none !important;
    border-radius: var(--rsm) !important;
    font-size: 1.1rem !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

.nav-dropdown-btn:hover {
    background: white !important;
    box-shadow: 0 2px 8px rgba(200,60,120,0.15) !important;
}

.nav-dropdown-content {
    display: none;
    position: absolute;
    background: white;
    border: 1.5px solid #ffd6e7;
    border-radius: var(--rsm);
    box-shadow: 0 4px 16px rgba(200,60,120,0.15);
    top: 100%;
    left: 0;
    right: 0;
    z-index: 1000;
    margin-top: 0.5rem;
}

.nav-dropdown-content button {
    display: block !important;
    width: 100% !important;
    text-align: left !important;
    padding: 0.8rem 1.2rem !important;
    background: transparent !important;
    border: none !important;
    color: var(--mid) !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    border-radius: 0 !important;
}

.nav-dropdown-content button:hover {
    background: #ffd6e7 !important;
    color: var(--pink4) !important;
}

.nav-dropdown-content button.active {
    background: var(--pink1) !important;
    color: var(--pink4) !important;
    font-weight: 700 !important;
}

/* ── MOBILE RESPONSIVE (≤ 768px) ── */
@media (max-width: 768px) {
    .nav-container {
        flex-direction: column;
        padding: 1rem;
        gap: 0.8rem;
        margin: -1.5rem -1rem 1.5rem -1rem;
    }

    .nav-profile {
        width: 100%;
        justify-content: space-between;
        min-width: auto;
    }

    .nav-links {
        display: none !important;
    }

    .nav-dropdown {
        display: block;
        position: relative;
        width: 100%;
    }

    .nav-dropdown-content {
        position: static !important;
        border: 1.5px solid #ffd6e7;
        margin-top: 0 !important;
        box-shadow: none;
    }

    .nav-dropdown-content.active {
        display: block !important;
    }
}

/* ── Streamlit generic button ── */
.stButton > button {
    background: linear-gradient(135deg, var(--pink4), var(--rose)) !important;
    color: white !important; border: none !important;
    border-radius: var(--rsm) !important;
    font-family: 'Nunito', sans-serif !important; font-weight: 700 !important;
    font-size: 0.85rem !important;
    transition: opacity 0.2s, transform 0.2s !important;
    padding: 0.45rem 1.1rem !important;
    width: 100% !important;
    cursor: pointer !important;
}
.stButton > button:hover { opacity: 0.88 !important; transform: translateY(-2px) !important; }
.stButton > button[kind="secondary"] {
    background: var(--pink2) !important;
    color: var(--pink4) !important;
}

/* Text inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    border-radius: var(--rsm) !important;
    border: 1.5px solid var(--pink2) !important;
    font-family: 'Nunito', sans-serif !important;
}

/* ── TYPOGRAPHY ── */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem; font-weight: 700; color: var(--dark); margin: 0 0 0.2rem;
}
.section-sub { color: var(--soft); font-size: 0.93rem; margin: 0 0 1.6rem; font-weight: 500; }
.accent-bar {
    width: 48px; height: 4px;
    background: linear-gradient(90deg, var(--pink4), var(--rose));
    border-radius: 2px; margin: 0.35rem 0 0.5rem;
}

/* ── HERO ── */
.hero-card {
    background: var(--card); backdrop-filter: blur(14px);
    border-radius: var(--radius); border: 1.5px solid rgba(255,173,201,0.4);
    box-shadow: var(--shadow-lg);
    padding: 2.5rem 3rem;
    display: flex; align-items: center; gap: 2.5rem;
    margin-bottom: 1.8rem; animation: fadeUp 0.6s ease both;
}
.hero-photo {
    width: 170px; height: 170px; border-radius: 22px;
    object-fit: cover; object-position: top;
    border: 3px solid white; box-shadow: 0 8px 28px rgba(200,60,120,0.22);
    flex-shrink: 0;
}
.hero-greeting {
    font-size: 0.78rem; font-weight: 800; letter-spacing: 0.13em;
    text-transform: uppercase; color: var(--pink4); margin: 0 0 0.45rem;
}
.hero-name {
    font-family: 'Playfair Display', serif; font-size: 2.6rem;
    font-weight: 700; color: var(--dark); margin: 0 0 0.25rem; line-height: 1.15;
}
.hero-tagline { font-size: 1rem; color: var(--mid); font-weight: 600; margin: 0 0 1rem; }
.hero-bio { font-size: 0.92rem; color: var(--mid); line-height: 1.75; margin: 0 0 1.3rem; max-width: 500px; }
.badge-row { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.badge {
    padding: 0.3rem 0.8rem; border-radius: 999px;
    font-size: 0.75rem; font-weight: 700;
    background: var(--pink2); color: var(--pink5);
}
.badge-alt { background: var(--blush); color: var(--pink4); }

/* ── STATS ── */
.stats-row { display: flex; gap: 1rem; margin-bottom: 1.8rem; flex-wrap: wrap; }
.stat-card {
    flex: 1; min-width: 120px; background: var(--card); backdrop-filter: blur(12px);
    border-radius: var(--radius); border: 1.5px solid rgba(255,173,201,0.3);
    box-shadow: var(--shadow); padding: 1.3rem 1rem; text-align: center;
    transition: transform 0.2s, box-shadow 0.2s; animation: fadeUp 0.7s ease both;
}
.stat-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.stat-num {
    font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 700;
    background: linear-gradient(135deg, var(--pink4), var(--rose));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1;
}
.stat-label { font-size: 0.72rem; color: var(--soft); font-weight: 700; margin-top: 0.25rem; text-transform: uppercase; letter-spacing: 0.06em; }

/* ── PROJECTS ── */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px,1fr)); gap: 1rem; margin-bottom: 1.8rem; }
.project-card {
    background: var(--card); border: 1.5px solid rgba(255,173,201,0.3);
    border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.4rem 1.3rem;
    transition: transform 0.2s, box-shadow 0.2s; animation: fadeUp 0.65s ease both;
}
.project-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-lg); }
.project-icon { font-size: 1.9rem; margin-bottom: 0.55rem; }
.project-name { font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: var(--dark); margin: 0 0 0.35rem; }
.project-desc { font-size: 0.82rem; color: var(--soft); line-height: 1.6; margin: 0; }

/* ── SKILLS ── */
.skills-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px,1fr)); gap: 1rem; margin-bottom: 1.8rem; }
.skill-card {
    background: var(--card); border: 1.5px solid rgba(255,173,201,0.3);
    border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.3rem 1.2rem;
    transition: transform 0.2s, box-shadow 0.2s; animation: fadeUp 0.65s ease both;
}
.skill-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-lg); }
.skill-icon { font-size: 1.6rem; margin-bottom: 0.5rem; }
.skill-name { font-weight: 700; font-size: 0.9rem; color: var(--dark); margin: 0 0 0.2rem; }
.skill-desc { font-size: 0.78rem; color: var(--soft); margin: 0; }

/* ── ABOUT ── */
.about-card {
    background: var(--card); backdrop-filter: blur(14px);
    border: 1.5px solid rgba(255,173,201,0.4); border-radius: var(--radius);
    box-shadow: var(--shadow-lg); padding: 2.2rem 2.5rem;
    margin-bottom: 1.6rem; animation: fadeUp 0.6s ease both;
}
.about-photo {
    width: 145px; height: 145px; border-radius: 18px;
    object-fit: cover; object-position: top;
    float: right; margin: 0 0 1rem 1.8rem;
    border: 3px solid white; box-shadow: 0 6px 20px rgba(200,60,120,0.2);
}
.about-text { font-size: 0.95rem; line-height: 1.8; color: var(--mid); }
.about-text p { margin: 0 0 0.95rem; }
.about-text p:last-child { margin: 0; }
.hl { color: var(--pink4); font-weight: 700; }

/* ── CERTIFICATES ── */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.1rem; margin-bottom: 1.8rem;
}
.cert-thumb {
    background: var(--card); border-radius: var(--radius);
    border: 1.5px solid rgba(255,173,201,0.3); box-shadow: var(--shadow);
    overflow: hidden; animation: fadeUp 0.6s ease both;
    transition: transform 0.22s, box-shadow 0.22s;
}
.cert-thumb:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); }
.cert-thumb-img { width: 100%; height: 180px; object-fit: cover; object-position: top; display: block; }
.cert-thumb-body { padding: 0.8rem 1rem 0.9rem; }
.cert-tag-pill {
    display: inline-block; padding: 0.18rem 0.6rem; border-radius: 999px;
    font-size: 0.68rem; font-weight: 800; color: white; margin-bottom: 0.4rem;
}
.cert-thumb-title {
    font-family: 'Playfair Display', serif; font-size: 0.88rem; font-weight: 700;
    color: var(--dark); margin: 0 0 0.18rem; line-height: 1.3;
}
.cert-thumb-meta { font-size: 0.72rem; color: var(--soft); font-weight: 600; }
.cert-detail-img {
    width: 100%; max-height: 480px; object-fit: contain;
    background: var(--pink1); padding: 1.5rem; display: block;
}
.cert-detail-body { padding: 1.3rem 1.8rem 1.6rem; }
.cert-detail-title { font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 700; color: var(--dark); margin: 0 0 0.25rem; }
.cert-detail-issuer { font-size: 0.84rem; font-weight: 700; color: var(--pink4); margin: 0 0 0.6rem; }
.cert-detail-desc { font-size: 0.88rem; color: var(--mid); line-height: 1.7; margin: 0; }

/* ── ADMIN ── */
.admin-badge {
    display: inline-block;
    background: linear-gradient(90deg, var(--pink4), var(--rose));
    color: white; font-size: 0.7rem; font-weight: 800;
    padding: 0.22rem 0.65rem; border-radius: 999px;
    text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.8rem;
}

/* ── VIDEO ── */
.video-wrap {
    background: var(--card); border: 1.5px solid rgba(255,173,201,0.3);
    border-radius: var(--radius); box-shadow: var(--shadow-lg);
    padding: 1.3rem 1.4rem 0.8rem; margin-bottom: 1.3rem;
    animation: fadeUp 0.6s ease both;
}
.video-label {
    font-family: 'Playfair Display', serif; font-size: 1.05rem;
    font-weight: 700; color: var(--dark); margin: 0 0 0.9rem;
}

/* ── ANIMATIONS ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ═══════════════════════════════════════════════════
   MOBILE RESPONSIVE  (≤ 768 px)
═══════════════════════════════════════════════════ */
@media (max-width: 768px) {
    .block-container { padding: 1rem 1rem 2rem !important; }

    /* Hero stacks vertically */
    .hero-card {
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        padding: 1.8rem 1.4rem !important;
        gap: 1.4rem !important;
    }
    .hero-photo { width: 130px !important; height: 130px !important; }
    .hero-name  { font-size: 2rem !important; }
    .hero-bio   { font-size: 0.88rem !important; max-width: 100% !important; }
    .badge-row  { justify-content: center !important; }

    /* Stats become 2-column */
    .stats-row { gap: 0.7rem !important; }
    .stat-card  { min-width: calc(50% - 0.4rem) !important; padding: 1rem 0.8rem !important; }
    .stat-num   { font-size: 1.6rem !important; }

    /* Projects & skills: 1 column */
    .projects-grid { grid-template-columns: 1fr !important; }
    .skills-grid   { grid-template-columns: 1fr 1fr !important; }

    /* About: photo stacks above text */
    .about-card   { padding: 1.5rem 1.3rem !important; }
    .about-photo  { float: none !important; display: block !important; margin: 0 auto 1.2rem !important; }
    .about-text   { font-size: 0.9rem !important; }

    /* Certs: 1 column on mobile */
    .cert-grid { grid-template-columns: 1fr !important; }
    .cert-thumb-img { height: 220px !important; }

    /* Section titles */
    .section-title { font-size: 1.5rem !important; }
}

@media (max-width: 480px) {
    .skills-grid { grid-template-columns: 1fr !important; }
    .hero-name   { font-size: 1.7rem !important; }
}
</style>
""", unsafe_allow_html=True)


# ── TOP NAVIGATION BAR ───────────────────────────────────────────────────────
nav_cols = st.columns([1, 0.2])

with nav_cols[0]:
    # Horizontal nav buttons for desktop
    st.markdown('<div class="nav-links">', unsafe_allow_html=True)
    nav_cols_inner = st.columns(len(NAV_PAGES))
    for i, page_name in enumerate(NAV_PAGES):
        with nav_cols_inner[i]:
            is_active = st.session_state.nav == page_name
            btn_class = "nav-btn active" if is_active else "nav-btn"
            if st.button(page_name, key=f"nav_{i}", use_container_width=True):
                st.session_state.nav = page_name
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with nav_cols[1]:
    # Admin section
    if not st.session_state.admin:
        if st.button("🔒", key="admin_toggle", help="Admin Login", use_container_width=True):
            st.session_state.show_admin_login = not st.session_state.get("show_admin_login", False)
    else:
        st.markdown('<div class="admin-badge" style="text-align: center;">✓</div>', unsafe_allow_html=True)
        if st.button("🚪", key="logout_btn", help="Logout", use_container_width=True):
            st.session_state.admin = False
            st.rerun()

# Admin login modal
if st.session_state.get("show_admin_login", False) and not st.session_state.admin:
    with st.expander("🔒 Enter Admin Password"):
        pw = st.text_input("Password", type="password", key="pw_field")
        if st.button("Login", key="login_btn"):
            if pw == ADMIN_PASSWORD:
                st.session_state.admin = True
                st.session_state.show_admin_login = False
                st.rerun()
            else:
                st.error("Incorrect password.")

st.markdown("<br>", unsafe_allow_html=True)

# ── SIDEBAR (PROFILE SECTION) ─────────────────────────────────────────────────
with st.sidebar:
    # Profile
    ph = img_html("photo.jpg", "sb-avatar", "Siddant Ojha")
    fb = '<div style="width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,#ffadc9,#ff6b9d);margin:0 auto 0.8rem;display:flex;align-items:center;justify-content:center;font-size:2.5rem;">👤</div>'
    st.markdown(f'<div class="sb-profile">{ph or fb}<p class="sb-name">Siddant Ojha</p><p class="sb-tag">Developer · Designer · Achiever</p></div>', unsafe_allow_html=True)
    
    st.markdown("<hr style='border:none;border-top:1px solid rgba(233,30,140,0.18);margin:1rem 0 0.8rem;'>", unsafe_allow_html=True)


page = st.session_state.nav   # single source of truth for the rest of the file


# ═══════════════════════════════════════════════════════════════════════════════
#  HOME
# ═══════════════════════════════════════════════════════════════════════════════
if page == "🏠  Home":
    ph = img_html("photo.jpg","hero-photo","Siddant Ojha")
    fb = '<div class="hero-photo" style="background:linear-gradient(135deg,#ffadc9,#ff6b9d);display:flex;align-items:center;justify-content:center;font-size:3.5rem;">👤</div>'
    st.markdown(f"""
    <div class="hero-card">
        {ph or fb}
        <div>
            <p class="hero-greeting">🌸 Welcome to my portfolio</p>
            <h1 class="hero-name">Siddant Ojha</h1>
            <p class="hero-tagline">Developer · Logo Designer · Competition Winner</p>
            <p class="hero-bio">
                I'm a passionate student from Kathmandu who builds things that matter —
                AI systems, productivity apps, and brand identities.
                I hold <strong>14 Codingal certifications</strong> and I'm always working
                on the next big idea.
            </p>
            <div class="badge-row">
                <span class="badge">🤖 AI Expert</span>
                <span class="badge badge-alt">📱 Android Dev</span>
                <span class="badge">🐍 Python Dev</span>
                <span class="badge badge-alt">☕ Java Dev</span>
                <span class="badge">🎨 Logo Designer</span>
                <span class="badge badge-alt">📍 Kathmandu</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stats-row">
        <div class="stat-card"><div class="stat-num">14</div><div class="stat-label">Certificates</div></div>
        <div class="stat-card"><div class="stat-num">3+</div><div class="stat-label">Major Projects</div></div>
        <div class="stat-card"><div class="stat-num">5+</div><div class="stat-label">Languages</div></div>
        <div class="stat-card"><div class="stat-num">100%</div><div class="stat-label">Dedication</div></div>
    </div>
    <p class="section-title">Featured Projects</p>
    <div class="accent-bar"></div>
    <p class="section-sub">Things I've built that I'm most proud of</p>
    <div class="projects-grid">
        <div class="project-card">
            <div class="project-icon">🤖</div>
            <p class="project-name">AI System</p>
            <p class="project-desc">Built a functional AI leveraging LLMs and Python — one of my most technically ambitious creations to date.</p>
        </div>
        <div class="project-card">
            <div class="project-icon">💰</div>
            <p class="project-name">WalletSaver App</p>
            <p class="project-desc">A smart finance app helping users track spending and save money — solving a real, everyday problem.</p>
        </div>
        <div class="project-card">
            <div class="project-icon">🎨</div>
            <p class="project-name">Logo & Brand Design</p>
            <p class="project-desc">Crafting clean, modern logos and brand identities where creativity meets purpose-driven strategy.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  ABOUT ME
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "👤  About Me":
    st.markdown("""
    <p class="section-title">About Me</p>
    <div class="accent-bar"></div>
    <p class="section-sub">The story behind the work</p>
    """, unsafe_allow_html=True)

    ph = img_html("photo.jpg","about-photo","Siddant Ojha")
    st.markdown(f"""
    <div class="about-card">
        {ph}
        <div class="about-text">
            <p>Hi, I'm <span class="hl">Siddant Ojha</span> — a student, programmer,
            and creative thinker from <span class="hl">Kathmandu, Nepal</span>.
            I've always been drawn to where technology meets problem-solving, and that
            passion has pushed me to build genuinely exciting things.</p>
            <p>I do <span class="hl">programming</span> and have won
            <span class="hl">many competitions</span>, earning
            <span class="hl">14 Codingal certifications</span> across AI, Python,
            Java, and Android development. My most impressive works include building
            an <span class="hl">AI system</span> from the ground up, a
            <span class="hl">WalletSaver app</span> that helps people manage their
            finances, and a portfolio of <span class="hl">professional logos</span>
            — because great ideas deserve great design.</p>
            <p>Whether I'm debugging code at midnight, sketching a logo, or competing
            on stage — I bring the same energy to everything I do.
            <span class="hl">This portfolio is only the beginning.</span></p>
        </div>
    </div>
    <p class="section-title" style="font-size:1.5rem;">Skills &amp; Strengths</p>
    <div class="accent-bar"></div><br>
    <div class="skills-grid">
        <div class="skill-card"><div class="skill-icon">🤖</div><p class="skill-name">Artificial Intelligence</p><p class="skill-desc">Certified AI Expert — hands-on with LLMs, Python AI &amp; machine learning</p></div>
        <div class="skill-card"><div class="skill-icon">🐍</div><p class="skill-name">Python Development</p><p class="skill-desc">Advance Python certified — games, data, and real-world apps</p></div>
        <div class="skill-card"><div class="skill-icon">📱</div><p class="skill-name">Android App Dev</p><p class="skill-desc">Pro Android Developer — building mobile apps with Thunkable</p></div>
        <div class="skill-card"><div class="skill-icon">☕</div><p class="skill-name">Java Programming</p><p class="skill-desc">Certified Java Developer with strong OOP fundamentals</p></div>
        <div class="skill-card"><div class="skill-icon">🎨</div><p class="skill-name">Logo Design</p><p class="skill-desc">Clean, modern brand identities where creativity meets strategy</p></div>
        <div class="skill-card"><div class="skill-icon">🏆</div><p class="skill-name">Competition Mindset</p><p class="skill-desc">14 certs, multiple wins — proven track record under pressure</p></div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  CERTIFICATES
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🏆  Certificates":

    # ── Full-size view ────────────────────────────────────────────────────────
    if st.session_state.selected_cert is not None:
        cert = CERTIFICATES[st.session_state.selected_cert]

        if st.button("← Back to all certificates"):
            st.session_state.selected_cert = None
            st.rerun()

        ci = img_html(cert["file"],"cert-detail-img",cert["title"])
        fb = f'<div class="cert-detail-img" style="height:260px;display:flex;align-items:center;justify-content:center;font-size:3rem;background:var(--pink1);">🏆</div>'
        st.markdown(f"""
        <div style="background:var(--card);border-radius:var(--radius);border:1.5px solid rgba(255,173,201,0.4);
                    box-shadow:var(--shadow-lg);overflow:hidden;margin-bottom:1.6rem;animation:fadeUp 0.5s ease both;">
            {ci or fb}
            <div class="cert-detail-body">
                <span class="cert-tag-pill" style="background:{cert['color']};">{cert['tag']}</span>
                <p class="cert-detail-title">{cert['title']}</p>
                <p class="cert-detail-issuer">🎓 {cert['issuer']} &nbsp;·&nbsp; {cert['grade']}
                    {"&nbsp;·&nbsp;" + cert['date'] if cert['date'] != '—' else ""}</p>
                <p class="cert-detail-desc">{cert['desc']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Gallery ───────────────────────────────────────────────────────────────
    else:
        st.markdown("""
        <p class="section-title">Certificates &amp; Awards</p>
        <div class="accent-bar"></div>
        <p class="section-sub">14 Codingal certifications — STEM accredited &nbsp;·&nbsp; Tap any card to view full size</p>
        """, unsafe_allow_html=True)

        # Filter buttons
        all_tags = ["All"] + sorted(set(c["tag"] for c in CERTIFICATES))
        tag_cols = st.columns(len(all_tags))
        for i, tag in enumerate(all_tags):
            with tag_cols[i]:
                is_active = (st.session_state.cert_tag == tag)
                if st.button(tag, key=f"tf_{tag}",
                             type="primary" if is_active else "secondary"):
                    st.session_state.cert_tag = tag
                    st.rerun()

        filtered = [c for c in CERTIFICATES
                    if st.session_state.cert_tag == "All"
                    or c["tag"] == st.session_state.cert_tag]

        # 3-column grid (CSS handles mobile collapse to 1)
        st.markdown('<div class="cert-grid">', unsafe_allow_html=True)
        for cert in filtered:
            idx = CERTIFICATES.index(cert)
            thumb = img_html(cert["file"],"cert-thumb-img",cert["title"])
            fb_t  = f'<div class="cert-thumb-img" style="background:linear-gradient(135deg,{cert["color"]}22,{cert["color"]}55);display:flex;align-items:center;justify-content:center;font-size:2.2rem;">🏆</div>'
            feat  = '<div style="position:absolute;top:0.6rem;right:0.6rem;background:linear-gradient(90deg,#e91e8c,#ff6b9d);color:white;font-size:0.62rem;font-weight:800;padding:0.18rem 0.5rem;border-radius:999px;">★ Featured</div>' if cert.get("featured") else ""
            st.markdown(f"""
            <div style="position:relative;">
                <div class="cert-thumb" id="cert_{idx}">
                    {thumb or fb_t}
                    <div class="cert-thumb-body">
                        <span class="cert-tag-pill" style="background:{cert['color']};">{cert['tag']}</span>
                        <p class="cert-thumb-title">{cert['title']}</p>
                        <p class="cert-thumb-meta">{cert['grade']}{"&nbsp;·&nbsp;"+cert['date'] if cert['date']!='—' else ""}</p>
                    </div>
                </div>
                {feat}
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # View buttons below the grid (one per cert)
        st.markdown("<br>**Click a certificate to view full size:**", unsafe_allow_html=True)
        btn_cols = st.columns(3)
        for i, cert in enumerate(filtered):
            idx = CERTIFICATES.index(cert)
            with btn_cols[i % 3]:
                if st.button(f"🔍 {cert['title']}", key=f"vb_{idx}"):
                    st.session_state.selected_cert = idx
                    st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
#  VIDEOS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🎬  Videos":
    st.markdown("""
    <p class="section-title">Videos</p>
    <div class="accent-bar"></div>
    <p class="section-sub">Showcases, demos &amp; highlights</p>
    """, unsafe_allow_html=True)

    for v in VIDEOS:
        st.markdown(f'<div class="video-wrap"><p class="video-label">🎬 {v["title"]}</p></div>',
                    unsafe_allow_html=True)
        st.video(f"https://www.youtube.com/watch?v={v['youtube_id']}")
        st.markdown("<br>", unsafe_allow_html=True)

    if st.session_state.admin:
        st.markdown("---")
        st.markdown('<div class="admin-badge">✏️ Add More Videos</div>', unsafe_allow_html=True)
        st.text_input("Video Title", key="v_title")
        st.text_input("YouTube ID (part after ?v=)", key="v_id")
        if st.button("How to add permanently"):
            st.code("""VIDEOS = [
    {"title": "My Project Showcase", "youtube_id": "Qlsa9zmz6Yo"},
    {"title": "New Video",           "youtube_id": "PASTE_ID_HERE"},
]""", language="python")
