from entities.Course import Course
class CourseRepository:
    def get_courses():
        bulltofta = Course("bulltofta",[3,3,3,3,3,3,4,3,3,4,3,3,3,4,3,4,3,3])
        sibbarp = Course("sibbarp",[4,5,6])
        return [bulltofta,sibbarp]
