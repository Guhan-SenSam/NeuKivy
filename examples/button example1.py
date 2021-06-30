from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from neukivy.app import NeuApp
from kivy.core.window import Window

kv_string = """
Screen:
    canvas:
        Color:
            rgba:app.theme_manager._bg_color_alp
        Rectangle:
            size:self.size
            pos:self.pos

    Label:
        size:self.size
        size_hint:None,None
        font_size:'40sp'
        text:'NeuKivy Buttons'
        pos_hint:{'center_y':.9, 'center_x':.5}
        color:app.theme_manager.text_color


    GridLayout:
        cols:3
        size:self.minimum_size
        padding:'40dp','40dp','40dp','40dp'
        pos_hint:{'center_y':.5}

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                size:150,150
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color
        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuRoundedButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                size:150,150
            Label:
                text:'NeuRoundedButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuCircularButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                radius:150
            Label:
                text:'NeuCircularButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuIconButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                icon:'cog'
                size:150,150
                font_size:'25sp'
            Label:
                text:'NeuIconButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuRoundedIconButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                icon:'cog'
                size:150,150
                font_size:'25sp'
            Label:
                text:'NeuRoundedIconButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuCircularIconButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                icon:'cog'
                radius:150
                font_size:'25sp'
            Label:
                text:'NeuCircularIconButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color


"""


class MainApp(NeuApp):
    def build(self):
        self.use_kivymd = True
        kv = Builder.load_string(kv_string)
        self.theme_manager.bg_color = (0.8, 0.8, 0.85)
        self.theme_manager.light_color = (0.9, 0.9, 0.95, 1)
        self.theme_manager.dark_color = (0.6, 0.6, 0.65, 1)
        self.theme_manager.text_color = (0.5, 0.2, 0.9, 1)
        return kv


if __name__ == "__main__":
    MainApp().run()
