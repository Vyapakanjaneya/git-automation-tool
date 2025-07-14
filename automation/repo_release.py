from automation.utils import get_github_client

def create_release(repo_name, tag, title, description):
    """Create a GitHub Release with a tag."""
    gh = get_github_client()
    repo = gh.get_user().get_repo(repo_name)

    # Create tag based on latest commit
    latest_commit_sha = repo.get_commits()[0].sha

    repo.create_git_ref(
        ref=f"refs/tags/{tag}",
        sha=latest_commit_sha
    )

    release = repo.create_git_release(
        tag=tag,
        name=title,
        message=description
    )

    print(f" Release '{tag}' created successfully!")
    return release


def upload_asset(repo_name, tag, file_path):
    """Upload an asset to an existing release."""
    gh = get_github_client()
    repo = gh.get_user().get_repo(repo_name)

    release = None
    for r in repo.get_releases():
        if r.tag_name == tag:
            release = r
            break

    if release is None:
        print(" Release not found!")
        return

    release.upload_asset(file_path)
    print(f" Asset uploaded to release '{tag}'.")
