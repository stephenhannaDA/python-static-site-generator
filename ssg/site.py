from pathlib import Path

class Site():
	def init(self, source, dest):
		self.source = Path(source)
		self.dest = Path(dest)

	def create_dir(self, path):
		directory = self.dest/relative_to(path)
		mkdir(directory, parents=True, exist_ok=True)

	def build():
		mkdir(self.dest, parents=True, exist_ok=True)
		for path self.source.rglob("*"):
			if isdir(path):
				create_dir(path)
			


