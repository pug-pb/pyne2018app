"""
Module colors to translate from RGB to hexcode to kivy color
Author: hildeberto Magalhães

# inspired from:
# https://www.webucator.com/blog/2015/03/python-color-constants-module/

* New colors could be defined
    - by RGB: NAME = get_color_from_hex(RGB(r, g, b).hex_format())
    - by Hex Code: NAME = get_color_from_hex('#00AAFF')

"""
from collections import namedtuple
from kivy.utils import get_color_from_hex

Color = namedtuple('RGB', 'red, green, blue')


class RGB(Color):
    def hex_format(self):
        """Returns color in hex format"""
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)


# Color Constants

# Most commons
BLACK = get_color_from_hex(RGB(0, 0, 0).hex_format())
WHITE = get_color_from_hex(RGB(255, 255, 255).hex_format())
RED = get_color_from_hex(RGB(255, 0, 0).hex_format())
LIME = get_color_from_hex(RGB(0, 255, 0).hex_format())
BLUE = get_color_from_hex(RGB(0, 0, 255).hex_format())
YELLOW = get_color_from_hex(RGB(255, 255, 0).hex_format())
CYAN = get_color_from_hex(RGB(0, 255, 255).hex_format())
AQUA = get_color_from_hex(RGB(0, 255, 255).hex_format())
MAGENTA = get_color_from_hex(RGB(255, 0, 255).hex_format())
SILVER = get_color_from_hex(RGB(192, 192, 192).hex_format())
GRAY = get_color_from_hex(RGB(128, 128, 128).hex_format())
MAROON = get_color_from_hex(RGB(128, 0, 0).hex_format())
OLIVE = get_color_from_hex(RGB(128, 128, 0).hex_format())
GREEN = get_color_from_hex(RGB(0, 128, 0).hex_format())
PURPLE = get_color_from_hex(RGB(128, 0, 128).hex_format())
TEAL = get_color_from_hex(RGB(0, 128, 128).hex_format())
NAVY = get_color_from_hex(RGB(0, 0, 128).hex_format())

