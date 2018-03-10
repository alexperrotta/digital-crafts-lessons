class Character(object):
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print "%s did %d damage to the %s." % (self.charType, self.power, enemy.charType)
        if enemy.health <= 0:
            print "The %s is dead." % (enemy.charType)

    def print_status(self):
        print "%s has %d health and %d power." % (self.charType, self.health, self.power)


class Hero(Character):  # the Hero class inherits from the Character class
    def __init__(self):
        self.charType = 'Hero'
        self.health = 10
        self.power = 5

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print "You do %d damage to the goblin." % self.power
    #     if enemy.health <= 0:
    #         print "The goblin is dead."

    # def print_status(self):
    #     print "You have %d health and %d power." % (self.health, self.power)


class Goblin(Character):
    def __init__(self):
        self.charType = 'Goblin'
        self.health = 6
        self.power = 2
    
    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print "The goblin does %d damage to you." % self.power
    #     if enemy.health <= 0:
    #         print "You are dead."

    # def print_status(self):
    #     print "The goblin has %d health and %d power." % (self.health, self.power)

class Zombie(Character):
    def __init__(self):
        self.charType = 'Zombie'
        self.health = 20
        self.power = 20


def main():
    barry_the_hero = Hero()  # Barry is the Hero class
    steve_the_goblin = Goblin()  # Steve is the Goblin class

    while steve_the_goblin.alive() and barry_the_hero.alive():
        barry_the_hero.print_status()
        steve_the_goblin.print_status()
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            barry_the_hero.attack(steve_the_goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if steve_the_goblin.alive():
            # Goblin attacks hero
            steve_the_goblin.attack(barry_the_hero, )


main()