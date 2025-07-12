from PySide6.QtWidgets import \
(
	QApplication,
	QMainWindow,
	QGridLayout,
	QWidget,
	QComboBox,
	QLabel,
	QPushButton,
)

from PySide6.QtCore import \
(
	QSettings,
	QByteArray,
	QSize,
)

import mixbox

from chip_data import chip_data
from button_properties import button_data
#import button_actions
from colours import Colours
from palette_chip import PaletteChip
from zorn_button import ZornColourButton

class MainWindow(QMainWindow):
	window_width = 600
	window_height = 700
	window_title = "Zorn Palette"
	central_widget = None
	grid_layout = None
	palette_chips = []
	buttons = []

	def __init__(self):
		super().__init__()
		self.setWindowTitle(self.window_title)
		self.resize(self.window_width, self.window_height)

		self.build_ui()
	

	def build_ui(self):
		# define this first...
		self.grid_layout = QGridLayout()
		self.grid_layout.setSpacing(0)
		self.grid_layout.setContentsMargins(0, 0, 0, 0)

		# so all this can be lumped together
		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)
		self.central_widget.setLayout(self.grid_layout)

		# and build the layout
		self.add_buttons()
		self.add_chips()


	def add_buttons(self):
		self.button_keys = list(button_data.keys())
		colours = list(Colours.keys())
		reverse_colours = list(reversed(colours))
		select_colour = "Select\nColour"
		colours.insert(0, select_colour)
		reverse_colours.insert(0, select_colour)
		colour_names = []

		for button_key in self.button_keys:
			properties = button_data[button_key]
			
			# attach the callback
			if properties["action"] == "set_colour":
				button = ZornColourButton()
				button.setFixedSize(QSize(100, 100))
				button.set_properties(properties)

				# colours appear in order for Colour 1 & Colour 2
				if properties["type"] == "hue":
					colour_names = colours
				# colours appear in reverse order for Mix 1 & Mix 2
				elif properties["type"] == "tint":
					colour_names = reverse_colours
				else:
					pass

				#print(colour_names)
				button.addItems(colour_names)
				# The lambda grabs, then disgards, the boolean usually
				# passed to the callback by connect().
				button.currentTextChanged.connect(lambda text, pointer = button: self.set_colour(pointer, text))
			else:
				button = QPushButton(button_key)
				# gets the name of the callback function from button properties
				button.clicked.connect(lambda _, p = properties: getattr(self, p["action"])())

			self.grid_layout.addWidget(button, properties["row"], properties["column"])
			self.buttons.append(button)

			# set up direction access to the colour-setting combo boxen


	def add_chips(self):
		# Isolate the chip IDs so they can be used
		# for stepping through the list of palette
		# chips when creating them and, later, 
		# updating them.
		chip_ids = list(chip_data.keys())

		# everything we need to create and place the palette chips
		# is in chip_data. We just need to step through using the
		# IDs and grab it.
		for current_chip_id in chip_ids:
			properties = chip_data[current_chip_id]
			chip = PaletteChip()
			chip.set_properties(properties)

			self.grid_layout.addWidget(chip, properties["row"], properties["column"])
			self.palette_chips.append(chip)


	def set_colour(self, button, text):
		priority_2 = []
		priority_3 = []
		priority_4 = []

		for chip in self.palette_chips:
			if chip.get_id() == button.get_id():
				chip.set_chip_colour(Colours[text])
				chip.set_rgb(Colours[text])

		# group chips by fill priority
		for chip in self.palette_chips:
			if chip.get_fill_priority() == 2:
				priority_2.append(chip)
			if chip.get_fill_priority() == 3:
				priority_3.append(chip)
			if chip.get_fill_priority() == 4:
				priority_4.append(chip)
		
		# get the IDs for the parent chips
		# get pointers to the parent chips
		# from the parent chips, get their RGB values
		# pass those RGB values to mixbox
		# start filling
		ratio = 0.5
		for chip in priority_2:
			parent_a_id = chip.get_parent_chip_a()
			parent_b_id = chip.get_parent_chip_b()

			for parent in self.palette_chips:
				if parent.get_id() == parent_a_id:
					colour_a = parent.get_rgb()
				elif parent.get_id() == parent_b_id:
					colour_b = parent.get_rgb()
				else:
					pass

			fill_colour = mixbox.lerp(colour_a, colour_b, ratio)
			chip.set_chip_colour(fill_colour)
			chip.set_rgb(fill_colour)
		
		for chip in priority_3:
			parent_a_id = chip.get_parent_chip_a()
			parent_b_id = chip.get_parent_chip_b()

			for parent in self.palette_chips:
				if parent.get_id() == parent_a_id:
					colour_a = parent.get_rgb()
				elif parent.get_id() == parent_b_id:
					colour_b = parent.get_rgb()
				else:
					pass

			fill_colour = mixbox.lerp(colour_a, colour_b, ratio)
			chip.set_chip_colour(fill_colour)
			chip.set_rgb(fill_colour)

		for chip in priority_4:
			parent_a_id = chip.get_parent_chip_a()
			parent_b_id = chip.get_parent_chip_b()

			for parent in self.palette_chips:
				if parent.get_id() == parent_a_id:
					colour_a = parent.get_rgb()
				elif parent.get_id() == parent_b_id:
					colour_b = parent.get_rgb()
				else:
					pass

			fill_colour = mixbox.lerp(colour_a, colour_b, ratio)
			chip.set_chip_colour(fill_colour)
			chip.set_rgb(fill_colour)


	def new(self):
		print("New")


	def load(self):
		print("Load")


	def reload(self):
		print("Reload")


	def save(self):
		print("Save")


	def save_as(self):
		print("Save as...")


	def quit(self):
		print("Quit")
		self.close()


if __name__ == "__main__":
	app = QApplication([]) # no args to pass along
	main_window = MainWindow()
	main_window.show() # PySide6 windows open on the primary monitor by default.
	app.exec()
