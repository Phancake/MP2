import undead as un

class Skeleton(un):
    def __init__(self, name):
        super().__init__()
        super().setHP(80)
        super().setName(name)

    def attack(self, target):
        if self.isDead() is False:
            damage = self.getHP() * 0.7
            target.setHP(target.getHP() - damage)
            print(self.getName() + "attacks" + target.getName())
        if target.getHP() <= 0:
            target.isDead(True)
            print(target.getName() + "is dead!")
        else:
            print(self.getName() + "cannot attack because of HP: " + str(target.getHP()))
