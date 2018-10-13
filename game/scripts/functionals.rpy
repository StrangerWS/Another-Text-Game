label new_chapter_init:
    stop sound fadeout 2
    stop music fadeout 2
    stop ambience fadeout 3
    nvl clear
    return
init -5 python:
    def FindGlossaryItem(link):
        for item in glossary:
            if item[link] == link:
                return item
        return None
    def NovelChar(who, color):
        return Character(who, kind = nvl, who_color = color, what_color="#FFB060")
    def OpenGlossary(link):
        item = glossary.get(link)
        renpy.hide_screen("inventory_button")
        renpy.show_screen("glossary_screen")
        renpy.show_screen("glossary_tooltip", item.description)
