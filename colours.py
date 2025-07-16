
'''
An expandable dictionary of colours for the ComboBoxes.
For colours to be passed into MixBox's lerp() function,
they need to be available as individual RGB components.
Once the proof of concept works, this dictionary can be
expanded to suit.
'''
Colours = \
{
	"Titanium\nWhite": 			(243, 244, 247),
	"Cadmium\nYellow\nLight": 	(254, 254, 0),
	"Cadmium\nYellow\nMedium":	(255, 206, 25),	
	"Cadmium\nOrange": 			(255, 148, 50),	
	"Cadmium\nRed Light": 		(254, 62, 39),	
	"Quinacridone\nRed": 		(209, 31, 107),	
	"Quinacridone\nMagenta": 	(187, 79, 165),
	"Dioxazine\nPurple": 		(108, 47, 142),
	"Ultramarine\nBlue": 		(36, 72, 150),
	"Phthalo\nBlue": 				(1, 122, 201),
	"Cobalt\nTeal": 				(0, 192, 203),
	"Phthalo\nGreen":				(1, 136, 77),
	"Yellow\nGreen": 				(85, 196, 78),
	"Ivory\nBlack": 				(43, 52, 51),
}

if __name__ == "__main__":
	for key, value in Colours.items():
		print(f"{key}: {value[0]}, {value[1]}, {value[2]}")
