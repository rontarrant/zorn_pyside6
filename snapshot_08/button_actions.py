# button_actions.py
#from palette_chip import PaletteChip

def new(window):
	print("New", window)

def load(window):
	print("Load", window)

def reload(window):
	print("Reload", window)

def save(window):
	print("Save", window)

def save_as(window):
	print("Save as...", window)

def quit(window):
	print("Quit", window)
	window.close()

def set_colour(chip, colour_1, colour_2, mix_1, mix_2):
	print("Set colour on ", chip)

