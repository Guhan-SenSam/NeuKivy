from kivy.core.text import LabelBase
from neukivy import fonts_path

fonts = [
    {
        "name": "Nunito",
        "fn_regular": fonts_path + "NunitoSans-Regular.ttf",
        "fn_bold": fonts_path + "NunitoSans-Bold.ttf",
        "fn_italic": fonts_path + "NunitoSans-Italic.ttf",
        "fn_bolditalic": fonts_path + "NunitoSans-BoldItalic.ttf",
    },
    {
        "name": "NunitoExtraLight",
        "fn_regular": fonts_path + "NunitoSans-ExtraLight.ttf",
        "fn_italic": fonts_path + "NunitoSans-ExtraLightItalic.ttf",
    },
    {
        "name": "NunitoLight",
        "fn_regular": fonts_path + "NunitoSans-Light.ttf",
        "fn_italic": fonts_path + "NunitoSans-LightItalic.ttf",
    },
    {
        "name": "NunitoSemiBold",
        "fn_regular": fonts_path + "NunitoSans-SemiBold.ttf",
        "fn_italic": fonts_path + "NunitoSans-SemiBoldItalic.ttf",
    },
    {
        "name": "NunitoExtraBold",
        "fn_regular": fonts_path + "NunitoSans-ExtraBold.ttf",
        "fn_italic": fonts_path + "NunitoSans-ExtraBoldItalic.ttf",
    },
    {
        "name": "NunitoBlack",
        "fn_regular": fonts_path + "NunitoSans-Black.ttf",
        "fn_italic": fonts_path + "NunitoSans-BlackItalic.ttf",
    },
    {
        "name": "Icons",
        "fn_regular": fonts_path + "materialdesignicons-webfont.ttf",
    },
]

for font in fonts:
    LabelBase.register(**font)
