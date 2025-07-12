# test PaletteChip
from PySide6.QtWidgets import QApplication


from palette_chip import PaletteChip
from chip_data import chip_data
from colours import Colours

app = QApplication()
my_chip = PaletteChip()
my_chip.set_properties(chip_data["chip_01"])

print(my_chip.get_row())
print(my_chip.get_column())
print(my_chip.get_parent_chip_a())
print(my_chip.get_parent_chip_b())
print(my_chip.get_fill_priority())

my_chip.set_rgb(Colours["Ultramarine\nBlue"])

colour_tuple = my_chip.get_rgb()
red = colour_tuple[0]
green = colour_tuple[1]
blue = colour_tuple[2]
print(red, green, blue)
