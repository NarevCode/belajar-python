class Hero:
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor): #ini adlah attribute
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.inputPower = inputPower
        self.inputArmor = inputArmor
        Hero.jumlah_hero += 1

    #void function, method tanpa return, tanpa return
    def siapa(self): #ini adalah attribute
        print("namaku adalah " + self.name)

    #method dengan argumen, tanpa return
    def healthUp(self,up): #ini jugua attrubute
         self.health += up

    #method dengan return
    def getHealth(self):  #ini jug sama attribute
        return self.health     


hero1 = Hero("badang", 100, 10, 5)
hero2 = Hero("bruno", 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
