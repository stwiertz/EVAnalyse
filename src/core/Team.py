class Team:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def __str__(self):
        return f"Team {self.name} , Score :{self.score}"