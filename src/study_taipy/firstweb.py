from taipy.gui import Gui, notify
import pandas as pd

debug_mode = True

text = "Original text"

page = """
# Gettting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|Run local|button|on_action=on_button_action|>

### chart 0
<|{list_to_display}|chart|>

### chat 1
<|{data_1}|chart|x=x_col|y=y_col1|>

### chart 2
<|{data_2}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|>

### chart 3
<|{data_3}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|color[1]=green|>

### chart 4
<|{data_4}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|type[1]=bar|>

### dataframe
<|{dataframe}|table|>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>
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

data_1 = {"x_col": [0, 1, 2], "y_col1": [4, 1, 2]}

data_2 = {"x_col": [0, 1, 2], "y_col_1": [4, 2, 1], "y_col_2": [3, 1, 2]}

data_3 = {"x_col": [0, 1, 2], "y_col_1": [4, 2, 1], "y_col_2": [3, 1, 2]}

data_4 = {"x_col": [0, 1, 2], "y_col_1": [4, 1, 2], "y_col_2": [3, 1, 2]}

dataframe = pd.DataFrame({"Text": ['Test', 'Other', 'Love'],
                          "Score Pos": [1, 1, 4],
                          "Score Neu": [2, 3, 1],
                          "Score Neg": [1, 2, 0],
                          "Overall": [0, -1, 4]})


Gui(page=page).run(port=7942, use_reloader=debug_mode)
