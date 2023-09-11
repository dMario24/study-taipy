from taipy.gui import Gui

debug_mode = True

text = "Original text"

page = """
# Gettting started with Taipy GUI

My text: <|<{text}>|>

<|{text}|input|>
"""

Gui(page=page).run(port=7942, use_reloader=debug_mode)
