import undead as un


class Vampire(un):
    def __init__(self, name):
        super().__init__()
        super().setHP(multiplier=1)
        super().setName(name)

    def bite(self, target):
        if self.isDead() is False and self.getHP() == 0:
            print(self.getName() + " cannot attack!")
        if target.isDead() is False:
            self.setHP(self.getHP() + (target.getHP() * 0.8))
            target.setHP(target.getHP() - (target.getHP() * 0.8))
            if target.getHP() <= 0:
                target.isDead(True)
                print(target.getName() + " is dead!")
        else:
            print(target.getName() + " is already dead!")

    def attack(self, target):
        if self.isDead() is False and self.getHP() == 0:
            print(self.getName() + " cannot attack!")
        if target.isDead() is False:
            target.setHP(target.getHP() - (self.getHP() * 1))
            if target.getHP() <= 0:
                target.isDead(True)
                print(target.getName() + " is dead!")

    def status(self):
        if self.getHP() == 0:
            self.isDead(False)

