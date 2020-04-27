# Using 0 to represent empty spaces, 1 to represent the starting marker, 
# 2 to represent the end marker and 3 to represent any obstacles
from src.process_input import driver


test_array = [[0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 3, 0, 0, 0],
			  [0, 0, 0, 3, 0, 0, 0],
			  [0, 1, 0, 3, 0, 2, 0],
			  [0, 0, 0, 3, 0, 0, 0],
			  [0, 0, 0, 3, 0, 0, 0],
			  [0, 0, 0, 3, 0, 0, 0]
			 ]

def main():
	driver(test_array)


if __name__ == '__main__':
	main()