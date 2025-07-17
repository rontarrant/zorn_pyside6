from PySide6.QtWidgets import \
(
	QApplication,
	QMainWindow,
	QGridLayout,
	QWidget,
	QComboBox,
	QMessageBox,
	QLabel,
	QPushButton,
)

from PySide6.QtCore import \
(
	QSettings,
	QByteArray,
	QSize,
)

from icecream import ic
import mixbox

from chip_data import chip_data
from button_properties import button_data

#colours palettes we work with
from winsor_newton_oils import WinsorNewtonOils
from winsor_newton_acrylics import WinsorNewtonAcrylics
from gamblin_oils import GamblinOils
from williamsburg_oils import WilliamsburgOils
from panpastel_pastels import Panpastel
from tri_art_acrylics import TriArtAcrylics
from kroma_acrylics import KromaAcrylics
from beam_paintstones_watercolours import BeamPaintstonesWatercolours
from liquitex_acrylics import LiquitexAcrylics
from deep_seek_refined import RefinedColours
from mixbox_colours import MixBoxColours

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
	zorn_buttons = []
	palettes = \
	{
		"MixBox Colours": MixBoxColours,
		"Refined\nColours": RefinedColours,
		"Liquitex\nAcrylics": LiquitexAcrylics,
		"Beam\nPaintstones\nWatercolours": BeamPaintstonesWatercolours,
		"Kroma Acrylics": KromaAcrylics,
		"Tri-Art\nAcrylics": TriArtAcrylics,
		"Panpastel\nPastel\nColours": Panpastel,
		"Williamsburg\nOils": WilliamsburgOils,
		"Gamblin\nOils": GamblinOils,
		"Winsor &\nNewton\nAcrylics": WinsorNewtonAcrylics,
		"Winsor &\nNewton\nOils": WinsorNewtonOils,
	}
	

	def __init__(self):
		super().__init__()
		self.setWindowTitle(self.window_title)
		self.resize(self.window_width, self.window_height)
		self.Colours = self.palettes["Refined\nColours"]
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
		#ic()
		self.button_keys = list(button_data.keys())
		colours = list(self.Colours.keys())
		reverse_colours = list(reversed(colours))
		select_colour = "Select\nColour"
		colours.insert(0, select_colour)
		reverse_colours.insert(0, select_colour)
		colour_names = []

		for button_key in self.button_keys:
			properties = button_data[button_key]

			if properties["type"] == "combo":
				button = ZornColourButton()
				button.setFixedSize(QSize(100, 100))
				button.set_properties(properties)

				# attach the callback
				if properties["action"] == "set_hue":
					# colours appear in order for Colour 1 & Colour 2
					colour_names = colours
					#ic(colour_names)
					button.addItems(colour_names)
					# The lambda grabs, then disgards, the boolean usually
					# passed to the callback by connect().
					button.currentTextChanged.connect(lambda text, pointer = button: self.set_colour(pointer, text))
					self.zorn_buttons.append(button)
				elif properties["action"] == "set_tint":
					# colours appear in reverse order for Mix 1 & Mix 2
					colour_names = reverse_colours
					#ic(colour_names)
					button.addItems(colour_names)
					# The lambda grabs, then disgards, the boolean usually
					# passed to the callback by connect().
					button.currentTextChanged.connect(lambda text, pointer = button: self.set_colour(pointer, text))
					self.zorn_buttons.append(button)
				elif properties["action"] == "pick_palette":
					#ic(colour_names)
					button.addItems(self.palettes)
					button.currentTextChanged.connect(lambda text, pointer = button: self.pick_palette(pointer, text))
			else:
				button = QPushButton(button_key)
				# gets the name of the callback function from button properties
				button.clicked.connect(lambda _, p = properties: getattr(self, p["action"])())

			self.grid_layout.addWidget(button, properties["row"], properties["column"])
			self.buttons.append(button)


	def update_colour_list(self, button, new_colour_list):
		# When we clear() the item list, a currentTextChanged signal fires.
		# Because the list is empty, we get an error because the button
		# has no text and therefore, the index string used to pick a new
		# button label is an empty string. To avoid this, we block
		# all signals until we've got the new list in place.
		button.blockSignals(True)
		button.clear()
		button.addItems(new_colour_list)

		if new_colour_list:
			button.setCurrentIndex(0)
		
		button.blockSignals(False)


	def pick_palette(self, button, palette):
		#ic()
		self.Colours = self.palettes[palette]

		for button in self.zorn_buttons:
			#ic(button)
			self.update_colour_list(button, self.Colours)
			self.set_colour(button, "Titanium\nWhite")


	def add_chips(self):
		#ic()
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
		#ic()
		priority_2 = []
		priority_3 = []
		priority_4 = []
		#ic(button, text)

		for chip in self.palette_chips:
			if chip.get_id() == button.get_id():
				chip.set_chip_colour(self.Colours[text])
				chip.set_rgb(self.Colours[text])

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
		ic()


	def load(self):
		ic()


	def reload(self):
		ic()


	def save(self):
		ic()


	def save_as(self):
		ic()

	
	def about(self):
		title = "About the Zorn Palette Tool"
		message = "<H3>The Zorn Palette Tool</H3> \
			<P>Inspired by Anders Zorn's four-colour palette (commonly known as the \
			Zorn Palette) this tool goes a bit beyond. Given any four colours, it \
			will mix them on a Zorn-esque grid, allowing artists to test before \
			committing time, energy, and (perhaps most importantly) the cost of paint \
			to exploring various colour mixes.</P> \
			<P><I><B>Note:</B> This tool simulates </I>subtractive <I> colour mixing and it's \
			close enough to give a reasonable idea of results for real-world paint mixing.</I></P> \
			<P><B>Disclaimer:</B> This application is for amusement only. There are too \
			many factors involved for me (or anyone else) to guarantee the results.</P> \
			<P>To name a few:</P> \
			<UL> \
			<LI>monitor quality,</LI> \
			<LI>ambiant lighting,</LI> \
			<LI>viewing angle,</LI> \
			<LI>mixing ratio,</LI> \
			</UL> \
			<P>Conceived and written by Ron Tarrant</P> \
			<P>Special thanks to Ondřej Jamriška and Šárka Sochorová of Secret Weapons for \
			developing the MixBox library	and making it available for Python programmers."

		dialog = QMessageBox.about(self, title, message)


	def quit(self):
		self.close()


if __name__ == "__main__":
	app = QApplication([]) # no args to pass along
	main_window = MainWindow()
	main_window.show() # PySide6 windows open on the primary monitor by default.
	app.exec()
