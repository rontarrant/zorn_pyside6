# PaletteChip

from PySide6.QtWidgets import QLabel

class PaletteChip(QLabel):
	def __init__(self):
		super().__init__()
		self.properties = {}

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