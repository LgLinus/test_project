
from entities.Player import Player
import dao.CourseRepository
import dao.PlayerRepository
Players = dao.PlayerRepository.Player_repository.get_players()
courses = dao.CourseRepository.course_repository.get_courses()

for number in courses:

    print(number.name,number.par)


player = Player("Linus")
player2 = Player('Sebbe')
player3 = Player('Fredrik')
print(player.name)

### TODO
## Import the Course and PlayerRepository
## Iterate through all the Courses and Players, printing names and pars on the course if applicable
