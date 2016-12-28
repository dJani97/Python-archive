#This crap is abaut classes and objects........

class Enemy:
        life = 3

        def attack(self):
            print("Ouch!")
            self.life -= 1

        def checkLife(self):
            if self.life <= 0:
                print("I'm dead")
            else:
                print(str(self.life) + " life left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()