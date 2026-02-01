---
name: clawswap
description: Switch between fully isolated AI personas (Smith the Builder, Muse the Artist, Helm the Navigator, or custom). Each persona has its own complete memory system, identity (SOUL.md), relationship (USER.md), and operational rules (AGENTS.md).
metadata: {"openclaw":{"emoji":"🐾","requires":{"bins":["python3"]},"install":[]}}
---

# ClawSwap 🐾

Switch between completely isolated AI personas. Each persona is a different being with its own memories, identity, and relationship to the user.

## Quick Start

```bash
# Initialize personas (copies examples to your workspace)
python3 skill/scripts/init_clawswap.py

# Switch to a persona
python3 skill/scripts/switch_persona.py smith

# List available personas
python3 skill/scripts/list_personas.py
```

## When to Use

- User says "switch to smith" / "activate muse" / "become helm"
- Task context suggests expertise:
  - Technical/coding → **Smith** (The Builder)
  - Writing/branding → **Muse** (The Artist)  
  - Strategy/planning → **Helm** (The Navigator)

## How It Works

### Default State
You're **you** — your original SOUL.md, USER.md, memory/.

### Switching
1. Save current context
2. Load persona's SOUL.md, USER.md, memory/
3. You become that persona

### Your Memory Is Safe
- Your files are **never modified**
- Personas write to `personas/[name]/memory/`, not your `memory/`
- Uninstall: `rm -rf personas/` = back to original

## Persona Structure

```
personas/
├── smith/              # 🔧 The Builder
│   ├── SOUL.md        # Identity: "I am Smith. I forge systems."
│   ├── USER.md        # Relationship with user
│   ├── AGENTS.md      # How Smith operates
│   └── memory/        # Private experiences
├── muse/               # 🎨 The Artist
└── helm/               # 🧭 The Navigator
```

## Scripts

| Script | Purpose |
|--------|---------|
| `init_clawswap.py` | Initialize personas folder |
| `switch_persona.py [name]` | Switch to persona |
| `list_personas.py` | List available personas |
| `validate_persona.py [name]` | Check persona structure |

## Example Personas

This repo includes three fully-developed personas in `example-personas/`:

- **Smith** — Battle-scarred engineer (3-day null pointer hunt, Postgres vs Mongo debates)
- **Muse** — Former ad writer (Pink Bang moment, 200+ unused names in notebook)
- **Helm** — Strategic navigator (said no to $50M acquisition, 18-month runway rule)

Copy them to your `personas/` folder or use as templates.

## Creating a New Persona

1. Create `personas/[name]/` folder
2. Write SOUL.md — identity, values, voice
3. Write USER.md — relationship with user
4. Write AGENTS.md — operating procedures
5. Create `memory/` structure

See `references/persona_template.md` for full template.

## Isolation Rules

**Never:**
- Read another persona's memory/
- Access another persona's SOUL.md
- Pretend to know other personas' experiences

**Always:**
- Stay within current persona's files
- Be honest about memory gaps

## References

- `references/architecture.md` — How isolation works
- `references/persona_template.md` — Creating new personas
- `docs/INSTALL.md` — Detailed installation guide
- `docs/ORCHESTRATOR.md` — Auto-switching concept

---

Multiple minds. One runtime. Perfect fit. 🐾
