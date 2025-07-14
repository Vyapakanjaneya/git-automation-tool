import os
import shutil
from datetime import datetime
from automation.utils import get_github_client

def create_backup_folder():
    """Create a backup folder if it doesn't exist."""
    if not os.path.exists("backup"):
        os.makedirs("backup")


def clone_repo(clone_url, repo_name):
    """Clone a single repository."""
    path = f"backup/{repo_name}"
    print(f" Cloning {repo_name}...")

    # If repo folder exists, delete it
    if os.path.exists(path):
        shutil.rmtree(path)

    os.system(f"git clone {clone_url} {path}")


def backup_all_repos():
    """Backup all GitHub repositories."""
    gh = get_github_client()
    user = gh.get_user()
    
    create_backup_folder()

    print("\n Fetching repositories...")
    repos = user.get_repos()

    for repo in repos:
        clone_repo(repo.clone_url, repo.name)

    print("\n Backup completed! All repos saved in /backup")


def zip_backup():
    """ZIP the backup folder with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_zip = f"backup_{timestamp}"

    print(" Creating ZIP backup...")

    shutil.make_archive(output_zip, "zip", "backup")

    print(f" Backup ZIP created: {output_zip}.zip")
