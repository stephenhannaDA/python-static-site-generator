import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
	__delimiter = "^(?:-|\+){3}\s*$"
	__regex = re.compile(__delimiter, re.MULTILINE)

	@classmethod
	def load(cls, string):
		_, fm, content = split(__regex, string, 2)
		load(fm, Loader = FullLoader)
		return cls(metadata, content)

	def Content(metadata, content):
		self.data = metadata
		self.data += {"content":content}

	@property
	def body():
		return self.data["content"]

	@property
	def type():
		return self.data["type"] if self.data in type else None

	def setter():
		self.data["type"] = type()

	def __getitem__(key):
		return self.data[key]

	def __iter__():
		return self.data.iter__()

	def __len__():
		return len(self.data)

	def __repr__():
		data = {}
		return str(data)

	for key, val in self.data.items():
		if key != "content":
			value = data[key]
