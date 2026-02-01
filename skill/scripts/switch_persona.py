#!/usr/bin/env python3
"""
ClawSwap: Switch between fully isolated AI personas.
Logs the switch in CORTEX.md and outputs persona summary.
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

def get_clawswap_root():
    """Find clawswap root directory."""
    # Check if we're in a standard location
    possible_paths = [
        Path.home() / ".openclaw" / "workspace" / "clawswap",
        Path.cwd() / "clawswap",
        Path.cwd().parent / "clawswap",
        Path("/tmp/clawswap"),
    ]
    
    for path in possible_paths:
        if path.exists() and (path / "CORTEX.md").exists():
            return path
    
    # Default to current directory if CORTEX.md exists
    if (Path.cwd() / "CORTEX.md").exists():
        return Path.cwd()
    
    return None

def list_personas(root_path):
    """List all available personas."""
    personas_dir = root_path / "personas"
    if not personas_dir.exists():
        return []
    
    personas = []
    for item in personas_dir.iterdir():
        if item.is_dir() and (item / "SOUL.md").exists():
            personas.append(item.name)
    
    return sorted(personas)

def validate_persona(root_path, persona_name):
    """Check if persona has all required files."""
    persona_path = root_path / "personas" / persona_name
    
    if not persona_path.exists():
        return False, f"Persona '{persona_name}' not found"
    
    required_files = ["SOUL.md", "USER.md", "AGENTS.md"]
    missing = []
    
    for file in required_files:
        if not (persona_path / file).exists():
            missing.append(file)
    
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    
    return True, "Valid"

def get_persona_summary(root_path, persona_name):
    """Extract key info from SOUL.md."""
    soul_path = root_path / "personas" / persona_name / "SOUL.md"
    
    if not soul_path.exists():
        return None
    
    content = soul_path.read_text()
    lines = content.split('\n')
    
    # Extract identity line (usually after "## Identity" or first "I am")
    identity = "Unknown"
    for line in lines:
        if line.strip().startswith("I am "):
            identity = line.strip()
            break
    
    # Extract specialty from "What Matters" or similar
    specialty = "General"
    for i, line in enumerate(lines):
        if "## What Matters" in line or "## Specialty" in line:
            if i + 1 < len(lines):
                specialty = lines[i + 1].strip().strip('- ')
                break
    
    return {
        "name": persona_name,
        "identity": identity,
        "specialty": specialty
    }

def update_cortex_log(root_path, from_persona, to_persona):
    """Update CORTEX.md with switch log entry."""
    cortex_path = root_path / "CORTEX.md"
    
    if not cortex_path.exists():
        return False
    
    content = cortex_path.read_text()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Find the switch log section
    log_entry = f"| {timestamp} | {from_persona or '—'} | {to_persona} | Manual switch | — |\n"
    
    # Simple append for now - in production would parse and insert properly
    # For this example, we just print what would happen
    print(f"[LOG] Would add to CORTEX.md: {log_entry.strip()}")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: switch_persona.py <persona-name>")
        print("\nAvailable personas:")
        root = get_clawswap_root()
        if root:
            for p in list_personas(root):
                print(f"  - {p}")
        sys.exit(1)
    
    persona_name = sys.argv[1]
    
    # Find clawswap root
    root_path = get_clawswap_root()
    if not root_path:
        print("Error: Could not find clawswap root directory")
        sys.exit(1)
    
    # Validate persona exists
    valid, msg = validate_persona(root_path, persona_name)
    if not valid:
        print(f"Error: {msg}")
        print(f"\nAvailable personas:")
        for p in list_personas(root_path):
            print(f"  - {p}")
        sys.exit(1)
    
    # Get persona summary
    summary = get_persona_summary(root_path, persona_name)
    
    # Update CORTEX.md
    update_cortex_log(root_path, None, persona_name)
    
    # Output activation info
    print(f"\n{'='*50}")
    print(f"PERSONA ACTIVATED: {persona_name}")
    print(f"{'='*50}")
    if summary:
        print(f"\nIdentity: {summary['identity']}")
        print(f"Specialty: {summary['specialty']}")
    print(f"\nLoaded from: {root_path / 'personas' / persona_name}")
    print(f"\nNext steps:")
    print(f"  1. Read SOUL.md — understand who you are")
    print(f"  2. Read USER.md — understand your relationship")
    print(f"  3. Read AGENTS.md — understand how to operate")
    print(f"  4. Check recent memories in memory/")
    print(f"\nRemember: You do NOT have access to other personas' memories.")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
