class Character():
    def __init__(self, builder):
        self.name = builder.name
        self.species = builder.species
        self.armor = builder.armor
        self.power = builder.power
        self.weapon = builder.weapon

    
class CharacterBuilder():
    def __init__(self):
        self.init_variables()

    def init_variables(self):
        self.name = None
        self.species = None
        self.armor = None
        self.power = None
        self.weapon = None

    def set_name(self, name):
        self.name = name
        return self
        
    def set_species(self, species):
        self.species = species
        return self

    def set_armor(self, armor):
        self.armor = armor
        return self

    def set_power(self, power):
        self.power = power
        return self

    def set_weapon(self, weapon):
        self.weapon = weapon
        return self
    
    def build(self):
        new_character = Character(self)
        self.init_variables()
        return new_character
    

def main():
    ch_builder = CharacterBuilder()

    characters = [
        (ch_builder.set_name('Galadriel').set_species('Elfa').set_power('Imortal')
        .set_armor('Armadura de mithril').build()),
        (ch_builder.set_name('Aragorn').set_species('humano')
        .set_armor('chain mail').set_weapon('Anduril').build()),
        (ch_builder.set_name('Frodo').set_species('hobbit').build()),
        (ch_builder.set_name('Smaug').set_species('dragao').set_power('fogo').build())
    ]    

    for character in characters:
        print(f"name: {character.name}")
        print(f"species: {character.species}")
        print(f"armor: {character.armor}")
        print(f"power: {character.power}")
        print(f"weapon: {character.weapon}\n")


if __name__ == "__main__":
   main()
