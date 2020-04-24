import operator

class Cell():
	
	def __init__(self, parent, coords, grid):
		self.parent = parent
		self.location = coords
		self.grid = grid

		self.g = self.calculate_g()
		self.h = self.calculate_h()

	def calculate_g():
		return tuple(map(operator.sub, self.grid.start, self.location))

	def calculate_h():
		pass

def run_a_star(grid):
	open_list = []
	closed_list =[]
	open_list.append(grid.start)

	while len(open_list) > 0:
