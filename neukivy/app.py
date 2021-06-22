from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.event import EventDispatcher


class Theme_Manger(EventDispatcher):

    bg_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    text_color = ListProperty([0, 0, 0, 0])


class ThemeableBehavior(EventDispatcher):

    theme_manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_manager = App.get_running_app().theme_manager


class NeuApp(App):

    theme_manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_manager = Theme_Manger()
