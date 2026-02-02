#!/usr/bin/env python3
"""
ClawSwap: Initialize personas directory with default personas.
Safe installation - won't touch your existing memory.
"""

import shutil
from pathlib import Path
from datetime import datetime

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
    """Find ClawSwap source directory with personas."""
    # Check skill installation location first
    skill_dir = Path(__file__).parent.parent.parent  # skill/../..
    if (skill_dir / "personas" / "smith" / "SOUL.md").exists():
        return skill_dir
    
    # Check if personas are bundled with skill
    if (skill_dir / "default-personas" / "smith" / "SOUL.md").exists():
        return skill_dir / "default-personas"
    
    # Check workspace (for development)
    workspace = Path.home() / ".openclaw" / "workspace" / "clawswap"
    if (workspace / "personas" / "smith" / "SOUL.md").exists():
        return workspace
    
    return None

def create_memory_structure(persona_path):
    """Create memory folder structure for a persona."""
    memory = persona_path / "memory"
    memory.mkdir(exist_ok=True)
    
    highlights = memory / "highlights"
    highlights.mkdir(exist_ok=True)
    (highlights / "daily").mkdir(exist_ok=True)
    (highlights / "weekly").mkdir(exist_ok=True)
    (highlights / "monthly").mkdir(exist_ok=True)
    (highlights / "yearly").mkdir(exist_ok=True)
    
    (memory / "core-memories").mkdir(exist_ok=True)

def copy_persona(source_dir, personas_dir, persona_name):
    """Copy a single persona from source to destination."""
    src = source_dir / "personas" / persona_name
    dst = personas_dir / persona_name
    
    if not src.exists():
        print(f"  ✗ Source not found: {src}")
        return False
    
    if dst.exists():
        shutil.rmtree(dst)
    
    shutil.copytree(src, dst)
    create_memory_structure(dst)
    print(f"  ✓ {persona_name}/")
    return True

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
    
    # Check if already initialized
    if personas_dir.exists() and any(personas_dir.iterdir()):
        print(f"⚠️  Personas directory already exists at: {personas_dir}")
        response = input("Reinstall? This will backup existing personas. [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled.")
            return
        # Backup existing
        backup_dir = personas_dir.parent / f"personas-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        shutil.move(str(personas_dir), str(backup_dir))
        print(f"Backed up to: {backup_dir}\n")
        personas_dir.mkdir(parents=True)
    
    personas_dir.mkdir(parents=True, exist_ok=True)
    
    # Interactive persona selection
    print("ClawSwap comes with 3 example personas:")
    print("  🔧 smith — The Builder (code, debug, architecture)")
    print("  🎨 muse — The Artist (write, name, brand)")
    print("  🧭 helm — The Navigator (strategy, plan, roadmap)")
    print("")
    print("Select installation option:")
    print("  1) Install ALL default personas")
    print("  2) Install NONE (create your own later)")
    print("  3) Choose which to install individually")
    print("")
    
    choice = input("Enter choice [1/2/3]: ").strip()
    
    installed = []
    
    if choice == "1":
        print("\nInstalling all personas...")
        if source_dir:
            for persona in ["smith", "muse", "helm"]:
                if copy_persona(source_dir, personas_dir, persona):
                    installed.append(persona)
        else:
            print("⚠️  Source not found. Creating empty structure...")
            for persona in ["smith", "muse", "helm"]:
                p_dir = personas_dir / persona
                p_dir.mkdir(exist_ok=True)
                create_memory_structure(p_dir)
                print(f"  ✓ {persona}/ (empty)")
                installed.append(persona)
                
    elif choice == "2":
        print("\nSkipping default personas.")
        print("Create your own later with: clawswap create-persona <name>")
        
    elif choice == "3":
        print("")
        if not source_dir:
            print("⚠️  Source not found. Cannot install individual personas.")
            return
            
        for persona in ["smith", "muse", "helm"]:
            response = input(f"Install {persona}? [y/N]: ").strip()
            if response.lower() == 'y':
                if copy_persona(source_dir, personas_dir, persona):
                    installed.append(persona)
    else:
        print("Invalid choice. Installing all personas by default...")
        if source_dir:
            for persona in ["smith", "muse", "helm"]:
                if copy_persona(source_dir, personas_dir, persona):
                    installed.append(persona)
    
    # Copy CLAWSWAP.md if exists
    if source_dir:
        clawswap_md_src = source_dir / "CLAWSWAP.md"
        clawswap_md_dst = workspace / "CLAWSWAP.md"
        if clawswap_md_src.exists() and not clawswap_md_dst.exists():
            shutil.copy(clawswap_md_src, clawswap_md_dst)
            print("\n✓ CLAWSWAP.md installed")
    
    print(f"\n{'='*60}")
    print("✓ Initialization complete!")
    print(f"{'='*60}\n")
    
    if installed:
        print(f"Installed personas: {', '.join(installed)}")
    
    print(f"\nYour original memory is safe at:")
    print(f"  {workspace / 'memory'}")
    print(f"\nPersonas are isolated at:")
    print(f"  {personas_dir}")
    if (workspace / "CLAWSWAP.md").exists():
        print(f"\nSystem guide:")
        print(f"  {workspace / 'CLAWSWAP.md'}")
    
    if installed:
        print("\nTry it out:")
        for persona in installed[:3]:  # Show first 3
            print(f"  activate {persona}")
    
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    main()
