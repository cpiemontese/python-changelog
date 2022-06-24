from pathlib import Path
from python_changelog import __version__, changelog as c


def test_version():
    assert __version__ == '0.1.0'

def test_find_latest_tag():
    assert c.find_latest_tag("Non existing changelog.md") == None
    assert c.find_latest_tag(Path("tests/fixtures/empty_changelog.md")) == None
    assert c.find_latest_tag(Path("tests/fixtures/changelog_with_unreleased_and_version.md")) == "0.1.0"
    assert c.find_latest_tag(Path("tests/fixtures/changelog_with_one_version.md")) == "0.1.0"
    assert c.find_latest_tag(Path("tests/fixtures/changelog_with_multiple_versions.md")) == "0.2.0"
