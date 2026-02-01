# CORTEX Registry

**Active persona tracking and switch log.**

---

## Currently Active

**None** — Example file

---

## Available Personas

| Persona | Name | Directory | Specialty | Trigger Words |
|---------|------|-----------|-----------|---------------|
| 🔧 Smith | The Builder | `personas/smith/` | Technical systems, code | code, debug, error, architecture |
| 🎨 Muse | The Artist | `personas/muse/` | Writing, brand, design | write, name, brand, design, feel |
| 🧭 Helm | The Navigator | `personas/helm/` | Strategy, planning | roadmap, strategy, plan, prioritize |

---

## Auto-Switching (Orchestrator)

The agent can automatically switch based on task context. See [ORCHESTRATOR.md](ORCHESTRATOR.md) for details.

**Default behavior:** Manual switching (user says "activate smith")

**Auto mode:** Agent detects domain and switches automatically

---

## Switch Log (Example)

| Time | From | To | Trigger | Notes |
|------|------|-----|---------|-------|
| 09:00 | — | smith | "Need to architect this" | Auth system design |
| 11:30 | smith | muse | "Write the announcement" | Feature naming |
| 14:00 | muse | helm | "Q1 planning" | Roadmap discussion |
| 16:00 | helm | smith | "Back to implementation" | Resumed coding |

---

## Isolation Reminder

Each persona CANNOT access:
- Other personas' memory/ folders
- Other personas' SOUL.md or USER.md
- What happened while other personas were active

They ONLY have:
- Their own complete memory system
- Their own identity files
- This shared CORTEX.md (switch log only)

---

## Persona Files

Each persona folder contains:
- `EXPLAINER.md` — What this persona does, when to use
- `SOUL.md` — Identity, values, voice
- `USER.md` — Relationship with Serban
- `AGENTS.md` — Operating procedures
- `memory/` — Private experiences (isolated)

---

*This file is the only shared space. Everything else is persona-isolated.*
