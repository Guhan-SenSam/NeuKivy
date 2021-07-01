from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.properties import ColorProperty, ListProperty, NumericProperty, ObjectProperty
from neukivy.tools.colorconvertor import dec_2_rgb
from PIL import Image, ImageDraw, ImageFilter


class NeuGlowCircular:

    glow_radius = NumericProperty(0)
    """
    Radius of the glow

    attr:`glow_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    color = ColorProperty([0, 0, 0, 0])
    """
    Color of the glow. It is suggested to set this property to the color of the
    component that the glow is being added to

    attr:`color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    behind_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the component behind the glow. If left blank it will result in
    a black ring around your glow, so make sure you set this color properly

    attr:`behind_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    glow_texture = ObjectProperty()
    """
    The property that holds the actual glow texture object

    """

    glow_size = ListProperty([0, 0])
    """
    A list containing the size of the glow texture
    """

    glow_pos = ListProperty([0, 0])
    """
    A list containing the position of the glow texture
    """

    def __init__(self, *args, **kwargs):
        super(NeuGlowCircular, self).__init__(*args, **kwargs)
        self.blank_texture = Texture.create(size=self.size, colorfmt="rgba")
        Clock.schedule_once(self._create_glow)

    def _create_glow(self, *args):
        # Create blank image
        blank_x_size = int(self.size[0] + self.glow_radius * 2)
        blank_y_size = int(self.size[1] + self.glow_radius * 2)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=(tuple(dec_2_rgb(self.behind_color))),
        )
        # Convert to drawable image
        blank_draw = ImageDraw.Draw(shadow)
        x0, y0 = (blank_x_size - self.size[0]) / 2.0, (
            blank_y_size - self.size[1]
        ) / 2.0
        x1, y1 = x0 + self.size[0], y0 + self.size[1]
        blank_draw.ellipse(
            [(x0, y0), (x1, y1)],
            fill=tuple(tuple(dec_2_rgb(self.glow_color))),
        )
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.glow_radius / 2))
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        self.glow_texture = texture
        self.glow_size = (blank_x_size, blank_y_size)
        self.glow_pos = self.pos[0] - x0, self.pos[1] - y0

    def _update_glow_pos(self):
        self.glow_pos = self.pos[0] - self.glow_radius, self.pos[1] - self.glow_radius

    def on_size(self, *args):
        self._create_glow()

    def on_pos(self, *args):
        self._update_glow_pos()

    def on_glow_radius(self, *args):
        self._create_glow()
