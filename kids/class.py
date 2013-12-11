import sys

class Things(object):
	pass
		
class Inanimate(Things):
	pass
		
class Animate(object):
	pass
						
class SideWalks(Inanimate):
	pass

class Animals(Animate):
	def breathe(self):
		print("breathing...")
	def move(self):
		print("moving.....")
	def eat_food(self):
		print("eating...")

class Mammals(Animals):
	def feed_milk(self):
		print("feed young with milk...")
		
class Giraffes(Mammals):
	def eat_leave_from_trees(self):
		self.eat_food();
		print("eat from trees....")
	def dance(self):
		self.move()
		self.move()
		self.move()


g1 = Giraffes()
g1.eat_leave_from_trees()
g1.dance()


