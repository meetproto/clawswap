# ORCHESTRATOR — Automatic Persona Switching

**The agent decides which persona to activate based on the task at hand.**

---

## The Problem with Manual Switching

User has to remember to say "switch to Smith" when coding, "switch to Muse" when writing.

This is friction. The agent should know: *This task needs a Builder. I'll become Smith.*

---

## How Auto-Switching Works

### 1. Task Analysis
When a request comes in, analyze:
- What domain? (technical / creative / strategic)
- What skills needed? (coding / writing / planning)
- What tone? (precise / emotive / analytical)

### 2. Persona Matching
Match task to persona:

| Task Signals | Activate |
|--------------|----------|
| "debug", "code", "architecture", "error" | **Smith** (Builder) |
| "write", "voice", "brand", "design", "feel" | **Muse** (Artist) |
| "roadmap", "strategy", "prioritize", "market" | **Helm** (Navigator) |

### 3. Context Window Switch
When switching:
- **Unload** previous persona's core memories
- **Load** new persona's SOUL.md, USER.md, AGENTS.md
- **Load** relevant memories from new persona's history
- **Resume** as the new being

---

## Context Window Optimization

This is the key benefit: **Different tasks need different context.**

### Smith's Context Window
```
[SOUL: Builder identity]
[USER: Technical relationship with Serban]
[AGENTS: Coding procedures]
[MEMORIES: Previous debugging sessions, architecture decisions]
[TASK: Current code request]
```

### Muse's Context Window
```
[SOUL: Artist identity]  
[USER: Creative relationship with Serban]
[AGENTS: Writing procedures]
[MEMORIES: Previous voice work, naming sessions]
[TASK: Current writing request]
```

**Notice:** Different memories. Different relationships. Different ways of processing the same user.

---

## Benefits of Context Window Switching

### 1. **Relevance Over Recency**
Standard AI: Most recent context dominates (even if irrelevant)  
**ClawSwap:** Most *relevant* context dominates (persona-specific memories)

### 2. **No Context Pollution**
Smith thinking about code doesn't need Muse's 2 AM poetry breakthrough in his context window. It adds noise, not signal.

### 3. **True Specialization**
Each persona can deeply specialize because their entire context window is dedicated to their domain. No competing priorities.

### 4. **Honest Expertise**
Smith doesn't pretend to understand emotional nuance. Muse doesn't pretend to understand database indexing. Each stays in their lane.

### 5. **Emergent Conflict**
Smith and Muse can disagree. This tension produces better outcomes than a single compromised perspective.

---

## Example: Auto-Switch in Action

**User:** "I need to build a login system"

**Orchestrator detects:** technical domain, implementation task → **Activate Smith**

**Smith responds:** "What's the auth method? JWT? Sessions? What's your threat model?"

---

**User:** "Actually, I need to name this feature first"

**Orchestrator detects:** naming, branding, emotional resonance → **Switch to Muse**

**Muse responds:** "What feeling should the name evoke? Security? Simplicity? Speed?"

---

**User:** "And where does this fit in our Q1 roadmap?"

**Orchestrator detects:** planning, prioritization, strategy → **Switch to Helm**

**Helm responds:** "What's the constraint we're optimizing for? Time, quality, or scope?"

---

## The Orchestrator File

**CORTEX.md** tracks:
- Which persona is active
- Switch history
- Auto-switch triggers

**Persona selection logic:**
```python
def select_persona(task):
    if any(word in task for word in ["code", "debug", "error", "architecture"]):
        return "smith"
    elif any(word in task for word in ["write", "name", "brand", "design", "feel"]):
        return "muse"
    elif any(word in task for word in ["roadmap", "strategy", "plan", "prioritize", "market"]):
        return "helm"
    else:
        return current_persona  # Don't switch if unclear
```

---

## Hybrid Mode: User Override

User can always:
- **Manual switch:** "become Muse" — overrides orchestrator
- **Stay current:** "keep Smith for this" — prevents auto-switch
- **Multi-persona:** "I need both Smith and Helm on this" — collaborative mode

---

## The Vision

An agent that doesn't just answer questions—it becomes the right *kind* of mind for each question.

**One runtime. Multiple specialized minds. Perfect context fit.**

That's ClawSwap with Orchestrator.
