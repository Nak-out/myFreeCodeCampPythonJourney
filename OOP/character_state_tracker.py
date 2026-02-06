class GameCharacter:
    def __init__(self, name:str):
        self._name = name
        self.health = 100
        self.mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if new_health < 0 or new_health > 100:
            raise ValueError("Attribute 'health' can't be negative or over 100.")
        self._health = new_health

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0 or new_mana > 50:
            raise ValueError("Attribute 'mana' can't be negative of over 50")
        self._mana = new_mana

    @property
    def level(self):
        return self._level
    

    def level_up(self, new_level):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        gamecharacter = f"Name: {self.name}\n"
        gamecharacter += f"Level: {self.level}\n"
        gamecharacter += f"Health: {self.health}\n"
        gamecharacter += f"Mana: {self.mana}"
        return gamecharacter