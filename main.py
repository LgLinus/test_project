
from entities.Player import Player
import dao.CourseRepository
courses = dao.CourseRepository.course_repository.get_courses()

print(courses)

player = Player("Linus")
player2 = Player('Sebbe')
player3 = Player('Fredrik')
print(player.name)

### TODO 

## Import the Course and PlayerRepository
## Iterate through all the Courses and Players, printing names and pars on the course if applicable
print(player2.name)
print(player3.name)