class ScoreCard:
    def __init__(self, players, course):
        self.players = players
        self.course = course

        self.active_course = 0

    def nextTurn(self):
        if self.active_course == self.course.total_tracks():
            print("game over")
            return

        self.active_course += 1

    def previousTurn(self):
        if self.active_course == 0:
            print("game over")
            return
        self.active_course -=1

    def __str__(self):
        playerString = map(lambda player: player.__str__(), self.players)
        return "players:[" + ",".join(playerString) + "]\ncourse:" + self.course.__str__() + "\nactiveCourse:" + str(self.active_course)
