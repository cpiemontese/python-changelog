__version__ = '0.1.0'

from python_changelog.changelog import find_latest_tag


def main():
	print(f"Latest tag is: {find_latest_tag()}")
