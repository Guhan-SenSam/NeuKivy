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
        cols:4
        size:self.minimum_size
        padding:'40dp','40dp','40dp','40dp'
        pos_hint:{'center_y':.5}

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'right'
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color
        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'left'
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'top'
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color
        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'bottom'
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuRoundedIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'right'
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuRoundedIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'left'
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color

        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuRoundedIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'bottom'
            Label:
                text:'NeuButton'
                size:self.texture_size
                size_hint:None,None
                pos_hint:{'center_x':.5}
                color:app.theme_manager.text_color


        BoxLayout:
            orientation:'vertical'
            spacing:'20dp'
            NeuRoundedIconTextButton:
                pos_hint:{'center_x':.5}
                up_elevation:2
                text:'NeuKivy'
                icon:'plus'
                size:150,150
                icon_pos:'top'
            Label:
                text:'NeuButton'
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
