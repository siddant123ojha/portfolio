import streamlit as st
import base64
from pathlib import Path

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Siddant Ojha | Portfolio",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── ADMIN PASSWORD ────────────────────────────────────────────────────────────
ADMIN_PASSWORD = "siddant2025"

# ── SESSION STATE ─────────────────────────────────────────────────────────────
if "admin"        not in st.session_state: st.session_state.admin        = False
if "page"         not in st.session_state: st.session_state.page         = "🏠  Home"
if "selected_cert" not in st.session_state: st.session_state.selected_cert = None

# ── CERTIFICATE DATA ──────────────────────────────────────────────────────────
CERTIFICATES = [
    {
        "file":    "cert_ai_expert.png",
        "title":   "AI Expert",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 9",
        "date":    "Jun 14, 2025",
        "desc":    "Awarded for completing the AI Expert: Hands-On AI, LLMs & Python Course with exceptional dedication.",
        "tag":     "🤖 AI",
        "color":   "#7c3aed",
        "featured": True,
    },
    {
        "file":    "cert_ai_programmer.png",
        "title":   "Young AI Programmer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 6",
        "date":    "—",
        "desc":    "Awarded for completing the Artificial Intelligence Course and earning the title of Young AI Programmer.",
        "tag":     "🤖 AI",
        "color":   "#059669",
        "featured": True,
    },
    {
        "file":    "cert_coding_grandmaster.png",
        "title":   "Coding Grandmaster",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Jul 28, 2023",
        "desc":    "For mastering the art of coding and learning to solve real-world problems.",
        "tag":     "💻 Coding",
        "color":   "#dc2626",
        "featured": True,
    },
    {
        "file":    "cert_coding_prodigy.png",
        "title":   "Coding Prodigy",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Jul 28, 2023",
        "desc":    "For gaining skills in analytical and advanced algorithmic thinking.",
        "tag":     "💻 Coding",
        "color":   "#7c3aed",
        "featured": False,
    },
    {
        "file":    "cert_coding_champion.png",
        "title":   "Coding Champion",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Jul 28, 2023",
        "desc":    "For gaining advanced coding skills and building a deeper understanding of complex coding concepts.",
        "tag":     "💻 Coding",
        "color":   "#0ea5e9",
        "featured": False,
    },
    {
        "file":    "cert_rising_star.png",
        "title":   "Rising Coding Star",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Jul 28, 2023",
        "desc":    "For quickly grasping coding principles and acquiring strong logic-building skills.",
        "tag":     "💻 Coding",
        "color":   "#dc2626",
        "featured": False,
    },
    {
        "file":    "cert_adv_python.png",
        "title":   "Advance Python Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Jun 11, 2023",
        "desc":    "For completing Advance Python modules and earning the title of Advance Python Developer.",
        "tag":     "🐍 Python",
        "color":   "#2563eb",
        "featured": True,
    },
    {
        "file":    "cert_python_game.png",
        "title":   "Python Game Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Jul 13, 2023",
        "desc":    "For completing Python game development modules and earning the title of Python Game Developer.",
        "tag":     "🐍 Python",
        "color":   "#2563eb",
        "featured": False,
    },
    {
        "file":    "cert_java.png",
        "title":   "Java Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Sep 25, 2023",
        "desc":    "For successfully completing the Java modules and earning the title of Java Developer.",
        "tag":     "☕ Java",
        "color":   "#ea580c",
        "featured": False,
    },
    {
        "file":    "cert_adv_animation.png",
        "title":   "Advance Animation & Game Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 6",
        "date":    "—",
        "desc":    "For completing Advance Scratch modules and earning the title of Advance Animation and Game Developer.",
        "tag":     "🎮 Game Dev",
        "color":   "#7c3aed",
        "featured": False,
    },
    {
        "file":    "cert_adv_android.png",
        "title":   "Advance Android Application Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 6",
        "date":    "—",
        "desc":    "For completing Advance Thunkable modules and earning the title of Advance Android Application Developer.",
        "tag":     "📱 Android",
        "color":   "#059669",
        "featured": False,
    },
    {
        "file":    "cert_pro_android_app_dev.png",
        "title":   "Pro Android Application Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 6",
        "date":    "—",
        "desc":    "For completing the Thunkable course and earning the title of Pro Android Application Developer.",
        "tag":     "📱 Android",
        "color":   "#ea580c",
        "featured": False,
    },
    {
        "file":    "cert_pro_android_app.png",
        "title":   "Pro Android App Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Dec 06, 2023",
        "desc":    "For completing Advanced Android App Development Modules and earning the title of Pro Android App Developer.",
        "tag":     "📱 Android",
        "color":   "#ea580c",
        "featured": False,
    },
    {
        "file":    "cert_app_dev.png",
        "title":   "Young App Developer",
        "issuer":  "Codingal · STEM Accredited",
        "grade":   "Grade 7",
        "date":    "Oct 18, 2023",
        "desc":    "For completing the App Development module and earning the title of Young App Developer.",
        "tag":     "📱 Android",
        "color":   "#059669",
        "featured": False,
    },
]

