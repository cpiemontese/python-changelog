from pathlib import Path
from python_changelog import __version__, changelog as c


def test_version():
    assert __version__ == '0.1.0'

def test_find_latest_tag():
    assert c.find_latest_tag(get_file_path("not existing changelog.md")) == None
    assert c.find_latest_tag(get_file_path("empty_changelog.md")) == None
    assert c.find_latest_tag(get_file_path("changelog_with_unreleased_and_version.md")) == "0.1.0"
    assert c.find_latest_tag(get_file_path("changelog_with_one_version.md")) == "0.1.0"
    assert c.find_latest_tag(get_file_path("changelog_with_multiple_versions.md")) == "0.2.0"

def test_changelog_extraction():
    assert c.get_changelog_of_latest_tag(get_file_path("changelog_with_multiple_versions.md")) == ('0.2.0', '\nSecond release 🚀🚀\n\n')
    assert c.get_changelog_of_latest_tag(get_file_path("empty_changelog.md")) == (None, '')
    assert c.get_changelog_of_latest_tag(get_file_path("changelog_with_one_version.md")) == ('0.1.0', '\nFirst release 🚀\n')

def get_file_path(filename):
    return Path("tests/fixtures/"+filename)