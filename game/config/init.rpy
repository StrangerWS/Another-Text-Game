init -5 python:
    import renpy.store as store
    import renpy.exports as renpy
    from operator import attrgetter


init -1 python:
    Player(u"Вермес", 100, 50)
    def item_use():
        item.use()

label init_classes:
    python:
        player = Player(u"Вермес", 100, 50)
        inventory = Inventory()
        junk = Item("Мусор", description = "Обычная кучка мусора")
        massive_trunk = Item("Огромная ветка", description = "Боюсь представить, зачем тебе это", space = 2)
        inventory.add(junk)
        inventory.add(junk)
        inventory.add(massive_trunk)
return
