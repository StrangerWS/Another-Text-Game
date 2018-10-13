style text_inventory_item:
    size 32
    color "#FFFFFF"
    hover_color "#FFB060"
style text_tooltip_item:
    size 32
    color "#F8F8F8"

screen inventory_tooltip(text):
    textbutton _(text):
        text_style "text_tooltip_item"
        xpos 150
        ypos 800

screen inventory_button():
    textbutton _(u"Инвентарь"):
        action [Show("inventory"), Hide("inventory_button")]
        align (.95,.04)

screen inventory():
    add "gui/game_menu.png"
    modal True
    hbox align (.95,.04) spacing 20:
        textbutton _("X"):
            action [Hide("inventory"), Show("inventory_button")]
            text_color "#FFB060"
    $ x = 150
    $ y = 120
    $ i = 0

    textbutton _("Inventory space: %d" % inventory.space):
        xpos 100
        ypos 60
        text_color "#FFB060"

    for item in inventory.items:

        if i + 1 == 15:
            $ x = 600
            $ y = 120
        textbutton _(item.name):
            xpos x
            ypos y
            action [Hide("inventory"), Hide("inventory_tooltip"), Show("inventory_button"), item.use]
            hovered [Show("inventory_tooltip", text = item.description)]
            unhovered [Hide("inventory_tooltip")]
            text_style "text_inventory_item"
        $ i += 1
        $ y += 40
