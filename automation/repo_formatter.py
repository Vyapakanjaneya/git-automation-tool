import os

def format_code(repo_name):
    """Run Black formatter on a repository."""
    print(" Formatting code with Black...")

    result = os.system(f"black {repo_name}")

    if result == 0:
        print(" Code formatted successfully.")
    else:
        print(" Failed to format code.")
