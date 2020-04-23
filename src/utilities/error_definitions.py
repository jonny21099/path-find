# Contains custom error definitions


class Error(Exception):
	# Base class for other exceptions
	pass

class SizeError(Error):
	# Raised when the size of the array is too large or small

	def __init__(self, size):
		print("Error: %s is an incompatible size" % size)
