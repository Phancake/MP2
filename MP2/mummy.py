import undead as un
class Mummy(un):
    def __init__(self, name):
        super().__init__()
        super().setHP(multiplier=1)
        super().setName(name)

    def eat(self, target):
        if isinstance(target, Mummy):
            print(self.getName(), 'cannot eat ', target.getName())
        else:
            self.setHP(self.getHP() + (target.getHP() / 2))
            target.setHP(target.getHP() - (target.getHP() / 2))
            if target.getHP() <= 0:
                target.isDead(True)
                print(self.getName(), 'cannot eat ', target.getName() + "because it is dead")

    def attack(self, target):
        if target.isDead() is False:
            if self.getHP() > 0:
                damage = (target.getHP() * 0.50 )+ (target.getHP() * 0.10)
                target.setHP(target.getHP() - damage)
                print(self.getName , 'attacks',  target.getName())

            if target.getHP() <= 0:
                target.isDead(True)
                print(self.getName(), 'cannot attack ', target.getName() , 'because it is dead')

    def setHP(self, hp):
        super().setHP(hp)
        if self.getHP() <= 0:
            self.isDead(True)
            print(self.getName(), 'is dead!')
    def revive(self): #di ko gets 'to be nag gpt ako icheck mo nga
        self.setHP(self.__initial_hp)
        self.isDead(False)
        print(self.getName(),'is revived!')
