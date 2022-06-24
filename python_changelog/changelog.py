from pathlib import Path
import re


def read_changelog(path):
	"""
	Test doc
	"""
	changelog_path = Path(path)
	if not changelog_path.exists():
		print(f"{path} not found")
		return None

	with open(changelog_path, "r") as changelog_file:
		for line in changelog_file.readlines():
			yield line

def find_latest_tag(path="CHANGELOG.md"):
	found = False
	for line in read_changelog(path):
		if line == None:
			return None
		
		tag = re.search("\[[0-9]+\.[0-9]+.[0-9]+\]", line)
		if tag:
			found = True
			return tag[0][1:-1]

	if not found:
		print("Could not find latest tag")
