import os

class Hero:
    def __init__(self):
        self.max_hp = 40
        self.current_hp = self.max_hp
        self.attack_power = 5
        self.resistance = 1
        self.experience = 0
        self.level = 1


    def attack(self, enemy):
        print(f"The hero attacks the fiend for {self.attack_power} damage!")
        enemy.recieve_damage(self.attack_power)


    def recieve_damage(self, damage_amount):
        damage_amount -= self.resistance
        print(f'The hero takes {damage_amount} due to {self.resistance} resistance.')
        self.current_hp -= damage_amount


    def defeat_enemy(self, enemy):
        print(f"The hero vanquished a mighty foe for {enemy.experience_reward} experience!")
        self.experience += enemy.experience_reward

        if self.experience >= (self.level * 20):
            self.level_up()


    def is_alive(self):
        return self.current_hp > 0


    def level_up(self):
        print("The hero gained a level!")
        self.level += 1
        self.max_hp += 10
        self.current_hp = self.max_hp
        self.attack_power += 2
        self.resistance += 1
        print(self)


    def __str__(self):
        return(f"Level {self.level} Hero: {self.current_hp} / {self.max_hp}\n  attack: {self.attack_power}\n  resistance: {self.resistance}\n  experience: {self.experience}")

class Dungeonmon:
    def __init__(self, level):
        print("A fiend is born!")
        self.level = level
        self.max_hp = 10 + (10 * self.level)
        self.current_hp = self.max_hp
        self.attack_power = 3 + (2 * self.level)
        self.resistance = 0 + (1 * self.level)
        self.experience_reward = 10


    def attack(self, hero):
        print(f"The fiend attacks for {self.attack_power} damage")
        hero.recieve_damage(self.attack_power)


    def recieve_damage(self, damage_amount):
        damage_amount -= self.resistance
        print(f'The fiend takes {damage_amount} due to {self.resistance} resistance.')
        self.current_hp -= damage_amount


    def is_alive(self):
        return self.current_hp > 0


    def __str__(self):
        return(f"Level {self.level} Dungeonmon: {self.current_hp} / {self.max_hp}\n  attack: {self.attack_power}\n  resistance: {self.resistance}")


def main():
    os.system('clear')
    hero = Hero()
    while hero.is_alive():
        current_enemy = Dungeonmon(hero.level)
        while hero.is_alive() and current_enemy.is_alive():
            print(hero)
            print(current_enemy)
            print('\n  ====BATTLE====\n')
            hero.attack(current_enemy)
            
            if current_enemy.is_alive():
                current_enemy.attack(hero)
            else: 
                hero.defeat_enemy(current_enemy)

            print('\n  ====ROUND OVER====\n')
            s = input("Press enter to continue to the next round. Or 'exit' to end the game.\n")
            if s == 'exit': 
                exit(0)
            os.system('clear')

    print("The hero died.")


if __name__ == '__main__':
    main()