VIDEOS = [
    {"title": "My Project Showcase", "youtube_id": "Qlsa9zmz6Yo"},
]

# ── HELPERS ───────────────────────────────────────────────────────────────────
def img_to_b64(path: str) -> str:
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

def img_html(path: str, css: str = "", alt: str = "") -> str:
    b64 = img_to_b64(path)
    if not b64:
        return ""
    ext = Path(path).suffix.lstrip(".").replace("jpg", "jpeg")
    return f'<img src="data:image/{ext};base64,{b64}" class="{css}" alt="{alt}">'

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Nunito:wght@300;400;600;700;800&display=swap');

:root {
    --lav1:#f3eeff; --lav2:#dfd0f8; --lav3:#b99de0; --lav4:#8b5ccf;
    --sky1:#e4f5ff; --sky2:#b6e4ff; --sky3:#6ec6e6; --sky4:#2fa8cc;
    --dark:#1c1830; --mid:#4a4470; --soft:#8e8aaa;
    --card:rgba(255,255,255,0.72);
    --radius:20px; --rsm:12px;
    --shadow:0 8px 30px rgba(100,70,180,0.13);
    --shadow-lg:0 16px 50px rgba(100,70,180,0.22);
}

.stApp {
    background: linear-gradient(145deg,#f3eeff 0%,#e4f5ff 55%,#f0eaff 100%);
    font-family:'Nunito',sans-serif; color:var(--dark);
}
#MainMenu,footer{visibility:hidden!important;}
[data-testid="stHeader"]{background:transparent!important;}
.block-container{padding:1.8rem 2.5rem 3rem!important;max-width:1150px!important;}

/* ── SIDEBAR ── */
[data-testid="stSidebar"]{
    background:linear-gradient(160deg,#e8daff 0%,#cceeff 100%)!important;
    border-right:1.5px solid var(--lav2);
}
[data-testid="stSidebar"]>div:first-child{padding-top:0!important;}
.sb-profile{text-align:center;padding:2.2rem 1rem 1.5rem;border-bottom:1px solid rgba(140,100,210,0.2);margin-bottom:0.5rem;}
.sb-avatar{width:108px;height:108px;border-radius:50%;object-fit:cover;object-position:top;
    border:3.5px solid white;box-shadow:0 4px 22px rgba(130,90,200,0.28);
    margin-bottom:0.85rem;display:block;margin-left:auto;margin-right:auto;}
.sb-name{font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;color:var(--dark);margin:0;}
.sb-tag{font-size:0.72rem;font-weight:600;color:var(--lav4);letter-spacing:0.06em;text-transform:uppercase;margin:0.3rem 0 0;}

/* ── HEADINGS ── */
.section-title{font-family:'Playfair Display',serif;font-size:2.1rem;font-weight:700;color:var(--dark);margin:0 0 0.25rem;}
.section-sub{color:var(--soft);font-size:0.95rem;margin:0 0 2rem;font-weight:500;}
.accent-bar{width:52px;height:4px;background:linear-gradient(90deg,var(--lav4),var(--sky4));border-radius:2px;margin:0.4rem 0 0.5rem;}

/* ── HERO ── */
.hero-card{background:var(--card);backdrop-filter:blur(14px);border-radius:var(--radius);
    border:1.5px solid rgba(200,180,255,0.35);box-shadow:var(--shadow-lg);
    padding:3rem 3.5rem;display:flex;align-items:center;gap:3rem;
    margin-bottom:2rem;animation:fadeUp 0.6s ease both;}
.hero-photo{width:185px;height:185px;border-radius:24px;object-fit:cover;object-position:top;
    border:3px solid white;box-shadow:0 8px 28px rgba(130,90,200,0.25);flex-shrink:0;}
.hero-greeting{font-size:0.82rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--lav4);margin:0 0 0.5rem;}
.hero-name{font-family:'Playfair Display',serif;font-size:2.9rem;font-weight:700;color:var(--dark);margin:0 0 0.3rem;line-height:1.15;}
.hero-tagline{font-size:1.05rem;color:var(--mid);font-weight:500;margin:0 0 1.2rem;}
.hero-bio{font-size:0.95rem;color:var(--mid);line-height:1.75;margin:0 0 1.5rem;max-width:520px;}
.badge-row{display:flex;flex-wrap:wrap;gap:0.5rem;}
.badge{padding:0.35rem 0.9rem;border-radius:999px;font-size:0.78rem;font-weight:700;}
.badge-lav{background:var(--lav2);color:var(--lav4);}
.badge-sky{background:var(--sky2);color:var(--sky4);}

/* ── STATS ── */
.stats-row{display:flex;gap:1.2rem;margin-bottom:2rem;flex-wrap:wrap;}
.stat-card{flex:1;min-width:140px;background:var(--card);backdrop-filter:blur(12px);
    border-radius:var(--radius);border:1.5px solid rgba(200,180,255,0.3);
    box-shadow:var(--shadow);padding:1.5rem 1.2rem;text-align:center;
    transition:transform 0.2s,box-shadow 0.2s;animation:fadeUp 0.7s ease both;}
.stat-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);}
.stat-num{font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:700;
    background:linear-gradient(135deg,var(--lav4),var(--sky4));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1;}
