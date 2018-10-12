define config.hyperlink_handlers = {"glos": OpenGlossary}

init -5 python:
    glossary = {}
    glossary["blueMounts"] = GlossaryItem("Blue Mounts", "")
    glossary["elders"] = GlossaryItem("Elders",  u"Древнейшие - живые божества Кельгарра. Они произошли из кристаллов внутри {a=glos:blueMounts}Синих Гор{/a} и были уничтожены {a=glos:karedis}Каредисом{/a}. Их рост достигал трёх метров в высоту, а кожа имела синий оттенок. После {a=glos:karedisGenocide}геноцида Каредиса{/a} в живых осталось только пятеро Древнейших, а их поселения стали называться {a=glos:wasteland}Пустошами.")
    glossary["karedis"] = GlossaryItem("Karedis")
    glossary["karedisGenocide"] = GlossaryItem("Karedis Genocide")
    glossary["kel"] = GlossaryItem("Kel", u"Кели - обобщённое название всех рас, известных в Кельгарре. Кель - представитель расы, созданной {a=glos:elders)}Древнейшими{/a}")
    glossary["wasteland"] = GlossaryItem("Wasteland")

style text_glossary_item:
    size 32
    hover_color "#FFFFFF"
    color "#FFB060"

screen glossary_tooltip(text):
    textbutton _(text):
        xpos 360
        ypos 80

screen glossary_screen():
    add "gui/game_menu.png"
    modal True
    hbox align (.95,.04) spacing 20:
        textbutton _("X"):
            action [Hide("glossary_screen"), Hide("glossary_tooltip"), Show("inventory_button")]
            text_color "#FFB060"

    frame:
        side("c r"):
            area(20, 60, 300, 1000)
            viewport id "glossary_list":
                mousewheel True
                for item in glossary:
                    textbutton _(item.name):
                        action [Show ("glossary_tooltip", text = item.description)]
                        text_style "text_glossary_item"
            vbar value YScrollValue("glossary_list")
        null height 20

    textbutton _("Glossary"):
        xpos 100
        ypos 60
        text_color "#FFB060"
