init -5 python:
    class Player(renpy.store.object):
        def __init__(self, name, max_hp=0, max_mp=0, dmg=20, defence=1, element=None):
            self.name = name
            self.hp = max_hp
            self.max_hp = max_hp
            self.mp = max_mp
            self.max_mp = max_mp
            self.dmg = dmg
            self.defence = defence
            self.element = element
