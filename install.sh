#!/bin/bash
# ClawSwap Interactive Installer
# Usage: curl -fsSL ... | bash

set -e

REPO_URL="https://github.com/meetproto/clawswap"
SKILL_NAME="clawswap"

echo "🐾 ClawSwap Installer"
echo ""

# Find OpenClaw workspace
if [ -d "$HOME/.openclaw/workspace" ]; then
    WORKSPACE="$HOME/.openclaw/workspace"
elif [ -d "$HOME/openclaw/workspace" ]; then
    WORKSPACE="$HOME/openclaw/workspace"
else
    echo "❌ Could not find OpenClaw workspace"
    echo "   Expected: ~/.openclaw/workspace or ~/openclaw/workspace"
    exit 1
fi

echo "📁 Workspace: $WORKSPACE"
echo ""

# Create temp directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Download latest release
echo "⬇️  Downloading ClawSwap..."
if command -v curl &> /dev/null; then
    curl -fsSL "$REPO_URL/releases/latest/download/clawswap-skill.skill" -o "clawswap-skill.skill" 2>/dev/null || {
        echo "   Download failed, cloning repo..."
        git clone --depth 1 "$REPO_URL" repo
    }
fi

# Find OpenClaw skills directory
SKILLS_DIR=""
if [ -d "/usr/local/lib/node_modules/openclaw/skills" ]; then
    SKILLS_DIR="/usr/local/lib/node_modules/openclaw/skills"
elif [ -d "/opt/openclaw/skills" ]; then
    SKILLS_DIR="/opt/openclaw/skills"
elif [ -d "$HOME/.npm-global/lib/node_modules/openclaw/skills" ]; then
    SKILLS_DIR="$HOME/.npm-global/lib/node_modules/openclaw/skills"
fi

# Install skill if we have a .skill file
if [ -f "clawswap-skill.skill" ] && [ -n "$SKILLS_DIR" ]; then
    echo "📦 Installing skill to OpenClaw..."
    if [ -w "$SKILLS_DIR" ]; then
        cp "clawswap-skill.skill" "$SKILLS_DIR/"
    else
        echo "   Requesting sudo for skill installation..."
        sudo cp "clawswap-skill.skill" "$SKILLS_DIR/"
    fi
    echo "✅ Skill installed"
fi

# Find personas source
if [ -d "repo/personas" ]; then
    PERSONAS_SRC="repo/personas"
    CLAWSWAP_SRC="repo/CLAWSWAP.md"
elif [ -d "personas" ]; then
    PERSONAS_SRC="personas"
    CLAWSWAP_SRC="CLAWSWAP.md"
else
    echo "❌ Could not find personas folder"
    exit 1
fi

# Copy CLAWSWAP.md
if [ -f "$CLAWSWAP_SRC" ]; then
    cp "$CLAWSWAP_SRC" "$WORKSPACE/"
    echo "✅ CLAWSWAP.md installed"
fi

# Interactive persona selection
echo ""
echo "👤 Persona Selection"
echo ""
echo "ClawSwap comes with 3 example personas:"
echo "  🔧 Smith — The Builder (code, debug, architecture)"
echo "  🎨 Muse — The Artist (write, name, brand)"
echo "  🧭 Helm — The Navigator (strategy, plan, roadmap)"
echo ""
echo "You can use them as-is, modify them, delete them, or create your own."
echo ""

# Check if personas already exist
if [ -d "$WORKSPACE/personas" ]; then
    echo "⚠️  Personas folder already exists at $WORKSPACE/personas"
    echo "   Skipping persona installation."
    echo "   Delete the folder first if you want to reinstall: rm -rf $WORKSPACE/personas"
else
    echo "Select installation option:"
    echo "  1) Install ALL default personas (smith, muse, helm)"
    echo "  2) Install NONE (create your own later)"
    echo "  3) Choose which to install"
    echo ""
    read -p "Enter choice [1/2/3]: " choice
    
    case $choice in
        1)
            echo ""
            echo "Installing all personas..."
            cp -r "$PERSONAS_SRC" "$WORKSPACE/"
            echo "✅ Installed: smith, muse, helm"
            ;;
        2)
            echo ""
            echo "Skipping default personas."
            echo "Create your own later with: clawswap create-persona <name>"
            mkdir -p "$WORKSPACE/personas"
            ;;
        3)
            echo ""
            mkdir -p "$WORKSPACE/personas"
            
            read -p "Install Smith (Builder)? [y/N]: " smith_choice
            if [[ $smith_choice =~ ^[Yy]$ ]]; then
                cp -r "$PERSONAS_SRC/smith" "$WORKSPACE/personas/"
                echo "  ✓ Smith installed"
            fi
            
            read -p "Install Muse (Artist)? [y/N]: " muse_choice
            if [[ $muse_choice =~ ^[Yy]$ ]]; then
                cp -r "$PERSONAS_SRC/muse" "$WORKSPACE/personas/"
                echo "  ✓ Muse installed"
            fi
            
            read -p "Install Helm (Navigator)? [y/N]: " helm_choice
            if [[ $helm_choice =~ ^[Yy]$ ]]; then
                cp -r "$PERSONAS_SRC/helm" "$WORKSPACE/personas/"
                echo "  ✓ Helm installed"
            fi
            ;;
        *)
            echo "Invalid choice. Installing all personas by default..."
            cp -r "$PERSONAS_SRC" "$WORKSPACE/"
            echo "✅ Installed: smith, muse, helm"
            ;;
    esac
fi

# Cleanup
cd "$WORKSPACE"
rm -rf "$TEMP_DIR"

echo ""
echo "✅ ClawSwap installation complete!"
echo ""
if [ -n "$SKILLS_DIR" ] && [ -f "$SKILLS_DIR/clawswap-skill.skill" ]; then
    echo "Skill location: $SKILLS_DIR/clawswap-skill.skill"
fi
echo "Personas location: $WORKSPACE/personas/"
echo "System guide: $WORKSPACE/CLAWSWAP.md"
echo ""
echo "Quick start:"
echo "  activate smith     # Switch to Smith (Builder)"
echo "  activate muse      # Switch to Muse (Artist)"
echo "  activate helm      # Switch to Helm (Navigator)"
echo ""
echo "Or let the orchestrator decide:"
echo "  'Debug this error'  → Auto-switches to Smith"
echo "  'Name this feature' → Auto-switches to Muse"
echo ""
