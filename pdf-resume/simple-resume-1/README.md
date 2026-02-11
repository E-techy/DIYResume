# 📄 Simple Resume 1 – PDF Template

A clean, structured, and professional PDF resume template built using **Python** and **ReportLab**.

This resume follows a traditional structured layout with clear section hierarchy, strong typography, and ATS-friendly formatting.

Part of the **DIYResume** project 🚀

---

## 📌 Project Title

**Simple Resume 1 – PDF Resume Template (Python Generator)**

📍 Location in Repository:

```
pdf-resume/simple-resume-1/
```

---

## 📖 Description

This is a professionally formatted PDF resume template designed for:

* Students
* Developers
* Engineers
* Job seekers
* Internship applicants

It includes:

* Professional Header (Name + Contact Info)
* Professional Summary
* Technical Skills (Structured Table Format)
* Work Experience (Bullet Format)
* Projects
* Education
* Certifications
* Achievements & Activities

The layout is clean, readable, minimal, and suitable for both digital submission and printing.

This version also includes a **Python script** so users can generate their own resume by simply editing structured data.

---

## 🛠 Technologies Used

* Python
* ReportLab (Platypus API)
* Structured PDF Layout System
* Table-based skill formatting
* Styled headings and spacing

---

## 📂 Folder Structure

```
pdf-resume/
└── simple-resume-1/
    ├── resume-pdf-simple-v1.pdf
    ├── resume-pdf-python-v1.py
    └── README.md
```

---

## ⚙ Installation (To Generate Your Own Resume)

### 1️⃣ Install Python

Download from:
[https://python.org](https://python.org)

Verify installation:

```bash
python --version
```

---

### 2️⃣ Install Required Dependency

```bash
pip install reportlab
```

---

## ▶ How To Generate The PDF

Navigate to this folder:

```bash
cd pdf-resume/simple-resume-1
```

Run the script:

```bash
python resume-pdf-python-v1.py
```

After running successfully, the output file will be generated:

```
resume-pdf-simple-v1.pdf
```

---

## ✏ How To Edit / Customize This Resume

There are **two ways** to customize it.

---

### ✅ Method 1: Edit the Python Script (Recommended)

Open:

```
resume-pdf-python-v1.py
```

Inside the file, edit the `RESUME_DATA` dictionary.

Example:

```python
RESUME_DATA = {
    "name": "Your Name",
    "contact": "Email | Phone | LinkedIn | GitHub",
}
```

---

### 🔹 Edit Skills

Modify:

```python
"skills": [
    ["Programming Languages", "Python, JavaScript"],
]
```

---

### 🔹 Edit Experience

Modify:

```python
"experience": {
    "title": "Software Developer – Company",
    "points": [
        "Built scalable applications",
    ],
}
```

---

### 🔹 Add New Sections

You can:

* Add new keys inside `RESUME_DATA`
* Modify layout styles
* Change heading colors
* Adjust spacing
* Change font sizes
* Add new tables
* Add hyperlinks

---

### ✅ Method 2: Edit the Generated PDF Directly

Use tools like:

* Adobe Acrobat Pro
* LibreOffice Draw
* Foxit PDF Editor

Best for small changes only.

---

## 🎨 How To Improve This PDF Resume

This template is intentionally simple. You can upgrade it further.

---

### 🔥 Layout Improvements

* Add sidebar layout
* Add profile photo section
* Add skill progress bars
* Two-column layout
* Add section icons

---

### 🎨 Design Improvements

* Custom fonts (TTF registration in ReportLab)
* Theme color system
* Section dividers
* Modern spacing scale
* Header background highlight

---

### 📊 Advanced Improvements

* Add QR code linking to portfolio
* Clickable hyperlinks
* Add GitHub stats preview
* Dynamic JSON-based resume loader
* Multiple theme versions (v1, v2, v3)

---

### 🤖 Advanced Technical Enhancements

* CLI-based resume builder
* Resume data from JSON file
* Web UI resume generator
* Resume version comparison system
* AI-generated summaries

---

## 🖼 Screenshots

Add a preview image inside this folder:

```
screenshot.png
```

Then reference it in README:

```md
![Resume Preview](screenshot.png)
```

---

## 📦 Dependencies

Required:

```
reportlab
```

No heavy frameworks required.

---

## 🎯 Who Is This For?

* Students applying for internships
* Developers applying for jobs
* Engineers needing ATS-friendly resume
* Contributors experimenting with PDF automation
* Anyone learning PDF generation with Python

---

## 🧹 Repository Standards Followed

This project follows DIYResume contribution rules:

* Lowercase folder naming
* Hyphen-based naming
* Structured file naming
* Clean folder structure
* Dedicated README file
* Script included for reproducibility

---

## 🚀 Future Improvements

* Modern v2 template
* Minimalist black & white version
* Corporate theme
* Sidebar layout version
* LaTeX comparison version

---

## 🤝 Contributing

If you want to improve this template:

1. Fork the repository
2. Create a new branch
3. Improve layout or structure
4. Follow naming conventions
5. Update README if needed
6. Submit a Pull Request

Please follow:
📌 CONTRIBUTING.md

---

## 🌟 About DIYResume

DIYResume is not about templates.

It’s about innovation.

Build:

* Interactive resumes
* AI resumes
* CLI resumes
* Experimental formats
* Futuristic resume ideas

Push boundaries.

---

## 📜 License

You may use an open-source license (MIT recommended).

---

## 🚀 Let’s Redefine Resumes

This is version 1.

Improve it.
Rebuild it.
Reimagine it.

Your resume should represent your creativity.

Build it your way.
