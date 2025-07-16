# palette_chips.py
###### This line doesn't work any more.
# What's happening:
# When the new palette is set, addItems() adds all new
# items to each ComboBox. Because all the text is changing,
# a currentTextChanged signal is fired by all ComboBoxen.
# And that means all chips with fill_priority of '1' are
# refreshed. And because all these chips go to a default
# state, they get the colour to fill themselves from
# "rgb": default and that colour (default) isn't valid
# because the variable 'default' is set to a colour
# from the default palette.
# So, that means we have to either find a way to change the
# value of 'default', keep the chips from refreshing until
# such time as a sane value can be assigned to 'default', or
# something else equally as cool/cute/etc.
from deep_seek_refined import *

default = RefinedColours["Titanium\nWhite"]

chip_data = \
{
	###### row 2 ######
	"colour_01":
	{
		"id": "colour_01",
		"row": 2,
		"column": 2,
		"rgb": default,
		"parent_chip_a": None,
		"parent_chip_b": None,
		"fill_priority": 1,
	},
	"chip_01":
	{
		"id": "chip_01",
		"row": 2,
		"column": 3,
		"rgb": default,
		"parent_chip_a": "colour_01",
		"parent_chip_b": "chip_02",
		"fill_priority": 3,
	},
	"chip_02":
	{
		"id": "chip_02",
		"row": 2,
		"column": 4,
		"rgb": default,
		"parent_chip_a": "colour_01",
		"parent_chip_b": "colour_02",
		"fill_priority": 2,
	},
	"chip_03":
	{
		"id": "chip_03",
		"row": 2,
		"column": 5,
		"rgb": default,
		"parent_chip_a": "chip_02",
		"parent_chip_b": "colour_02",
		"fill_priority": 3,
	},
	"colour_02":
	{
		"id": "colour_02",
		"row": 2,
		"column": 6,
		"rgb": default,
		"parent_chip_a": None,
		"parent_chip_b": None,
		"fill_priority": 1,
	},
	###### row 3 ######
	"mix_01":
	{
		"id": "mix_01",
		"row": 3,
		"column": 1,
		"rgb": default,
		"parent_chip_a": None,
		"parent_chip_b": None,
		"fill_priority": 1,
	},
	"chip_04":
	{
		"id": "chip_04",
		"row": 3,
		"column": 2,
		"rgb": default,
		"parent_chip_a": "mix_01",
		"parent_chip_b": "colour_01",
		"fill_priority": 4,
	},
	"chip_05":
	{
		"id": "chip_05",
		"row": 3,
		"column": 3,
		"rgb": default,
		"parent_chip_a": "mix_01",
		"parent_chip_b": "chip_01",
		"fill_priority": 4,
	},
	"chip_06":
	{
		"id": "chip_06",
		"row": 3,
		"column": 4,
		"rgb": default,
		"parent_chip_a": "mix_01",
		"parent_chip_b": "chip_02",
		"fill_priority": 4,
	},
	"chip_07":
	{
		"id": "chip_07",
		"row": 3,
		"column": 5,
		"rgb": default,
		"parent_chip_a": "mix_01",
		"parent_chip_b": "chip_03",
		"fill_priority": 4,
	},
	"chip_08":
	{
		"id": "chip_08",
		"row": 3,
		"column": 6,
		"rgb": default,
		"parent_chip_a": "mix_01",
		"parent_chip_b": "colour_02",
		"fill_priority": 4,
	},
	###### row 4 ######
	"chip_09":
	{
		"id": "chip_09",
		"row": 4,
		"column": 1,
		"rgb": default,
		"parent_chip_a": "mix_01",
		"parent_chip_b": "chip_15",
		"fill_priority": 3,
	},
	"chip_10":
	{
		"id": "chip_10",
		"row": 4,
		"column": 2,
		"rgb": default,
		"parent_chip_a": "chip_09",
		"parent_chip_b": "colour_01",
		"fill_priority": 4,
	},
	"chip_11":
	{
		"id": "chip_11",
		"row": 4,
		"column": 3,
		"rgb": default,
		"parent_chip_a": "chip_09",
		"parent_chip_b": "chip_01",
		"fill_priority": 4,
	},
	"chip_12":
	{
		"id": "chip_12",
		"row": 4,
		"column": 4,
		"rgb": default,
		"parent_chip_a": "chip_09",
		"parent_chip_b": "chip_02",
		"fill_priority": 4,
	},
	"chip_13":
	{
		"id": "chip_13",
		"row": 4,
		"column": 5,
		"rgb": default,
		"parent_chip_a": "chip_09",
		"parent_chip_b": "chip_03",
		"fill_priority": 4,
	},
	"chip_14":
	{
		"id": "chip_14",
		"row": 4,
		"column": 6,
		"rgb": default,
		"parent_chip_a": "chip_09",
		"parent_chip_b": "colour_02",
		"fill_priority": 4,
	},
	###### row 5 ######
	"chip_15":
	{
		"id": "chip_15",
		"row": 5,
		"column": 1,
		"rgb": default,
		"parent_chip_a": "mix_01",
		"parent_chip_b": "mix_02",
		"fill_priority": 2,
	},
	"chip_16":
	{
		"id": "chip_16",
		"row": 5,
		"column": 2,
		"rgb": default,
		"parent_chip_a": "chip_15",
		"parent_chip_b": "colour_01",
		"fill_priority": 4,
	},
	"chip_17":
	{
		"id": "chip_17",
		"row": 5,
		"column": 3,
		"rgb": default,
		"parent_chip_a": "chip_15",
		"parent_chip_b": "chip_01",
		"fill_priority": 4,
	},
	"chip_18":
	{
		"id": "chip_18",
		"row": 5,
		"column": 4,
		"rgb": default,
		"parent_chip_a": "chip_15",
		"parent_chip_b": "chip_02",
		"fill_priority": 4,
	},
	"chip_19":
	{
		"id": "chip_19",
		"row": 5,
		"column": 5,
		"rgb": default,
		"parent_chip_a": "chip_15",
		"parent_chip_b": "chip_03",
		"fill_priority": 4,
	},
	"chip_20":
	{
		"id": "chip_20",
		"row": 5,
		"column": 6,
		"rgb": default,
		"parent_chip_a": "chip_15",
		"parent_chip_b": "colour_02",
		"fill_priority": 4,
	},
	###### row 6 ######
	"chip_21":
	{
		"id": "chip_21",
		"row": 6,
		"column": 1,
		"rgb": default,
		"parent_chip_a": "chip_15",
		"parent_chip_b": "mix_02",
		"fill_priority": 3,
	},
	"chip_22":
	{
		"id": "chip_22",
		"row": 6,
		"column": 2,
		"rgb": default,
		"parent_chip_a": "chip_21",
		"parent_chip_b": "colour_01",
		"fill_priority": 4,
	},
	"chip_23":
	{
		"id": "chip_23",
		"row": 6,
		"column": 3,
		"rgb": default,
		"parent_chip_a": "chip_21",
		"parent_chip_b": "chip_01",
		"fill_priority": 4,
	},
	"chip_24":
	{
		"id": "chip_24",
		"row": 6,
		"column": 4,
		"rgb": default,
		"parent_chip_a": "chip_21",
		"parent_chip_b": "chip_02",
		"fill_priority": 4,
	},
	"chip_25":
	{
		"id": "chip_25",
		"row": 6,
		"column": 5,
		"rgb": default,
		"parent_chip_a": "chip_21",
		"parent_chip_b": "chip_03",
		"fill_priority": 4,
	},
	"chip_26":
	{
		"id": "chip_26",
		"row": 6,
		"column": 6,
		"rgb": default,
		"parent_chip_a": "chip_21",
		"parent_chip_b": "colour_02",
		"fill_priority": 4,
	},
	###### row 7 ######
	"mix_02":
	{
		"id": "mix_02",
		"row": 7,
		"column": 1,
		"rgb": default,
		"parent_chip_a": None,
		"parent_chip_b": None,
		"fill_priority": 1,
	},
	"chip_27":
	{
		"id": "chip_27",
		"row": 7,
		"column": 2,
		"rgb": default,
		"parent_chip_a": "mix_02",
		"parent_chip_b": "colour_01",
		"fill_priority": 4,
	},
	"chip_28":
	{
		"id": "chip_28",
		"row": 7,
		"column": 3,
		"rgb": default,
		"parent_chip_a": "mix_02",
		"parent_chip_b": "chip_01",
		"fill_priority": 4,
	},
	"chip_29":
	{
		"id": "chip_29",
		"row": 7,
		"column": 4,
		"rgb": default,
		"parent_chip_a": "mix_02",
		"parent_chip_b": "chip_02",
		"fill_priority": 4,
	},
	"chip_30":
	{
		"id": "chip_30",
		"row": 7,
		"column": 5,
		"rgb": default,
		"parent_chip_a": "mix_02",
		"parent_chip_b": "chip_03",
		"fill_priority": 4,
	},
	"chip_31":
	{
		"id": "chip_31",
		"row": 7,
		"column": 6,
		"rgb": default,
		"parent_chip_a": "mix_02",
		"parent_chip_b": "colour_02",
		"fill_priority": 4,
	},
}

if __name__ == "__main__":
	# access all chips by key/value pairs
	for key, value in chip_data.items():
		print(key, value)

	print("\n")

	# access a single chip by key
	print("chip_09: ", chip_data["chip_09"])

	print("\n")

	# show a chip's parent chips
	current_chip = chip_data["chip_04"]
	parent_chip_a = current_chip["parent_chip_a"]
	parent_chip_b = current_chip["parent_chip_b"]
	print("parent_chip_a: ", parent_chip_a, ", parent_chip_b: ", parent_chip_b)

	# show the RGB tuples of a chip's parent chips
	colour_a = chip_data[parent_chip_a]["rgb"]
	colour_b = chip_data[parent_chip_b]["rgb"]
	print("colour_a: ", colour_a, ", colour_b: ", colour_b)

	# show the RGB components for one of a chip's parent chip
	for component in colour_a:
		print("component: ", component)
