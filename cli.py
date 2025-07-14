import sys

from automation.repo_creator import create_repo
from automation.repo_committer import init_local_repo, push_to_github
from automation.repo_issues import (
    create_issue, comment_issue, close_issue,
    add_label, list_issues
)
from automation.repo_backup import backup_all_repos, zip_backup
from automation.repo_stats import get_repo_stats, stats_all
from automation.repo_docs import generate_changelog, update_readme
from automation.repo_version import bump_version
from automation.repo_formatter import format_code
from automation.utils import get_github_client
from automation.repo_committer import create_backdated_commit
from automation.repo_release import create_release, upload_asset
from automation.repo_delete import delete_remote_repo, delete_local_repo, delete_full


def show_usage():
    print("""
GitHub Automation Tool - Version 6.0

Commands:
    python cli.py create <repo-name>

Issue Commands:
    python cli.py issue-create <repo> <title>
    python cli.py issue-comment <repo> <issue_number> <comment>
    python cli.py issue-close <repo> <issue_number>
    python cli.py issue-label <repo> <issue_number> <label>
    python cli.py issue-list <repo>

Backup Commands:
    python cli.py backup
    python cli.py backup-zip

Stats Commands:
    python cli.py stats <repo>
    python cli.py stats-all

Documentation Commands:
    python cli.py changelog <repo>
    python cli.py update-readme <repo>

Versioning Commands:
    python cli.py bump-version <repo> <major|minor|patch>

Formatter:
    python cli.py format <repo>
""")


def main():
    if len(sys.argv) < 2:
        show_usage()
        return

    command = sys.argv[1]


    if command == "create":
        repo_name = sys.argv[2]
        created = create_repo(repo_name)

        if created:
            init_local_repo(repo_name)
            push_to_github(repo_name)
        return

    # =====  (Issues) =====
    if command == "issue-create":
        create_issue(sys.argv[2], " ".join(sys.argv[3:]))
        return

    if command == "issue-comment":
        repo = sys.argv[2]
        issue_number = int(sys.argv[3])
        comment = " ".join(sys.argv[4:])
        comment_issue(repo, issue_number, comment)
        return

    if command == "issue-close":
        close_issue(sys.argv[2], int(sys.argv[3]))
        return

    if command == "issue-label":
        repo = sys.argv[2]
        issue_number = int(sys.argv[3])
        label = sys.argv[4]
        add_label(repo, issue_number, label)
        return

    if command == "issue-list":
        list_issues(sys.argv[2])
        return

    # =====  (Backup) =====
    if command == "backup":
        backup_all_repos()
        return

    if command == "backup-zip":
        zip_backup()
        return

    # =====  (Stats) =====
    if command == "stats":
        get_repo_stats(sys.argv[2])
        return

    if command == "stats-all":
        stats_all()
        return

    # ===== (Documentation + Versioning + Formatter) =====

    if command == "changelog":
        repo_name = sys.argv[2]
        gh = get_github_client()
        repo = gh.get_user().get_repo(repo_name)
        commits = repo.get_commits()
        generate_changelog(repo_name, commits)
        return

    if command == "update-readme":
        repo_name = sys.argv[2]
        version = "manual"
        update_readme(repo_name, f"{repo_name} project", version)
        return

    if command == "bump-version":
        repo_name = sys.argv[2]
        part = sys.argv[3]
        new_version = bump_version(repo_name, part)
        update_readme(repo_name, f"{repo_name} project", new_version)
        return

    if command == "format":
        repo_name = sys.argv[2]
        format_code(repo_name)
        return
    
        # ===== Backdated commits  =====
    if command == "backdate":
        repo = sys.argv[2]
        message = sys.argv[3]
        date = sys.argv[4]  # exact date string
        create_backdated_commit(repo, message, date)
        return

    # ===== Releases =====
    if command == "release":
        repo = sys.argv[2]
        tag = sys.argv[3]
        title = sys.argv[4]
        description = " ".join(sys.argv[5:])
        create_release(repo, tag, title, description)
        return

    if command == "upload-asset":
        repo = sys.argv[2]
        tag = sys.argv[3]
        file_path = sys.argv[4]
        upload_asset(repo, tag, file_path)
        return
    
        # =====  DELETE REPOSITORIES =====

    if command == "delete":
        repo_name = sys.argv[2]
        delete_remote_repo(repo_name)
        return

    if command == "delete-local":
        repo_name = sys.argv[2]
        delete_local_repo(repo_name)
        return

    if command == "delete-full":
        repo_name = sys.argv[2]
        delete_full(repo_name)
        return



    # ===== Unknown command =====
    print(" Unknown command")
    show_usage()


if __name__ == "__main__":
    main()
