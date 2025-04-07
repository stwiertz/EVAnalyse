class Player:
    def __init__(self, healthbar = ((0, 0), (1, 1)), isOrange = True):
        self._healthBar = healthbar
        self._health = 100
        self.isOrange = isOrange
    
    def isNamed(self):
        return self._name is not None
    
    def setName(self, name):
        self._name = name

    def setHealth(self, health):
        self._health = health
        if health < 0:
            self._health = 0
        elif health > 100:
            self._health = 100
    
    def getHealthBar(self):
        return self._healthBar
    
    
    
    def __str__(self):
        """Return a string representation of the player."""
        return f"Player {self.name} , HP :{self.health}"
    

