import undead as un

class Lich(un):
    def __init__(self, name):
        super().__init__()
        super().setHP(multiplier=1)
        super().setName(name)
    def spell(self,target):
        if self.isDead() is False:
            spell_hp = target.getHP() * 0.10
            self.setHP(target.getHP() + spell_hp)
            print(self.getName() + " cast a spell to" + target.getName())
        #maglalagay pa ba ng else rito
        else:
            print(self.getName() + "cannot cast spell because of HP: " + str(target.getHP()))

    def attack(self,target):
        if self.isDead() is False:
            damage = self.getHP() * 0.70
            target.setHP(target.getHP() - damage)
        if self.getHP() <= 0:
            print(self.getName() + "cannot attack anymore because of HP:" + str(self.getHP()) + "but still alive!")
