import os
import subprocess
from automation.utils import get_github_client

def run_cmd(cmd, cwd=None, env=None):
    """Run a shell command and print output."""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd, env=env,
        capture_output=True, text=True
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0


def init_local_repo(repo_name):
    """Initialize a local git repository with README & .gitignore."""
    if not os.path.exists(repo_name):
        os.makedirs(repo_name)

    with open(os.path.join(repo_name, "README.md"), "w") as f:
        f.write(f"# {repo_name}\n\nCreated automatically by GitHub Automation Tool.")

    with open(os.path.join(repo_name, ".gitignore"), "w") as f:
        f.write("__pycache__/\nvenv/\n.env\nconfig.json\n")

    run_cmd("git init", cwd=repo_name)
    run_cmd("git add .", cwd=repo_name)
    run_cmd('git commit -m "Initial commit"', cwd=repo_name)

    print(f" Local repo '{repo_name}' initialized successfully.")


def push_to_github(repo_name):
    """Push initial commit."""
    config = load_config()
    username = config["username"]
    remote_url = f"https://github.com/{username}/{repo_name}.git"

    run_cmd(f"git remote add origin {remote_url}", cwd=repo_name)
    run_cmd("git branch -M main", cwd=repo_name)
    run_cmd("git push -u origin main", cwd=repo_name)

    print(f" Successfully pushed to GitHub: {remote_url}")


# ----------  BACKDATED COMMITS   ----------
def create_backdated_commit(repo_name, message, date):
    """
    Create a commit with a specific past date.
    Example date: "2020-02-12 14:30:00"
    """
    print(f" Creating backdated commit at: {date}")

    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_DATE"] = date

    run_cmd("git add .", cwd=repo_name, env=env)
    run_cmd(f'git commit -m "{message}"', cwd=repo_name, env=env)
    run_cmd("git push", cwd=repo_name, env=env)

    print(" Backdated commit pushed successfully.")
