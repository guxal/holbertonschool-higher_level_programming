def magic_string():
	magic_string.c = getattr(magic_string, "c", 0) + 1
	w = "Holberton, " * magic_string.c
	return w[:-2]
