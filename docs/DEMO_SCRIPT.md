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
- [ ] No notifications / DND enabled

---

## Segment 1: Introduction (0:00 – 0:30)

**What to say:**
> "This is the Habit Formation Coach AI — a specialized assistant built on James Clear's *Atomic Habits* framework. It generates structured, citation-backed habit plans using identity-based design, implementation intentions, habit stacking, and environment design. Every output is grounded in the book and labeled with its source concept. Let me show you how it works."

**What to show:** Landing page of the app (clean, dark theme, loaded, ready for input)

---

## Segment 2: Core Habit Plan Generation (0:30 – 2:00)

**Prompt to type:**
```
I want to build a daily reading habit — 20 pages every morning.
```

**What to show:**
- Type the goal into the input field
- Click "Analyze & Generate Structured Plan"
- Walk through each numbered output section:

  1. **Habit Loop Analysis** — Point to the color-coded table. *"This maps the goal to all four stages of the habit loop — Cue, Craving, Response, Reward — and identifies which of the Four Laws is being applied."*
  2. **Identity Statement** — *"Every plan starts with identity, not the goal. The user becomes the person who reads daily before they track a single page."*
  3. **Implementation Intention** — *"Exact when and where — this removes decision fatigue entirely."*
  4. **Habit Stack** — *"The new habit is anchored to an existing one. The coffee ritual becomes the trigger."*
  5. **Environment Design** — Point to the law-labeled table. *"Each environment change is labeled with the specific law it applies."*
  6. **Two-Minute Rule** — *"The minimum viable version — identity first, volume second."*
  7. **Weekly Tracker** — *"Seven checkboxes. Target is 5 out of 7, not perfection."*
  8. **Assessment Panel** — *"The plan is scored against a rubric: cue, identity, environment, reward, two-minute rule, and tracking."*

**Key narration point:**
> "Notice every section carries a citation in the format *(Atomic Habits — Concept Name)* — every recommendation is traceable to the source material."

---

## Segment 3: Second Example — Different Goal (2:00 – 3:00)

**Prompt to type:**
```
I want to start meditating for 10 minutes each day.
```

**What to show:**
- New input, instant generation
- Compare output to the previous — different identity statement, different anchor habit, different environment tips
- Point to the References panel at the bottom

**Narration cue:**
> "Every plan is generated fresh — different goal, different identity, different habit stack, different behavioral risk. The underlying logic is identical: the Four Laws applied to whatever the user brings."

---

## Segment 4: Citation System Demo (3:00 – 3:45)

**What to show:**
- Zoom in on any citation tag in the output — e.g. *(Atomic Habits — Habit Stacking)* on the habit stack card
- Scroll to the References panel at the bottom of the plan
- Point to the behavioral risk card

**Narration cue:**
> "Every claim is attributed to a specific concept from the book. If a recommendation draws on general behavioral science rather than *Atomic Habits* directly, the app flags it explicitly. There is no ambiguity about what is book-grounded and what is not."

---

## Segment 5: Wrap-Up (3:45 – 4:30)

**What to show:**
- Switch to the GitHub repository page
- Briefly show: `kb/` folder (reference materials), `docs/` folder (system prompt, writeup, this script), `app/` folder

**What to say:**
> "The full project includes three reference documents derived from *Atomic Habits*, a complete system prompt defining the assistant's persona and interaction rules, a Flask web app with structured visual outputs, and full documentation for every function. Everything is grounded in the framework, visually clear for a demo, and traceable back to the source material."

---

## Optional Extension: Failure Mode / Assessment (if time permits, ~30 sec)

**What to show:**
- Point to the Behavioral Assessment panel (Section 7)
- Point to the Behavioral Risk card (Section 8)

**What to say:**
> "Two sections that go beyond most habit tools: a scored evaluation of the plan's structural quality — does it have a cue, identity statement, environment design, immediate reward? And a specific behavioral risk flag for this habit type, with the failure mode named and cited."

*(Atomic Habits — The Two-Minute Rule)* — the most common risk for new habits.
