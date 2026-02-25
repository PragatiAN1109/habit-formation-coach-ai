# Demo Script — Habit Formation Coach AI

**Total Time:** 4–5 minutes
**Format:** Screen recording with live narration
**Tool:** Flask App running at localhost:5000

---

## Pre-Demo Setup Checklist

- [ ] Flask app running (`python server.py`)
- [ ] Browser open at http://localhost:5000
- [ ] Terminal hidden or minimized
- [ ] Screen resolution clean (1280x720 minimum)
- [ ] No notifications

---

## Segment 1: Introduction (0:00 – 0:30)

**What to say:**
> "This is the Habit Formation Coach AI — a specialized assistant built on James Clear's Atomic Habits framework. It generates personalized habit plans using identity-based design, implementation intentions, habit stacking, and environment design. Let me show you how it works."

**What to show:** Landing page of the app (clean, loaded, ready for input)

---

## Segment 2: Core Habit Plan Generation (0:30 – 2:00)

**Prompt to type:**
```
I want to build a daily reading habit — 20 pages every morning.
```

**What to show:**
- Type the goal into the input field
- Click "Generate My Habit Plan"
- Walk through each output section:
  1. **Identity Statement** — "I am the type of person who invests in learning every day."
  2. **Implementation Intention** — "I will read 20 pages at 7:15 AM in my kitchen, after breakfast."
  3. **Habit Stacking** — "After I finish my morning coffee, I will open my book and read."
  4. **Environment Design** — "Place your current book on the breakfast table tonight."
  5. **Weekly Tracker** — Show the 7-day tracker output

**Narration cues:**
- "Notice how the plan starts with identity — not just a goal, but who you're becoming."
- "The implementation intention removes decision fatigue — you know exactly when and where."
- "Habit stacking borrows the momentum of an existing habit."

---

## Segment 3: Second Example — Different Goal Area (2:00 – 3:00)

**Prompt to type:**
```
I want to start meditating for 10 minutes each day.
```

**What to show:**
- New input, instant generation
- Compare output to the previous example — different identity statement, different anchor habit
- Point out the KB citation format in the output

**Narration cue:**
> "Every plan is generated fresh — different goal, different identity, different habit stack. The underlying logic comes from the same knowledge base."

---

## Segment 4: Knowledge Base Citation Demo (3:00 – 3:45)

**What to show:**
- Point to any `[KB: ...]` citation in the output
- Explain: "Every recommendation is traceable back to a specific section of the knowledge base. If the information isn't in the KB, the app says so explicitly."

**Narration cue:**
> "This citation system ensures the assistant is grounded in the source material — not just generating generic advice."

---

## Segment 5: Wrap-Up (3:45 – 4:30)

**What to show:**
- Return to the repository structure (GitHub page or file tree)
- Briefly show: `kb/` folder, `docs/` folder, `app/` folder

**What to say:**
> "The full project includes a three-file knowledge base, detailed documentation including a system prompt and writeup, and this clean Flask web app. Everything is designed to be demo-friendly, modular, and grounded in the Atomic Habits framework."

---

## Optional Extension: Pitfalls Callout (if time permits)

**What to say:**
> "One thing this assistant is designed to prevent: starting too big. The Two-Minute Rule is built into every plan — notice the habit stack always starts with the smallest possible action, not the ambitious outcome."

`[KB: CommonPitfalls.md — Pitfall 1: Starting Too Big]`
