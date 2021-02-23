class Hero: # template
#class variabel
    jumlah = 0
    #instance variable =>akan dieksekusi saat  ojek dibuat
    #ini juga bisa disebut attribut dari objek dibawah
    def __init__(self, inputName, inputHealt, inputPower, inputArmor):
         self.name = inputName
         self.health = inputHealt
         self.power = inputPower
         self.armor = inputArmor
         Hero.jumlah += 1
         print("membuat hero dengan nama " + inputName)

#pembuatan objek
hero1 = Hero("zilong", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("layla", 100, 15, 1 )
print(Hero.jumlah)
hero3 = Hero("miya", 500, 100, 0) 
print(Hero.jumlah)

