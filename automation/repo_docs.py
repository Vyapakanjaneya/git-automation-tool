import os
from datetime import datetime

def generate_changelog(repo_name, commits):
    """Generate CHANGELOG.md based on commit messages."""
    path = f"{repo_name}/CHANGELOG.md"

    with open(path, "w") as f:
        f.write("# Changelog\n\n")
        f.write(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for c in commits:
            f.write(f"- {c.commit.author.date.strftime('%Y-%m-%d')}: {c.commit.message}")



def update_readme(repo_name, description, version):
    """Generate README.md from template."""
    template_path = "templates/README_template.md"
    output_path = f"{repo_name}/README.md"

    with open(template_path, "r") as template:
        content = template.read()

    content = (
        content.replace("{{repo_name}}", repo_name)
        .replace("{{description}}", description)
        .replace("{{version}}", version)
    )

    with open(output_path, "w") as f:
        f.write(content)

    print(" README.md updated from template.")
