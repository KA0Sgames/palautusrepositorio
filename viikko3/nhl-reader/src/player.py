class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return self.name + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists)
