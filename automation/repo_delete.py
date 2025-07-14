import os
import shutil
from automation.utils import get_github_client

def delete_remote_repo(repo_name):
    """Delete a GitHub repo permanently (with confirmation)."""
    gh = get_github_client()
    user = gh.get_user()

    # Check if repo exists
    try:
        repo = user.get_repo(repo_name)
    except:
        print(f" Repo '{repo_name}' not found.")
        return

    print(f" WARNING: You are about to delete the GitHub repo '{repo_name}' permanently!")
    confirm = input("Type YES/NO to continue: ")

    if confirm != "YES":
        print(" Deletion cancelled.")
        return

    repo.delete()
    print(f" GitHub repo '{repo_name}' deleted successfully!")


def delete_local_repo(repo_name):
    """Delete local project folder."""
    if not os.path.exists(repo_name):
        print(f" Local folder '{repo_name}' does not exist.")
        return

    print(f" WARNING: This will delete your local folder '{repo_name}'!")
    confirm = input("Type YES to continue: ")

    if confirm != "YES":
        print(" Deletion cancelled.")
        return

    shutil.rmtree(repo_name)
    print(f" Local repo folder '{repo_name}' deleted.")


def delete_full(repo_name):
    """Delete both the remote repo and the local folder."""
    delete_remote_repo(repo_name)
    delete_local_repo(repo_name)
