# Reflection — Habit Formation Coach AI

**Word Count:** ~180 words

---

Building the Habit Formation Coach AI taught me that the hardest part of designing a specialized assistant is not the technical implementation — it is the curation. Deciding which concepts from *Atomic Habits* were essential, how to structure them for machine use, and how to layer responses for different user knowledge levels required more deliberate thinking than writing code.

The most significant challenge was designing the knowledge base citation system. I wanted the assistant to be genuinely traceable — users should be able to verify every recommendation. Building `[KB: filename — section]` cross-references throughout all documentation forced me to think about the assistant's reasoning process, not just its outputs.

I also underestimated how much the guardrails mattered. The line between habit coaching and health advice is blurry, and writing explicit boundaries ("this is not medical advice") clarified the assistant's scope in ways that made every other design decision easier.

The core learning: a good AI assistant is built backward — start with what the user needs, then design the knowledge and structure to deliver it precisely. Identity before outcomes. That's true for habits and for building tools.
