# 🌟 Siddant Ojha — Portfolio Setup Guide

## Folder Structure
Put all these files in ONE folder (e.g. `my_portfolio/`):

```
my_portfolio/
├── app.py               ← main portfolio app
├── requirements.txt     ← dependencies
├── photo.jpg            ← YOUR photo (rename your photo to this)
├── certificate.png      ← YOUR certificate image (rename to this)
└── README.md            ← this file
```

---

## Quick Start (Windows)

### Step 1 — Install Python
Download from https://python.org if not already installed.

### Step 2 — Open Terminal in your folder
Right-click inside the folder → "Open in Terminal" (or PowerShell)

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the app
```bash
streamlit run app.py
```

Your browser will open automatically at http://localhost:8501 🎉

---

## Customising Your Portfolio

### Add your photo
Rename your profile photo to `photo.jpg` and place it in the folder.

### Add your certificate
Rename your certificate image to `certificate.png` and place it in the folder.

### Add YouTube videos
Open `app.py`, find this section near the bottom of the Videos page:
```python
videos = [
    # {"title": "My AI Demo", "youtube_id": "PASTE_ID_HERE"},
]
```
Replace `PASTE_ID_HERE` with the YouTube video ID (the part after `?v=` in the URL).
For example: `https://youtube.com/watch?v=dQw4w9WgXcQ` → ID is `dQw4w9WgXcQ`

### Change your admin password
In `app.py`, find this line near the top:
```python
ADMIN_PASSWORD = "siddant2025"
```
Change `siddant2025` to your own secret password.

### Edit text content
All text is inside `app.py`. Search for any phrase you want to change and edit it directly.

---

## Admin Mode
Click **🔒 Admin Login** at the bottom of the sidebar and enter your password.
Admin mode gives you an edit panel on each page.

---

## Deploy Online (Share with judges)
Use **Streamlit Community Cloud** (free):
1. Upload your project to GitHub (private repo is fine)
2. Go to https://share.streamlit.io
3. Connect your repo and deploy — you'll get a public URL!

> ⚠️ When deploying online, don't include your real `photo.jpg` or `certificate.png`
> in a public repo. Use Streamlit Secrets for sensitive config.
