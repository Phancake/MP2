import undead as un


class Zombie(un):
    def __init__(self, name):
        super().__init__()
        super().setHP(multiplier=1)
        super().setName(name)

    def eat(self, target):
        if target.isDead() is False:
            self.setHP(self.getHP() + (target.getHP() / 2))
            target.setHP(target.getHP() - (target.getHP() / 2))
            if target.getHP() <= 0:
                target.isDead(True)
                print(target.getName() + " is dead!")
        else:
            print(target.getName() + " is already dead!")

    def attack(self, target):
        if target.isDead() is False:
            target.setHP(target.getHP() - (self.getHP()/2))
            if target.getHP() <= 0:
                target.isDead(True)
                print(target.getName() + " is dead!")


