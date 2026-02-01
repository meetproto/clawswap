#!/usr/bin/env python3
"""
ClawSwap: Validate a persona has all required files.
"""

import sys
from pathlib import Path

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

def validate_persona(root_path, persona_name):
    """Check persona has all required files and structure."""
    persona_path = root_path / "personas" / persona_name
    
    if not persona_path.exists():
        return False, ["Persona directory does not exist"], {}
    
    required_files = {
        "SOUL.md": "Identity, values, voice",
        "USER.md": "Relationship to user",
        "AGENTS.md": "Operating procedures"
    }
    
    optional_files = {
        "TOOLS.md": "Preferred tools",
        "HEARTBEAT.md": "Periodic tasks",
        "SYSTEM.md": "Documentation"
    }
    
    errors = []
    warnings = []
    status = {"required": {}, "optional": {}, "memory": {}}
    
    # Check required files
    for file, desc in required_files.items():
        path = persona_path / file
        exists = path.exists()
        status["required"][file] = exists
        if not exists:
            errors.append(f"Missing required: {file} ({desc})")
    
    # Check optional files
    for file, desc in optional_files.items():
        path = persona_path / file
        exists = path.exists()
        status["optional"][file] = exists
    
    # Check memory structure
    memory_path = persona_path / "memory"
    status["memory"]["exists"] = memory_path.exists()
    
    if memory_path.exists():
        # Check subdirectories
        for subdir in ["highlights/daily", "highlights/monthly", "highlights/yearly", "core-memories"]:
            subpath = memory_path / subdir
            status["memory"][subdir] = subpath.exists()
    else:
        warnings.append("No memory/ folder — persona has no experience storage")
    
    is_valid = len(errors) == 0 and status["required"].get("SOUL.md", False)
    
    return is_valid, errors, status

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_persona.py <persona-name>")
        sys.exit(1)
    
    persona_name = sys.argv[1]
    root_path = get_clawswap_root()
    
    if not root_path:
        print("Error: Could not find clawswap root directory")
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print(f"VALIDATING: {persona_name}")
    print(f"{'='*60}\n")
    
    is_valid, errors, status = validate_persona(root_path, persona_name)
    
    # Print status
    print("Required files:")
    for file, exists in status["required"].items():
        symbol = "✓" if exists else "✗"
        print(f"  {symbol} {file}")
    
    print("\nOptional files:")
    for file, exists in status["optional"].items():
        symbol = "✓" if exists else "○"
        print(f"  {symbol} {file}")
    
    print("\nMemory structure:")
    if status["memory"]["exists"]:
        print("  ✓ memory/ folder exists")
        for subdir, exists in status["memory"].items():
            if subdir != "exists":
                symbol = "✓" if exists else "○"
                print(f"    {symbol} {subdir}")
    else:
        print("  ✗ No memory/ folder")
    
    print(f"\n{'='*60}")
    
    if is_valid:
        print("Result: ✓ VALID")
        if errors:
            print("\nWarnings:")
            for e in errors:
                print(f"  ! {e}")
    else:
        print("Result: ✗ INVALID")
        print("\nErrors:")
        for e in errors:
            print(f"  ✗ {e}")
    
    print(f"{'='*60}\n")
    
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()
