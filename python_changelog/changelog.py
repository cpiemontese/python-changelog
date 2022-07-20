import re

from datetime import datetime
from pathlib import Path
from unittest import skip

TAG_REGEX = re.compile(r"\[[0-9]+\.[0-9]+.[0-9]+\]")
CHANGELOG_START_REGEX = re.compile(r"^## \[(Unreleased|Next)")


def read_file(path):
    """
    Read a file from a path and return lines as a generator
    """
    changelog_path = Path(path)
    if not changelog_path.exists():
        print(f"{path} not found")
        return None

    with open(changelog_path) as changelog_file:
        for line in changelog_file.readlines():
            yield line


def bump_changelog(path, previous_version, version):
    file = []
    with open(Path(path), "r+") as changelog:
        file = changelog.readlines()

    with open(Path(path), "w") as changelog:
        added_diff_link = False
        changelog_start = None

        for idx, line in enumerate(file):
            if line == None:
                skip

            # Add new version at the top of the file
            changelog_match = re.search(CHANGELOG_START_REGEX, line)
            if changelog_match is not None:
                changelog_start = extract_changelog_start(changelog_match[0])

                today = datetime.today().strftime("%Y-%m-%d")

                file.insert(idx + 1, "\n")
                file.insert(idx + 1, f"## [{version}] - {today}")
                file.insert(idx + 1, "\n")

            # Add diff links to github
            if not added_diff_link and line.startswith("["):
                added_diff_link = True
                file.pop(idx)
                file.insert(
                    idx,
                    f"[{changelog_start}]: https://github.com/olivierlacan/keep-a-changelog/compare/{version}...HEAD",
                )
                file.insert(idx + 1, "\n")
                file.insert(
                    idx + 2,
                    f"[{version}]: https://github.com/olivierlacan/keep-a-changelog/compare/{previous_version}...{version}",
                )
                file.insert(idx + 3, "\n")

        changelog.writelines(file)


def extract_changelog_start(string_containing_changelog_start: str):
    parts = string_containing_changelog_start.split("[")
    return parts[1]


def get_changelog_of_latest_tag(path):
    latest_tag = None
    changelog = ""
    changelog_started = False

    for (line, _) in read_file(path):
        if line == None:
            skip

        tag = re.search(TAG_REGEX, line)

        a_new_tag = tag and changelog_started
        link_section_starting = line.startswith("[")

        if a_new_tag or link_section_starting:
            break
        elif tag:
            changelog_started = True
            latest_tag = tag[0][1:-1] if latest_tag == None else latest_tag
        elif changelog_started:
            changelog += replace_h3_with_h1(line)

    return latest_tag, changelog.strip("\n")


def replace_h3_with_h1(line):
    return re.sub("^###", "#", line)
