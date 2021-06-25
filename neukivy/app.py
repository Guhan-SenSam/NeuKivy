from kivy.app import App
from kivy.event import EventDispatcher
from kivy.logger import Logger
from kivy.properties import BooleanProperty, ColorProperty, ListProperty, ObjectProperty
from neukivy.kivymdconfig import factory_register
from neukivy.uix.behaviors.themeablebehavior import ThemeableBehavior


class Theme_Manger(EventDispatcher):

    bg_color = ListProperty([0, 0, 0])
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

    primary_color = ColorProperty([0, 0, 0, 0])
    """
    The primary color of your app. Will be used in various parts of the ui to add
    contrast

    attr:`primary_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0,0]`.
    """

    text_color = ColorProperty([1, 1, 1, 1])
    """
    Color of text used in the app.

    attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1,1,1,1]`.
    """

    disabled_text_color = ColorProperty([0.2, 0.2, 0.2, 1])
    """
    Color of text if a widget has been disabled

    attr:`disabled_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0.2, 0.2, 0.2, 1]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_bg_color(self, *args):
        if len(self.bg_color) > 3:
            Logger.info(
                "NeuKivy:'bg_color' alpha channel cannot be set. Ignoring provided alpha channel value"
            )
        self._bg_color_noalp = [self.bg_color[0], self.bg_color[1], self.bg_color[2], 0]
        self._bg_color_alp = [self.bg_color[0], self.bg_color[1], self.bg_color[2], 1]


class NeuApp(App):

    theme_manager = ObjectProperty()
    """
    Instance of `ThemeableBehavior` that can be used to set app default colors.
    These color values will be set to all widgets provided they do not already have
    their own color properties set. In which case the custom color properties will be
    used for that widget alone
    """

    use_kivymd = BooleanProperty(False)
    """
    If set to `True` you can use KivyMD widgets inside NeuKivy. This is useful as the entire ui
    of an app cannot consist of neumorphic widgets. This property enables you to use material
    design widgets provided in KivyMD.
    Check KivyMD documentation here
    (https://kivymd.readthedocs.io/en/latest/)
    """

    theme_cls = ObjectProperty()
    """
    This property is used in order to allow KivyMD widgets to work within NeuKivy.
    It allows you to access all the color definitions and theme support available
    inside KivyMD. Remember `theme_manager` is used to set colors for all NeuKivy widgets
    whereas the colors for KivyMD widgets are controlled by the `theme_cls`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_manager = Theme_Manger()

    def on_use_kivymd(self, *args):
        if self.use_kivymd:
            # Check to see if kivymd is installed
            try:
                import kivymd
            except ImportError:

                raise ImportError(
                    """Please install kivymd before using it in your application"""
                )
            factory_register()
            from kivymd.theming import ThemeManager

            self.theme_cls = ThemeManager()
