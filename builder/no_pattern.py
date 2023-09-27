class Character():
    def __init__(self, name, species, armor, power, weapon):
        self.name = name
        self.species = species
        self.armor = armor
        self.power = power
        self.weapon = weapon

def main():
    characters = [
    Character(name='Galadriel', species='Elfa', armor='armadura de mithril',
                        power='imortal', weapon=None),
    Character(name='Aragorn', species='humano', armor='chain mail',
                        power=None, weapon='Anduril'),
    Character(name='Frodo', species='hobbit', armor=None,
                        power=None, weapon=None),
    Character(name='Smaug', species='dragao', armor=None,
                        power='fogo', weapon=None)
    ]    
    for character in characters:
        print(f"name: {character.name}")
        print(f"species: {character.species}")
        print(f"armor: {character.armor}")
        print(f"power: {character.power}")
        print(f"weapon: {character.weapon}\n")



if __name__ == "__main__":
   main()