# Many variotions
ALICEBLUE = get_color_from_hex(RGB(240, 248, 255).hex_format())
ANTIQUEWHITE = get_color_from_hex(RGB(250, 235, 215).hex_format())
AQUAMARINE = get_color_from_hex(RGB(127, 255, 212).hex_format())
AQUAMARINE_MEDIUM = get_color_from_hex(RGB(102, 205, 170).hex_format())
AZURE = get_color_from_hex(RGB(240, 255, 255).hex_format())
BANANA = get_color_from_hex(RGB(227, 207, 87).hex_format())
BEIGE = get_color_from_hex(RGB(245, 245, 220).hex_format())
BISQUE = get_color_from_hex(RGB(255, 228, 196).hex_format())
BLANCHEDALMOND = get_color_from_hex(RGB(255, 235, 205).hex_format())
BLUEVIOLET = get_color_from_hex(RGB(138, 43, 226).hex_format())
BRICK = get_color_from_hex(RGB(156, 102, 31).hex_format())
BROWN = get_color_from_hex(RGB(165, 42, 42).hex_format())
BURLYWOOD = get_color_from_hex(RGB(222, 184, 135).hex_format())
CADETBLUE = get_color_from_hex(RGB(95, 158, 160).hex_format())
CADMIUMORANGE = get_color_from_hex(RGB(255, 97, 3).hex_format())
CADMIUMYELLOW = get_color_from_hex(RGB(255, 153, 18).hex_format())
CARROT = get_color_from_hex(RGB(237, 145, 33).hex_format())
CHOCOLATE = get_color_from_hex(RGB(210, 105, 30).hex_format())
COBALT = get_color_from_hex(RGB(61, 89, 171).hex_format())
COBALTGREEN = get_color_from_hex(RGB(61, 145, 64).hex_format())
COLDGREY = get_color_from_hex(RGB(128, 138, 135).hex_format())
CORAL = get_color_from_hex(RGB(255, 127, 80).hex_format())
CORNFLOWERBLUE = get_color_from_hex(RGB(100, 149, 237).hex_format())
CORNSILK1 = get_color_from_hex(RGB(255, 248, 220).hex_format())
CRIMSON = get_color_from_hex(RGB(220, 20, 60).hex_format())
DARKGOLDENROD = get_color_from_hex(RGB(184, 134, 11).hex_format())
DARKGRAY = get_color_from_hex(RGB(169, 169, 169).hex_format())
DARKGREEN = get_color_from_hex(RGB(0, 100, 0).hex_format())
DARKRED = get_color_from_hex(RGB(139, 0, 0).hex_format())
DARKCYAN = get_color_from_hex(RGB(0, 100, 0).hex_format())
DARKBLUE = get_color_from_hex(RGB(0, 0, 139).hex_format())
DARKMAGENTA = get_color_from_hex(RGB(139, 0, 139).hex_format())
DARKKHAKI = get_color_from_hex(RGB(189, 183, 107).hex_format())
DARKOLIVEGREEN = get_color_from_hex(RGB(85, 107, 47).hex_format())
DARKORANGE = get_color_from_hex(RGB(255, 140, 0).hex_format())
DARKORCHID = get_color_from_hex(RGB(153, 50, 204).hex_format())
DARKSALMON = get_color_from_hex(RGB(233, 150, 122).hex_format())
DARKSEAGREEN = get_color_from_hex(RGB(143, 188, 143).hex_format())
DARKSLATEBLUE = get_color_from_hex(RGB(72, 61, 139).hex_format())
DARKSLATEGRAY = get_color_from_hex(RGB(47, 79, 79).hex_format())
DARKTURQUOISE = get_color_from_hex(RGB(0, 206, 209).hex_format())
DARKVIOLET = get_color_from_hex(RGB(148, 0, 211).hex_format())
DEEPPINK = get_color_from_hex(RGB(255, 20, 147).hex_format())
DEEPSKYBLUE = get_color_from_hex(RGB(0, 191, 255).hex_format())
DIMGRAY = get_color_from_hex(RGB(105, 105, 105).hex_format())
DODGERBLUE = get_color_from_hex(RGB(30, 144, 255).hex_format())
EGGSHELL = get_color_from_hex(RGB(252, 230, 201).hex_format())
EMERALDGREEN = get_color_from_hex(RGB(0, 201, 87).hex_format())
FIREBRICK = get_color_from_hex(RGB(178, 34, 34).hex_format())
FLESH = get_color_from_hex(RGB(255, 125, 64).hex_format())
FLORALWHITE = get_color_from_hex(RGB(255, 250, 240).hex_format())
FORESTGREEN = get_color_from_hex(RGB(34, 139, 34).hex_format())
GAINSBORO = get_color_from_hex(RGB(220, 220, 220).hex_format())
GHOSTWHITE = get_color_from_hex(RGB(248, 248, 255).hex_format())
GOLD = get_color_from_hex(RGB(255, 215, 0).hex_format())
GOLDENROD = get_color_from_hex(RGB(218, 165, 32).hex_format())
GRAY10 = get_color_from_hex(RGB(26, 26, 26).hex_format())
GRAY20 = get_color_from_hex(RGB(51, 51, 51).hex_format())
GRAY30 = get_color_from_hex(RGB(77, 77, 77).hex_format())
GRAY40 = get_color_from_hex(RGB(102, 102, 102).hex_format())
GRAY50 = get_color_from_hex(RGB(127, 127, 127).hex_format())
GRAY60 = get_color_from_hex(RGB(153, 153, 153).hex_format())
GRAY70 = get_color_from_hex(RGB(179, 179, 179).hex_format())
GRAY80 = get_color_from_hex(RGB(204, 204, 204).hex_format())
GRAY90 = get_color_from_hex(RGB(229, 229, 229).hex_format())
GREENYELLOW = get_color_from_hex(RGB(173, 255, 47).hex_format())
HONEYDEW = get_color_from_hex(RGB(240, 255, 240).hex_format())
HOTPINK = get_color_from_hex(RGB(255, 105, 180).hex_format())
INDIANRED = get_color_from_hex(RGB(205, 92, 92).hex_format())
INDIGO = get_color_from_hex(RGB(75, 0, 130).hex_format())
IVORY = get_color_from_hex(RGB(255, 255, 240).hex_format())
KHAKI = get_color_from_hex(RGB(240, 230, 140).hex_format())
LAVENDER = get_color_from_hex(RGB(230, 230, 250).hex_format())
LAVENDERBLUSH = get_color_from_hex(RGB(255, 240, 245).hex_format())
LAWNGREEN = get_color_from_hex(RGB(124, 252, 0).hex_format())
LEMONCHIFFON = get_color_from_hex(RGB(255, 250, 205).hex_format())
LIGHTBLUE = get_color_from_hex(RGB(173, 216, 230).hex_format())
LIGHTCORAL = get_color_from_hex(RGB(240, 128, 128).hex_format())
LIGHTCYAN = get_color_from_hex(RGB(224, 255, 255).hex_format())
LIGHTGOLDENROD = get_color_from_hex(RGB(255, 236, 139).hex_format())
LIGHTGOLDENRODYELLOW = get_color_from_hex(RGB(250, 250, 210).hex_format())
LIGHTGREY = get_color_from_hex(RGB(211, 211, 211).hex_format())
LIGHTPINK = get_color_from_hex(RGB(255, 182, 193).hex_format())
LIGHTSALMON = get_color_from_hex(RGB(255, 160, 122).hex_format())
LIGHTSEAGREEN = get_color_from_hex(RGB(32, 178, 170).hex_format())
LIGHTSKYBLUE = get_color_from_hex(RGB(135, 206, 250).hex_format())
LIGHTSLATEBLUE = get_color_from_hex(RGB(132, 112, 255).hex_format())
LIGHTSLATEGRAY = get_color_from_hex(RGB(119, 136, 153).hex_format())
LIGHTSTEELBLUE = get_color_from_hex(RGB(176, 196, 222).hex_format())
LIGHTYELLOW = get_color_from_hex(RGB(255, 255, 224).hex_format())
LIMEGREEN = get_color_from_hex(RGB(50, 205, 50).hex_format())
LINEN = get_color_from_hex(RGB(250, 240, 230).hex_format())
MANGANESEBLUE = get_color_from_hex(RGB(3, 168, 158).hex_format())
MEDIUMORCHID = get_color_from_hex(RGB(186, 85, 211).hex_format())
MEDIUMPURPLE = get_color_from_hex(RGB(147, 112, 219).hex_format())
MEDIUMSEAGREEN = get_color_from_hex(RGB(60, 179, 113).hex_format())
MEDIUMSLATEBLUE = get_color_from_hex(RGB(123, 104, 238).hex_format())
MEDIUMSPRINGGREEN = get_color_from_hex(RGB(0, 250, 154).hex_format())
MEDIUMTURQUOISE = get_color_from_hex(RGB(72, 209, 204).hex_format())
MEDIUMVIOLETRED = get_color_from_hex(RGB(199, 21, 133).hex_format())
MELON = get_color_from_hex(RGB(227, 168, 105).hex_format())
MIDNIGHTBLUE = get_color_from_hex(RGB(25, 25, 112).hex_format())
MINT = get_color_from_hex(RGB(189, 252, 201).hex_format())
MINTCREAM = get_color_from_hex(RGB(245, 255, 250).hex_format())
MISTYROSE = get_color_from_hex(RGB(255, 228, 225).hex_format())
MOCCASIN = get_color_from_hex(RGB(255, 228, 181).hex_format())
NAVAJOWHITE = get_color_from_hex(RGB(255, 222, 173).hex_format())
OLDLACE = get_color_from_hex(RGB(253, 245, 230).hex_format())
OLIVEDRAB = get_color_from_hex(RGB(107, 142, 35).hex_format())
ORANGE = get_color_from_hex(RGB(255, 128, 0).hex_format())
ORANGERED = get_color_from_hex(RGB(255, 69, 0).hex_format())
ORCHID = get_color_from_hex(RGB(218, 112, 214).hex_format())
PALEGOLDENROD = get_color_from_hex(RGB(238, 232, 170).hex_format())
PALEGREEN = get_color_from_hex(RGB(152, 251, 152).hex_format())
PALETURQUOISE = get_color_from_hex(RGB(187, 255, 255).hex_format())
PALEVIOLETRED = get_color_from_hex(RGB(219, 112, 147).hex_format())
PAPAYAWHIP = get_color_from_hex(RGB(255, 239, 213).hex_format())
PEACHPUFF = get_color_from_hex(RGB(255, 218, 185).hex_format())
PEACOCK = get_color_from_hex(RGB(51, 161, 201).hex_format())
PINK = get_color_from_hex(RGB(255, 192, 203).hex_format())
PLUM = get_color_from_hex(RGB(221, 160, 221).hex_format())
POWDERBLUE = get_color_from_hex(RGB(176, 224, 230).hex_format())
PURPLE = get_color_from_hex(RGB(155, 48, 255).hex_format())
RASPBERRY = get_color_from_hex(RGB(135, 38, 87).hex_format())
RAWSIENNA = get_color_from_hex(RGB(199, 97, 20).hex_format())
ROSYBROWN = get_color_from_hex(RGB(188, 143, 143).hex_format())
ROYALBLUE = get_color_from_hex(RGB(65, 105, 225).hex_format())
SALMON = get_color_from_hex(RGB(250, 128, 114).hex_format())
SANDYBROWN = get_color_from_hex(RGB(244, 164, 96).hex_format())
SAPGREEN = get_color_from_hex(RGB(48, 128, 20).hex_format())
SEAGREEN = get_color_from_hex(RGB(84, 255, 159).hex_format())
SEASHELL = get_color_from_hex(RGB(255, 245, 238).hex_format())
SEPIA = get_color_from_hex(RGB(94, 38, 18).hex_format())
SIENNA = get_color_from_hex(RGB(160, 82, 45).hex_format())
SKYBLUE = get_color_from_hex(RGB(135, 206, 235).hex_format())
SLATEBLUE = get_color_from_hex(RGB(106, 90, 205).hex_format())
SLATEGRAY = get_color_from_hex(RGB(112, 128, 144).hex_format())
SNOW = get_color_from_hex(RGB(255, 250, 250).hex_format())
SPRINGGREEN = get_color_from_hex(RGB(0, 255, 127).hex_format())
STEELBLUE = get_color_from_hex(RGB(70, 130, 180).hex_format())
TAN = get_color_from_hex(RGB(210, 180, 140).hex_format())
THISTLE = get_color_from_hex(RGB(216, 191, 216).hex_format())
TOMATO = get_color_from_hex(RGB(255, 99, 71).hex_format())
TURQUOISE = get_color_from_hex(RGB(64, 224, 208).hex_format())
TURQUOISEBLUE = get_color_from_hex(RGB(0, 199, 140).hex_format())
VIOLET = get_color_from_hex(RGB(238, 130, 238).hex_format())
VIOLETRED = get_color_from_hex(RGB(208, 32, 144).hex_format())
WARMGREY = get_color_from_hex(RGB(128, 128, 105).hex_format())
WHEAT = get_color_from_hex(RGB(245, 222, 179).hex_format())
WHITESMOKE = get_color_from_hex(RGB(245, 245, 245).hex_format())
