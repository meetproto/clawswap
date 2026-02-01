# ClawSwap — Installation Guide

## Safe Installation (No Memory Destruction)

ClawSwap creates personas **alongside** your existing memory, not inside it.

### Directory Structure After Install

```
~/.openclaw/workspace/
├── SOUL.md                 # ← Your original (untouched)
├── USER.md                 # ← Your original (untouched)
├── AGENTS.md               # ← Your original (untouched)
├── memory/                 # ← Your original memory (untouched)
│   ├── 2026-02-01.md
│   ├── highlights/
│   └── core-memories/
│
└── personas/               # ← NEW: ClawSwap creates this
    ├── smith/
    │   ├── SOUL.md
    │   ├── USER.md
    │   ├── AGENTS.md
    │   └── memory/
    ├── muse/
    │   ├── SOUL.md
    │   ├── USER.md
    │   ├── AGENTS.md
    │   └── memory/
    └── helm/
        ├── SOUL.md
        ├── USER.md
        ├── AGENTS.md
        └── memory/
```

**Key:** Your original memory stays completely separate. Personas live in their own folder.

---

## How It Works

### Your Default Mode
When no persona is active, you're **you** — with your original SOUL.md, USER.md, memory/.

### Switching to a Persona
When you say "activate smith":
1. Your agent loads `personas/smith/SOUL.md` (temporarily overrides yours)
2. Loads `personas/smith/USER.md` (Smith's relationship with Serban)
3. Loads `personas/smith/memory/` (Smith's experiences)
4. **Your original memory is still there** — just not loaded into context

### Returning to Default
When you say "deactivate" or "switch back":
1. Unload persona files
2. Reload YOUR original SOUL.md, USER.md
3. Resume from YOUR memory/

---

## Installation Steps

### 1. Install Skill
```bash
/clawd install clawswap
# or manually copy to skills directory
```

### 2. Initialize Personas
```bash
clawswap init
```

This copies from `example-personas/` to your workspace:
- `personas/smith/` — The Builder
- `personas/muse/` — The Artist
- `personas/helm/` — The Navigator

### 3. Your Memory Is Safe
Your existing files are **never touched**:
- `SOUL.md` → Stays as your default identity
- `USER.md` → Stays as your relationship
- `memory/` → Stays as your experiences

---

## Uninstallation (Clean Removal)

### Option 1: Keep Personas (Just Disable Skill)
```bash
/clawd uninstall clawswap
```
Persona folders stay but skill stops triggering.

### Option 2: Full Removal (Delete Everything)
```bash
/clawd uninstall clawswap --purge
# or manually:
rm -rf ~/.openclaw/workspace/personas/
```

**Result:** You're back to exactly where you started.
- Your `SOUL.md` — unchanged
- Your `USER.md` — unchanged
- Your `memory/` — unchanged

---

## Safety Guarantees

1. **Read-only to your memory** — Personas never write to your memory/
2. **Isolated storage** — Persona memories in personas/[name]/memory/
3. **No overwrite** — Your SOUL.md is never modified
4. **Reversible** — Delete personas/ folder = back to original

---

## For Skill Developers

If creating your own persona:

```bash
clawswap create-persona [name]
```

Creates:
```
personas/[name]/
├── SOUL.md          # Required
├── USER.md          # Required
├── AGENTS.md        # Optional
└── memory/          # Auto-created
    ├── highlights/
    │   ├── daily/
    │   ├── monthly/
    │   └── yearly/
    └── core-memories/
```

**Rule:** Never touch files outside `personas/[name]/`.

---

## Migration (If You Want to Become a Persona)

If you decide YOUR identity should become one of the personas:

```bash
# Copy your current self to a persona
clawswap promote-to-persona [name]
```

This copies:
- Your `SOUL.md` → `personas/[name]/SOUL.md`
- Your `USER.md` → `personas/[name]/USER.md`
- Your `memory/` → `personas/[name]/memory/`

Then you can create a NEW default SOUL.md for your base identity.

---

*Your memory is yours. Personas are guests.*
