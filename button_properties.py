# button properties

from button_actions import *

button_data = \
{
	###### Row 0 ######
	"New":
	{
		"id": "new",
		"row": 0,
		"column": 0,
		"action": "new",
		"type": "file",
	},
	"Load":
	{
		"id": "load",
		"row": 0,
		"column": 1,
		"action": "load",
		"type": "file",
	},
	"Reload":
	{
		"id": "reload",
		"row": 0,
		"column": 2,
		"action": "reload",
		"type": "file",
	},
	"Save":
	{
		"id": "save",
		"row": 0,
		"column": 3,
		"action": "save",
		"type": "file",
	},
	"Save As...":
	{
		"id": "saveas",
		"row": 0,
		"column": 4,
		"action": "save_as",
		"type": "file",
	},
	"About":
	{
		"id": "about",
		"row": 0,
		"column": 5,
		"action": "about",
		"type": "file",
	},
	"Quit":
	{
		"id": "quit",
		"row": 0,
		"column": 6,
		"action": "quit",
		"type": "file",
	},
	###### Row 1 ######
	"Palette Picker":
	{
		"id": "palette_picker",
		"row": 1,
		"column": 1,
		"action": "pick_palette",
		"type": "combo",
	},
	"Colour 1":
	{
		"id": "colour_01",
		"row": 1,
		"column": 2,
		"action": "set_hue",
		"type": "combo",
	},
	"Colour 2":
	{
		"id": "colour_02",
		"row": 1,
		"column": 6,
		"action": "set_hue",
		"type": "combo",
	},
	"Mix 1":
	{
		"id": "mix_01",
		"row": 3,
		"column": 0,
		"action": "set_tint",
		"type": "combo",
	},
	"Mix 2":
	{
		"id": "mix_02",
		"row": 7,
		"column": 0,
		"action": "set_tint",
		"type": "combo",
	},
}