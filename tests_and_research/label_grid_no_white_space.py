from PySide6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QSizePolicy
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import sys
from colours import Colours

app = QApplication(sys.argv)

main_window = QWidget()
grid_layout = QGridLayout(main_window) # Set main_window as parent of the layout

# Remove spacing between cells and margins around the grid
grid_layout.setSpacing(0)
grid_layout.setContentsMargins(0, 0, 0, 0)

index = 0
colours_list = list(Colours.values())

# Create and add labels
for row in range(3):
	for col in range(3):
		label = QLabel()
		
		# Set fixed size for each label
		label.setFixedSize(100, 100) 
		
		# Set background color using RGB tuple
		r = (row * 80) % 256
		g = (col * 80) % 256
		b = ((row + col) * 40) % 256
		colour_value = colours_list[index]
		colour = f"rgb({colour_value[0]}, {colour_value[1]}, {colour_value[2]})"
		#colour = f"rgb({r}, {g}, {b})"
		label.setStyleSheet(f"background-color: {colour};")
		
		# Center the text within the 100x100 label
		label.setAlignment(Qt.AlignCenter)

		grid_layout.addWidget(label, row, col)
		index += 1


main_window.setLayout(grid_layout) # This line is often redundant if layout is created with parent
main_window.show()

sys.exit(app.exec())