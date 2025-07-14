import os

def read_version(repo_name):
    version_file = f"{repo_name}/VERSION"

    if not os.path.exists(version_file):
        return "0.1.0"

    with open(version_file, "r") as f:
        return f.read().strip()


def write_version(repo_name, version):
    with open(f"{repo_name}/VERSION", "w") as f:
        f.write(version)


def bump_version(repo_name, part):
    """Bump version: major | minor | patch."""
    version = read_version(repo_name)
    major, minor, patch = map(int, version.split("."))

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1

    new_version = f"{major}.{minor}.{patch}"
    write_version(repo_name, new_version)

    print(f" Version bumped: {version} → {new_version}")
    return new_version