.stat-label{font-size:0.78rem;color:var(--soft);font-weight:600;margin-top:0.3rem;text-transform:uppercase;letter-spacing:0.06em;}

/* ── PROJECTS ── */
.projects-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1.1rem;margin-bottom:2rem;}
.project-card{background:var(--card);border:1.5px solid rgba(200,180,255,0.3);
    border-radius:var(--radius);box-shadow:var(--shadow);padding:1.5rem 1.4rem;
    transition:transform 0.2s,box-shadow 0.2s;animation:fadeUp 0.65s ease both;}
.project-card:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg);}
.project-icon{font-size:2rem;margin-bottom:0.6rem;}
.project-name{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:700;color:var(--dark);margin:0 0 0.4rem;}
.project-desc{font-size:0.83rem;color:var(--soft);line-height:1.6;}

/* ── SKILLS ── */
.skills-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:1.1rem;margin-bottom:2rem;}
.skill-card{background:var(--card);backdrop-filter:blur(12px);border:1.5px solid rgba(200,180,255,0.3);
    border-radius:var(--radius);box-shadow:var(--shadow);padding:1.4rem 1.3rem;
    transition:transform 0.2s,box-shadow 0.2s;animation:fadeUp 0.65s ease both;}
.skill-card:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg);}
.skill-icon{font-size:1.7rem;margin-bottom:0.6rem;}
.skill-name{font-weight:700;font-size:0.92rem;color:var(--dark);margin:0 0 0.25rem;}
.skill-desc{font-size:0.8rem;color:var(--soft);margin:0;}

