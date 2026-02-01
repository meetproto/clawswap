# Shared Memory

**Accessible by all personas.** Contains switch history, orchestrator rules, and shared context.

---

## Switch Log

Track persona switches:

```
2026-02-01 09:00 | default → smith | Task: "debug auth error"
2026-02-01 11:30 | smith → muse | Task: "name this feature"
2026-02-01 14:00 | muse → helm | Task: "Q1 roadmap planning"
```

---

## Orchestrator Triggers

When to auto-activate each persona:

**Smith (Builder):**
- Keywords: code, debug, error, bug, fix, architecture, implement, database, API
- Context: technical problems, implementation decisions

**Muse (Artist):**
- Keywords: write, name, brand, design, copy, voice, feel, story, narrative
- Context: creative work, emotional resonance, user experience

**Helm (Navigator):**
- Keywords: roadmap, strategy, plan, prioritize, market, business, growth, constraint
- Context: strategic decisions, resource allocation, long-term planning

---

## Shared Context

Information all personas need:

- Current project phase
- Upcoming deadlines
- Active constraints (budget, time, team)
- Recent decisions (regardless of who made them)

---

## Persona Handoff Notes

When switching, the outgoing persona can leave notes:

```
[smith → muse handoff]
Time: 2026-02-01 11:30
Context: Auth system working, need name for "remember me" feature
Smith note: "Working implementation. Needs user-facing name."
```

---

*Shared across all personas. Not private to any single mind.*
