"""
DIYResume - Simple Resume 1 (PDF Generator)
--------------------------------------------

This script generates a professional PDF resume using Python and ReportLab.

How to use:
1. Install dependency: pip install reportlab
2. Edit the RESUME_DATA section below
3. Run: python resume-pdf-python-v1.py
4. Your PDF will be generated in the same folder
"""

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    ListFlowable,
    ListItem
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4


# ============================================================
# 📝 EDIT YOUR RESUME DATA HERE
# ============================================================

RESUME_DATA = {
    "name": "YOUR FULL NAME",
    "contact": "Email: your.email@example.com | Phone: +91-XXXXXXXXXX | LinkedIn: linkedin.com/in/yourprofile | GitHub: github.com/yourusername",

    "summary": (
        "Highly motivated and detail-oriented professional with strong expertise "
        "in software development, artificial intelligence, and full-stack technologies. "
        "Proven ability to design, develop, and deploy scalable applications."
    ),

    "skills": [
        ["Programming Languages", "Python, Java, JavaScript, C++, SQL"],
        ["Web Technologies", "HTML, CSS, React, Node.js, Express"],
        ["AI/ML Tools", "TensorFlow, PyTorch, Scikit-learn"],
        ["Databases", "MySQL, MongoDB, PostgreSQL"],
        ["Tools & Platforms", "Git, Docker, AWS, Linux"],
    ],

    "experience": {
        "title": "Software Developer Intern – Company Name (Jan 2024 – Present)",
        "points": [
            "Developed scalable web applications using modern frameworks.",
            "Implemented AI-powered features improving efficiency by 30%.",
            "Collaborated with cross-functional teams for production deployment.",
            "Optimized backend APIs reducing response time by 40%.",
        ],
    },

    "projects": {
        "title": "AI Virtual Assistant Platform",
        "points": [
            "Built a real-time AI assistant with voice and chat features.",
            "Integrated live video interaction system.",
            "Designed scalable backend architecture.",
        ],
    },

    "education": "Bachelor of Technology in Computer Science – University Name (2022 – 2026)",
    "coursework": "Relevant Coursework: Data Structures, Algorithms, Machine Learning, Database Systems, Cloud Computing",

    "certifications": [
        "AWS Certified Cloud Practitioner",
        "Google Data Analytics Certification",
        "Machine Learning Specialization – Coursera",
    ],

    "achievements": [
        "Winner – National Level Hackathon 2024",
        "Open-source contributor with 500+ GitHub commits",
        "Active participant in coding competitions",
    ],
}


# ============================================================
# 🎨 PDF GENERATION LOGIC (No need to modify unless styling)
# ============================================================

def generate_resume(data, filename="resume-pdf-simple-v1.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        "NameStyle",
        parent=styles["Heading1"],
        fontSize=24,
        spaceAfter=10,
    )

    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.HexColor("#1F4E79"),
        spaceBefore=12,
        spaceAfter=6,
    )

    normal_style = styles["Normal"]

    # Header
    elements.append(Paragraph(data["name"], name_style))
    elements.append(Paragraph(data["contact"], normal_style))
    elements.append(Spacer(1, 12))

    # Summary
    elements.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    elements.append(Paragraph(data["summary"], normal_style))
    elements.append(Spacer(1, 10))

    # Skills
    elements.append(Paragraph("TECHNICAL SKILLS", section_style))
    skills_table = Table(data["skills"], colWidths=[2.2 * inch, 3.8 * inch])
    skills_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(skills_table)
    elements.append(Spacer(1, 10))

    # Experience
    elements.append(Paragraph("WORK EXPERIENCE", section_style))
    elements.append(Paragraph(f"<b>{data['experience']['title']}</b>", normal_style))
    elements.append(ListFlowable(
        [ListItem(Paragraph(point, normal_style)) for point in data["experience"]["points"]],
        bulletType="bullet"
    ))
    elements.append(Spacer(1, 10))

    # Projects
    elements.append(Paragraph("PROJECTS", section_style))
    elements.append(Paragraph(f"<b>{data['projects']['title']}</b>", normal_style))
    elements.append(ListFlowable(
        [ListItem(Paragraph(point, normal_style)) for point in data["projects"]["points"]],
        bulletType="bullet"
    ))
    elements.append(Spacer(1, 10))

    # Education
    elements.append(Paragraph("EDUCATION", section_style))
    elements.append(Paragraph(data["education"], normal_style))
    elements.append(Paragraph(data["coursework"], normal_style))
    elements.append(Spacer(1, 10))

    # Certifications
    elements.append(Paragraph("CERTIFICATIONS", section_style))
    elements.append(ListFlowable(
        [ListItem(Paragraph(cert, normal_style)) for cert in data["certifications"]],
        bulletType="bullet"
    ))
    elements.append(Spacer(1, 10))

    # Achievements
    elements.append(Paragraph("ACHIEVEMENTS & ACTIVITIES", section_style))
    elements.append(ListFlowable(
        [ListItem(Paragraph(ach, normal_style)) for ach in data["achievements"]],
        bulletType="bullet"
    ))

    doc.build(elements)
    print(f"\n✅ Resume generated successfully: {filename}")


# ============================================================
# 🚀 RUN SCRIPT
# ============================================================

if __name__ == "__main__":
    generate_resume(RESUME_DATA)
