#!/usr/bin/env python3
"""
ClawSwap: Initialize personas directory with default personas.
Safe installation - won't touch your existing memory.
"""

import shutil
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

def get_clawswap_source():
    """Find ClawSwap source directory."""
    # Check common locations
    possible_paths = [
        Path(__file__).parent.parent.parent,  # skill/../..
        Path.home() / ".openclaw" / "workspace" / "clawswap",
        Path.cwd(),
    ]
    
    for path in possible_paths:
        if (path / "example-personas" / "smith" / "SOUL.md").exists():
            return path
    
    return None

def create_memory_structure(persona_path):
    """Create memory folder structure for a persona."""
    memory = persona_path / "memory"
    memory.mkdir(exist_ok=True)
    
    highlights = memory / "highlights"
    highlights.mkdir(exist_ok=True)
    (highlights / "daily").mkdir(exist_ok=True)
    (highlights / "monthly").mkdir(exist_ok=True)
    (highlights / "yearly").mkdir(exist_ok=True)
    
    (memory / "core-memories").mkdir(exist_ok=True)

def main():
    workspace = get_workspace_root()
    personas_dir = get_personas_dir()
    source_dir = get_clawswap_source()
    
    print(f"\n{'='*60}")
    print("CLAWSWAP INITIALIZATION")
    print(f"{'='*60}\n")
    
    print(f"Workspace: {workspace}")
    print(f"Your memory: {workspace / 'memory'} (will NOT be touched)")
    print(f"Personas will be created at: {personas_dir}\n")
    
    # Safety check
    if personas_dir.exists():
        print("⚠ Personas directory already exists.")
        response = input("Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Cancelled.")
            return
    
    personas_dir.mkdir(parents=True, exist_ok=True)
    
    if source_dir:
        # Copy from ClawSwap source
        source_personas = source_dir / "example-personas"
        
        for persona in ["smith", "muse", "helm"]:
            src = source_personas / persona
            dst = personas_dir / persona
            
            if src.exists():
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
                create_memory_structure(dst)
                print(f"✓ Created {persona}/")
            else:
                print(f"✗ Source not found: {src}")
    else:
        print("⚠ ClawSwap source not found. Creating empty structure...")
        for persona in ["smith", "muse", "helm"]:
            p_dir = personas_dir / persona
            p_dir.mkdir(exist_ok=True)
            create_memory_structure(p_dir)
            print(f"✓ Created {persona}/ (empty)")
    
    print(f"\n{'='*60}")
    print("✓ Initialization complete!")
    print(f"{'='*60}\n")
    
    print("Your original memory is safe at:")
    print(f"  {workspace / 'memory'}")
    print(f"\nPersonas are isolated at:")
    print(f"  {personas_dir}")
    
    print("\nTry it out:")
    print("  switch_persona.py smith")
    print("  list_personas.py")
    
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    main()
