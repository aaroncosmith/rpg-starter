class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, opponent):
        opponent.health -= self.power
        if opponent.name == "zombie":
            opponent.health += self.power
        elif self.name != "goblin":
            print("You do %d damage to the %s." % (self.power, opponent.name))
      
        else:
            print("The goblin does %d damage to the %s." % (self.power, opponent.name))

    def alive(self):
        if self.health <= 0:
            print("The %s is dead." % self.name)
            return False
        else:
            return True

    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))


goblin = Character("goblin", 6, 2)
hero = Character("hero", 10, 5)
zombie = Character("zombie", 2, 1)

def main():
    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(zombie)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if zombie.alive():
            zombie.attack(hero)
        else:
            break
main()