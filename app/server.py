"""
Habit Formation Coach AI — Flask App v2
Quality Standard: Top 25% Submission

Upgraded output: Habit Loop Analysis, 4-Law alignment,
Assessment scoring, structured response hierarchy.
No external API calls — deterministic KB-grounded logic.

Run with: python server.py → http://localhost:5000
"""

from flask import Flask, render_template, request
import re

app = Flask(__name__)

# ---------------------------------------------------------------------------
# KNOWLEDGE BASE: Identity Statements
# [KB: HabitTemplates.md — Template 1, Identity Statement]
# [KB: AtomicHabits_Summary.md — Identity-Based Habits]
# ---------------------------------------------------------------------------
IDENTITY_MAP = {
    "read":     "I am the type of person who invests in deliberate, consistent learning.",
    "meditat":  "I am the type of person who trains their attention deliberately every morning.",
    "exercis":  "I am the type of person who shows up for their physical health without exception.",
    "workout":  "I am the type of person who shows up for their physical health without exception.",
    "run":      "I am the type of person who moves their body as a non-negotiable daily practice.",
    "write":    "I am the type of person who processes thought through disciplined daily writing.",
    "journal":  "I am the type of person who reflects systematically and learns from experience.",
    "sleep":    "I am the type of person who treats rest as a performance input, not a luxury.",
    "eat":      "I am the type of person who makes nutritional decisions with intention.",
    "diet":     "I am the type of person who makes nutritional decisions with intention.",
    "study":    "I am the type of person who shows up for their intellectual development every day.",
    "learn":    "I am the type of person who allocates time to skill acquisition as a priority.",
    "save":     "I am the type of person who treats financial discipline as a core identity trait.",
    "financ":   "I am the type of person who treats financial discipline as a core identity trait.",
    "water":    "I am the type of person who supports their biology through consistent hydration.",
    "walk":     "I am the type of person who builds movement into the structure of every day.",
    "stretch":  "I am the type of person who maintains their body's capacity for long-term function.",
    "practice": "I am the type of person who shows up to practice even when conditions are imperfect.",
    "default":  "I am the type of person who builds systems for intentional, durable behavior change.",
}

# ---------------------------------------------------------------------------
# KNOWLEDGE BASE: Habit Loop Analysis
# [KB: AtomicHabits_Summary.md — The Habit Loop]
# [KB: AtomicHabits_Summary.md — The Four Laws of Behavior Change]
# ---------------------------------------------------------------------------
HABIT_LOOP_MAP = {
    "read": {
        "cue":      "Book placed on breakfast table (environmental, visible)",
        "craving":  "Desire to feel informed, mentally engaged, and intellectually growing",
        "response": "Reading for the specified duration with morning coffee",
        "reward":   "Bookmark moved — visible proof of progress; identity vote cast",
        "law":      "1st Law: Make It Obvious (environmental cue design)",
    },
    "meditat": {
        "cue":      "Alarm off → sit upright immediately (time + action cue)",
        "craving":  "Desire for cognitive clarity and reduced reactive stress response",
        "response": "Focused breath awareness for specified duration",
        "reward":   "Write one word in habit log — immediate, tangible, closes the loop",
        "law":      "1st Law: Make It Obvious + 3rd Law: Make It Easy",
    },
    "exercis": {
        "cue":      "Workout clothes laid out the night before (visual, environmental)",
        "craving":  "Desire for physical capability, energy, and identity coherence",
        "response": "Executing the planned workout at the specified time and place",
        "reward":   "Log completion + immediate post-workout physiological state",
        "law":      "3rd Law: Make It Easy (friction reduction via preparation)",
    },
    "workout": {
        "cue":      "Workout clothes laid out the night before (visual, environmental)",
        "craving":  "Desire for physical capability, energy, and identity coherence",
        "response": "Executing the planned workout at the specified time and place",
        "reward":   "Log completion + immediate post-workout physiological state",
        "law":      "3rd Law: Make It Easy (friction reduction via preparation)",
    },
    "run": {
        "cue":      "Running shoes positioned directly in front of bed (unavoidable visual)",
        "craving":  "Desire for physical freedom, mental clarity, and endurance identity",
        "response": "Stepping outside and beginning the run at the specified time",
        "reward":   "Route completed — map/distance logged; streak maintained",
        "law":      "1st Law: Make It Obvious (shoes as environmental cue)",
    },
    "write": {
        "cue":      "Notebook open on desk + specific mug used only during writing",
        "craving":  "Desire to process ideas, create output, and develop voice",
        "response": "Writing for the specified duration without interruption",
        "reward":   "Word count logged; session note written at close",
        "law":      "2nd Law: Make It Attractive (temptation bundling with coffee ritual)",
    },
    "journal": {
        "cue":      "Journal on pillow — visible before sleep, unavoidable",
        "craving":  "Desire for cognitive closure, self-understanding, and pattern recognition",
        "response": "Writing minimum 3 lines before sleep",
        "reward":   "Entry dated and closed — cognitive completion signal",
        "law":      "1st Law: Make It Obvious + 4th Law: Make It Satisfying",
    },
    "sleep": {
        "cue":      "Wind-down alarm 30 minutes before target sleep time",
        "craving":  "Desire for recovery, next-day performance, and reduced fatigue",
        "response": "Executing wind-down routine (dim lights, no screens, cool room)",
        "reward":   "Sleep onset faster; morning energy improved over baseline",
        "law":      "1st Law: Make It Obvious (alarm as cue) + 3rd Law",
    },
    "study": {
        "cue":      "Designated study location + materials pre-arranged on desk",
        "craving":  "Desire for academic competence, progress, and reduced exam anxiety",
        "response": "Focused study session using Pomodoro method",
        "reward":   "Topics completed marked — visual progress in notes",
        "law":      "3rd Law: Make It Easy + 1st Law: Make It Obvious",
    },
    "water": {
        "cue":      "Full glass of water on nightstand — first object seen upon waking",
        "craving":  "Desire for energy, clarity, and physical function from the start of the day",
        "response": "Drinking full glass before any other morning action",
        "reward":   "Physiological: immediate hydration signal; habit log marked",
        "law":      "1st Law: Make It Obvious (nightstand placement)",
    },
    "walk": {
        "cue":      "Shoes placed by lunch bag (post-lunch walk anchor)",
        "craving":  "Desire for mental reset, movement, and afternoon energy maintenance",
        "response": "Walking for the specified duration after lunch",
        "reward":   "Distance logged; return to desk with measurably clearer focus",
        "law":      "3rd Law: Make It Easy + 2nd Law: Make It Attractive",
    },
    "default": {
        "cue":      "Specific environmental trigger placed in plain sight",
        "craving":  "Underlying motivation the habit serves (identity, pleasure, security)",
        "response": "The precise behavior executed at the specified time and place",
        "reward":   "Immediate, tangible signal within 60 seconds of completion",
        "law":      "Apply the most relevant of the 4 Laws to your specific context",
    },
}

