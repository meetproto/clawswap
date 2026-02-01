#!/usr/bin/env python3
"""
ClawSwap: Switch between fully isolated AI personas.
Personas live in personas/[name]/ — separate from your main memory.
"""

import sys
import os
from datetime import datetime
from pathlib import Path

def get_workspace_root():
    """Find OpenClaw workspace root."""
    # Check common locations
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
    """Get personas directory (creates if needed)."""
    workspace = get_workspace_root()
    personas_dir = workspace / "personas"
    
    if not personas_dir.exists():
        print(f"Creating personas directory: {personas_dir}")
        personas_dir.mkdir(parents=True)
    
    return personas_dir

def list_personas():
    """List all available personas."""
    personas_dir = get_personas_dir()
    
    if not personas_dir.exists():
        return []
    
    personas = []
    for item in personas_dir.iterdir():
        if item.is_dir() and (item / "SOUL.md").exists():
            personas.append(item.name)
    
    return sorted(personas)

def validate_persona(persona_name):
    """Check if persona has all required files."""
    personas_dir = get_personas_dir()
    persona_path = personas_dir / persona_name
    
    if not persona_path.exists():
        return False, f"Persona '{persona_name}' not found in {personas_dir}"
    
    required_files = ["SOUL.md", "USER.md"]
    missing = []
    
    for file in required_files:
        if not (persona_path / file).exists():
            missing.append(file)
    
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    
    return True, "Valid"

def get_persona_summary(persona_name):
    """Extract key info from SOUL.md."""
    personas_dir = get_personas_dir()
    soul_path = personas_dir / persona_name / "SOUL.md"
    
    if not soul_path.exists():
        return None
    
    content = soul_path.read_text()
    lines = content.split('\n')
    
    identity = "Unknown"
    for line in lines:
        if line.strip().startswith("I am ") or line.strip().startswith("I'm "):
            identity = line.strip()
            break
    
    return {
        "name": persona_name,
        "identity": identity
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: switch_persona.py <persona-name>")
        print("\nAvailable personas:")
        for p in list_personas():
            print(f"  - {p}")
        
        print(f"\nPersonas directory: {get_personas_dir()}")
        print("\nTo create a new persona:")
        print("  clawswap create-persona <name>")
        sys.exit(1)
    
    persona_name = sys.argv[1]
    
    # Validate persona exists
    valid, msg = validate_persona(persona_name)
    if not valid:
        print(f"Error: {msg}")
        print(f"\nAvailable personas:")
        for p in list_personas():
            print(f"  - {p}")
        sys.exit(1)
    
    # Get persona summary
    summary = get_persona_summary(persona_name)
    
    # Output activation info
    print(f"\n{'='*50}")
    print(f"PERSONA ACTIVATED: {persona_name}")
    print(f"{'='*50}")
    if summary:
        print(f"\nIdentity: {summary['identity']}")
    
    personas_dir = get_personas_dir()
    print(f"\nLoaded from: {personas_dir / persona_name}")
    print(f"\nYour original memory is safe at: {get_workspace_root() / 'memory'}")
    print(f"\nThis persona writes to: {personas_dir / persona_name / 'memory'}")
    print(f"\nRemember: You do NOT have access to other personas' memories.")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
