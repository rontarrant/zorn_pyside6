# button properties

from button_actions import *

button_data = \
{
	###### Row 0 ######
	"New":
	{
		"id": "new",
		"row": 0,
		"column": 1,
		"action": "new",
	},
	"Load":
	{
		"id": "load",
		"row": 0,
		"column": 2,
		"action": "load",
	},
	"Reload":
	{
		"id": "reload",
		"row": 0,
		"column": 3,
		"action": "reload",
	},
	"Save":
	{
		"id": "save",
		"row": 0,
		"column": 4,
		"action": "save",
	},
	"Save As...":
	{
		"id": "saveas",
		"row": 0,
		"column": 5,
		"action": "save_as",
	},
	"Quit":
	{
		"id": "quit",
		"row": 0,
		"column": 6,
		"action": "quit",
	},
	###### Row 1 ######
	"Colour 1":
	{
		"id": "colour_01",
		"row": 1,
		"column": 2,
		"action": "set_colour",
		"type": "hue",
	},
	"Colour 2":
	{
		"id": "colour_02",
		"row": 1,
		"column": 6,
		"action": "set_colour",
		"type": "hue",
	},
	"Mix 1":
	{
		"id": "mix_01",
		"row": 3,
		"column": 0,
		"action": "set_colour",
		"type": "tint",
	},
	"Mix 2":
	{
		"id": "mix_02",
		"row": 7,
		"column": 0,
		"action": "set_colour",
		"type": "tint",
	},
}