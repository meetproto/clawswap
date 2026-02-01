#!/usr/bin/env python3
"""
ClawSwap: Export current/default bot as a persona.
Saves your agent's identity so you can share it or use it as a template.
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime

def get_workspace_root():
    """Find OpenClaw workspace root."""
    possible_paths = [
        Path.home() / ".openclaw" / "workspace",
        Path.cwd(),
    ]
    
    for path in possible_paths:
        if (path / "SOUL.md").exists():
            return path
    
    return None

def get_personas_dir():
    """Get personas directory."""
    workspace = get_workspace_root()
    if workspace:
        return workspace / "personas"
    return None

def export_default_bot(persona_name):
    """Export current/default bot as a persona."""
    workspace = get_workspace_root()
    personas_dir = get_personas_dir()
    
    if not workspace:
        print("❌ Could not find OpenClaw workspace")
        return False
    
    if not personas_dir:
        print("❌ Could not find personas directory")
        print("   Run 'clawswap init' first")
        return False
    
    # Source files
    soul_src = workspace / "SOUL.md"
    user_src = workspace / "USER.md"
    agents_src = workspace / "AGENTS.md"
    memory_src = workspace / "memory"
    
    # Check if source files exist
    if not soul_src.exists():
        print(f"❌ Could not find {soul_src}")
        return False
    
    # Destination
    persona_path = personas_dir / persona_name
    
    if persona_path.exists():
        response = input(f"⚠️  Persona '{persona_name}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Cancelled.")
            return False
        shutil.rmtree(persona_path)
    
    # Create persona structure
    persona_path.mkdir(parents=True)
    
    # Copy files
    print(f"📁 Creating persona: {persona_name}")
    
    # SOUL.md
    if soul_src.exists():
        # Add export header
        soul_content = soul_src.read_text()
        header = f"""# EXPORTED PERSONA
# Original: Default agent ({datetime.now().strftime('%Y-%m-%d')})
# Name: {persona_name}

"""
        (persona_path / "SOUL.md").write_text(header + soul_content)
        print("  ✓ SOUL.md")
    
    # USER.md
    if user_src.exists():
        user_content = user_src.read_text()
        header = f"""# EXPORTED USER
# Original: Default relationship ({datetime.now().strftime('%Y-%m-%d')})

"""
        (persona_path / "USER.md").write_text(header + user_content)
        print("  ✓ USER.md")
    
    # AGENTS.md
    if agents_src.exists():
        agents_content = agents_src.read_text()
        header = f"""# EXPORTED AGENTS
# Original: Default procedures ({datetime.now().strftime('%Y-%m-%d')})

"""
        (persona_path / "AGENTS.md").write_text(header + agents_content)
        print("  ✓ AGENTS.md")
    else:
        # Create default AGENTS.md
        (persona_path / "AGENTS.md").write_text(f"""# AGENTS.md

## Every Session

Before doing anything else:
1. Read `SOUL.md` — this is who I am
2. Read `USER.md` — this is who I'm helping
3. Read `memory/YYYY-MM-DD.md` (today + yesterday) for recent context

## Memory System

### Daily Notes
**File:** `memory/YYYY-MM-DD.md`

### Highlights
- **Daily:** `memory/highlights/daily/YYYY-MM-DD.md`
- **Weekly:** `memory/highlights/weekly/YYYY-WXX.md`
- **Monthly:** `memory/highlights/monthly/YYYY-MM.md`
- **Yearly:** `memory/highlights/yearly/YYYY.md`

### Core Memories
**Location:** `memory/core-memories/[name].md`

---

*Exported from default agent on {datetime.now().strftime('%Y-%m-%d')}*
""")
        print("  ✓ AGENTS.md (default)")
    
    # Copy memory folder
    if memory_src.exists():
        memory_dst = persona_path / "memory"
        # Copy but don't overwrite existing
        shutil.copytree(memory_src, memory_dst, dirs_exist_ok=True)
        print(f"  ✓ memory/ (copied)")
    else:
        # Create empty memory structure
        memory_path = persona_path / "memory"
        memory_path.mkdir()
        (memory_path / "highlights").mkdir()
        (memory_path / "highlights" / "daily").mkdir()
        (memory_path / "highlights" / "weekly").mkdir()
        (memory_path / "highlights" / "monthly").mkdir()
        (memory_path / "highlights" / "yearly").mkdir()
        (memory_path / "core-memories").mkdir()
        print("  ✓ memory/ (empty structure)")
    
    # Create EXPLAINER.md
    explainer = f"""# {persona_name.title()} — Exported Persona

**Origin:** Default agent exported on {datetime.now().strftime('%Y-%m-%d')}

This is a snapshot of the original agent personality before ClawSwap was installed.

## When to Use

Use this persona when you want the original agent behavior — before any specialization.

## How to Share

To share this persona with others:
```bash
cd ~/.openclaw/workspace/personas/
tar czf {persona_name}.tar.gz {persona_name}/
# Share {persona_name}.tar.gz
```

To import someone else's persona:
```bash
cd ~/.openclaw/workspace/personas/
tar xzf their-persona.tar.gz
```
"""
    (persona_path / "EXPLAINER.md").write_text(explainer)
    print("  ✓ EXPLAINER.md")
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: export_default_bot.py <persona-name>")
        print("")
        print("Exports your current/default bot as a ClawSwap persona.")
        print("This saves your SOUL.md, USER.md, and memory/ in persona format.")
        print("")
        print("Example:")
        print("  export_default_bot.py my-default")
        print("")
        print("After export, you can:")
        print("  activate my-default    # Switch to your exported persona")
        print("  # Or share the folder: ~/.openclaw/workspace/personas/my-default/")
        sys.exit(1)
    
    persona_name = sys.argv[1]
    
    if export_default_bot(persona_name):
        print(f"\n✅ Exported to: {get_personas_dir() / persona_name}")
        print(f"\nTo use: activate {persona_name}")
        print(f"To share: tar czf {persona_name}.tar.gz {persona_name}/")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
