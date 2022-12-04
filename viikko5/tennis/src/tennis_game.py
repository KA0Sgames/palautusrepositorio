class TennisGame:
    ZERO_WON_POINTS = 0
    ONE_WON_POINT = 1
    TWO_WON_POINTS = 2
    THREE_WON_POINTS = 3
    FOUR_WON_POINTS = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = self.ZERO_WON_POINTS
        self.player2_score = self.ZERO_WON_POINTS

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_even_score(self, won_points_per_player):
        scores = {
            self.ZERO_WON_POINTS: "Love-All",
            self.ONE_WON_POINT: "Fifteen-All",
            self.TWO_WON_POINTS: "Thirty-All",
            self.THREE_WON_POINTS: "Forty-All"
            }

        if won_points_per_player in scores:
            return scores[won_points_per_player]
        else:
            return "Deuce"

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            score = self.get_even_score(self.player1_score)

        elif self.player1_score >= self.FOUR_WON_POINTS or self.player2_score >= self.FOUR_WON_POINTS:
            minus_result = self.player1_score - self. player2_score

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == self.ZERO_WON_POINTS:
                    score = score + "Love"
                elif temp_score == self.ONE_WON_POINT:
                    score = score + "Fifteen"
                elif temp_score == self.TWO_WON_POINTS:
                    score = score + "Thirty"
                elif temp_score == self.THREE_WON_POINTS:
                    score = score + "Forty"

        return score