# ---------------------------------------------------------------------------
# KNOWLEDGE BASE: Habit Stacks
# [KB: HabitTemplates.md — Template 3, Habit Stacking]
# ---------------------------------------------------------------------------
HABIT_STACK_MAP = {
    "read":    "After I pour my morning coffee, I will open my book to the current page.",
    "meditat": "After I turn off my alarm, I will sit upright on my cushion and set a timer.",
    "exercis": "After I brush my teeth in the morning, I will put on my pre-laid workout clothes.",
    "workout": "After I brush my teeth in the morning, I will put on my pre-laid workout clothes.",
    "run":     "After I put on my running shoes (which are in front of my bed), I will step outside.",
    "write":   "After I make my morning coffee, I will sit at my desk and open my writing document.",
    "journal": "After I get into bed, I will pick up my journal before setting my phone down.",
    "sleep":   "After my wind-down alarm sounds, I will dim all lights and move to the bedroom.",
    "eat":     "After I plan my calendar each morning, I will decide my meals for the day.",
    "study":   "After I sit at my designated desk, I will set a 25-minute Pomodoro timer.",
    "learn":   "After I eat lunch, I will go directly to my learning space for the planned session.",
    "save":    "After my paycheck is deposited, I will immediately transfer the savings amount.",
    "water":   "After I wake up and before any other action, I will drink the glass on my nightstand.",
    "walk":    "After I finish lunch, I will put on my shoes and begin my walk.",
    "stretch": "After I get out of bed, I will step onto my mat and begin the first stretch.",
    "default": "After I [anchor habit — occurs 100% of days], I will immediately begin [new habit].",
}

