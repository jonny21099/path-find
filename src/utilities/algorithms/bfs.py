from collections import deque


def run_bfs(grid):
	frontier = deque()
	solution = {}
	visited = set()

	frontier.append(grid.start)
	solution[grid.start] = grid.start


	while len(frontier) > 0:

		x, y = frontier.popleft()

		if (x - 1, y) in grid.path and (x - 1, y) not in visited:
			left_cell = (x - 1, y)
			solution[left_cell] = x, y
			frontier.append(left_cell)
			visited.add(left_cell)

		if (x + 1, y) in grid.path and (x + 1, y) not in visited:
			right_cell = (x + 1, y)
			solution[right_cell] = x, y
			frontier.append(right_cell)
			visited.add(right_cell)

		if (x, y + 1) in grid.path and (x, y + 1) not in visited:
			above_cell = (x, y + 1)
			solution[above_cell] = x, y
			frontier.append(above_cell)
			visited.add(above_cell)

		if (x, y - 1) in grid.path and (x, y - 1) not in visited:
			below_cell = (x, y - 1)
			solution[below_cell] = x, y
			frontier.append(below_cell)
			visited.add(below_cell)


	return find_shortest(grid, solution)


def find_shortest(grid, solution):
	x, y = grid.end
	path_reverse = []
	while (x,y) != grid.start:
		path_reverse.append((x, y))
		x, y = solution[x,y]

	return path_reverse