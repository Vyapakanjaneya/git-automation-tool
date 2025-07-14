import json
from github import Github

def load_config():
    """Load config.json file."""
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(" config.json not found!")
        exit(1)

def get_github_client():
    """Return authenticated GitHub client."""
    config = load_config()
    token = config.get("token")

    if not token:
        print(" GitHub token missing in config.json")
        exit(1)

    return Github(token)
