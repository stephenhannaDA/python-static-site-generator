from typing import List
from pathlib import Path
import shutil

class Parser:
	extensions: List[str] = []

	def valid_extension(self, extension):
		return extension in self.extensions

	def parse(self, path, source, dest):
		raise NotImplementedError

	def read(self, path):
		with open(path, 'r') as file:
			return read(file)
	def write(self, path, dest, content, ext=".html"):
		full_path = self.dest / path.with_suffix(ext).name
		with open(full_path, "w") as file:
			write(content, file)

	def copy(self, path, source, dest):
		shutil.copy2(path, dest/path.relative_to(self.source))

class ResourceParser(Parser):
	extensions = [".jpg", ".png", ".gif", ".css", ".html"]


	def parse(path, source, dest):
		copy(path, source, dest)