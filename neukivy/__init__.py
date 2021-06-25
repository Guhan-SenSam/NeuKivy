import os
import kivy


kivy.require("2.0.0")

path = os.path.dirname(__file__)
"""Path to NeuKivy package directory."""

fonts_path = os.path.join(path, f"fonts{os.sep}")
"""Path to fonts directory."""


import neukivy.factory_registers  # NOQA
import neukivy.font_definitions  # NOQA
