# QuickGuides Repository

This repository hosts a collection of Markdown guides, structured for automated publishing to a future documentation website (e.g., using Hugo, Jekyll, or MkDocs).

## 📂 Structure

All guides are stored in the `content/` directory, organized by category:

```
QuickGuides/
├── content/
│   ├── devops/
│   │   └── docker-basics.md
│   ├── python/
│   │   └── virtual-envs.md
│   └── general/
├── guide_manager.py  # Automation tool
└── README.md
```

## 🛠 Adding a Guide

Use the `guide_manager.py` script to add guides. It automatically handles:
1.  **File Naming:** Slugifies titles (e.g., "My Guide" -> `my-guide.md`).
2.  **Metadata:** Adds YAML Frontmatter (Title, Date, Category) for the website.
3.  **Git:** Commits and pushes the new guide.

### Usage

**Pipe content (Best for copying from other tools):**
```bash
echo "# My Steps..." | python3 guide_manager.py "How to Setup X" "devops"
```

**Manual:**
```bash
python3 guide_manager.py "My Guide Title" "category" --content "# Hello World"
```

## 🌐 Future Website Integration

The `content/` folder is designed to be the source for a Static Site Generator.
*   **MkDocs:** Point `docs_dir` to `content`.
*   **Hugo:** Symlink `content` to Hugo's `content` folder.
