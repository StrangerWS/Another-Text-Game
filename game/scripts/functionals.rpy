label new_chapter_init:
    stop sound fadeout 2
    stop music fadeout 2
    stop ambience fadeout 3
    nvl clear
    return

label access_inventory:
    show screen inventory_button
    return

label restrict_inventory:
    hide screen inventory_button
    return

init -5 python:
    def NovelChar(who, color):
        return Character(who, kind = nvl, who_color = color, what_color="#FFB060")