/* ── ABOUT ── */
.about-card{background:var(--card);backdrop-filter:blur(14px);border:1.5px solid rgba(200,180,255,0.35);
    border-radius:var(--radius);box-shadow:var(--shadow-lg);padding:2.5rem 2.8rem;
    margin-bottom:1.8rem;animation:fadeUp 0.6s ease both;}
.about-photo{width:160px;height:160px;border-radius:20px;object-fit:cover;object-position:top;
    float:right;margin:0 0 1rem 2rem;border:3px solid white;box-shadow:0 6px 22px rgba(130,90,200,0.22);}
.about-text{font-size:0.97rem;line-height:1.82;color:var(--mid);}
.about-text p{margin:0 0 1rem;}
.about-text p:last-child{margin:0;}
.highlight{color:var(--lav4);font-weight:700;}

/* ── CERTIFICATE GALLERY ── */
.cert-filter-row{display:flex;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.8rem;}
.cert-filter{padding:0.35rem 1rem;border-radius:999px;font-size:0.8rem;font-weight:700;
    border:1.5px solid var(--lav2);background:transparent;cursor:pointer;
    color:var(--mid);transition:all 0.18s;}
.cert-filter.active,.cert-filter:hover{background:var(--lav2);color:var(--lav4);}

.cert-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1.3rem;margin-bottom:2rem;}
.cert-thumb{background:var(--card);backdrop-filter:blur(12px);
    border-radius:var(--radius);border:1.5px solid rgba(200,180,255,0.3);
    box-shadow:var(--shadow);overflow:hidden;
    transition:transform 0.22s,box-shadow 0.22s;
    animation:fadeUp 0.65s ease both;cursor:pointer;}
.cert-thumb:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);}
.cert-thumb-img{width:100%;height:200px;object-fit:cover;object-position:top;display:block;}
.cert-thumb-body{padding:0.9rem 1.1rem 1rem;}
.cert-thumb-tag{display:inline-block;padding:0.2rem 0.65rem;border-radius:999px;
    font-size:0.7rem;font-weight:700;margin-bottom:0.45rem;color:white;}
.cert-thumb-title{font-family:'Playfair Display',serif;font-size:0.95rem;font-weight:700;
    color:var(--dark);margin:0 0 0.2rem;line-height:1.3;}
.cert-thumb-meta{font-size:0.75rem;color:var(--soft);font-weight:600;}

/* Featured badge */
.feat-badge{position:absolute;top:0.65rem;right:0.65rem;
    background:linear-gradient(90deg,var(--lav4),var(--sky4));
    color:white;font-size:0.65rem;font-weight:800;
    padding:0.2rem 0.55rem;border-radius:999px;letter-spacing:0.05em;}
.cert-thumb-wrap{position:relative;}

/* ── FULL-SIZE CERT VIEW ── */
.cert-detail{background:var(--card);backdrop-filter:blur(14px);
    border:1.5px solid rgba(200,180,255,0.35);border-radius:var(--radius);
    box-shadow:var(--shadow-lg);overflow:hidden;margin-bottom:1.8rem;
    animation:fadeUp 0.5s ease both;}
.cert-detail-img{width:100%;max-height:500px;object-fit:contain;
    background:var(--lav1);padding:2rem;display:block;}
.cert-detail-body{padding:1.5rem 2rem 1.8rem;}
.cert-detail-title{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;color:var(--dark);margin:0 0 0.3rem;}
.cert-detail-issuer{font-size:0.87rem;font-weight:700;color:var(--lav4);margin:0 0 0.7rem;}
.cert-detail-desc{font-size:0.9rem;color:var(--mid);line-height:1.7;margin:0;}
.back-btn{display:inline-flex;align-items:center;gap:0.4rem;
    background:var(--lav2);color:var(--lav4);border:none;border-radius:var(--rsm);
    font-family:'Nunito',sans-serif;font-weight:700;font-size:0.85rem;
    padding:0.5rem 1.1rem;cursor:pointer;margin-bottom:1.2rem;transition:all 0.18s;}
