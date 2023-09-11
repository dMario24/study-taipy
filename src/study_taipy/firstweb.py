from taipy.gui import Gui, notify

debug_mode = True

text = "Original text"

page = """
# Gettting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|Run local|button|on_action=on_button_action|>

<|{list_to_display}|chart|>
"""


def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"


def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return


# Step4: Charts
list_to_display = [100/x for x in range(1, 100)]

Gui(page=page).run(port=7942, use_reloader=debug_mode)
