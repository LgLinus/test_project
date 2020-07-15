from Entities.Course import Course
from Entities.Player import Player
course_selection = input("write your course name")
par = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
course = Course(course_selection,par)
print(course.name)
print(course.par)
print(course.total_tracks())

player = Player("Linus")
print(player.name)
