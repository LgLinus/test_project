from entities.Course import Course
from entities.Player import Player

course_name = input("write your course name")
par = [3,3,4,3,3,4,3,3,4,3,4,3,3,4,3,4,3,4]
course = Course(course_name,par)

print(course.name)
print(course.par)
print(course.total_tracks())

player = Player("Linus")
print(player.name)
