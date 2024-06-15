import undead as un
import random


class Ghost(un):
    def __init__(self, name):
        super().__init__()
        super().setHP(multiplier=1)
        super().setName(name)

    def haunt(self, target):
        if target.isDead() is False:
            target.setHP(target.getHP() - (target.getHP() * 0.5))
            if target.getHP() <= 0:
                target.isDead(True)
                print(target.getName() + " is dead!")
        else:
            print(target.getName() + " is already dead!")

    def attack(self, target):
        if target.isDead() is False:
            target.setHP(target.getHP() - (self.getHP() * 1))
            if target.getHP() <= 0:
                target.isDead(True)
                print(target.getName() + " is dead!")

    def passive(self):
        if random.randint(1, 100) <= 20:
            print(self.getName() + " evaded the attack!")
        else:
            self.setHP(self.getHP() - 10)
            if self.getHP() <= 0:
                self.isDead(True)
                print(self.getName() + " is dead!")
