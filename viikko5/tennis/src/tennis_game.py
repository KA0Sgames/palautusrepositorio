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
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_even_score(self, won_points_per_player):
        even_scores = {
            self.ZERO_WON_POINTS: "Love-All",
            self.ONE_WON_POINT: "Fifteen-All",
            self.TWO_WON_POINTS: "Thirty-All",
            self.THREE_WON_POINTS: "Forty-All"
            }

        if won_points_per_player in even_scores:
            return even_scores[won_points_per_player]
        else:
            return "Deuce"

    def get_uneven_score_with_four_or_over_points_won_by_one_player(self):
        AT_LEAST_TWO_FOR_PLAYER_TWO = -2
        ONE_FOR_PLAYER_TWO = -1
        ONE_FOR_PLAYER_ONE = 1
        AT_LEAST_TWO_FOR_PLAYER_ONE = 2
        
        difference_of_points = {
            AT_LEAST_TWO_FOR_PLAYER_TWO: "Win for player2",
            ONE_FOR_PLAYER_TWO: "Advantage player2",
            ONE_FOR_PLAYER_ONE: "Advantage player1",
            AT_LEAST_TWO_FOR_PLAYER_ONE: "Win for player1"
            }
        
        minus_result = self.player1_score - self. player2_score
        
        if minus_result < AT_LEAST_TWO_FOR_PLAYER_TWO:
            minus_result = AT_LEAST_TWO_FOR_PLAYER_TWO
        elif minus_result > AT_LEAST_TWO_FOR_PLAYER_ONE:
            minus_result = AT_LEAST_TWO_FOR_PLAYER_ONE

        return difference_of_points[minus_result]

    def get_uneven_score_with_players_having_less_than_four_points_won_each(self):
        representation_of_points_won = {
            self.ZERO_WON_POINTS: "Love",
            self.ONE_WON_POINT: "Fifteen",
            self.TWO_WON_POINTS: "Thirty",
            self.THREE_WON_POINTS: "Forty"
        }

        representation_of_score = representation_of_points_won[self.player1_score]
        representation_of_score += "-"
        representation_of_score += representation_of_points_won[self.player2_score]

        return representation_of_score



    def get_score(self):
        if self.player1_score == self.player2_score:
            score = self.get_even_score(self.player1_score)
        elif self.player1_score >= self.FOUR_WON_POINTS or self.player2_score >= self.FOUR_WON_POINTS:
            score = self.get_uneven_score_with_four_or_over_points_won_by_one_player()
        else:
            score = self.get_uneven_score_with_players_having_less_than_four_points_won_each()

        return score