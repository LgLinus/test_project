from dao.CourseRepository import CourseRepository
from dao.PlayerRepository import PlayerRepository 

from entities.ScoreCard import ScoreCard

players = PlayerRepository.get_players()
courses = CourseRepository.get_courses()

for player in players:
    print(player)

for course in courses:
    print(course)

active_card = ScoreCard(players, courses[0])

print("\n")
print(active_card,"\n")

active_card.nextTurn()
active_card.nextTurn()
print(active_card,"\n")

active_card.previousTurn()
print(active_card,"\n")
