class Superhero:
    def __init__(self, name, power, alias, strength_level):
        self.name = name
        self.power = power
        self.alias = alias
        self.strength_level = strength_level

    def use_power(self):
        return f"{self.alias} uses their power: {self.power}!"

    def display_info(self):
        return f"Superhero: {self.name}\nAlias: {self.alias}\nPower: {self.power}\nStrength Level: {self.strength_level}"

# Example of creating a Superhero object
hero1 = Superhero("Clark Kent", "Super Strength", "Superman", 100)
print(hero1.display_info())
print(hero1.use_power())

