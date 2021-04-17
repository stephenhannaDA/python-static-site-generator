import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
	__delimiter = "^(?:-|\+){3}\s*$"
	__regex = re.compile(__delimiter, re.MULTILINE)

	@classmethod
	def load(cls, string):
		_, fm, content = cls.__regex.split(string, 2)
		load(fm, Loader = FullLoader)
		return cls(metadata, content)

	def Content(metadata, content):
		self.data = metadata
		self.data += {"content":content}

	@property
	def body():
		return self.data["content"]

	@property
	def type(self):
		return self.data["type"] if self.data in type else None

	@type.setter
	def type(self):
		self.data["type"] = type()

	def __getitem__(self, key):
		return self.data[key]

	def __iter__(self):
		return self.data.iter__()

	def __len__(self):
		return len(self.data)

	def __repr__(self):
		data = {}
		return str(data)

	for key, val in self.data.items():
		if key != "content":
			value = data[key]
