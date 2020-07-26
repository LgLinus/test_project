
from entities.Player import Player
import dao.CourseRepository
import dao.PlayerRepository
players = dao.PlayerRepository.Player_repository.get_players()
courses = dao.CourseRepository.course_repository.get_courses()
for player in players:
    print(player.name)



### TODO
## Import the Course and PlayerRepository
## Iterate through all the Courses and Players, printing names and pars on the course if applicable