# Habit Formation Coach AI — Flask App

## Overview

A minimal Flask web application that generates structured habit plans based on the Atomic Habits framework. No external API calls — all logic is deterministic and grounded in the project's knowledge base.

---

## Requirements

- Python 3.8+
- pip

---

## Installation & Running Locally

```bash
# 1. Navigate to the app directory
cd app

# 2. (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python server.py
```

The app will start on **http://localhost:5000**

---

## What It Generates

Enter any habit goal and the app produces a complete plan with:

| Output | Description | KB Source |
|--------|-------------|-----------|
| Identity Statement | Who you're becoming, not just what you're doing | AtomicHabits_Summary.md |
| Implementation Intention | Exact when/where plan | HabitTemplates.md — Template 2 |
| Habit Stack | Link to existing habit | HabitTemplates.md — Template 3 |
| Environment Design | 3 specific environment tips | AtomicHabits_Summary.md |
| Two-Minute Rule Starter | Smallest possible version | AtomicHabits_Summary.md |
| Weekly Tracker | 7-day visual tracker | HabitTemplates.md — Template 5 |
| Pitfall Warning | Most common failure to avoid | CommonPitfalls.md |

---

## Example Inputs

- `I want to read 20 pages every morning`
- `Start meditating for 10 minutes daily`
- `Build a daily exercise habit — 30 minutes each morning`
- `I want to journal every night before bed`
- `Start saving money — set aside $50 per week`

---

## Architecture

```
app/
├── server.py           # Flask routes + deterministic habit plan logic
├── requirements.txt    # Flask dependency
└── templates/
    └── index.html      # Single-page UI with full CSS styling
```

All knowledge base logic is encoded in Python dictionaries in `server.py`, mapped directly to the `/kb/*.md` files in the repository.

---

## Notes

- No database required
- No external API calls
- Runs entirely on localhost
- Designed for screen recording demos (clean, uncluttered UI)
