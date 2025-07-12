from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

app = QApplication(sys.argv)

label = QLabel("Hello, PySide6!")

# Define your RGB tuple
rgb_color = (255, 165, 0) # Orange

# Format the RGB tuple into the CSS-compatible string
color_string = f"rgb({rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]})"

# Set the stylesheet using the formatted string
label.setStyleSheet(f"background-color: {color_string};")

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.show()

sys.exit(app.exec())
