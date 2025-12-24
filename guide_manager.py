#!/usr/bin/env python3
import os
import sys
import argparse
import datetime
import subprocess
import re
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).parent.resolve()
CONTENT_DIR = REPO_ROOT / "content"

def slugify(text):
    """Converts 'My Cool Guide' to 'my-cool-guide'."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def git_push(filepath, message):
    """Commits and pushes changes."""
    try:
        subprocess.run(["git", "add", "."], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "push"], cwd=REPO_ROOT, check=True)
        print(f"✅ Pushed to repo successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git Error: {e}")

def create_guide(title, category, content):
    """Creates a new markdown guide with Frontmatter."""
    
    # ensure category folder exists
    category_slug = slugify(category)
    folder_path = CONTENT_DIR / category_slug
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # Filename
    filename = f"{slugify(title)}.md"
    file_path = folder_path / filename
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # YAML Frontmatter (for static site generators)
    frontmatter = f"""
---
title: "{title}"
date: {timestamp}
category: {category}
slug: {slugify(title)}
---

"""
    
    # Write file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(content)
        if not content.endswith('\n'):
            f.write('\n')
            
    print(f"📘 Guide created: {file_path}")
    
    # Push
    git_push(file_path, f"Add guide: {title} ({category})")

def main():
    parser = argparse.ArgumentParser(description="QuickGuide Manager")
    parser.add_argument("title", help="Title of the guide")
    parser.add_argument("category", help="Category (e.g., 'devops', 'python')", default="general")
    parser.add_argument("--content", help="Content of the guide (optional, defaults to stdin)", default=None)
    
    args = parser.parse_args()
    
    content = ""
    if args.content:
        content = args.content
    elif not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        print("Error: No content provided. Pipe content in or use --content.")
        sys.exit(1)
        
    create_guide(args.title, args.category, content)

if __name__ == "__main__":
    main()
