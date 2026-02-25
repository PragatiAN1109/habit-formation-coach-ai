"""
Habit Formation Coach AI — Flask App
Based on the Atomic Habits framework by James Clear

Run with: python server.py
Serves on: http://localhost:5000
"""

from flask import Flask, render_template, request
import re

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Knowledge Base: Identity Statements by Goal Area
# [KB: HabitTemplates.md — Template 1, Identity Statement]
# ---------------------------------------------------------------------------
IDENTITY_MAP = {
    "read": "I am the type of person who invests in learning every single day.",
    "meditat": "I am the type of person who prioritizes stillness and mental clarity.",
    "exercis": "I am the type of person who takes care of my body through consistent movement.",
    "workout": "I am the type of person who takes care of my body through consistent movement.",
    "run": "I am the type of person who shows up for my health, one step at a time.",
    "write": "I am the type of person who expresses ideas and documents my growth.",
    "journal": "I am the type of person who reflects daily and grows through self-awareness.",
    "sleep": "I am the type of person who protects my rest and recovery.",
    "eat": "I am the type of person who nourishes my body with intention.",
    "diet": "I am the type of person who nourishes my body with intention.",
    "study": "I am the type of person who shows up for my education every day.",
    "learn": "I am the type of person who dedicates time to growing every day.",
    "save": "I am the type of person who manages money with intention and discipline.",
    "financ": "I am the type of person who manages money with intention and discipline.",
    "drink water": "I am the type of person who hydrates and energizes my body daily.",
    "water": "I am the type of person who hydrates and energizes my body daily.",
    "walk": "I am the type of person who moves my body and clears my mind daily.",
    "stretch": "I am the type of person who cares for my body's flexibility and longevity.",
    "practice": "I am the type of person who shows up to practice even when it's hard.",
    "default": "I am the type of person who builds intentional, lasting habits.",
}

# ---------------------------------------------------------------------------
# Knowledge Base: Habit Stacks by Goal Area
# [KB: HabitTemplates.md — Template 3, Habit Stacking]
# ---------------------------------------------------------------------------
HABIT_STACK_MAP = {
    "read": "After I pour my morning coffee, I will read for the planned duration.",
    "meditat": "After I turn off my morning alarm, I will sit up, close my eyes, and breathe.",
    "exercis": "After I brush my teeth in the morning, I will put on my workout clothes.",
    "workout": "After I brush my teeth in the morning, I will put on my workout clothes.",
    "run": "After I put on my shoes in the morning, I will step outside for my run.",
    "write": "After I make my morning coffee, I will open my notebook or document and write.",
    "journal": "After I get into bed at night, I will pick up my journal and write 3 lines.",
    "sleep": "After I finish dinner, I will begin my wind-down routine (dim lights, no screens).",
    "eat": "After I plan my day each morning, I will decide what I will eat for lunch and dinner.",
    "study": "After I arrive at my desk, I will open my notes and start with the first topic.",
    "learn": "After I eat lunch, I will spend time on the skill I am building.",
    "save": "After I get paid, I will immediately transfer my savings amount before spending.",
    "water": "After I wake up and before I do anything else, I will drink a full glass of water.",
    "walk": "After I eat lunch, I will put on my shoes and walk for the planned duration.",
    "stretch": "After I get out of bed each morning, I will roll out my mat and stretch.",
    "default": "After I [choose an existing daily habit], I will practice my new habit immediately.",
}

# ---------------------------------------------------------------------------
# Knowledge Base: Environment Design Tips
# [KB: AtomicHabits_Summary.md — Environment Design]
# ---------------------------------------------------------------------------
ENV_DESIGN_MAP = {
    "read": [
        "Place your current book on your pillow or nightstand — visible, unavoidable.",
        "Keep a book in every bag you carry as a low-friction cue.",
        "Remove social media apps from your home screen to reduce competing cues.",
    ],
    "meditat": [
        "Set up a dedicated meditation spot (cushion, chair) in a quiet corner.",
        "Place your meditation timer on your nightstand, not your phone.",
        "Put a sticky note on your mirror: 'Breathe first. Phone second.'",
    ],
    "exercis": [
        "Lay out your workout clothes the night before — remove the decision barrier.",
        "Keep your gym bag packed and by the door.",
        "Schedule workouts in your calendar like meetings — they are not optional.",
    ],
    "run": [
        "Place your running shoes directly in front of your bed.",
        "Prepare your playlist the night before.",
        "Set a wake-up alarm labeled: 'Run day — shoes are waiting.'",
    ],
    "write": [
        "Keep your notebook open on your desk — open = invitation to write.",
        "Turn off all notifications during your writing window.",
        "Use a specific mug only during writing sessions — it becomes a cue.",
    ],
    "journal": [
        "Keep your journal on your pillow so you see it before sleep.",
        "Use a pen you enjoy — reduce friction by making it a pleasure.",
        "Write just 3 lines minimum — low bar, high consistency.",
    ],
    "sleep": [
        "Set a 'wind-down alarm' 30 minutes before bed — this is your cue.",
        "Remove screens from the bedroom or use blue-light glasses.",
        "Keep the bedroom cool and dark — your environment is your sleep system.",
    ],
    "study": [
        "Designate a specific study location used only for studying.",
        "Keep all study materials on your desk, ready to use.",
        "Use the Pomodoro timer — 25 min focus, 5 min break — placed on your desk.",
    ],
    "water": [
        "Place a full glass of water on your nightstand every evening.",
        "Keep a water bottle visible on your desk at all times.",
        "Set a phone reminder at 10am, 2pm, and 6pm until the habit is automatic.",
    ],
    "default": [
        "Make the cue for your habit visible and obvious in your environment.",
        "Reduce friction — prepare everything you need in advance.",
        "Remove competing cues that lead to bad habits in the same space.",
    ],
}

