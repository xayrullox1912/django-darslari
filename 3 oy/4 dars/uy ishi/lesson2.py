class Player:
   def __init__(self,name,health,power):
       self.name = name
       self.health = health
       self.power = power

   def attack(self,target):
        raise NotImplementedError("attack() har bir farzand klassda aniqlansin")

   def heal(self,target):
        raise NotImplementedError("attack() har bir farzand klassda aniqlansin")

   def status(self):
       return f"{self.name} - health {self.health} - power {self.power}"


   def uron(self):
       if self.health < 0:
            self.health = 0
       if self.power < 0:
            self.power = 0


class Warrior(Player):
    base_health = 100
    base_power = 90
    hit_damage = 25
    hit_cost = 30

    def __init__(self,name):
        super().__init__(name,  Warrior.base_health,Warrior.base_power)

    def attack(self,target):
        if self.power < Warrior.hit_cost:
            print(f"{self.name} quvvatsiz hujum qila olmaydi")
            return
        target.health -= Warrior.hit_damage
        target.power -= Warrior.hit_cost
        target.uron()
        self.uron()
        print(f"{self.name} {target.name}ga hujum qilib {Warrior.hit_damage} hpni oldi ")

class Archer(Player):
    base_health = 80
    base_power = 90
    hit_damage = 15
    hit_cost = 20

    def __init__(self,name):
        super().__init__(name,  Archer.base_health,Archer.base_power)

    def attack(self,target):
        if self.power < Archer.hit_cost:
            print(f"{self.name} quvvatsiz hujum qila olmaydi")
            return
        target.health -= Archer.hit_damage
        target.power -= Archer.hit_cost
        target.uron()
        self.uron()
        print(f"{self.name} {target.name}ga hujum qilib {Archer.hit_damage} hpni oldi ")


class Healer(Player):
    base_health = 70
    base_power = 90
    heal_amout = 20
    heal_cost = 20

    def __init__(self, name):
        super().__init__(name, Healer.base_health, Healer.base_power)

    def attack(self, target):
        print(f"{self.name} davolovchi hujum qila olmaydi")


    def heal(self, target):
        if self.power < Healer.heal_cost:
            print(f"{self.name} quvvatsiz shifo bera olmaydi")
            return
        target.health += Healer.heal_amout
        target.power -= Healer.heal_cost
        target.uron()
        self.uron()
        print(f"{self.name} {target.name}ga {Healer.heal_amout} hp berdi ")

if __name__ == "__main__":
    p1 = Warrior("Temur")
    p2 = Archer("Ilyos")
    p3 = Healer("Lola")

    p1.status()
    p2.status()
    p3.status()
    print()

    p1.attack(p2)
    p2.attack(p1)
    p3.heal(p1)
    print()

    p1.status()
    p2.status()
    p3.status()