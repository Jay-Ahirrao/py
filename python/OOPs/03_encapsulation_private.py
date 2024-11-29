class Student :
    def __init__(self, name, grades) :
        self.__name = name
        self.__grades = grades

    def get_details(self):
        print(f"Student Name : '{self.__name}' ")
        for i in range(len(self.__grades)) : 
            print(f"Grade of subject {i+1} : {self.__grades[i]}")

    def add_grades(self , new_grade):
        self.__grades.append(new_grade)
        
    def get_avg(self):
        print(f"Student Name : '{self.__name}' ")
        for i in range(len(self.__grades)) :
            sum = 0 
            sum += self.__grades[i]
        print(f"Average of all grades : '{sum/len(self.__grades) :.3f}' ")

s1 = Student("Jay",[89,96,92,94,95])
s1.get_details()
s1.add_grades(97)

s1.get_avg()