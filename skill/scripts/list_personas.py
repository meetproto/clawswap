#!/usr/bin/env python3
"""
ClawSwap: List all available personas.
Personas are stored in personas/ directory, separate from your main memory.
"""

from pathlib import Path

def get_workspace_root():
    """Find OpenClaw workspace root."""
    possible_paths = [
        Path.home() / ".openclaw" / "workspace",
        Path.cwd(),
        Path.cwd().parent,
    ]
    
    for path in possible_paths:
        if (path / "SOUL.md").exists() or (path / "memory").exists():
            return path
    
    return Path.cwd()

def get_personas_dir():
    """Get personas directory."""
    return get_workspace_root() / "personas"

def get_persona_info(persona_name):
    """Get summary info about a persona."""
    personas_dir = get_personas_dir()
    persona_path = personas_dir / persona_name
    
    info = {
        "name": persona_name,
        "valid": False,
        "identity": "Unknown",
        "has_memories": False
    }
    
    if not persona_path.exists():
        return info
    
    soul_path = persona_path / "SOUL.md"
    if soul_path.exists():
        info["valid"] = True
        content = soul_path.read_text()
        for line in content.split('\n'):
            if line.strip().startswith("I am ") or line.strip().startswith("I'm "):
                info["identity"] = line.strip()
                break
    
    memory_path = persona_path / "memory"
    info["has_memories"] = memory_path.exists()
    
    return info

def main():
    personas_dir = get_personas_dir()
    workspace = get_workspace_root()
    
    print(f"\n{'='*60}")
    print(f"CLAWSWAP PERSONAS")
    print(f"{'='*60}\n")
    print(f"Workspace: {workspace}")
    print(f"Personas:  {personas_dir}\n")
    
    if not personas_dir.exists():
        print("No personas directory found.")
        print("\nTo initialize:")
        print("  clawswap init")
        return
    
    personas = sorted([d.name for d in personas_dir.iterdir() if d.is_dir()])
    
    if not personas:
        print("No personas found.")
        print("\nTo create default personas:")
        print("  clawswap init")
        return
    
    print(f"Found {len(personas)} persona(s):\n")
    
    for name in personas:
        info = get_persona_info(name)
        
        status = "✓" if info["valid"] else "✗"
        mem_status = "(has memories)" if info["has_memories"] else "(new)"
        
        print(f"  {status} {name}")
        print(f"    {info['identity'][:60]}...")
        print(f"    {mem_status}")
        print()
    
    print(f"{'='*60}")
    print("\nTo switch: switch_persona.py <name>")
    print("To create: clawswap create-persona <name>")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
