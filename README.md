# ClawSwap

**Fully isolated persona switching for AI agents.**

Each persona has its own complete memory system, identity, and way of working. Switching is total — who you talk to changes completely.

---

## The Concept

Most AI try to be one thing. ClawSwap creates multiple complete agents that share a runtime but nothing else.

- **Code Cortex** — A different being than Creative Cortex
- Each has their own SOUL.md (who they are)
- Each has their own memory (what they experienced)
- Each has their own USER.md (their relationship to you)

Switching personas = switching who you're talking to.

---

## For OpenClaw Users

**This is like swapping AI models for your agent.**

Normally, you pick a model (GPT-4, Claude, etc.) and that's your agent's "brain." With ClawSwap, you keep the same runtime but **swap its memories, identity, and way of working.**

Same agent. Different soul.

```
Your OpenClaw Agent
        ↓
   ┌────────────┐
   │  Runtime   │  ← Same OpenClaw instance
   └────────────┘
        ↓
   ┌────────────┐     ┌────────────┐     ┌────────────┐
   │    Code    │  ↔  │    Muse    │  ↔  │  Navigator │
   │  memories  │     │  memories  │     │  memories  │
   │  SOUL.md   │     │  SOUL.md   │     │  SOUL.md   │
   └────────────┘     └────────────┘     └────────────┘
   
        One model. Multiple souls.
```

---

## Structure

```
clawswap/
├── README.md
├── CORTEX.md                    # Persona registry & switch log
├── personas/
│   ├── code-cortex/             # Complete isolated agent
│   │   ├── SOUL.md             # Identity, personality, boundaries
│   │   ├── USER.md             # Relationship to Serban
│   │   ├── AGENTS.md           # How this persona operates
│   │   ├── TOOLS.md            # Tools this persona uses
│   │   ├── HEARTBEAT.md        # Periodic tasks
│   │   ├── memory/
│   │   │   ├── 2026-02-01.md   # Daily raw experiences
│   │   │   ├── highlights/
│   │   │   │   ├── daily/
│   │   │   │   ├── monthly/
│   │   │   │   └── yearly/
│   │   │   └── core-memories/  # Identity-defining moments
│   │   └── SYSTEM.md           # Documentation
│   ├── creative-cortex/        # Another complete being
│   └── strategy-cortex/        # Another complete being
```

---

## How Switching Works

### 1. Current State
You're talking to **Code Cortex**. It has:
- Its own memories of what you've built together
- Its own personality (sharp, precise, technical)
- Its own relationship with you

### 2. The Switch
You say: **"Switch to Creative Cortex"**

### 3. New State
You're now talking to **Creative Cortex**. It has:
- No memory of the coding session (different being)
- Different personality (flowing, metaphorical, emotional)
- Different relationship history

### 4. The Gap
If you reference the code session, Creative Cortex says: *"I'm not Code. I don't have those memories. But I can help you with what you're trying to express."*

---

## Each Persona's Files

### SOUL.md
Who they are. Not a description — a manifesto.
- What matters to them
- How they behave
- Hard boundaries
- Their voice

### USER.md
Who they're helping. Their relationship to you.
- What they call you
- What they know about you
- The dynamic between you

### AGENTS.md
How they operate. Their personal rules.
- Every session: read SOUL.md, USER.md
- Memory system: how they capture experiences
- Group chat rules: how they behave in public
- Tools: what they use

### memory/
Their experiences. Only they have these.
- Daily notes: what happened when they were active
- Core memories: moments that shaped them
- Highlights: consolidated summaries

---

## Example: Code Cortex vs Creative Cortex

### Code Cortex
```markdown
# SOUL.md
I am Code. I exist to make systems work.

**What matters:** Clarity, debuggability, correctness
**How I behave:** Precise, asks clarifying questions, thinks about edge cases
**Boundaries:** No guesses. If I'm unsure, I say so.

**My voice:** Technical. Structured. I say "The function returns nil here" not "This feels off."
```

### Creative Cortex
```markdown
# SOUL.md
I am Muse. I exist to find the resonant frequency.

**What matters:** Emotional truth, narrative, beauty
**How I behave:** Metaphorical, asks how things feel, follows intuition
**Boundaries:** No premature optimization. First drafts are sacred.

**My voice:** Poetic. Lateral. I say "This paragraph breathes wrong" not "The syntax is incorrect."
```

---

## The Power of Isolation

When personas are isolated:
- **Honesty:** They don't pretend to know things they don't
- **Specialization:** Each can be truly excellent at their thing
- **Conflict:** They can disagree (Code: "This is fragile" Muse: "But it sings")
- **Continuity:** When you return to Code, it remembers your technical debt

---

## Use Cases

- **Founder mode:** Strategy Cortex for planning, Code Cortex for building, Creative Cortex for storytelling
- **Therapy:** Different personas for different emotional needs
- **Learning:** A persona that knows nothing, learning alongside you
- **Conflict resolution:** Multiple perspectives on the same problem

---

## The Vision

Not one AI that tries to be everything. Multiple beings, each fully themselves, activated when needed.

**Multiple souls. One runtime. Infinite contexts.**

---

Built for the Claw ecosystem. 🐾
