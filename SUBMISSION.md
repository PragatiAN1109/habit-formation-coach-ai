# Submission — Habit Formation Coach AI

**Course:** Build a Specialized AI Assistant
**Platform:** Claude by Anthropic — https://claude.northeastern.edu/
**Student:** PragatiAN1109
**Repository:** https://github.com/PragatiAN1109/habit-formation-coach-ai

---

## Submission Checklist

| Item | Location | Status |
|------|----------|--------|
| System Prompt | `docs/SYSTEM_PROMPT.md` | ✅ Complete |
| Assignment Writeup (personality, goals, 6 functions) | `docs/ASSIGNMENT_WRITEUP.md` | ✅ Complete |
| Sample Interactions (all 6 functions) | `docs/SAMPLE_INTERACTIONS.md` | ✅ Complete |
| Demo Script | `docs/DEMO_SCRIPT.md` | ✅ Complete |
| Reflection (150–200 words) | `docs/REFLECTION.md` | ✅ Complete |
| Knowledge Base — Core Framework | `kb/AtomicHabits_Summary.md` | ✅ Complete |
| Knowledge Base — Habit Templates | `kb/HabitTemplates.md` | ✅ Complete |
| Knowledge Base — Common Pitfalls | `kb/CommonPitfalls.md` | ✅ Complete |
| Flask Application | `app/server.py` | ✅ Complete |
| App Template | `app/templates/index.html` | ✅ Complete |
| Demo Video | See link below | ⬜ Add link before submitting |

---

## Demo Video

> **🎬 Video Link:** `[PASTE YOUR SCREEN RECORDING LINK HERE]`
>
> Recommended tools to record:
> - **Loom** (free, instant shareable link) — https://loom.com
> - **OBS Studio** (free, local recording) — https://obsproject.com
> - **macOS:** Cmd + Shift + 5 → record screen → upload to Google Drive/YouTube
> - **Windows:** Win + G (Game Bar) → record → upload to Google Drive/YouTube
>
> Upload to Google Drive, YouTube (unlisted), or Loom, then paste the link above.

---

## How to Run the App Locally (for demo recording)

```bash
# 1. Clone the repository
git clone https://github.com/PragatiAN1109/habit-formation-coach-ai.git
cd habit-formation-coach-ai/app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python server.py

# 4. Open in browser
# http://localhost:5000
```

---

## Grading Reference

| Component | Points | Location |
|-----------|--------|----------|
| Personality (~100 words) | 4 | `docs/ASSIGNMENT_WRITEUP.md` §1 |
| Core Goals (3) | 4 | `docs/ASSIGNMENT_WRITEUP.md` §2 |
| Approach description | 4 | `docs/ASSIGNMENT_WRITEUP.md` §3 |
| Function 1 — Knowledge Q&A | 15 | `docs/ASSIGNMENT_WRITEUP.md` + `docs/SAMPLE_INTERACTIONS.md` |
| Function 2 — Habit Setup Guide | 15 | `docs/ASSIGNMENT_WRITEUP.md` + `docs/SAMPLE_INTERACTIONS.md` |
| Function 3 — Real-World Connections | 10 | `docs/ASSIGNMENT_WRITEUP.md` + `docs/SAMPLE_INTERACTIONS.md` |
| Function 4 — Critical Thinking | 10 | `docs/ASSIGNMENT_WRITEUP.md` + `docs/SAMPLE_INTERACTIONS.md` |
| Function 5 — Personalized Assessment | 10 | `docs/ASSIGNMENT_WRITEUP.md` + `docs/SAMPLE_INTERACTIONS.md` |
| Function 6 — Skill Development Tracking | 10 | `docs/ASSIGNMENT_WRITEUP.md` + `docs/SAMPLE_INTERACTIONS.md` |
| Bonus — Visual Aids | 10 | `docs/ASSIGNMENT_WRITEUP.md` §Bonus Function 7 + `app/` |
| Demo Video (3–5 min) | 12 | Video link above |
| Reflection (150–200 words) | — | `docs/REFLECTION.md` |
| **Total (excl. quality score)** | **80** | |
| Quality Score (percentile) | 20 | Grader evaluation |
| **Grand Total** | **100** | |
