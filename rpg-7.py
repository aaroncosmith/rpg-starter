class Character: 
    def __init__(self, name, health, power, enemy):
        self.name = name
        self.health = health
        self.power = power
        self.enemy = bool
    def attack():


hero = Character("Hero", "10", "5", False)
goblin = Character("Goblin", "6", "2", True)

def main():
    # DONE!
    # hero_health = 10
    # hero_power = 5
    # goblin.power = 6
    # goblin_power = 2

    while goblin.power > 0 and hero_health > 0:
        print("You have %d health and %d power." % (hero_health, hero_power))
        print("The goblin has %d health and %d power." % (goblin.power, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            goblin.power -= hero_power
            print("You do %d damage to the goblin." % hero_power)
            if goblin.power <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.power > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does %d damage to you." % goblin_power)
            if hero_health <= 0:
                print("You are dead.")

main()
