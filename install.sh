#!/bin/bash
# ClawSwap One-Line Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/meetproto/clawswap/main/install.sh | bash

set -e

REPO_URL="https://github.com/meetproto/clawswap"
SKILL_NAME="clawswap"

echo "🐾 Installing ClawSwap..."

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

# Create temp directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Download latest release
echo "⬇️  Downloading ClawSwap..."
if command -v curl &> /dev/null; then
    curl -fsSL "$REPO_URL/releases/latest/download/clawswap-skill.skill" -o "clawswap-skill.skill" || {
        # Fallback: clone and package
        echo "   Download failed, cloning repo..."
        git clone --depth 1 "$REPO_URL" repo
        cd repo/skill
        # Try to package if skill-creator is available
        if command -v python3 &> /dev/null && [ -f "/home/me/.npm-global/lib/node_modules/openclaw/skills/skill-creator/scripts/package_skill.py" ]; then
            python3 "/home/me/.npm-global/lib/node_modules/openclaw/skills/skill-creator/scripts/package_skill.py" . ../../clawswap-skill.skill
            cd ../..
        else
            # Manual copy
            echo "   Copying skill source..."
            mkdir -p "$WORKSPACE/.skills/clawswap"
            cp -r skill/* "$WORKSPACE/.skills/clawswap/"
            cd ..
        fi
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
        echo "✅ Skill installed to: $SKILLS_DIR"
    else
        echo "⚠️  Need sudo to install skill to: $SKILLS_DIR"
        sudo cp "clawswap-skill.skill" "$SKILLS_DIR/"
        echo "✅ Skill installed"
    fi
else
    echo "⚠️  Could not find OpenClaw skills directory"
    echo "   Skill file saved to: $TEMP_DIR/clawswap-skill.skill"
    echo "   Install manually: sudo cp clawswap-skill.skill /usr/local/lib/node_modules/openclaw/skills/"
fi

# Copy personas to workspace
echo "👤 Setting up personas..."
if [ -d "repo/personas" ]; then
    PERSONAS_SRC="repo/personas"
elif [ -d "personas" ]; then
    PERSONAS_SRC="personas"
else
    echo "❌ Could not find personas folder"
    exit 1
fi

# Copy personas if not already exists
if [ ! -d "$WORKSPACE/personas" ]; then
    cp -r "$PERSONAS_SRC" "$WORKSPACE/"
    echo "✅ Personas installed: smith, muse, helm"
else
    echo "⚠️  Personas folder already exists at $WORKSPACE/personas"
    echo "   Skipping copy. Delete it first if you want fresh install."
fi

# Cleanup
cd "$WORKSPACE"
rm -rf "$TEMP_DIR"

echo ""
echo "✅ ClawSwap installed!"
echo ""
if [ -n "$SKILLS_DIR" ] && [ -f "$SKILLS_DIR/clawswap-skill.skill" ]; then
    echo "Skill location: $SKILLS_DIR/clawswap-skill.skill"
    echo "Should appear in: /clawd list-skills"
fi
echo "Personas location: $WORKSPACE/personas/"
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
