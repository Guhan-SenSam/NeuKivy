from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.graphics.texture import Texture
from PIL import Image, ImageDraw, ImageFilter
from neukivy.tools.colorconvertor import dec_2_rgb
from kivy.graphics import *


class NeuMorphRoundedRectangle:

    blank_texture = ObjectProperty(None)

    dark_shadow = ObjectProperty(None)
    dark_shadow_pos = ListProperty([0, 0])
    dark_shadow_size = ListProperty([0, 0])

    light_shadow = ObjectProperty(None)
    light_shadow_pos = ListProperty([0, 0])
    light_shadow_size = ListProperty([0, 0])

    increment = NumericProperty(0)
    elevation = NumericProperty(0)
    elevation_data = {
        0: 0,
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
    }

    pixel_depth = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(NeuMorphRoundedRectangle, self).__init__(*args, **kwargs)
        self.blank_texture = Texture.create(size=self.size, colorfmt="rgba")
        self._create_shadow()

    def _create_shadow(self, *args):
        if self.pixel_depth == 0:
            self.dark_shadow = self.blank_texture
            self.light_shadow = self.blank_texture
            return
        self.increment = self.pixel_depth / 2.5
        # Create dark_shadow
        self.dark_shadow = self._outer_shadow_gen(
            self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
        )
        self.dark_shadow_size = (
            self.width + self.pixel_depth,
            self.height + self.pixel_depth,
        )
        self.dark_shadow_pos = (
            self.x - self.increment,
            self.y - self.pixel_depth / 2 - self.increment,
        )
        # Create light shadow
        self.light_shadow = self._outer_shadow_gen(
            self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
        )
        self.light_shadow_size = (
            self.width + self.pixel_depth,
            self.height + self.pixel_depth,
        )
        self.light_shadow_pos = (
            self.x - self.pixel_depth / 2 - self.increment,
            self.y - self.increment,
        )

    def _outer_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=(tuple(dec_2_rgb(self.theme_manager.bg_color))),
        )
        # Convert to drawable image
        blank_draw = ImageDraw.Draw(shadow)
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.rounded_rectangle(
            [(x0, y0), (x1, y1)], radius=self.radius, fill=tuple(color)
        )
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment))
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def on_size(self, *args, **kwargs):
        self._create_shadow()

    def on_pos(self, *args, **kwargs):
        self._create_shadow()

    def on_elevation(self, instance, value):
        if value < 0:
            raise ValueError("Widget elevation cannot be negative")
        if not abs(value) <= 5:
            raise ValueError("Widget elevation cannot be greater than 5")
        self.pixel_depth = self.elevation_to_pixels(value)
        self._create_shadow()

    def elevation_to_pixels(self, elevation):
        return self.elevation_data[elevation]


class NeuMorphRoundedRectangleEmboss:

    blank_texture = ObjectProperty(None)

    dark_shadow = ObjectProperty(None)
    dark_shadow_pos = ListProperty([0, 0])
    dark_shadow_size = ListProperty([0, 0])

    light_shadow = ObjectProperty(None)
    light_shadow_pos = ListProperty([0, 0])
    light_shadow_size = ListProperty([0, 0])

    outline = ObjectProperty(None)

    increment = NumericProperty(0)
    elevation = NumericProperty(0)
    elevation_data = {
        0: 0,
        -1: 10,
        -2: 20,
        -3: 30,
        -4: 40,
        -5: 50,
    }

    pixel_depth = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(NeuMorphRoundedRectangleEmboss, self).__init__(*args, **kwargs)
        self.blank_texture = Texture.create(size=self.size, colorfmt="rgba")
        self._create_shadow()

    def _create_shadow(self, *args):
        if self.pixel_depth == 0:
            self.dark_shadow = self.blank_texture
            self.light_shadow = self.blank_texture
            return
        self.increment = self.pixel_depth / 2.5
        # Create widget outline
        self.outline = self.widget_outline(
            self.width, self.height, self.pixel_depth, dec_2_rgb(self.comp_color)
        )
        # Create dark_shadow
        self.dark_shadow = self._inner_shadow_gen(
            self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
        )
        self.dark_shadow_size = (
            self.width + self.pixel_depth,
            self.height + self.pixel_depth,
        )
        self.dark_shadow_pos = (
            self.x - self.pixel_depth / 2 + self.increment / 2,
            self.y - self.pixel_depth / 2 - self.increment / 2,
        )
        # Create light shadow
        self.light_shadow = self._inner_shadow_gen(
            self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
        )
        self.light_shadow_size = (
            self.width + self.pixel_depth,
            self.height + self.pixel_depth,
        )
        self.light_shadow_pos = (
            self.x - self.pixel_depth / 2 - self.increment / 2,
            self.y - self.pixel_depth / 2 + self.increment / 2,
        )

    def widget_outline(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        outline = Image.new(
            "RGBA",
            (size_x, size_y),
            color=tuple(dec_2_rgb(self.bg_color)),
        )
        blank_draw = ImageDraw.Draw(outline)
        x0, y0 = 0, 0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.rounded_rectangle(
            [(x0, y0), (x1, y1)],
            radius=self.radius,
            outline=tuple(color),
            width=10,
        )
        texture = Texture.create(size=(size_x, size_y), colorfmt="rgba")
        texture.blit_buffer(outline.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def _inner_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=(50, 50, 50, 0),
        )
        blank_draw = ImageDraw.Draw(shadow)
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = size_x + self.pixel_depth / 2, size_y + self.pixel_depth / 2
        blank_draw.rounded_rectangle(
            [(x0, y0), (x1, y1)],
            radius=self.radius,
            outline=tuple(color),
            width=(int(self.increment)),
        )
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment / 2))
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def on_size(self, *args, **kwargs):
        self._create_shadow()

    def on_pos(self, *args, **kwargs):
        self._create_shadow()

    def on_elevation(self, instance, value):
        if value > 0:
            raise ValueError("Widget elevation cannot be positive")
        if not abs(value) <= 5:
            raise ValueError("Widget elevation cannot be greater than 5")
        self.pixel_depth = self.elevation_to_pixels(value)
        self._create_shadow()

    def elevation_to_pixels(self, elevation):
        return self.elevation_data[elevation]
