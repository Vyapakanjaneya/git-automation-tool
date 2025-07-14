from automation.utils import get_github_client
from github.GithubException import GithubException

def get_repo_stats(repo_name):
    """Fetch and display stats for a single repo."""
    gh = get_github_client()
    user = gh.get_user()
    repo = user.get_repo(repo_name)

    print(f"\n Stats for: {repo.full_name}")
    print("-" * 40)

    print(f" Stars: {repo.stargazers_count}")
    print(f" Forks: {repo.forks_count}")
    print(f" Watchers: {repo.watchers_count}")
    print(f" Open Issues: {repo.open_issues_count}")
    print(f" Default Branch: {repo.default_branch}")
    print(f" Size: {repo.size} KB")
    print(f" License: {repo.license.name if repo.license else 'None'}")
    print(f" Last Updated: {repo.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

    # Count contributors
    contributors = repo.get_contributors()
    contributor_count = sum(1 for _ in contributors)
    print(f" Contributors: {contributor_count}")

    # Safe commit counting (handles empty repo)
    try:
        commit_count = repo.get_commits().totalCount
    except GithubException as e:
        if "empty" in str(e).lower():
            commit_count = 0
        else:
            raise e

    print(f" Total Commits: {commit_count}\n")


def stats_all():
    """Display stats for all repositories."""
    gh = get_github_client()
    user = gh.get_user()

    print("\n Fetching stats for ALL repos...\n")

    for repo in user.get_repos():
        get_repo_stats(repo.name)

    print(" All statistics displayed.\n")
