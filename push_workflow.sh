#!/bin/bash

# Push workflow script
# 1. Check for uncommitted changes
# 2. git pull (get latest changes)
# 3. Clear translation.rst
# 4. git push (current commits, excluding translation.rst)

echo "🚀 Starting push workflow..."

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  You have uncommitted changes!"
    echo "Please commit your changes first, then run this script."
    echo "Or run: git stash && ./push_workflow.sh && git stash pop"
    exit 1
fi

# Step 1: Pull latest changes
echo "📥 Pulling latest changes..."
if ! git pull; then
    echo "❌ Pull failed due to conflicts!"
    echo "Please resolve conflicts manually, then run this script again."
    exit 1
fi

# Step 2: Clear translation.rst file
echo "🧹 Clearing translation.rst contents..."
echo "" > docs/source/translation.rst
echo "✅ Cleared translation.rst"

# Step 3: Push current commits (excluding translation.rst)
echo "📤 Pushing current commits (excluding translation.rst)..."
git add .
git reset docs/source/translation.rst  # Unstage translation.rst
git commit -m "Update current changes (translation.rst cleared locally)"
git push

echo "✅ Push workflow completed!"
echo "📝 Note: translation.rst was cleared locally but not pushed" 