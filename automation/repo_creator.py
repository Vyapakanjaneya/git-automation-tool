from automation.utils import get_github_client, load_config

def create_repo(repo_name, description="Created via automation tool"):
    """Create a GitHub repository and return True if created."""
    gh = get_github_client()
    user = gh.get_user()

    # Check if repo already exists
    for repo in user.get_repos():
        if repo.name == repo_name:
            print(f" Repository '{repo_name}' already exists!")
            return False

    # Create the repo
    try:
        user.create_repo(
            name=repo_name,
            description=description,
            private=False
        )
        print(f" GitHub repo '{repo_name}' created successfully!")
        return True
    except Exception as e:
        print(f" Error: {e}")
        return False
