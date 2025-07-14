from automation.utils import get_github_client

def create_issue(repo_name, title, body=""):
    """Create a new issue in a given repo."""
    gh = get_github_client()
    user = gh.get_user()
    repo = user.get_repo(repo_name)

    issue = repo.create_issue(title=title, body=body)
    print(f" Issue created: #{issue.number} - {title}")


def comment_issue(repo_name, issue_number, comment):
    """Add a comment to an existing issue."""
    gh = get_github_client()
    user = gh.get_user()
    repo = user.get_repo(repo_name)

    issue = repo.get_issue(number=issue_number)
    issue.create_comment(comment)

    print(f" Comment added to issue #{issue_number}")


def close_issue(repo_name, issue_number):
    """Close an issue."""
    gh = get_github_client()
    user = gh.get_user()
    repo = user.get_repo(repo_name)

    issue = repo.get_issue(number=issue_number)
    issue.edit(state="closed")

    print(f" Issue #{issue_number} closed.")


def add_label(repo_name, issue_number, label_name, color="FF5733"):
    """Add a label to an issue."""
    gh = get_github_client()
    user = gh.get_user()
    repo = user.get_repo(repo_name)

    # Create label if not exists
    try:
        label = repo.get_label(label_name)
    except:
        label = repo.create_label(name=label_name, color=color)

    issue = repo.get_issue(number=issue_number)
    issue.add_to_labels(label)

    print(f" Label '{label_name}' added to issue #{issue_number}")


def list_issues(repo_name):
    """List all issues in the repository."""
    gh = get_github_client()
    user = gh.get_user()
    repo = user.get_repo(repo_name)

    issues = repo.get_issues()

    print(f"\n Issues in {repo_name}:")
    for issue in issues:
        print(f"#{issue.number} - {issue.title} [{issue.state}]")
    print()
