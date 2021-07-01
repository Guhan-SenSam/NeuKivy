from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from neukivy.app import NeuApp

kv_string = """
Screen:
    canvas:
        Color:
            rgba:app.theme_manager._bg_color_alp
        Rectangle:
            size:self.size
            pos:self.pos

    Label:
        text:'NeuSlider'
        pos_hint:{'center_x':.5,'center_y':.94}
        font_size:'30sp'
        font_name:'NunitoLight'

    NeuSlider:
        pos_hint:{'center_x':.5,'center_y':.8}
        elevation:2
        border_width:10
        thumb_color:0.9,.3,.3,1

    NeuSlider:
        pos_hint:{'center_x':.5,'center_y':.6}
        elevation:-2
        border_width:10
        thumb_color:0.8,.4,.1,1

    NeuSlider:
        pos_hint:{'center_x':.5,'center_y':.4}
        elevation:-2
        border_width:10
        thumb_color:0.2,0.9,.2,1
        thumb_padding:20

    NeuSlider:
        pos_hint:{'center_x':.5,'center_y':.2}
        elevation:-2
        border_width:5
        thumb_color:0.4,.4,.9,1
        height:dp(20)







"""


class MainApp(NeuApp):
    def build(self):
        self.use_kivymd = True
        self.kv = Builder.load_string(kv_string)
        self.theme_manager.bg_color = (0.2, 0.2, 0.2)
        self.theme_manager.light_color = (0.3, 0.3, 0.3, 1)
        self.theme_manager.dark_color = (0.1, 0.1, 0.1, 1)
        self.theme_manager.text_color = (0.5, 0.2, 0.9, 1)
        return self.kv


if __name__ == "__main__":
    MainApp().run()
