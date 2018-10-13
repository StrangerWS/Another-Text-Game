init -5 python:
    class Item(store.object):
        def __init__(self, name, description, player=None, type="junk", value=0, image="", cost=0, space=1):
            self.name = name
            self.description = description
            self.player = player # which character can use this item?
            self.type = type # what type of item it is?
            self.value = 0 # how much it restores hp or mp, or increases damage?
            self.image = image # image file to use for this item
            self.cost = cost # how much does it cost in shops?
            self.space = space # how much space it consumes?
        def use(self): #here we define what should happen when we use the item
            if self.type == "healing": #healing item
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                else:
                    player.hp = player.hp+self.value
                inventory.drop(self) # consumable item - drop after use
            elif self.type == "mana": #mp restore item
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                else:
                    player.mp = player.mp+self.value
                inventory.drop(self) # consumable item - drop after use
            elif self.type == "manaheal":
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                else:
                    player.hp = player.hp+self.value
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                else:
                    player.mp = player.mp+self.value
                inventory.drop(self) # consumable item - drop after use
            elif self.type == "weapon":
                player.dmg += self.value
            elif self.type == "armor":
                player.defence = self.value
            else:
                pass
