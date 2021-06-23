from kivy.app import App
from kivy.logger import Logger
from kivy.properties import ObjectProperty, ListProperty, ColorProperty
from kivy.event import EventDispatcher
from kivy.clock import Clock


class Theme_Manger(EventDispatcher):

    bg_color = ColorProperty([0, 0, 0])
    """
    Background Color of the app. Only RGB channels to be defined.
    The alpha channel is determined internally for each component.

    :attr:`bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0]`.
    """

    _bg_color_alp = ColorProperty([0, 0, 0, 0])
    """
    Background Color of the app with alpha channel as `1`. This property is used
    internally and is read only. Changing it will lead to unexpected behavior.

    attr:`bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0,0]`.
    """

    _bg_color_noalp = ColorProperty([0, 0, 0, 0])
    """
    Background Color of the app with alpha channel as `0`. This property is used
    internally and is read only. Changing it will lead to unexpected beahvior.

    """

    light_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the lighter shadow for a widget.

    attr:`light_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0,0]`.
    """

    dark_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the darker shadow for a widget.

    attr:`dark_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0,0]`.
    """

    text_color = ColorProperty([1, 1, 1, 1])
    """
    Color of text used in the app.

    attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1,1,1,1]`.
    """

    def on_bg_color(self, *args):
        if len(self.bg_color) > 3:
            Logger.info(
                "NeuKivy:App 'bg_color' alpha channel cannot be set. Ignoring provided alpha channel value"
            )
        self._bg_color_noalp = [self.bg_color[0], self.bg_color[1], self.bg_color[2], 0]
        self._bg_color_alp = [self.bg_color[0], self.bg_color[1], self.bg_color[2], 1]


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
        if self.text_color == [0, 0, 0, 0]:
            self.text_color = self.theme_manager.text_color


class NeuApp(App):

    theme_manager = ObjectProperty()
    """
    Instance of `ThemeableBehavior` that can be used to set app default colors.
    These color values will be set to all widgets provided they do not already have
    their own color properties set. In which case the custom color properties will be
    used for that widget alone
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_manager = Theme_Manger()
