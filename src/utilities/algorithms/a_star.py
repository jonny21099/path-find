import time

class Cell():
	
	def __init__(self, parent, coords):
		self.parent = parent
		self.location = coords


		self.g = 0
		self.h = 0
		self.f = 0
	
	def __str__(self):
		return "%s" % (self.location,)

	def __repr__(self):
		return "%s" % (self.location,)

	def __eq__(self, other):
		return self.location == other.location

def run_a_star(grid):
	open_list = []
	closed_list = []
	solution = []

	start_cell = Cell(None, grid.start)


	open_list.append(start_cell)

	while len(open_list) > 0:

		current_cell = open_list[0]

		for cell in open_list:
			if cell.f < current_cell.f:
				current_cell = cell

		# print(len(open_list))
		open_list.remove(current_cell)
		# print(len(open_list))
		closed_list.append(current_cell)

		if current_cell.location == grid.end:
			current = current_cell
			while current is not None:
				solution.append(current.location)
				current = current.parent

			return solution[::-1]

		children = []

		for adjacent_cell in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

			cell_location = (current_cell.location[0] + adjacent_cell[0],
				current_cell.location[1] + adjacent_cell[1])

			if cell_location[0] > grid.height or cell_location[0] < 0 or cell_location[1] > grid.width or cell_location[1] < 0 or cell_location in grid.walls:
				continue

			new_cell = Cell(current_cell, cell_location)

			children.append(new_cell)


		for child in children:

			for closed in closed_list:
				if child == closed:
					continue


			child.g = current_cell.g + 1
			# Using Manhattan distance as our Heuristic
			child.h = ((child.location[0] - grid.end[0])) ** 2 + ((child.location[1] - grid.end[1])) ** 2
			child.f = child.g + child.h


			for open_cell in open_list:
				if child == open_cell and child.g > open_cell.g:
					continue


			# if not any(x.location == child.location for x in ):
			open_list.append(child)

			# time.sleep(.7)

	# print(open_list)












