# PaletteChip
from PySide6.QtWidgets import QLabel

from deep_seek_refined import default

class PaletteChip(QLabel):
	def __init__(self):
		super().__init__()
		self.properties = {}
		self.setFixedSize(100, 100)
		self.set_chip_colour(default)
	

	def set_chip_colour(self, rgb: tuple):
		#print("set_chip_colour", rgb)
		colour = f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})"
		self.setStyleSheet(f"background-color: {colour};")

	def get_id(self):
		return self.properties["id"]
	
	
	def set_properties(self, properties: dict):
		self.properties = properties


	def get_row(self) -> int:
		return self.properties["row"]
	

	def get_column(self) -> int:
		return self.properties["column"]
	

	def get_rgb(self) -> tuple:
		return self.properties["rgb"]
	

	def set_rgb(self, rgb_components: tuple):
		self.properties["rgb"] = rgb_components
	

	def get_parent_chip_a(self) -> str:
		return self.properties["parent_chip_a"]
	

	def get_parent_chip_b(self) -> str:
		return self.properties["parent_chip_b"]
	
	
	def get_fill_priority(self) -> int:
		return self.properties["fill_priority"]

## label.setStyleSheet("background-color: lightblue;")