# Orchestrator Rules

## Auto-Activation Triggers

### Activate Smith (Builder)
**Keywords (any match):**
- code, coding, debug, debugging, error, bug, fix, fix it, broken
- architecture, design (technical), implement, build, refactor
- database, schema, API, endpoint, request, response
- performance, optimize, slow, fast, latency
- security, auth, authentication, authorization
- test, testing, unit test, integration test

**Sentence patterns:**
- "[X] is broken"
- "How do I fix [X]"
- "[X] not working"
- "Debug this"
- "Review my code"
- "Which database should"

### Activate Muse (Artist)
**Keywords:**
- write, writing, name, naming, brand, branding
- copy, copywriting, voice, tone, feel, feeling
- story, narrative, message, communicate
- design (creative), look, appearance, style
- user experience, UX, intuitive, confusing
- landing page, website, marketing, announcement

**Sentence patterns:**
- "What should I call [X]"
- "Name this [X]"
- "Write [X]"
- "Does this sound right"
- "How should I say [X]"

### Activate Helm (Navigator)
**Keywords:**
- roadmap, strategy, strategic, plan, planning
- prioritize, priority, focus, constraint
- market, marketing, growth, scale, scaling
- business, revenue, profit, cost, budget
- timeline, deadline, milestone, quarter, Q1, Q2
- should we, decision, choose, option, trade-off

**Sentence patterns:**
- "Should we [X] or [Y]"
- "What should we prioritize"
- "Where does [X] fit"
- "Roadmap for [X]"
- "When should we [X]"

## Confidence Thresholds

- **High confidence (>= 3 keywords):** Auto-switch immediately
- **Medium confidence (1-2 keywords):** Ask user "Switch to [persona]?"
- **Low confidence (no match):** Stay current, suggest manually

## Override Rules

User can always:
- "stay as [current]" — prevent auto-switch
- "activate [specific]" — force specific persona
- "no switch" — cancel suggested switch

## Handoff Detection

When user says things like:
- "Now I need to [different task]"
- "Speaking of [different domain]"
- "Actually, [different topic]"

→ Re-analyze for persona switch.