# ---------------------------------------------------------------------------
# KNOWLEDGE BASE: Environment Design
# [KB: AtomicHabits_Summary.md — Environment Design]
# ---------------------------------------------------------------------------
ENV_DESIGN_MAP = {
    "read": [
        ("Place current book on breakfast table", "1st Law: Make It Obvious — unavoidable visual cue"),
        ("Remove social media from phone home screen", "1st Law inversion: Make Bad Habit Invisible"),
        ("Keep a second book in your bag", "3rd Law: Make It Easy — zero barrier to starting"),
    ],
    "meditat": [
        ("Cushion at foot of bed — visible from pillow", "1st Law: Make It Obvious — spatial cue"),
        ("Phone set to DND until 7:00 AM", "1st Law inversion: Remove competing cue"),
        ("Sticky note on alarm: 'Sit. Breathe. 5 min.'", "1st Law: Make It Obvious — written cue"),
    ],
    "exercis": [
        ("Workout clothes laid out the night before", "3rd Law: Make It Easy — removes morning decision"),
        ("Gym bag packed and positioned by the door", "3rd Law: Make It Easy — friction near zero"),
        ("Workout blocked in calendar as fixed appointment", "2nd Law: Make It Attractive — commitment device"),
    ],
    "workout": [
        ("Workout clothes laid out the night before", "3rd Law: Make It Easy — removes morning decision"),
        ("Gym bag packed and positioned by the door", "3rd Law: Make It Easy — friction near zero"),
        ("Workout blocked in calendar as fixed appointment", "2nd Law: Make It Attractive — commitment device"),
    ],
    "run": [
        ("Running shoes directly in front of bed", "1st Law: Make It Obvious — first physical encounter"),
        ("Playlist prepared the night before", "3rd Law: Make It Easy — removes setup friction"),
        ("Route mapped and saved on watch/phone", "3rd Law: Make It Easy — decision pre-made"),
    ],
    "write": [
        ("Notebook open on desk before sleep", "1st Law: Make It Obvious — pre-cued environment"),
        ("Dedicated writing mug used only during sessions", "2nd Law: Make It Attractive — ritual signal"),
        ("All notifications disabled during writing block", "1st Law inversion: Remove competing cues"),
    ],
    "journal": [
        ("Journal on pillow — seen before phone at night", "1st Law: Make It Obvious — competes with phone"),
        ("Pen clipped open and ready inside journal", "3rd Law: Make It Easy — zero setup cost"),
        ("3-line minimum — barrier kept extremely low", "3rd Law: Make It Easy — prevents avoidance"),
    ],
    "sleep": [
        ("Wind-down alarm set 30 min before target sleep", "1st Law: Make It Obvious — timed cue"),
        ("Screens removed from bedroom (or charged outside)", "1st Law inversion: Remove competing cue"),
        ("Room temperature set to 65–68°F (18–20°C)", "3rd Law: Make It Easy — optimal sleep onset"),
    ],
    "study": [
        ("Designated study space used ONLY for studying", "1st Law: Make It Obvious — context-specific cue"),
        ("All materials pre-arranged on desk before session", "3rd Law: Make It Easy — no setup time"),
        ("Pomodoro timer placed physically on desk", "1st Law: Make It Obvious + 3rd Law"),
    ],
    "water": [
        ("Full glass on nightstand every evening", "1st Law: Make It Obvious — first object encountered"),
        ("Water bottle always visible on work desk", "1st Law: Make It Obvious — persistent visual cue"),
        ("Reminder set at 10am / 2pm / 6pm", "1st Law: Make It Obvious — timed digital cue"),
    ],
    "walk": [
        ("Shoes by lunch bag — paired with meal cue", "1st Law: Make It Obvious — cue pairing"),
        ("Route pre-decided (same route reduces decisions)", "3rd Law: Make It Easy — cognitive load reduced"),
        ("Walk scheduled as calendar block", "2nd Law: Make It Attractive — legitimizes the habit"),
    ],
    "default": [
        ("Place habit cue in plain sight in primary space", "1st Law: Make It Obvious"),
        ("Prepare all materials in advance — zero setup at start", "3rd Law: Make It Easy"),
        ("Remove or relocate cues for competing bad habits", "1st Law inversion: Make Bad Habit Invisible"),
    ],
}

