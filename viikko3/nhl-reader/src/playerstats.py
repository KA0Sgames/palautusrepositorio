class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.player_reader.get_players()

        filtered_players = list(filter(lambda x: x.nationality == nationality, players))
        filtered_players.sort(key=lambda c: c.goals + c.assists, reverse=True)

        return filtered_players