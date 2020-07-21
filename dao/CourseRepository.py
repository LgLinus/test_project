import entities.Course
class course_repository:
    def get_courses ():
        bulltofta = entities.Course.Course("bulltofta:",[3,3,3,3,3,3,4,3,3,4,3,3,3,4,3,4,3,3])
        sibbarp = entities.Course.Course("sibbarp:",[4,5,6])

        return (bulltofta.name,bulltofta.par),(sibbarp.name,sibbarp.par)