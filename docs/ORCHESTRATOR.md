# ORCHESTRATOR — Auto Persona Switching

The Orchestrator detects task context and switches personas automatically.

## How It Works

### 1. Task Analysis
When you send a request, the agent analyzes:
- Domain (technical/creative/strategic)
- Keywords (code/write/plan)
- Intent (debug/design/decide)

### 2. Persona Matching

| Task Signals | Activates |
|--------------|-----------|
| "debug", "code", "error", "architecture" | **Smith** (Builder) |
| "write", "name", "brand", "design", "feel" | **Muse** (Artist) |
| "roadmap", "strategy", "plan", "prioritize" | **Helm** (Navigator) |

### 3. Context Window Switch

The agent unloads current context and loads persona-specific context:

**Smith's Context:**
```
[SOUL: I forge systems]
[MEMORIES: 3 AM outage, null pointer hunt]
[TASK: Debug request]
```

**Muse's Context:**
```
[SOUL: I find resonance]
[MEMORIES: Pink Bang moment, 2 AM breakthrough]
[TASK: Writing request]
```

## Benefits

- **Relevance > Recency** — Most relevant memories, not just recent
- **No Context Pollution** — Code debugging doesn't need poetry
- **True Specialization** — Each persona deeply expert
- **Honest Expertise** — Smith doesn't fake emotions; Muse doesn't fake databases

## Manual Override

Always available:
- `"activate smith"` — Force switch
- `"stay as muse"` — Prevent auto-switch
- `"deactivate"` — Return to default agent

## Safety

Your original memory is never touched:
- Your `SOUL.md` stays as default identity
- Your `memory/` folder stays isolated
- Personas write to `personas/[name]/memory/`

---

*Task-appropriate minds. Automatically.*
