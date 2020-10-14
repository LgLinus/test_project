from entities.Course import Course
class CourseRepository:
    def get_courses():
        bulltofta = Course("Malmö, Bulltofta ",[3, 3, 3, 3, 3, 3, 4, 3, 3, 4, 3, 3, 3, 4, 3, 4, 3, 3])
        sibbarp = Course("Malmö, Sibbarp ",[3, 3, 3, 3, 3, 3, 3, 4, 3])
        Lund_StH = Course('Lund Sankt Hans backar ', [3, 3, 3, 3, 4, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3,])
        Lund_Vip = Course('Lund, Vipeholm ', [4, 3, 3, 3, 3, 3, 3, 3, 3])
        return [bulltofta, sibbarp, Lund_StH, Lund_Vip]

