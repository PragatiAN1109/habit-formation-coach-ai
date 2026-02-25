# 🧠 Habit Formation Coach AI

> **University Assignment:** Build a Specialized AI Assistant
> Built on the *Atomic Habits* framework by James Clear

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-2.3+-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 📌 Overview

The **Habit Formation Coach AI** helps users build lasting habits using the science-backed principles from *Atomic Habits*. It generates personalized habit plans using identity-based design, implementation intentions, habit stacking, environment design, and weekly tracking — with full knowledge base citations.

---

## 🗂️ Repository Structure

```
habit-formation-coach-ai/
├── README.md                        ← You are here
├── LICENSE                          ← MIT
├── .gitignore
│
├── docs/                            ← Assignment documentation
│   ├── SYSTEM_PROMPT.md             ← Assistant persona & interaction rules
│   ├── ASSIGNMENT_WRITEUP.md        ← Full writeup with all 6 functions
│   ├── DEMO_SCRIPT.md               ← 4-5 minute structured demo script
│   └── REFLECTION.md                ← 150-200 word reflection
│
├── kb/                              ← Knowledge base (3 files)
│   ├── AtomicHabits_Summary.md      ← Core framework concepts
│   ├── HabitTemplates.md            ← 7 habit design templates
│   └── CommonPitfalls.md            ← 8 common pitfalls + solutions
│
└── app/                             ← Flask application
    ├── server.py                    ← Main app + deterministic logic
    ├── requirements.txt             ← Flask dependency
    ├── README.md                    ← How to run locally
    └── templates/
        └── index.html               ← Single-page UI
```

---

## ✨ Six Core Functions

| # | Function | Description |
|---|----------|-------------|
| 1 | **Knowledge Q&A** | Progressive-depth answers about habit science |
| 2 | **Habit Setup Guide** | Step-by-step personalized plan (identity → tracker) |
| 3 | **Real-World Connections** | Case studies connecting theory to everyday life |
| 4 | **Critical Thinking Prompts** | Reflective questions to deepen engagement |
| 5 | **Personalized Assessment** | Diagnostic questions → tailored recommendations |
| 6 | **Skill Development Tracking** | Weekly visual tracker with "never miss twice" coaching |

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

For any habit goal you enter, the app produces:

1. **Identity Statement** — `[KB: AtomicHabits_Summary.md — Identity-Based Habits]`
2. **Implementation Intention** — `[KB: HabitTemplates.md — Template 2]`
3. **Habit Stack** — `[KB: HabitTemplates.md — Template 3]`
4. **Environment Design Tips** — `[KB: AtomicHabits_Summary.md — Environment Design]`
5. **Two-Minute Rule Starter** — `[KB: AtomicHabits_Summary.md — The Two-Minute Rule]`
6. **Weekly Tracker** — `[KB: HabitTemplates.md — Template 5]`
7. **Pitfall Warning** — `[KB: CommonPitfalls.md — Pitfall 1]`

---

## 📚 Knowledge Base

The assistant cites all recommendations using the format:
```
[KB: filename — section]
```
If not found in KB, the assistant says: *"Not found in KB — general guidance below."*

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

*Built with care for the "Build a Specialized AI Assistant" university assignment.*
