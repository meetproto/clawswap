# ClawSwap

**Multi-persona AI system.** One runtime, multiple minds, perfect fit.

## The Three Personas

| Persona | Role | For Tasks Like |
|---------|------|----------------|
| 🔧 **Smith** | The Builder | Code, debugging, architecture |
| 🎨 **Muse** | The Artist | Writing, naming, brand voice |
| 🧭 **Helm** | The Navigator | Strategy, planning, decisions |

## How It Works

```
Your Agent
    ↓
switch to smith → Loads Smith's memories, voice, expertise
switch to muse  → Loads Muse's memories, voice, expertise
switch to helm  → Loads Helm's memories, voice, expertise
```

Each persona has their own:
- **SOUL.md** — Identity and values
- **USER.md** — Relationship with you  
- **memory/** — Daily, weekly, monthly, yearly highlights + core memories

Your original agent files stay untouched.

## Installation

### One-Liner
```bash
curl -fsSL https://raw.githubusercontent.com/meetproto/clawswap/main/install.sh | bash
```

### Manual
```bash
# 1. Download skill
curl -fsSL https://github.com/meetproto/clawswap/releases/latest/download/clawswap-skill.skill -o ~/.openclaw/workspace/.skills/clawswap-skill.skill

# 2. Copy personas
cp -r personas/ ~/.openclaw/workspace/

# 3. Done
```

See [docs/INSTALL.md](docs/INSTALL.md) for detailed setup and safety info.

## Usage

```bash
# Switch manually
activate smith

# Or let orchestrator auto-detect
# "Debug this error" → auto-switches to Smith
# "Name this feature" → auto-switches to Muse
```

See [docs/ORCHESTRATOR.md](docs/ORCHESTRATOR.md) for auto-switching details.

## Default Personas (Delete What You Don't Need)

Three example personas included by default:

- `smith/` — Battle-scarred engineer (3-day null pointer hunt, Postgres vs Mongo)
- `muse/` — Former ad writer (Pink Bang moment, 200+ unused names)
- `helm/` — Strategic navigator (said no to $50M acquisition)

**Use them, modify them, or delete them:**
```bash
rm -rf ~/.openclaw/workspace/personas/smith  # Don't need Smith? Delete him.
```

Create your own: `clawswap create-persona my-persona`

## Uninstall

```bash
rm -rf ~/.openclaw/workspace/personas/
```

Your original agent files remain untouched.

---

Built for OpenClaw. 🐾
