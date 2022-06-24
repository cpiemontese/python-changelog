from pathlib import Path


def read_changelog(path = "CHANGELOG.md"):
	"""
	Test doc
	"""
	changelog_path = Path(path)
	if not changelog_path.exists():
		print(f"{path} not found")
		exit(-1)

	with open(changelog_path, "r") as changelog_file:
		for line in changelog_file.readlines():
			print(line)
