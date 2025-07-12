# ZornButton
from PySide6.QtWidgets import QComboBox

from button_properties import button_data

class ZornColourButton(QComboBox):
	def __init__(self):
		super().__init__()

		self.properties = {}
		self.setFixedSize(100, 100)
	
	def set_properties(self, properties: dict):
		self.properties = properties

	def get_id(self) -> str:
		return self.properties["id"]
