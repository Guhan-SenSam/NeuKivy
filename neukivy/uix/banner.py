from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from neukivy.uix.behaviors.themeablebehavior import ThemeableBehavior
from neukivy.uix.card import NeuCard

Builder.load_string(
    """
#:import Window kivy.core.window.Window
<NeuBanner>:
    size_hint:1,None
    height:self.minimum_height
    y: Window.height - self.height

    NeuCard:
        id:card
        size_hint:1,None
        height:self.minimum_height
        orientation: "vertical"
        spacing: "10dp"
        padding:10,10,10,10
        elevation:root._elevation
        border_width:root.border_width
        comp_color:root.comp_color
        light_color:root.light_color
        dark_color:root.dark_color

        Label:
            id: text
            text_size: self.parent.width-dp(20), None
            size: self.texture_size
            size_hint:None,None
            text:root.text
            pos_hint:{'center_x':.5}
            font_name: root.font_name if root.font_name else 'NunitoBlack'
            color:root.text_color


        BoxLayout:
            id:container
            size_hint: None, None
            size: self.minimum_size
            pos_hint: {"right": 1}
            padding: 0, 0, "10dp",0
            spacing: "10dp"


<NeuBannerAction>:
    size_hint: None, None
    size: self.minimum_size
    pos_hint:{'center_y':.5}

"""
)


class NeuBanner(BoxLayout, ThemeableBehavior):

    text = StringProperty("Banner")
    """
    Text to be displayed in the banner

    attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text_color = ListProperty([0, 0, 0, 0])
    """
    Color of the text

    attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_name = StringProperty()
    """

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'NunitoBlack'`.
    """

    banner_height = NumericProperty("100dp")
    """
    Banner height

    attr:`banner_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `100dp`.
    """

    padding = ListProperty([dp(20), dp(20), dp(20), dp(20)])
    """
    Padding of the BoxLayout that is holding the Banner Card. This property
    will control how much gap should be given around the card to ensure that
    the neumorphic shadow effect is visible

    attr:`padding` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(20), dp(20), dp(20), dp(20)]`.
    """

    over_widget = ObjectProperty()
    """
    Widget that the banner is above. Set this property to the widget that is directly
    underneath the banner. This widget will be moved down when the banner is shown.

    attr:`over_widget` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to None.
    """

    elevation = NumericProperty(3)
    """
    Elevation of the banner. Hint: The widget will look better with a small positive elevation

    attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `3`.
    """

    border_width = NumericProperty(10)
    """
    Border width for negative elevation

    attr:`border_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `10`.
    """

    duration = NumericProperty(0.3)
    """
    Duration of the animations

    attr:`duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.3`.
    """

    interpolation = StringProperty("in_out_circ")
    """
    Interpolation to be used in all animations

    attr:`interpolation` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"in_out_circ"`.
    """

    shown = BooleanProperty(False)
    """
    Read only property that depicts if the banner is shown or not

    attr:`shown` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    opacity = NumericProperty(0)
    """
    Opacity of the banner. Do not chnage this property as it is set internally to show
    and close the banner.
    """

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    _elevation = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_widget(self, widget, *args):
        if widget.__class__ is NeuBannerAction:
            self.ids.container.add_widget(widget)
        else:
            return super().add_widget(widget)

    def show(self, *args):
        if not self.shown:
            anim = Animation(
                y=self.over_widget.y - self.height,
                duration=self.duration,
                t=self.interpolation,
            )
            anim.start(self.over_widget)
            anim.bind(on_complete=self.show_animation)

    def show_animation(self, *args):
        self.shown = True
        self.opacity = 1
        anim = Animation(
            _elevation=self.elevation, duration=self.duration, t=self.interpolation
        )
        anim.start(self)

    def close(self, *args):
        if self.shown:
            anim = Animation(_elevation=0, duration=self.duration, t=self.interpolation)
            anim.start(self)
            anim.bind(on_complete=self.close_animation)

    def close_animation(self, *args):
        self.shown = False
        anim = Animation(
            y=self.over_widget.y + self.height,
            duration=self.duration,
            t=self.interpolation,
        )
        anim.start(self.over_widget)
        Animation(
            opacity=0,
            duration=self.duration,
            t=self.interpolation,
        ).start(self)

    def on_touch_up(self, touch):
        if self.ids.container.collide_point(*touch.pos) and self.shown:
            pass
        elif self.ids.card.collide_point(*touch.pos) and self.shown:
            self.close()


class NeuBannerAction(BoxLayout):
    pass
