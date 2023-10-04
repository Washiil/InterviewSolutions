def __init__(self):
		self.keys = []
		self.values = []

def put(self, key: int, value: int) -> None:
		if key not in self.keys:
				self.keys.append(key)
				self.values.append(value)
		else:
				self.values[self.keys.index(key)] = value

def get(self, key: int) -> int:
		if key in self.keys:
				return self.values[self.keys.index(key)]
		else:
				return -1

def remove(self, key: int) -> None:
		if key in self.keys:
				index = self.keys.index(key)
				self.keys.pop(index)
				self.values.pop(index)