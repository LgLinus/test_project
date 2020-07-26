class Course:
    def __init__(self,name,par):
       self.name = name
       self.par = par


    def __str__(self):
        parString = ' '.join([str(n) for n in self.par])

        return self.name + parString


    def total_tracks(self):
        return len(self.par)