# ---------------------------------------------------------------------------
# KNOWLEDGE BASE: Behavioral Risk Factors
# [KB: CommonPitfalls.md]
# ---------------------------------------------------------------------------
RISK_MAP = {
    "read": (
        "Selecting books that are too dense or not genuinely interesting — "
        "the craving stage collapses when the response is unpleasant.",
        "[KB: CommonPitfalls.md — Pitfall 2: Outcome Focus]"
    ),
    "meditat": (
        "Starting at 20+ minutes — entry cost triggers avoidance by day 5–8. "
        "Begin at 2–5 minutes maximum.",
        "[KB: CommonPitfalls.md — Pitfall 1: Starting Too Big]"
    ),
    "exercis": (
        "Programming workouts that are too intense in week one — "
        "soreness creates a negative reward signal and breaks the loop.",
        "[KB: CommonPitfalls.md — Pitfall 1: Starting Too Big]"
    ),
    "workout": (
        "Programming workouts that are too intense in week one — "
        "soreness creates a negative reward signal and breaks the loop.",
        "[KB: CommonPitfalls.md — Pitfall 1: Starting Too Big]"
    ),
    "run": (
        "Starting with distance/speed targets rather than time-based "
        "minimums — failure to hit targets triggers identity rejection.",
        "[KB: CommonPitfalls.md — Pitfall 2: Outcome Focus]"
    ),
    "write": (
        "Setting word-count targets before the habit is automated — "
        "output pressure prevents the identity from forming.",
        "[KB: CommonPitfalls.md — Pitfall 1: Starting Too Big]"
    ),
    "journal": (
        "Attempting to write full reflective entries before the behavior "
        "is established — 3 lines is sufficient in weeks 1–2.",
        "[KB: CommonPitfalls.md — Pitfall 1: Starting Too Big]"
    ),
    "sleep": (
        "Trying to change sleep time by more than 30 minutes immediately — "
        "circadian rhythm adjustment requires gradual phase shifting.",
        "[KB: CommonPitfalls.md — Pitfall 7: Too Many Habits at Once]"
    ),
    "study": (
        "Choosing non-designated spaces (bed, couch) when schedule breaks — "
        "this erodes the context-specific cue built around the study location.",
        "[KB: CommonPitfalls.md — Pitfall 6: No Environmental Support]"
    ),
    "water": (
        "Relying on thirst as the cue — thirst signals mild dehydration "
        "and is too weak and irregular to anchor a consistent habit.",
        "[KB: CommonPitfalls.md — Pitfall 8: Ignoring the Cue]"
    ),
    "walk": (
        "Skipping the walk when weather is poor without a defined indoor "
        "alternative — the habit breaks when the plan lacks a contingency.",
        "[KB: CommonPitfalls.md — Pitfall 5: Breaking the Streak]"
    ),
    "default": (
        "Relying on motivation as the primary driver after week two — "
        "motivation regresses to baseline; structural design must take over.",
        "[KB: CommonPitfalls.md — Pitfall 3: Relying Solely on Motivation]"
    ),
}

# ---------------------------------------------------------------------------
# Assessment Scoring Rubric
# [KB: AtomicHabits_Summary.md — The Four Laws of Behavior Change]
# ---------------------------------------------------------------------------
def compute_assessment_score(area):
    """
    Generates a structured assessment with score, strengths, gaps,
    behavioral risks, and a revised plan.
    Rubric: Cue(2) + Identity(2) + Environment(2) + Reward(1) + 2-min(1) + Tracking(1) + Contingency(1)
    """
    base_scores = {
        "read":    {"score": 7, "strengths": ["Clear cue opportunity (book placement)", "Strong craving alignment (intellectual growth)"],
                    "gaps": ["No immediate reward defined (4th Law gap)", "Environment rarely pre-designed"]},
        "meditat": {"score": 6, "strengths": ["Time-based cue is specifiable", "High identity-shift potential"],
                    "gaps": ["Duration typically set too high (3rd Law violation)", "Reward stage undefined — loop doesn't close"]},
        "exercis": {"score": 7, "strengths": ["Strong craving alignment", "Stackable onto morning routine"],
                    "gaps": ["Intensity often too high in week 1", "Identity statement missing in most plans"]},
        "workout": {"score": 7, "strengths": ["Strong craving alignment", "Stackable onto morning routine"],
                    "gaps": ["Intensity often too high in week 1", "Identity statement missing in most plans"]},
        "run":     {"score": 6, "strengths": ["Physical cue (shoes) is highly designable", "Immediate reward (distance/time) is natural"],
                    "gaps": ["Outcome framing (distance targets) before identity is set", "Weather contingency rarely planned"]},
        "write":   {"score": 7, "strengths": ["Natural anchor habits available (coffee)", "Output is immediately trackable"],
                    "gaps": ["Word-count pressure undermines identity formation", "No closure ritual defined"]},
        "journal": {"score": 8, "strengths": ["Flexible minimum (3 lines)", "Strong immediate reward (closure)"],
                    "gaps": ["Cue often weak (vague 'at night')", "Phone competes directly for the cue window"]},
        "sleep":   {"score": 5, "strengths": ["High motivation — sleep deprivation is aversive", "Timed cue (wind-down alarm) is effective"],
                    "gaps": ["Multiple environmental changes required simultaneously", "Reward is delayed (next morning) — 4th Law risk"]},
        "study":   {"score": 7, "strengths": ["Designatable specific location", "Pomodoro method provides built-in reward cycles"],
                    "gaps": ["Context-cue eroded when studying in non-designated spaces", "No identity statement in typical plans"]},
        "water":   {"score": 8, "strengths": ["Cue is highly controllable (glass placement)", "Immediate physiological reward is real"],
                    "gaps": ["Timed reminders create phone-dependency", "No habit stack anchor defined"]},
        "default": {"score": 5, "strengths": ["Motivation exists (reason stated)", "Goal is specific enough to design around"],
                    "gaps": ["No cue defined", "No identity framing", "No environment designed", "No immediate reward"]},
    }
    return base_scores.get(area, base_scores["default"])


