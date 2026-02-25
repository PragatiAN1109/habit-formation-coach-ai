# 🧠 Habit Formation Coach AI

> A Specialized AI Assistant built on the **Atomic Habits** framework by James Clear.
> University Assignment — Build a Specialized AI Assistant

---

## 📌 Overview

The Habit Formation Coach AI helps users build lasting habits using the science-backed principles from *Atomic Habits*. It guides users through identity-based habit design, implementation intentions, habit stacking, and environment design.

## 🗂️ Repository Structure

```
habit-formation-coach-ai/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── SYSTEM_PROMPT.md
│   ├── ASSIGNMENT_WRITEUP.md
│   ├── DEMO_SCRIPT.md
│   └── REFLECTION.md
├── kb/
│   ├── AtomicHabits_Summary.md
│   ├── HabitTemplates.md
│   └── CommonPitfalls.md
└── app/
    ├── server.py
    ├── requirements.txt
    ├── README.md
    └── templates/
        └── index.html
```

## ✨ Core Functions

| # | Function | Description |
|---|----------|-------------|
| 1 | Knowledge Q&A | Progressive-depth answers about habit science |
| 2 | Habit Setup Guide | Step-by-step personalized habit plan |
| 3 | Real-World Connections | Case studies and examples |
| 4 | Critical Thinking Prompts | Reflective questions to deepen understanding |
| 5 | Personalized Assessment | Identify habit strengths & gaps |
| 6 | Skill Development Tracking | Weekly progress tracker |

## 🚀 Quick Start (Flask App)

```bash
cd app
pip install -r requirements.txt
python server.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## 📚 Knowledge Base

See the `/kb` directory for curated summaries used by the assistant:
- `AtomicHabits_Summary.md` — Core framework concepts
- `HabitTemplates.md` — Habit design templates
- `CommonPitfalls.md` — What to avoid

## 📄 License

MIT — see [LICENSE](LICENSE)
