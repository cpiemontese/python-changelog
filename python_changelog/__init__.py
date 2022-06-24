__version__ = '0.1.0'

from python_changelog.changelog import get_changelog_of_latest_tag


def main():
	print(get_changelog_of_latest_tag('CHANGELOG.md'))
