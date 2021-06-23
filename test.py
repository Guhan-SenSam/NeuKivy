from neukivy.app import NeuApp
from kivy.lang import Builder
from kivy.animation import Animation

kv_string = """
Screen:
    canvas:
        Color:
            rgba:app.theme_manager.bg_color
        Rectangle:
            size:self.size
            pos:self.pos

    NeuButtonRounded:
        id:button
        pos_hint:{'center_x':.7,'center_y':.5}
        text:'NeuKivy'
        text_color:.9,.4,.6,1
        size:200,200

    NeuButtonRounded:
        id:button
        pos_hint:{'center_x':.3,'center_y':.5}
        text:'NeuKivy'
        text_color:.9,.4,.6,1
        size:200,200
        down_elevation:-3
        up_elevation:-2

"""


class MainApp(NeuApp):
    def build(self):
        kv = Builder.load_string(kv_string)
        # Set the app colors at start.
        # The bg_color property should not have an alpha value. This is auto computed
        self.theme_manager.bg_color = (0.2, 0.2, 0.2)
        self.theme_manager.light_color = (0.3, 0.3, 0.3, 1)
        self.theme_manager.dark_color = (0.07, 0.07, 0.07, 1)
        self.theme_manager.text_color = (0.5, 0.4, 0.2, 1)
        return kv


if __name__ == "__main__":
    MainApp().run()
