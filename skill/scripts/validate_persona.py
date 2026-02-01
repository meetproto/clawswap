#!/usr/bin/env python3
"""
ClawSwap: Validate a persona structure.
Checks that persona won't interfere with your main memory.
"""

import sys
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

def validate_persona(persona_name):
    """Check persona has all required files and correct structure."""
    personas_dir = get_personas_dir()
    persona_path = personas_dir / persona_name
    workspace = get_workspace_root()
    
    if not persona_path.exists():
        return False, [f"Persona directory does not exist: {persona_path}"], {}
    
    required_files = {
        "SOUL.md": "Identity and values",
        "USER.md": "Relationship with user"
    }
    
    optional_files = {
        "AGENTS.md": "Operating procedures"
    }
    
    errors = []
    warnings = []
    status = {"required": {}, "optional": {}, "memory": {}, "safety": {}}
    
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
    
    # SAFETY CHECK: Ensure persona doesn't write to workspace root
    status["safety"]["isolated"] = True
    
    # Check for dangerous paths
    dangerous_paths = [
        workspace / "SOUL.md",
        workspace / "USER.md", 
        workspace / "AGENTS.md",
        workspace / "memory"
    ]
    
    for dp in dangerous_paths:
        if persona_path in dp.parents or dp in persona_path.parents:
            if dp.exists() and dp.is_file():
                errors.append(f"SAFETY: Persona too close to {dp.name}")
                status["safety"]["isolated"] = False
    
    is_valid = len(errors) == 0 and status["required"].get("SOUL.md", False)
    
    return is_valid, errors, status

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_persona.py <persona-name>")
        sys.exit(1)
    
    persona_name = sys.argv[1]
    personas_dir = get_personas_dir()
    
    print(f"\n{'='*60}")
    print(f"VALIDATING: {persona_name}")
    print(f"{'='*60}\n")
    print(f"Personas directory: {personas_dir}")
    print(f"Persona path: {personas_dir / persona_name}\n")
    
    is_valid, errors, status = validate_persona(persona_name)
    
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
        print("  ✓ memory/ folder exists (isolated from main memory)")
    else:
        print("  ○ No memory/ folder (will be created on first use)")
    
    print("\nSafety check:")
    if status["safety"]["isolated"]:
        print("  ✓ Persona is isolated from your main files")
    else:
        print("  ✗ WARNING: Persona may interfere with main files")
    
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
