#!/usr/bin/env python3
"""
ClawSwap: List all available personas and their status.
"""

import os
from pathlib import Path
from datetime import datetime

def get_clawswap_root():
    """Find clawswap root directory."""
    possible_paths = [
        Path.home() / ".openclaw" / "workspace" / "clawswap",
        Path.cwd() / "clawswap",
        Path.cwd().parent / "clawswap",
        Path("/tmp/clawswap"),
    ]
    
    for path in possible_paths:
        if path.exists() and (path / "CORTEX.md").exists():
            return path
    
    if (Path.cwd() / "CORTEX.md").exists():
        return Path.cwd()
    
    return None

def get_persona_info(root_path, persona_name):
    """Get summary info about a persona."""
    persona_path = root_path / "personas" / persona_name
    
    info = {
        "name": persona_name,
        "valid": False,
        "identity": "Unknown",
        "has_memories": False,
        "memory_count": 0
    }
    
    if not persona_path.exists():
        return info
    
    # Check SOUL.md
    soul_path = persona_path / "SOUL.md"
    if soul_path.exists():
        info["valid"] = True
        content = soul_path.read_text()
        for line in content.split('\n'):
            if line.strip().startswith("I am "):
                info["identity"] = line.strip()
                break
    
    # Check memory folder
    memory_path = persona_path / "memory"
    if memory_path.exists():
        info["has_memories"] = True
        # Count memory files
        count = 0
        for item in memory_path.rglob("*.md"):
            count += 1
        info["memory_count"] = count
    
    return info

def main():
    root_path = get_clawswap_root()
    
    if not root_path:
        print("Error: Could not find clawswap root directory")
        print("Make sure you're in or near a clawswap installation")
        sys.exit(1)
    
    personas_dir = root_path / "personas"
    
    if not personas_dir.exists():
        print("Error: No personas directory found")
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print(f"CLAWSWAP PERSONAS")
    print(f"Root: {root_path}")
    print(f"{'='*60}\n")
    
    personas = sorted([d.name for d in personas_dir.iterdir() if d.is_dir()])
    
    if not personas:
        print("No personas found.")
        print(f"\nCreate one in: {personas_dir}")
        return
    
    print(f"Found {len(personas)} persona(s):\n")
    
    for name in personas:
        info = get_persona_info(root_path, name)
        
        status = "✓ Valid" if info["valid"] else "✗ Invalid"
        mem_status = f"({info['memory_count']} memories)" if info["has_memories"] else "(no memories)"
        
        print(f"  📁 {name}")
        print(f"     Status: {status}")
        print(f"     Identity: {info['identity'][:50]}...")
        print(f"     Memories: {mem_status}")
        print()
    
    print(f"{'='*60}")
    print("\nTo switch: switch_persona.py <persona-name>")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    import sys
    main()
