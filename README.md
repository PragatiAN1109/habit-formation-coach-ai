# 🧠 Habit Formation Coach AI

> **University Assignment:** Build a Specialized AI Assistant
> Built on the *Atomic Habits* framework by James Clear

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-2.3+-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 🎬 Demo Video

**[▶ Watch Demo Recording — Google Drive](https://drive.google.com/file/d/1TN477dpEMz1YqYbsrtIutVE37S5yFsOi/view?usp=sharing)**

---

## 📌 Overview

The **Habit Formation Coach AI** helps users build lasting habits using the science-backed principles from *Atomic Habits*. It generates personalized habit plans using identity-based design, implementation intentions, habit stacking, environment design, and weekly tracking — with full academic-style citations traceable to the source material.

---

## 🗂️ Repository Structure

```
habit-formation-coach-ai/
├── README.md                        ← You are here
├── SUBMISSION.md                    ← Submission checklist + video link
├── LICENSE                          ← MIT
├── .gitignore
│
├── docs/                            ← Assignment documentation
│   ├── SYSTEM_PROMPT.md             ← Assistant persona & interaction rules
│   ├── ASSIGNMENT_WRITEUP.md        ← Full writeup with all 6 functions
│   ├── SAMPLE_INTERACTIONS.md       ← Polished sample output for all 6 functions
│   └── REFLECTION.md                ← 150-200 word reflection
│
├── kb/                              ← Knowledge base (3 reference documents)
│   ├── AtomicHabits_Summary.md      ← Core framework concepts
│   ├── HabitTemplates.md            ← Habit design templates
│   └── CommonPitfalls.md            ← Common failure modes + solutions
│
└── app/                             ← Flask application
    ├── server.py                    ← Main app + deterministic plan logic
    ├── requirements.txt             ← Flask dependency
    ├── README.md                    ← How to run locally
    └── templates/
        └── index.html               ← Single-page UI (dark theme)
```

---

## ✨ Six Core Functions

| # | Function | Description |
|---|----------|-------------|
| 1 | **Knowledge Q&A** | Progressive-depth answers about habit science |
| 2 | **Habit Setup Guide** | Full plan: identity → loop → stack → environment → tracker |
| 3 | **Real-World Connections** | Case studies connecting theory to everyday life |
| 4 | **Critical Thinking Prompts** | 3 psychology-grounded reflective questions per failure mode |
| 5 | **Personalized Assessment** | Scored evaluation (X/10) with strengths, gaps, and revised plan |
| 6 | **Skill Development Tracking** | 4-week tracker with identity review and escalation path |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/PragatiAN1109/habit-formation-coach-ai.git
cd habit-formation-coach-ai/app

# Install dependencies
pip install -r requirements.txt

# Run the app
python server.py
```

Open **[http://localhost:5000](http://localhost:5000)** in your browser.

---

## 📊 What the App Generates

For any habit goal entered, the app produces an 8-section structured plan:

| Section | Content | Citation |
|---------|---------|----------|
| 1 | Habit Loop Analysis (Cue/Craving/Response/Reward) | *(Atomic Habits — The Habit Loop)* |
| 2 | Identity Statement | *(Atomic Habits — Identity-Based Habits)* |
| 3 | Implementation Intention | *(Atomic Habits — Implementation Intentions)* |
| 4 | Habit Stack | *(Atomic Habits — Habit Stacking)* |
| 5 | Environment Design (law-labeled table) | *(Atomic Habits — Environment Design)* |
| 6 | Two-Minute Rule Starter | *(Atomic Habits — The Two-Minute Rule)* |
| 7 | Weekly Tracker + Assessment Score | *(Atomic Habits — Habit Tracking)* |
| 8 | Behavioral Risk Factor | *(Atomic Habits — The Four Laws)* |

---

## 📚 Citation Format

All recommendations use academic-style citations:
```
(Atomic Habits — Concept Name)
```
If content draws on general behavioral science rather than the book directly, the app states: *"General behavioral science principle (not directly from Atomic Habits)."*

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

*Built for the "Build a Specialized AI Assistant" university assignment · Northeastern University · 2026*
