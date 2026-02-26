# Reflection — Habit Formation Coach AI

**Word Count:** ~190 words

---

Building the Habit Formation Coach AI taught me that the hardest part of designing a specialized assistant is not the technical implementation — it is the curation. Deciding which concepts from *Atomic Habits* were essential, how to structure them for consistent output, and how to layer responses for different user knowledge levels required more deliberate thinking than writing code.

The most significant challenge was designing the citation system. I wanted every recommendation to be traceable to its source. Early versions referenced internal document names, which looked technical but meant nothing to an end user or grader. Refactoring to the academic format — *(Atomic Habits — Concept Name)* — forced cleaner thinking: each claim had to map to a specific, nameable idea in the book, or be flagged explicitly as general behavioral science.

I also underestimated how much the guardrails mattered. The line between habit coaching and health advice is blurry, and writing explicit boundaries clarified the assistant's scope in ways that made every other design decision easier.

The core learning: a good AI assistant is built backward — start with what the user needs to understand, then design the knowledge structure to deliver it precisely. Identity before outcomes. That turns out to be true for building tools as much as for building habits.