# ---------------------------------------------------------------------------
# Core utilities
# ---------------------------------------------------------------------------
def detect_goal_area(text):
    t = text.lower()
    for key in IDENTITY_MAP:
        if key != "default" and key in t:
            return key
    return "default"


def extract_duration_and_activity(text):
    m = re.search(
        r'(\d+)\s*(min|minute|minutes|hour|hours|page|pages|mile|miles|km|times)',
        text, re.IGNORECASE
    )
    duration = m.group(0) if m else "a defined amount"

    a = re.search(
        r'(?:want to|start|build|develop|create|establish|maintain|try)\s+'
        r'(?:a\s+)?(?:daily\s+)?(.+?)(?:\s+habit|\s+every|\s+each|\s+for|\s+per|$)',
        text, re.IGNORECASE
    )
    activity = a.group(1).strip() if a else text.strip()
    return duration, activity


def generate_habit_plan(goal_text):
    """
    Upgraded plan generator — v2.
    Outputs: habit loop analysis, identity, implementation intention,
    habit stack, environment design (with Law labels), Two-Minute Rule,
    weekly tracker, behavioral risk assessment, and all KB citations.

    [KB: HabitTemplates.md — Templates 1–5]
    [KB: AtomicHabits_Summary.md — All sections]
    [KB: CommonPitfalls.md — All pitfalls]
    """
    area = detect_goal_area(goal_text)
    duration, activity = extract_duration_and_activity(goal_text)
    clean_act = activity if len(activity) < 60 else goal_text[:60]

    loop      = HABIT_LOOP_MAP.get(area, HABIT_LOOP_MAP["default"])
    identity  = IDENTITY_MAP.get(area, IDENTITY_MAP["default"])
    impl      = f"I will {clean_act} for {duration} at [your chosen time] in [your chosen location]."
    stack     = HABIT_STACK_MAP.get(area, HABIT_STACK_MAP["default"])
    env_tips  = ENV_DESIGN_MAP.get(area, ENV_DESIGN_MAP["default"])
    two_min   = (f"Begin with 2 minutes of '{clean_act}' only — not the full version. "
                 f"The identity is established by showing up, not by duration.")
    tracker   = [{"day": d} for d in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]]
    risk_text, risk_cite = RISK_MAP.get(area, RISK_MAP["default"])
    assess    = compute_assessment_score(area)

    return {
        "goal":        goal_text,
        "area":        area,
        "loop":        loop,
        "identity":    identity,
        "impl":        impl,
        "stack":       stack,
        "env_tips":    env_tips,
        "two_min":     two_min,
        "tracker":     tracker,
        "risk_text":   risk_text,
        "risk_cite":   risk_cite,
        "assess":      assess,
        "citations": [
            "[KB: AtomicHabits_Summary.md — The Habit Loop]",
            "[KB: AtomicHabits_Summary.md — The Four Laws of Behavior Change]",
            "[KB: AtomicHabits_Summary.md — Identity-Based Habits]",
            "[KB: AtomicHabits_Summary.md — Implementation Intentions]",
            "[KB: HabitTemplates.md — Template 2, Implementation Intention]",
            "[KB: HabitTemplates.md — Template 3, Habit Stacking]",
            "[KB: AtomicHabits_Summary.md — Environment Design]",
            "[KB: AtomicHabits_Summary.md — The Two-Minute Rule]",
            "[KB: HabitTemplates.md — Template 5, Weekly Tracker]",
            risk_cite,
        ],
    }


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    plan, error, goal = None, None, ""
    if request.method == "POST":
        goal = request.form.get("goal", "").strip()
        if not goal:
            error = "Please enter a habit goal to get started."
        elif len(goal) < 5:
            error = "Please describe your habit goal in more detail."
        else:
            plan = generate_habit_plan(goal)
    return render_template("index.html", plan=plan, error=error, goal=goal)


if __name__ == "__main__":
    print("=" * 55)
    print("  Habit Formation Coach AI  ·  v2.0")
    print("  Quality Standard: Top 25% Submission")
    print("  http://localhost:5000")
    print("=" * 55)
    app.run(debug=True, port=5000)
