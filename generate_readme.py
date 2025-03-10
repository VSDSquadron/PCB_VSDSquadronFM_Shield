import os
import sys
import subprocess

"""
This script automates the process of updating the README.md file with images
from the 'production' folders inside each shield directory. It does the following:

1. Iterates over all folders in the repository.
2. Finds the 'production' folder in each shield directory.
3. Collects all images but **skips** those containing specified keywords.
4. Appends the filtered images **directly** to the bottom of `README.md`.
5. If no `--no-push` flag is provided, commits and pushes changes to the repo.

Usage:
- Run normally to update `README.md` and push changes: `python script.py`
- Use `--no-push` to skip Git operations: `python script.py --no-push`
"""

# Define the repository path (script runs from repo root)
repo_path = os.getcwd()

# Define matching keywords for images (if found, those images will be skipped)
image_keywords = ["back", "bottomview", "bot", "-b"]

# Markdown file path
readme_path = os.path.join(repo_path, "README.md")

# Get all directories dynamically
shield_folders = [d for d in os.listdir(repo_path) if os.path.isdir(os.path.join(repo_path, d))]

# Markdown content
image_md_content = "\n\n# Shields Images\n\n"

for shield in shield_folders:
    production_path = os.path.join(repo_path, shield, "production")
    
    if not os.path.exists(production_path):
        print(f"Skipping {shield}, no 'production' folder found.")
        continue
    
    images = [img for img in os.listdir(production_path) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Skip images if they contain any of the defined keywords
    filtered_images = [img for img in images if not any(kw in img.lower() for kw in image_keywords)]

    if filtered_images:
        image_md_content += f"## {shield}\n"
        for img in filtered_images:
            image_path = f"{shield}/production/{img}"
            image_md_content += f"![{img}]({image_path})\n\n"

# Update the README.md file
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Remove old image content if it exists
if "# Shields Images" in readme_content:
    readme_content = readme_content.split("# Shields Images")[0].strip()

# Append new image content
readme_content += image_md_content

# Write back to README.md
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated, skipping images with keywords:", image_keywords)

# Check if the --no-push flag is provided
if "--no-push" in sys.argv:
    print("🚀 Skipping Git operations as '--no-push' is enabled.")
    sys.exit(0)

# Git operations: Add, Commit, and Push changes
try:
    subprocess.run(["git", "add", "README.md"], check=True)
    subprocess.run(["git", "commit", "-m", "Updated README.md with latest shield images"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ Changes pushed to the repository.")
except subprocess.CalledProcessError as e:
    print(f"⚠️ Git operation failed: {e}")
