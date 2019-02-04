from classes import Character
from magic import Magic

print("Welcome to the game!")

# Magic
fire = Magic("Fire", 10, 30, "dark")
wind = Magic("Wind", 15, 50, "dark")
ice = Magic("Ice", 20, 70, "dark")

magic_list = [fire, wind, ice]

player = Character("Hero", 500, 100, 50, magic_list)
enemy = Character("Villain", 1000, 100, 20, magic_list)

player.stats()
enemy.stats()

print("---------------------------------------")

running = True
while running:
    # PLAYER'S TURN
    print(player.name)
    print("Choose your action: ")
    player.choose_action()
    try:
        choice = int(input(">>>: "))
    except ValueError:
        print("Choose a number!")
        continue

    action_index = choice - 1
    if action_index == 0:
        damage = player.generate_atk_damage()
        enemy.take_damage(damage)
        print("You attacked {} and dealt {} damage.".format(enemy.name, damage))
    elif action_index == 1:
        player.choose_magic()
        magic_choice = int(input(">>>: "))
        magic_index = player.magic[magic_index]
        magic_damage = magic.generate_magic_damage()
        magic_name = magic.name
        magic_cost = magic.mp_cost
        # enemy.take_damage(damage)
        # self.take_damage(dmg)
        # print("You attacked {} and dealt {} damage.".format(enemy.name, dmg))
    else:
        print("Choose a correct number")
        continue

    # ENEMY'S TURN
    enemy_choice = 0
    if enemy_choice == 0:
        enemy_damage = enemy.generate_atk_damage()
        player.take_damage(enemy_damage)
    # elif enemy_choice == 1:
    #     enemy_damage = enemy.generate_atk_damage()
    #     player.take_damage(enemy_damage)
    #     enemy.take_damage(mp_damage)

        print("{} attacked {} and dealt {} damage".format(enemy.name, player.name, enemy_damage))
# we don't need an else here, because there is no other option atmo

    print("---------------------------------------")
    player.stats()
    enemy.stats()
    if player.hp == 0:
        print("You lost.")
        running = False
    if enemy.hp == 0:
        print("You won!")
        running = False
