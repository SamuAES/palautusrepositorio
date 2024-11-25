class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def game_is_tied(self):
        if self.m_score1 == self.m_score2:
            return True

    def tie_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def over_three_points_won(self):
        if self.m_score1 >= 4 or self.m_score2 >=4:
            return True

    def point_difference(self):
        return abs(self.m_score1 - self.m_score2)

    def player_with_advantage(self):
        if self.m_score1 > self.m_score2:
            return "Advantage player1"
        else:
            return "Advantage player2"
        
    def game_over(self):
        if self.m_score1 > self.m_score2:
            return "Win for player1"
        else:
            return "Win for player2"

    def player_score(self, player_score):
        if player_score == 0:
            return "Love"
        elif player_score == 1:
            return "Fifteen"
        elif player_score == 2:
            return "Thirty"
        else:
            return "Forty"

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.game_is_tied():
            return self.tie_score()
        
        elif self.over_three_points_won():
            if self.point_difference() >= 2:
                return self.game_over()
            else:
                return self.player_with_advantage()
            
        else:
            return f"{self.player_score(self.m_score1)}-{self.player_score(self.m_score2)}"
