class Scorecard:
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