# ---------------------------------------------------------------------------
# Deterministic logic: detect goal area from user input
# ---------------------------------------------------------------------------
def detect_goal_area(goal_text):
    goal_lower = goal_text.lower()
    for key in IDENTITY_MAP:
        if key != "default" and key in goal_lower:
            return key
    return "default"


def extract_duration_and_activity(goal_text):
    """Extract time/quantity and activity from the habit goal."""
    # Look for duration patterns
    duration_match = re.search(
        r'(\d+)\s*(min|minute|minutes|hour|hours|page|pages|mile|miles|km|times)', 
        goal_text, re.IGNORECASE
    )
    duration = duration_match.group(0) if duration_match else "a set amount"
    
    # Extract core activity (first verb phrase after "want to", "start", "build", etc.)
    activity_match = re.search(
        r'(?:want to|start|build|develop|create|establish|maintain|try)\s+(?:a\s+)?(?:daily\s+)?(.+?)(?:\s+habit|\s+every|\s+each|\s+for|\s+per|$)',
        goal_text, re.IGNORECASE
    )
    if activity_match:
        activity = activity_match.group(1).strip()
    else:
        activity = goal_text.strip()
    
    return duration, activity


def generate_habit_plan(goal_text):
    """
    Core function: generate a complete habit plan from a goal string.
    Uses deterministic logic based on KB templates.
    No external API calls.
    
    [KB: HabitTemplates.md — Templates 1-5]
    [KB: AtomicHabits_Summary.md — Identity-Based Habits, Implementation Intentions]
    """
    area = detect_goal_area(goal_text)
    duration, activity = extract_duration_and_activity(goal_text)

    # 1. Identity Statement [KB: HabitTemplates.md — Template 1]
    identity = IDENTITY_MAP.get(area, IDENTITY_MAP["default"])

    # 2. Implementation Intention [KB: HabitTemplates.md — Template 2]
    clean_activity = activity if len(activity) < 60 else goal_text[:60]
    implementation = (
        f"I will {clean_activity} for {duration} at [your chosen time] "
        f"in [your chosen location]."
    )

    # 3. Habit Stack [KB: HabitTemplates.md — Template 3]
    stack = HABIT_STACK_MAP.get(area, HABIT_STACK_MAP["default"])

    # 4. Environment Design [KB: AtomicHabits_Summary.md — Environment Design]
    env_tips = ENV_DESIGN_MAP.get(area, ENV_DESIGN_MAP["default"])

    # 5. Two-Minute Rule version [KB: AtomicHabits_Summary.md — The Two-Minute Rule]
    two_min = f"Start with just 2 minutes of '{clean_activity}' — not the full version. Build the identity first."

    # 6. Weekly Tracker [KB: HabitTemplates.md — Template 5]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    tracker = [{"day": d, "done": False} for d in days]

    # 7. Pitfall warning [KB: CommonPitfalls.md — Pitfall 1]
    pitfall = (
        "Most people start too big and quit by week two. "
        "Use the Two-Minute Rule: begin with the smallest possible version. "
        "Never miss twice — one miss is an accident, two is a new (bad) habit."
    )

    return {
        "goal": goal_text,
        "area": area,
        "identity": identity,
        "implementation": implementation,
        "stack": stack,
        "env_tips": env_tips,
        "two_min": two_min,
        "tracker": tracker,
        "pitfall": pitfall,
        "kb_citations": [
            "[KB: AtomicHabits_Summary.md — Identity-Based Habits]",
            "[KB: HabitTemplates.md — Template 2, Implementation Intention]",
            "[KB: HabitTemplates.md — Template 3, Habit Stacking]",
            "[KB: AtomicHabits_Summary.md — Environment Design]",
            "[KB: AtomicHabits_Summary.md — The Two-Minute Rule]",
            "[KB: HabitTemplates.md — Template 5, Weekly Tracker]",
            "[KB: CommonPitfalls.md — Pitfall 1: Starting Too Big]",
        ],
    }


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    plan = None
    error = None
    goal = ""

    if request.method == "POST":
        goal = request.form.get("goal", "").strip()
        if not goal:
            error = "Please enter a habit goal to get started."
        elif len(goal) < 5:
            error = "Please describe your habit goal in a bit more detail."
        else:
            plan = generate_habit_plan(goal)

    return render_template("index.html", plan=plan, error=error, goal=goal)


if __name__ == "__main__":
    print("=" * 50)
    print("  Habit Formation Coach AI")
    print("  Running at http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
