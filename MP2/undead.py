class Undead:
    def __init__(self, name=None, hp=None):
        if name is not None and hp is not None:
            self.__hp = hp
            self.__name = "Undead" + name
        else:
            self.__hp = 100
            self.__name = "Undead"
            self.__isDead = False

    # dead is a boolean
    def isDead(self, dead=None):
        if dead is None:
            return self.__isDead
        else:
            self.__isDead = dead

    def getName(self):
        return self.__name

    def getHP(self):
        return self.__hp

    def setName(self, name):
        self.__name = name

    def setHP(self, hp=None, multiplier=None):
        if multiplier is None:
            self.__hp = hp
        else:
            self.__hp = self.__hp * multiplier


