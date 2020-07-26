class Scorecard:
    def __init__(self, players, course):
        self.players = players
        self.course = course

        self.active_course = 0

    def nextTurn(self):
        self.active_course +=1

    def previousTurn(self):
        self.active_course -=1













