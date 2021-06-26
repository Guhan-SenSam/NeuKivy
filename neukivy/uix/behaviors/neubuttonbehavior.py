from kivy.clock import Clock
from kivy.properties import BooleanProperty, NumericProperty


class NeuButtonBehavior:

    up_elevation = NumericProperty(3)
    """
    Elevation level when the button is in the up state.

    attr:`up_elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `3`.
    """

    down_elevation = NumericProperty(1)
    """
    Elevation level when the button is in the down state.

    attr:`down_elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    pressed = BooleanProperty(False)
    """
    Read only property that represents if the button is pressed or not.

    attr:`pressed` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    do_text_shrink = BooleanProperty(True)
    """
    When set to `True`, text on a button will shrink when the button is pressed.
    This is done to mimic the effect that the text is going into the screen on press.
    The amount of change in font size can be adjusted using the property `text_shrink_amount`.

    If you have created a custom widget and want to use this effect in a widget. Set the `id`
    value of your text(which is inside the widget) to `label`. The effect will apply to to any
    label with id = 'label'.

    attr:`do_text_shrink` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    text_shrink_amount = NumericProperty(1)
    """
    Amount to decrease the font_size on button press. Will only work if `do_text_shrink` is `True`.
    You can try setting this to a negative value to make the text shrink.
    If `text_shrink_amount = 1` then the font_size will decrease by '1sp'.

    attr:`text_shrink_amount` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    disabled = BooleanProperty(False)
    """
    Whether the widget has been disabled or not

    attr:`disabled` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_press")
        self.register_event_type("on_release")
        Clock.schedule_once(self.elevation_setter, 0)

    def elevation_setter(self, *args):
        self.elev = self.up_elevation

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.disabled:
            self.pressed = True
            self.elev = self.down_elevation
            self.dispatch("on_press")
            if "label" in self.ids and self.do_text_shrink:
                self.ids.label.font_size = (
                    self.ids.label.font_size - self.text_shrink_amount
                )

    def on_touch_up(self, touch):
        if self.pressed and not self.disabled:
            self.elev = self.up_elevation
            self.pressed = False
            self.dispatch("on_release")
            if "label" in self.ids and self.do_text_shrink:
                self.ids.label.font_size = (
                    self.ids.label.font_size + self.text_shrink_amount
                )

    def on_press(self, *args):
        pass

    def on_release(self, *args):
        pass
