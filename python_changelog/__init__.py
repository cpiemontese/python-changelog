__version__ = "0.1.0"

from python_changelog.changelog import bump_changelog, get_changelog_of_latest_tag


def main():
    print(bump_changelog("CHANGELOG.md", "1.0.0", "1.0.1"))