.back-btn:hover{background:var(--lav3);color:white;}

/* ── VIDEO ── */
.video-wrap{background:var(--card);border:1.5px solid rgba(200,180,255,0.3);
    border-radius:var(--radius);box-shadow:var(--shadow-lg);
    padding:1.5rem 1.5rem 1rem;margin-bottom:1.5rem;
    animation:fadeUp 0.6s ease both;}
.video-title-text{font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;
    color:var(--dark);margin:0 0 1rem;}

/* ── ADMIN ── */
.admin-badge{display:inline-block;background:linear-gradient(90deg,var(--lav4),var(--sky4));
    color:white;font-size:0.72rem;font-weight:700;letter-spacing:0.08em;
    padding:0.25rem 0.7rem;border-radius:999px;text-transform:uppercase;margin-bottom:1rem;}

/* ── ANIMATIONS ── */
@keyframes fadeUp{from{opacity:0;transform:translateY(18px);}to{opacity:1;transform:translateY(0);}}

/* ── Streamlit radio nav ── */
div[data-testid="stRadio"]>label{display:none;}
div[data-testid="stRadio"]>div{display:flex;flex-direction:column;gap:0.2rem;padding:0.5rem 0.8rem;}
div[data-testid="stRadio"]>div>label{background:transparent;border-radius:var(--rsm)!important;
    padding:0.6rem 1rem!important;font-family:'Nunito',sans-serif!important;
    font-size:0.9rem!important;font-weight:600!important;color:var(--mid)!important;
    cursor:pointer;transition:background 0.18s,color 0.18s;}
div[data-testid="stRadio"]>div>label:hover{background:rgba(255,255,255,0.55)!important;}
div[data-testid="stRadio"]>div>label[data-checked="true"],
div[data-testid="stRadio"]>div>label[aria-checked="true"]{
    background:linear-gradient(90deg,var(--lav2),var(--sky1))!important;color:var(--lav4)!important;}

/* ── Streamlit button ── */
.stButton>button{background:linear-gradient(135deg,var(--lav4),var(--sky4))!important;
    color:white!important;border:none!important;border-radius:var(--rsm)!important;
    font-family:'Nunito',sans-serif!important;font-weight:700!important;
    transition:opacity 0.2s,transform 0.2s!important;}
.stButton>button:hover{opacity:0.88!important;transform:translateY(-2px)!important;}

/* ── Streamlit inputs ── */
.stTextInput>div>div>input,.stTextArea>div>div>textarea{
    border-radius:var(--rsm)!important;border:1.5px solid var(--lav2)!important;
    font-family:'Nunito',sans-serif!important;}

