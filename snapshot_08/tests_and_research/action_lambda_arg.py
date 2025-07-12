def set_colour(button_id):
    print(f"Setting color for: {button_id}")

buttons_data = \
{
    "Mix 2": {
        "id": "mix_2",
        "row": 3,
        "column": 7,
        "action": None, # Placeholder for the action
    },
    "Mix 3": {
        "id": "mix_3",
        "row": 4,
        "column": 7,
        "action": None,
    },
}

# Assign the lambda function after the dictionary is defined
for key, button_info in buttons_data.items():
    # The 'button_id_val=button_info["id"]' captures the specific ID
    # at the time the lambda is created for each button.
    button_info["action"] = lambda button_id_val=button_info["id"]: set_colour(button_id_val)

# Simulate calling the actions
buttons_data["Mix 2"]["action"]()
buttons_data["Mix 3"]["action"]()

# You can also access it directly if you know the key
# buttons_data["Mix 2"]["action"]()