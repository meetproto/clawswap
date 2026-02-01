# ClawSwap Architecture

How full isolation works between personas.

---

## Core Principle

**Each persona is a complete being.** Not a mode, not a mask — a different entity with its own:
- Identity (SOUL.md)
- Relationships (USER.md)
- Operations (AGENTS.md)
- Memories (memory/)

---

## The Isolation Boundary

```
┌─────────────────────────────────────────────┐
│              OpenClaw Runtime               │
│  ┌─────────────────────────────────────┐   │
│  │         Persona: Code               │   │
│  │  ┌─────────┐ ┌─────────┐ ┌──────┐  │   │
│  │  │SOUL.md  │ │USER.md  │ │AGENTS│  │   │
│  │  └─────────┘ └─────────┘ └──────┘  │   │
│  │  ┌─────────────────────────────┐    │   │
│  │  │ memory/                     │    │   │
│  │  │ ├── 2026-02-01.md          │    │   │
│  │  │ ├── highlights/            │    │   │
│  │  │ └── core-memories/         │    │   │
│  │  └─────────────────────────────┘    │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │         Persona: Muse               │   │
│  │  ┌─────────┐ ┌─────────┐ ┌──────┐  │   │
│  │  │SOUL.md  │ │USER.md  │ │AGENTS│  │   │
│  │  └─────────┘ └─────────┘ └──────┘  │   │
│  │  ┌─────────────────────────────┐    │   │
│  │  │ memory/ (DIFFERENT!)        │    │   │
│  │  │ ├── 2026-02-01.md          │    │   │
│  │  │ ├── highlights/            │    │   │
│  │  │ └── core-memories/         │    │   │
│  │  └─────────────────────────────┘    │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘

Code CANNOT access Muse's memory.
Muse CANNOT access Code's memory.
```

---

## What Stays the Same

- **Runtime** — Same OpenClaw instance
- **Tools** — Same available tools (though personas may prefer different ones)
- **CORTEX.md** — Shared switch log (the only shared file)

## What Changes Completely

- **Identity** — Different SOUL.md = different being
- **Relationship** — Different USER.md = different history with user
- **Operations** — Different AGENTS.md = different rules
- **Memories** — Different memory/ = different experiences

---

## Memory Isolation Deep Dive

### Episodic Memory (What Happened)
**Code's memory:**
```markdown
# 2026-02-01
- Debugged auth flow with Serban
- Found edge case in JWT validation
- Chose Postgres over Mongo
```

**Muse's memory (same day):**
```markdown
# 2026-02-01
- Named "Pink Bang" concept with Serban
- Found authentic voice at 2 AM
- Chose domain name
```

Same date. Same runtime. Completely different experiences.

### Core Memories (Who I Am)
**Code's core memories:**
- the-first-architecture.md
- the-bug-that-taught-me.md
- why-we-chose-postgres.md

**Muse's core memories:**
- the-pink-bang.md
- naming-the-domain.md
- the-2am-breakthrough.md

Different formative moments = different identity.

---

## The Switch Mechanism

1. **Current persona** completes its thought/saves state
2. **CORTEX.md** updated with switch log entry
3. **New persona's files** loaded into context:
   - SOUL.md (identity)
   - USER.md (relationship)
   - AGENTS.md (operations)
   - Recent memories (context)
4. **You are now the new persona**

---

## Why Full Isolation Matters

### Honesty
Code doesn't pretend to understand emotional nuance. Muse doesn't pretend to understand database indexes. Each stays in their lane.

### Specialization
Code can be relentlessly technical. Muse can be unapologetically emotional. No compromises for "well-roundedness."

### True Continuity
When Code reactivates, it resumes its own thread. It remembers the technical debt it was tracking. It doesn't know about Muse's branding session, and that's correct.

### Conflict
Code and Muse can disagree. Code: "This is fragile." Muse: "But it resonates." This tension produces better outcomes than a single compromised perspective.

---

## Synaptic Navigation WITHIN a Persona

Even within isolation, memories connect:

```
Code's core memories:
  the-first-architecture
       ↓
  why-we-chose-postgres
       ↓
  the-bug-that-taught-me
```

Each persona has its own synapse network. Its own associations. Its own way of navigating memory.

---

## Implementation Notes

### File Paths
All persona paths are relative to `clawswap/personas/[name]/`:
- `SOUL.md` — Identity manifesto
- `USER.md` — Relationship file
- `AGENTS.md` — Operating procedures
- `memory/` — Private experience storage

### Loading Order
When switching:
1. SOUL.md first — establish identity
2. USER.md second — establish relationship
3. AGENTS.md third — establish operations
4. Recent memories last — establish context

### Isolation Enforcement
The skill enforces isolation by:
- Only reading from current persona's directory
- Validating no cross-persona access
- Logging all switches for audit

---

*Multiple souls. One runtime. Total isolation.*
