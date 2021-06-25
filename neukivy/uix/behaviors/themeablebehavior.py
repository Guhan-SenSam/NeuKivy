from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty


class ThemeableBehavior(EventDispatcher):

    theme_manager = ObjectProperty()
    """
    Theme Manager object that contains all the default color values of the app instance.
    If a widget does not define its own color values it will automatically use the app defaults.
    It is suggested to not customize the color for each component as this will ruin the neumorphic style.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_manager = App.get_running_app().theme_manager
        Clock.schedule_once(self.color_setter, -1)

    def color_setter(self, *args):
        """
        Sets the color properties of a widget to the app defaults if no color properties
        for that widget are provided.
        """
        if self.comp_color == [0, 0, 0, 0]:
            self.comp_color = self.theme_manager._bg_color_alp
        if self.dark_color == [0, 0, 0, 0]:
            self.dark_color = self.theme_manager.dark_color
        if self.light_color == [0, 0, 0, 0]:
            self.light_color = self.theme_manager.light_color
        if hasattr(self, "text_color") and self.text_color == [0, 0, 0, 0]:
            self.text_color = self.theme_manager.text_color
