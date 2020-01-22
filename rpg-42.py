import random
import time
class Character:
    def __init__(self, name, health, power, luck, coins):
        self.name = name
        self.health = health
        self.power = power
        self.luck = luck
        self.coins = coins

    def attack(self, opponent):
        temp_damage = random.randint(1, self.power)
        opponent.health -= temp_damage
        print("The %s does %d damage to the %s." % (self.name, temp_damage, opponent.name))

    def alive(self):
        if self.health <= 0:
            print("The %s is dead." % self.name)
            self.on_death(hero)
            return False
        else:
            return True
    def on_death(self, opponent):
        opponent.coins += self.coins
        print("You recieve %s coins off of a %s's corspe." % (self.coins, self.name))


    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))



class Hero(Character):
    def __init__(self, name, health, power, luck, coins):
        super().__init__(name, health, power, luck, coins)
    def attack(self, opponent):
        temp_damage = random.randint(1, self.power)
        luck_roll = random.randint(1, 101)
        if luck_roll <= self.luck:
            opponent.health -= temp_damage * 2
            print("You score a critical hit on a %s for %s!!!!" % (opponent.name, temp_damage * 2))
        elif opponent == shadow:
            luck_roll = random.randint(1, 101)
            if luck_roll > opponent.luck:
                print("The %s completely evades your attack!" % opponent.name)
            else:
                opponent.health -= temp_damage
                print("You hit a %s for %s damage." % (opponent.name, temp_damage))

        else:
            opponent.health -= temp_damage
            print("You hit a %s for %s damage." % (opponent.name, temp_damage))
        
    def alive(self):
        if self.health <= 0:
            print("The %s is dead." % self.name)
            return False
        else:
            return True
    def restore(self):
        self.health += 10
        print("Hero's heath is restored by %d!" % 10)
        time.sleep(1)
    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Shadow(Character):
    def __init__(self, name, health, power, luck, coins):
        super().__init__(name, health, power, luck, coins)
    def evade(self, opponent):
        luck_roll = random.randint(1, 101)
        if luck_roll <= self.luck:
            self.health += opponent.attack
        else:
            self.health -= opponent.attack

class Zombie(Character):
    def __init__(self, name, health, power, luck, coins):
        super().__init__(name, health, power, luck, coins)
    
    def alive(self):
        if self.health <= 0:
            self.health = 1
            print("%s doesn't seem to take any damage..." % self.name)
            return True
        else: 
            return True

class Goblin(Character):
    def __init__(self, name, health, power, luck, coins):
        super().__init__(name, health, power, luck, coins)
    
    def attack(self, opponent):
        luck_roll = random.randint(1, 101)
        if luck_roll <= self.luck:
            temp_damage = random.randint(1, self.power)
            opponent.health -= temp_damage
            self.health += temp_damage
            print("The %s does a special attack: Life Tap! dealing %s to %s and healing the %s for %s." % (self.name, temp_damage, opponent.name, self.name, temp_damage))
        else:
            temp_damage = random.randint(1, self.power)
            opponent.health -= temp_damage





class Medic(Character):
    def __init__(self, name, health, power, luck, coins):
        super().__init__(name, health, power, luck, coins)
    def heal(self, ally):
        luck_roll = random.randint(1, 101)
        if luck_roll <= self.luck:
            heal_amount = random.randint(1, 13)
            ally.health += heal_amount
            print("The %s healed the %s for %s." % (self.name, ally.name, heal_amount))

class Gorgon(Character):
    def __init__(self, name, health, power, luck, coins):
        super().__init__(name, health, power, luck, coins)
    def attack(self, opponent):
        luck_roll = random.randint(1, 101)
        if luck_roll <= self.luck:
            opponent.health = 0
            print("The %s has deathtouched the %s!!!" % (self.name, opponent.name))
        else: 
            temp_damage = random.randint(1, self.power)
            opponent.health -= temp_damage
            print("The %s does %d damage to the %s." % (self.name, temp_damage, opponent.name))




medic = Medic("Medic", 20, 5, 20, 2)
shadow = Shadow("Shadow", 1, 5, 10, 5)
hero = Hero("Hero", 35, 15, 20, 0)
goblin = Goblin("Goblin", 40, 3, 10, 5)
gorgon = Gorgon("Gorgon", 42, 5, 5, 10)
john = Goblin("A Fiestier Goblin", 40, 5, 20, 20)
herb = Zombie("Herb the Zombie", 1, 1, 1, 100000000)

class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the %s" % enemy.name)
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
                medic.heal(hero)
            elif user_input == 2:
                medic.heal(hero)
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
            medic.heal(hero)
        if hero.alive():
            print("You defeated the %s" % enemy.name)
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            elif user_input == 1 and hero.coins < 5:
                print("You can't afford this! Go fight some more monsters!!!")
            elif user_input == 2 and hero.coins < 10:
                print("You can't afford this! Go fight some more monsters!!!")
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)

enemies = [shadow, gorgon, goblin, john, herb]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
