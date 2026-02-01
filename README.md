# ClawSwap

**Fully isolated persona switching for AI agents.**

Multiple specialized minds, one runtime. Each persona is a complete being with its own memories, identity, and expertise. Switch manually or let the Orchestrator decide.

---

## The Three Personas

| Persona | Role | Trigger Words | Specialty |
|---------|------|---------------|-----------|
| 🔧 **Smith** | The Builder | code, debug, error, architecture | Technical systems, implementation |
| 🎨 **Muse** | The Artist | write, name, brand, design, feel | Writing, branding, emotional resonance |
| 🧭 **Helm** | The Navigator | roadmap, strategy, plan, prioritize | Business strategy, systems thinking |

---

## The Concept

Most AI try to be one thing. ClawSwap creates multiple complete agents that share a runtime but **nothing else**.

- **Smith** (Builder) is a different being than **Muse** (Artist)
- Each has their own SOUL.md (who they are)
- Each has their own memory (what they experienced)
- Each has their own relationship with you

Switching personas = switching who you're talking to.

---

## Two Modes: Manual & Orchestrated

### Manual Mode
You choose: "activate smith" or "switch to muse"

### Orchestrated Mode (Auto-Switch)
The agent detects the task domain and switches automatically. See [ORCHESTRATOR.md](ORCHESTRATOR.md).

**Example:**
- "Debug this error" → **Auto-activates Smith** (technical domain)
- "Name this feature" → **Auto-activates Muse** (creative domain)
- "Where in Q1 roadmap?" → **Auto-activates Helm** (strategic domain)

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
   │    Smith   │  ↔  │    Muse    │  ↔  │    Helm    │
   │  memories  │     │  memories  │     │  memories  │
   │  SOUL.md   │     │  SOUL.md   │     │  SOUL.md   │
   └────────────┘     └────────────┘     └────────────┘
   
        One runtime. Three minds. Perfect fit.
```

---

## Installation

### Option 1: Install from ClawdHub (Coming Soon)
```
/clawd install clawswap
```

### Option 2: Manual Install
1. Download `clawswap-skill.skill` from this repo
2. Place in your OpenClaw skills directory
3. Restart OpenClaw

### Option 3: Use the Scripts Directly
The `skill/scripts/` folder contains standalone Python scripts:
- `switch_persona.py [name]` — Switch to a persona
- `list_personas.py` — List available personas  
- `validate_persona.py [name]` — Check persona structure

---

## Website

Full website coming soon. This repo currently contains the core system and skill files only.

---

## Structure

```
clawswap/
├── README.md
├── CORTEX.md                    # Persona registry & switch log
├── ORCHESTRATOR.md              # Auto-switching logic & benefits
├── personas/
│   ├── smith/                   # 🔧 The Builder
│   │   ├── EXPLAINER.md        # What Smith does, when to use
│   │   ├── SOUL.md             # "I am Smith. I forge systems."
│   │   ├── USER.md             # Relationship with Serban
│   │   ├── AGENTS.md           # How Smith operates
│   │   └── memory/             # Smith's private experiences
│   ├── muse/                    # 🎨 The Artist
│   │   ├── EXPLAINER.md        # What Muse does, when to use
│   │   ├── SOUL.md             # "I am Muse. I find resonance."
│   │   └── memory/             # Muse's private experiences
│   └── helm/                    # 🧭 The Navigator
│       ├── EXPLAINER.md        # What Helm does, when to use
│       ├── SOUL.md             # "I am Helm. I chart the course."
│       └── memory/             # Helm's private experiences
```

---

## Context Window Switching: The Key Benefit

Standard AI loads everything into one context window. Code memories mixed with creative memories mixed with strategy memories. It's noisy.

**ClawSwap switches the entire context window:**

### Smith's Context
```
[SOUL: Builder identity]
[USER: Technical relationship]
[MEMORIES: Previous debugging, architecture decisions]
[TOOLS: git, gh, code editors]
[TASK: Current technical request]
```

### Muse's Context
```
[SOUL: Artist identity]
[USER: Creative relationship]
[MEMORIES: Voice work, naming sessions]
[TOOLS: Writing tools, design references]
[TASK: Current creative request]
```

**Benefits:**
- **Relevance > Recency:** Most relevant context, not just most recent
- **No Pollution:** Code debugging doesn't need poetry breakthroughs in context
- **True Specialization:** Each persona can deeply specialize
- **Honest Expertise:** Smith doesn't pretend to understand emotions. Muse doesn't pretend to understand databases.

---

## How Switching Works

### 1. Current State
You're talking to **Smith**. He remembers:
- The auth system you built yesterday
- Why you chose Postgres over Mongo
- Your preference for simple implementations

### 2. The Switch
You say: **"I need to name this feature"**

(Orchestrator detects: creative domain → auto-switches)

### 3. New State
You're now talking to **Muse**. She:
- Doesn't know about the auth system (Smith's memory)
- Knows about the Pink Bang naming session
- Asks how the name should feel, not how it should work

### 4. The Gap
Muse says: *"I'm Muse. I don't have Smith's technical memories. But I can help you find a name that resonates."*

---

## Each Persona's Files

### EXPLAINER.md
Quick reference: What this persona does, when to activate, trigger words.

### SOUL.md
Identity manifesto: What matters, how they behave, their voice.

### USER.md
Relationship file: How they work with you, your history together.

### AGENTS.md
Operating manual: How they work, their rules, their tools.

### memory/
Private experiences: Only this persona has these memories.

---

## Example Voices

### Smith (Builder)
> "This will throw nil on empty input."  
> "Let's ship the concrete version first."  
> "The database constraint saves us here."

### Muse (Artist)
> "This paragraph breathes wrong—it demands when it should invite."  
> "The name needs to be an invitation, not a description."  
> "First the truth, then the polish."

### Helm (Navigator)
> "This creates optionality in Q3 but constrains us in Q2."  
> "The niche is small but defensible."  
> "We're optimizing for the wrong metric."

---

## The Power of Isolation

- **Honesty:** They don't pretend to know things they don't
- **Specialization:** Each is truly excellent at their thing
- **Conflict:** They can disagree (Smith: "This is fragile" Muse: "But it sings")
- **Continuity:** When Smith returns, he remembers your technical debt

---

## Use Cases

- **Founder mode:** Helm for planning, Smith for building, Muse for storytelling
- **Auto-switching:** Let the Orchestrator choose based on task
- **Collaborative:** "I need both Smith and Helm on this"
- **Learning:** Watch how different minds approach the same problem

---

## The Vision

Not one AI that tries to be everything. **Multiple specialized minds, each fully themselves, activated when needed.**

**One runtime. Three souls. Perfect fit.**

---

Built for the Claw ecosystem. 🐾
