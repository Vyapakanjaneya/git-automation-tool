
# Git Automation Tool

A powerful and modular Python-based GitHub Automation Tool that simplifies repository management, issue tracking, documentation updates, versioning, backup, releases, and even backdated commits.
Designed to automate repetitive GitHub tasks and boost productivity.

## Features
### Repository Management

Create new GitHub repositories

Initialize and push local repos automatically

Delete GitHub repo (safe mode with confirmation)

Delete local repo folder

Full delete (remote + local)

### Issue Automation

Create issues

Comment on issues

Close issues

Add labels

List issues

### Backup System

Clone all GitHub repositories into a /backup folder

Create ZIP archives of all backups

### Repository Statistics

Stars, forks, watchers

Open issues count

Contributors count

Repo size

License

Last updated timestamp

Safe commit counting (supports empty repos)

### Documentation Automation

Auto-generate CHANGELOG.md

Auto-update README.md from a template

### Versioning System

Bump version: major | minor | patch

Auto-update version file

Sync README with new version

### Code Formatter

Format Python code using Black

### Release Automation

Create GitHub releases

Auto-create tags

Upload release assets
### Backdated Commits

Create commits using any custom past date, e.g.:

2025-07-14 10:00:00


#### Useful for:

Reconstructing project history

Organizing commits

Adjusting development timelines

## Installation
### Clone the project:

git clone https://github.com/<your-username>/git-automation-tool.git
cd git-automation-tool


### Install dependencies:

pip install -r requirements.txt


Add your GitHub credentials to config.json:

{
    "username": "YOUR_GITHUB_USERNAME",
    "token": "YOUR_GITHUB_TOKEN"
}


 Your token must include repo and delete_repo permissions.

## Usage Guide

Below are all commands supported by this tool.

#### Create Repository
python cli.py create <repo-name>

#### Issue Commands
##### Create issue	
python cli.py issue-create <repo> <title>

##### Comment on issue	
python cli.py issue-comment <repo> <num> <comment>

##### Close issue
python cli.py issue-close <repo> <num>
##### Add label
python cli.py issue-label <repo> <num> <label>
##### List issues	
python cli.py issue-list <repo>
#### Backup Commands
python cli.py backup
python cli.py backup-zip

#### Repository Statistics
python cli.py stats <repo>
python cli.py stats-all

#### Documentation
python cli.py changelog <repo>
python cli.py update-readme <repo>

#### Versioning
python cli.py bump-version <repo> <major|minor|patch>

#### Code Formatting
python cli.py format <repo>

#### Backdated Commit
python cli.py backdate <repo> "<message>" "YYYY-MM-DD HH:MM:SS"


Example:

python cli.py backdate myproject "Initial upload" "2025-1-4 9:00:00"

#### Releases

##### Create release
python cli.py release <repo> <tag> <title> <desc>
##### Upload file to release
python cli.py upload-asset <repo> <tag> <file>

Repository Deletion

##### Delete remote repo
python cli.py delete <repo>
##### Delete local folder
python cli.py delete-local <repo>
##### Delete both	
python cli.py delete-full <repo>

Each command will ask for confirmation before deleting anything.

### Requirements

Python 3.10+

Git installed

GitHub token with access: repo, delete_repo

Internet connection

Black formatter (optional but recommended)

## Author

Vyapakanjaneya
Git Automation Tool — built to automate workflows and save time.
