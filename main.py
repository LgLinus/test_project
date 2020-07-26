from entities import ScoreCard

import dao.CourseRepository
import dao.PlayerRepository
players = dao.PlayerRepository.Player_repository.get_players()
courses = dao.CourseRepository.course_repository.get_courses()


for player in players:
    print(player)

for course in courses:
    print(course)

active_card = ScoreCard.Scorecard(players, courses[0])
print(active_card.course.name, active_card.players[0].name)
active_card.nextTurn()

print(active_card.active_course)
active_card.nextTurn()
print(active_card.active_course)
active_card.previousTurn()
print(active_card.active_course)
### TODO
## Iterate through all the Courses and Players, printing names and pars on the course if applicable