/* ── RESPONSIVE / MOBILE ── */
@media (max-width: 768px) {
    .block-container { padding: 1.5rem 1rem 3rem !important; }
    .hero-card { flex-direction: column; gap: 1.5rem; padding: 2rem 1.5rem; text-align: center; }
    .hero-photo { width: 140px; height: 140px; }
    .hero-name { font-size: 2.2rem; }
    .badge-row { justify-content: center; }
    .about-card { padding: 2rem 1.5rem; }
    .about-photo { float: none; display: block; margin: 0 auto 1.5rem; width: 140px; height: 140px; }
    .stats-row { gap: 0.8rem; }
    .stat-card { min-width: 45%; padding: 1rem 0.5rem; }
    .stat-num { font-size: 1.6rem; }
    .cert-detail-img { padding: 1rem; max-height: 300px; }
    .cert-detail-body { padding: 1.2rem; }
    .video-wrap { padding: 1rem; }
}
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    photo_html = img_html("photo.jpg", "sb-avatar", "Siddant Ojha")
    fallback = '<div style="width:108px;height:108px;border-radius:50%;background:linear-gradient(135deg,#b99de0,#6ec6e6);margin:0 auto 0.85rem;display:flex;align-items:center;justify-content:center;font-size:2.8rem;">👤</div>'
    st.markdown(f"""
    <div class="sb-profile">
        {photo_html or fallback}
        <p class="sb-name">Siddant Ojha</p>
        <p class="sb-tag">Developer · Designer · Achiever</p>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("Nav", ["🏠  Home","👤  About Me","🏆  Certificates","🎬  Videos"],
                    label_visibility="collapsed")
    st.session_state.page = page

    st.markdown("<hr style='border:none;border-top:1px solid rgba(140,100,210,0.2);margin:1.2rem 0 0.8rem;'>",
                unsafe_allow_html=True)
    if not st.session_state.admin:
        with st.expander("🔒 Admin Login"):
            pw = st.text_input("Password", type="password", key="pw_field")
            if st.button("Login"):
                if pw == ADMIN_PASSWORD:
                    st.session_state.admin = True
                    st.rerun()
                else:
                    st.error("Incorrect password.")
    else:
        st.markdown('<div class="admin-badge">✓ Admin Mode Active</div>', unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.admin = False
            st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: HOME
# ═══════════════════════════════════════════════════════════════════════════════
if page == "🏠  Home":
    photo = img_html("photo.jpg","hero-photo","Siddant Ojha")
    fallback_hero = '<div class="hero-photo" style="background:linear-gradient(135deg,#b99de0,#6ec6e6);display:flex;align-items:center;justify-content:center;font-size:4rem;">👤</div>'

    st.markdown(f"""
    <div class="hero-card">
        {photo or fallback_hero}
        <div>
            <p class="hero-greeting">✦ Welcome to my portfolio</p>
            <h1 class="hero-name">Siddant Ojha</h1>
            <p class="hero-tagline">Developer · Logo Designer · Competition Winner</p>
            <p class="hero-bio">
                I'm a passionate student from Kathmandu who builds things that matter —
                AI systems, productivity apps, and brand identities.
                I hold <strong>14 Codingal certifications</strong> and I'm always working on the next big idea.
            </p>
            <div class="badge-row">
                <span class="badge badge-lav">🤖 AI Expert</span>
                <span class="badge badge-sky">📱 Android Dev</span>
                <span class="badge badge-lav">🐍 Python Dev</span>
                <span class="badge badge-sky">☕ Java Dev</span>
                <span class="badge badge-lav">🎨 Logo Designer</span>
                <span class="badge badge-sky">📍 Kathmandu, Nepal</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stats-row">
        <div class="stat-card"><div class="stat-num">14</div><div class="stat-label">Certificates</div></div>
        <div class="stat-card"><div class="stat-num">3+</div><div class="stat-label">Major Projects</div></div>
        <div class="stat-card"><div class="stat-num">5+</div><div class="stat-label">Languages Learned</div></div>
        <div class="stat-card"><div class="stat-num">100%</div><div class="stat-label">Dedication</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="section-title">Featured Projects</p>
    <div class="accent-bar"></div>
    <p class="section-sub">Things I've built that I'm most proud of</p>
    <div class="projects-grid">
        <div class="project-card">
            <div class="project-icon">🤖</div>
            <p class="project-name">AI System</p>
            <p class="project-desc">Built a functional AI — one of my most technically ambitious creations, leveraging LLMs and Python.</p>
        </div>
        <div class="project-card">
            <div class="project-icon">💰</div>
            <p class="project-name">WalletSaver App</p>
            <p class="project-desc">A smart personal finance app helping users track spending and save money effortlessly.</p>
        </div>
        <div class="project-card">
            <div class="project-icon">🎨</div>
            <p class="project-name">Logo & Brand Design</p>
            <p class="project-desc">Crafting clean, modern logos and visual identities — where creativity meets purpose-driven design.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: ABOUT ME
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "👤  About Me":
    st.markdown("""
    <p class="section-title">About Me</p>
    <div class="accent-bar"></div>
    <p class="section-sub">The story behind the work</p>
    """, unsafe_allow_html=True)

    photo = img_html("photo.jpg","about-photo","Siddant Ojha")
    st.markdown(f"""
    <div class="about-card">
        {photo}
        <div class="about-text">
            <p>
                Hi, I'm <span class="highlight">Siddant Ojha</span> — a student, programmer,
                and creative thinker from <span class="highlight">Kathmandu, Nepal</span>.
                I've always been drawn to the intersection of technology and problem-solving,
                and that passion has led me to build some genuinely exciting things.
            </p>
            <p>
                I do <span class="highlight">programming</span> and have won
                <span class="highlight">many competitions</span> over the years, earning
                <span class="highlight">14 Codingal certifications</span> across AI, Python,
                Java, Android development, and more. My most impressive works include building
                an <span class="highlight">AI system</span> from the ground up — a project
                that pushed my technical limits and proved what's possible with curiosity and code.
                I also built <span class="highlight">WalletSaver</span>, a productivity app
                designed to help people take control of their finances in a smart, intuitive way.
                Beyond software, I <span class="highlight">create logos</span> and visual
                identities — because great ideas deserve great design.
            </p>
            <p>
                I believe the best work comes from staying relentlessly curious, embracing
                difficult challenges, and never settling for "good enough." Whether I'm
                debugging code at midnight, sketching a logo, or competing on a stage —
                I bring the same energy and drive to everything I do.
                <span class="highlight">This portfolio is only the beginning.</span>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="section-title" style="font-size:1.55rem;">Skills &amp; Strengths</p>
    <div class="accent-bar"></div><br>
    <div class="skills-grid">
        <div class="skill-card"><div class="skill-icon">🤖</div>
            <p class="skill-name">Artificial Intelligence</p>
            <p class="skill-desc">Certified AI Expert — hands-on with LLMs, Python AI, and machine learning projects</p></div>
        <div class="skill-card"><div class="skill-icon">🐍</div>
            <p class="skill-name">Python Development</p>
            <p class="skill-desc">Advance Python Developer certified — from game dev to data to real-world apps</p></div>
        <div class="skill-card"><div class="skill-icon">📱</div>
            <p class="skill-name">Android App Development</p>
            <p class="skill-desc">Pro Android App Developer — building mobile apps with Thunkable and advanced modules</p></div>
        <div class="skill-card"><div class="skill-icon">☕</div>
            <p class="skill-name">Java Programming</p>
            <p class="skill-desc">Certified Java Developer with strong fundamentals in object-oriented programming</p></div>
        <div class="skill-card"><div class="skill-icon">🎨</div>
            <p class="skill-name">Logo Design</p>
            <p class="skill-desc">Crafting clean, modern brand identities where creativity meets strategy</p></div>
        <div class="skill-card"><div class="skill-icon">🏆</div>
            <p class="skill-name">Competition Mindset</p>
            <p class="skill-desc">14 certifications, multiple wins — proven track record of performing under pressure</p></div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: CERTIFICATES
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🏆  Certificates":

    # ── If a cert is selected, show full-size view ────────────────────────────
    if st.session_state.selected_cert is not None:
        cert = CERTIFICATES[st.session_state.selected_cert]

        if st.button("← Back to all certificates"):
            st.session_state.selected_cert = None
            st.rerun()

        cert_img = img_html(cert["file"], "cert-detail-img", cert["title"])
        fallback = f'<div class="cert-detail-img" style="display:flex;align-items:center;justify-content:center;height:260px;background:var(--lav1);font-size:3rem;">🏆</div>'
        st.markdown(f"""
        <div class="cert-detail">
            {cert_img or fallback}
            <div class="cert-detail-body">
                <span class="cert-thumb-tag" style="background:{cert['color']};">{cert['tag']}</span>
                <p class="cert-detail-title">{cert['title']}</p>
                <p class="cert-detail-issuer">🎓 {cert['issuer']} &nbsp;·&nbsp; {cert['grade']}
                    {"&nbsp;·&nbsp; " + cert['date'] if cert['date'] != '—' else ""}</p>
                <p class="cert-detail-desc">{cert['desc']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Gallery view ─────────────────────────────────────────────────────────
    else:
        st.markdown("""
        <p class="section-title">Certificates &amp; Awards</p>
        <div class="accent-bar"></div>
        <p class="section-sub">14 Codingal certifications — STEM accredited · Click any card to view full size</p>
        """, unsafe_allow_html=True)

        # Filter tabs
        all_tags  = ["All"] + sorted(set(c["tag"] for c in CERTIFICATES))
        tag_cols  = st.columns(len(all_tags))
        active_tag = st.session_state.get("cert_tag", "All")

        for i, tag in enumerate(all_tags):
            with tag_cols[i]:
                if st.button(tag, key=f"tag_{tag}",
                             type="primary" if tag == active_tag else "secondary"):
                    st.session_state.cert_tag = tag
                    active_tag = tag
                    st.rerun()

        filtered = [c for c in CERTIFICATES if active_tag == "All" or c["tag"] == active_tag]

        # 3-column grid
        cols_per_row = 3
        for row_start in range(0, len(filtered), cols_per_row):
            row_certs = filtered[row_start: row_start + cols_per_row]
            cols = st.columns(cols_per_row)
            for col, cert in zip(cols, row_certs):
                idx = CERTIFICATES.index(cert)
                with col:
                    thumb = img_html(cert["file"], "cert-thumb-img", cert["title"])
                    fallback_thumb = f'<div class="cert-thumb-img" style="background:linear-gradient(135deg,{cert["color"]}22,{cert["color"]}44);display:flex;align-items:center;justify-content:center;font-size:2.5rem;">🏆</div>'
                    featured_badge = '<span class="feat-badge">★ Featured</span>' if cert.get("featured") else ""
                    st.markdown(f"""
                    <div class="cert-thumb-wrap">
                        <div class="cert-thumb">
                            {thumb or fallback_thumb}
                            <div class="cert-thumb-body">
                                <span class="cert-thumb-tag" style="background:{cert['color']};">{cert['tag']}</span>
                                <p class="cert-thumb-title">{cert['title']}</p>
                                <p class="cert-thumb-meta">
                                    {cert['grade']}
                                    {"&nbsp;·&nbsp;" + cert['date'] if cert['date'] != '—' else ""}
                                </p>
                            </div>
                        </div>
                        {featured_badge}
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button("View certificate", key=f"cert_{idx}"):
                        st.session_state.selected_cert = idx
                        st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: VIDEOS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🎬  Videos":
    st.markdown("""
    <p class="section-title">Videos</p>
    <div class="accent-bar"></div>
    <p class="section-sub">Showcases, demos &amp; highlights</p>
    """, unsafe_allow_html=True)

    for v in VIDEOS:
        st.markdown(f"""
        <div class="video-wrap">
            <p class="video-title-text">🎬 {v['title']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.video(f"https://www.youtube.com/watch?v={v['youtube_id']}")
        st.markdown("<br>", unsafe_allow_html=True)

    if st.session_state.admin:
        st.markdown("---")
        st.markdown('<div class="admin-badge">✏️ Add More Videos</div>', unsafe_allow_html=True)
        st.text_input("Video Title", key="vid_title")
        st.text_input("YouTube Video ID (part after ?v= in the URL)", key="vid_id")
        if st.button("How to add permanently"):
            st.code("""# In app.py, find the VIDEOS list near the top and add:
VIDEOS = [
    {"title": "My Project Showcase", "youtube_id": "Qlsa9zmz6Yo"},
    {"title": "New Video Title",      "youtube_id": "PASTE_ID_HERE"},
]""", language="python")
