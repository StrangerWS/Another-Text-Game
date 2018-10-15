define config.hyperlink_handlers = {"glos": OpenGlossary}

init -5 python:
    glossary = {}
    glossary["blueMounts"] = GlossaryItem("Синие Горы", "Синие Горы")
    glossary["elders"] = GlossaryItem("Древнейшие",  u"Древнейшие - живые божества Кельгарра. Они произошли из кристаллов внутри {a=glos:blueMounts}Синих Гор{/a} и были уничтожены {a=glos:karedis}Каредисом{/a}. Их рост достигал трёх метров в высоту, а кожа имела синий оттенок. После {a=glos:karedisGenocide}геноцида Каредиса{/a} в живых осталось только пятеро Древнейших, а их поселения стали называться {a=glos:wasteland}Пустошами.")
    glossary["karedis"] = GlossaryItem("Каредис", "Каредис")
    glossary["karedisGenocide"] = GlossaryItem("Геноцид Каредиса", "Геноцид Каредиса")
    glossary["kel"] = GlossaryItem("Кель", u"Кели - обобщённое название всех рас, известных в Кельгарре. Кель - представитель расы, созданной {a=glos:elders}Древнейшими{/a}")
    glossary["wasteland"] = GlossaryItem("Пустоши", "Пустоши")

style text_glossary_item:
    size 32
    hover_color "#FFFFFF"
    color "#FFB060"

screen glossary_tooltip(text):
    textbutton _(text):
        xpos 500
        ypos 140
        xmaximum 800
        ymaximum 800
        text_color "#FFB060"

screen glossary_screen():
    tag glossary_screen
    add "gui/game_menu.png"
    modal True
    hbox align (.95,.04) spacing 20:
        textbutton _("X"):
            action [Hide("glossary_screen"), Hide("glossary_tooltip")]
            text_color "#FFB060"

    frame:
        area(60, 140, 400, 800)
        viewport id "glossary_list":
            mousewheel True
            scrollbars "vertical"
            ymaximum 800
            xmaximum 400
            vbox:
                for item in glossary.values():
                    textbutton _(item.name):
                        action [Show ("glossary_tooltip", text = item.description)]
                        text_style "text_glossary_item"
    textbutton _("Glossary"):
        xpos 100
        ypos 60
        text_color "#FFB060"
