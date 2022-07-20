from pathlib import Path
from python_changelog import __version__, changelog as c


def test_version():
    assert __version__ == "0.1.0"


def test_changelog_extraction():
    assert c.get_changelog_of_latest_tag(
        get_file_path("changelog_with_multiple_versions.md")
    ) == ("0.2.0", "Second release 🚀🚀")
    assert c.get_changelog_of_latest_tag(get_file_path("empty_changelog.md")) == (
        None,
        "",
    )
    assert c.get_changelog_of_latest_tag(
        get_file_path("changelog_with_one_version.md")
    ) == ("0.1.0", "First release 🚀")
    assert c.get_changelog_of_latest_tag(get_file_path("changelog_with_links.md")) == (
        "0.2.0",
        "Second release 🚀🚀",
    )
    assert c.get_changelog_of_latest_tag(get_file_path("changelog_with_h1.md")) == (
        "0.1.0",
        "First release 🚀\n\n# Added\n- Mario\n- Luigi\n- Simone ###",
    )


def get_file_path(filename):
    path = Path("tests/fixtures/" + filename)
    print(path)
    return path
