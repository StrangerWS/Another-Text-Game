# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = NovelChar(None, None)
define thgt = Character(None, kind = nvl, what_color = "#FFB060", what_prefix = "~ ", what_suffix = " ~")
define bard = NovelChar(u"Вермес", "#00FF88")
define king = NovelChar(u"Колетт Ниакар", "#FF3300")
define boy = NovelChar(u"Мальчик", "#b27b43")
define kuat = NovelChar(u"Куатрис", "#f5f500")
define man = NovelChar(u"Мужик", "#b27b43")

define menu = nvl_menu

# Declare background images
image bg autumn leaves = "images/seasons/autumn_leaves.jpg"
