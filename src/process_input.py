from src.utilities.algorithms.bfs import run_bfs
from src.utilities.algorithms.a_star import run_a_star

def driver(array):
	# TODO: Check errors

	grid = Grid(array)
	arr = run_a_star(grid)
	print(arr)


class Grid():

	def __init__(self, array):
		self.grid = array
		self.height = len(array) - 1
		self.width = len(array[0]) - 1
		self.start = ()
		self.end = ()
		self.walls = []
		self.path = []

		self.analyze_grid()



	def analyze_grid(self):
		for i, row in enumerate(self.grid):
			for j, column in enumerate(row):
				if column == 1:
					self.start = (i, j)

				elif column == 2:
					self.end = (i, j)
					self.path.append((i,j))

				elif column == 0:
					self.path.append((i,j))

				elif column == 3:
					self.walls.append((i,j))


