class Warrior:
    attack = 5
    health = 50
    is_alive = True


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    term = 0
    while unit_1.health > 0 and unit_2.health > 0:

        if term % 2 == 0:
            unit_2.health -= unit_1.attack
        else:
            unit_1.health -= unit_2.attack
        term += 1

    if unit_1.health <= 0:
        unit_1.is_alive = False
        return False
    else:
        unit_2.is_alive = False
        return True


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    print(fight(chuck, bruce))# == True
    print(fight(dave, carl))# == False
    print(chuck.is_alive)# == True
    print(bruce.is_alive)# == False
    print(carl.is_alive)# == True
    print(dave.is_alive)# == False
    print(fight(carl, mark))# == False
    print(carl.is_alive)# == False

    print("Coding complete? Let's try tests!")