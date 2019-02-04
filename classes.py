import random

class Character:
    def __init__(self, name, hp, mp, atk, magic):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Attack", "Magic"]
        self.magic = magic

    def stats(self):
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        print(f"{self.mp}/{self.maxmp}")

    def generate_atk_damage(self):
        dmg = random.randint(self.atk_low, self.atk_high)
        return dmg

    # def generate_mp_damage(self):
    #     mp_dmg = random.randint(self.mp_low, self.mp_high)
    #     return mp_dmg

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
            # print("You die")
        return self.hp
# {}
    def choose_action(self):
        index = 1
        print("ACTIONS: ")
        for element in self.action:
            print("{}. {}".format(index, element))
            index = index + 1
            # print("{}. {}".format(index, element))
            # index = index + 2

    def choose_magic(self):
        index = 1
        print("MAGIC: ")
        for element in self.magic:
            print("{}. {}".format(index, element))
            index = index + 1

    def reduce_mp(self, used_mp):
        self.mp = self.mp - used_mp
        if self.mp < used_mp:
            print("You don't have enough mojo.")

        return self.mp
