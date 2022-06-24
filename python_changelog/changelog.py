from pathlib import Path
import re
from unittest import skip

tag_regex = re.compile(r"\[[0-9]+\.[0-9]+.[0-9]+\]")

def read_file(path):
	"""
	Read a file from a path and return lines as a generator
	"""
	changelog_path = Path(path)
	if not changelog_path.exists():
		print(f"{path} not found")
		return None

	with open(changelog_path, "r") as changelog_file:
		for line in changelog_file.readlines():
			yield line

def get_changelog_of_latest_tag(path):
	latest_tag = None
	changelog = ""
	changelog_started = False

	for line in read_file(path):
		if line == None:
			skip
		
		tag = re.search(tag_regex, line)

		a_new_tag = tag and changelog_started
		link_section_starting = line.startswith('[')
	
		if a_new_tag or link_section_starting:
			break
		elif tag:
			changelog_started = True
			latest_tag = tag[0][1:-1] if latest_tag == None else latest_tag
		elif changelog_started:
			changelog += replace_h3_with_h1(line)

	return latest_tag, changelog.strip('\n')

def replace_h3_with_h1(line):
    re.sub('^###', '#', line)
