class Pong:
    def __init__(self, max_score):
        self.maxScore = max_score
        self.score1 = 0
        self.score2 = 0
        self.is_player_1 = False

    def play(self, ballPos, playerPos):
        if self.score1 == self.maxScore or self.score2 == self.maxScore:
            return "Game Over!"

        self.is_player_1 = not self.is_player_1

        if self.is_player_1:                            # Check turn
            if abs(playerPos - ballPos) > 3:            # Player 1 missed the ball
                self.score1 += 1
                if self.score1 == self.maxScore:
                    return "Player 2 has won the game!"
                return "Player 1 has missed the ball!"
            else:                                       # Player 1 hit the ball
                return "Player 1 has hit the ball!"
        else:
            if abs(playerPos - ballPos) > 3:            # Player 2 missed the ball
                self.score2 += 1
                if self.score2 == self.maxScore:
                    return "Player 1 has won the game!"
                return "Player 2 has missed the ball!"
            else:                                       # Player 2 hit the ball
                return "Player 2 has hit the ball!"
