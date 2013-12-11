import copy
class Animal(object):
	"""docstring for Animal"""
	def __init__(self, legs, color):
		self.legs = legs
		self.color = color

cow = Animal(4, "yellow")
cow_alias = copy.copy(cow)
print(cow)
print(cow_alias)		