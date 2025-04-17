print("Hello MFs")
# ASK chatgpt to explain it ..
class Emp :
    def __init__(self, name, eid) :
        self.name = name
        self.eid = eid

    def print_info(self) :
        return f"Name : {self.name} \t, ID : {self.eid} "

class Manager(Emp) :
    def __init__(self,name , eid ,dept) :
        super().__init__(name , eid)
        self.dept = dept;
    def print_info(self) :
        return f"Name : {self.name} \t, ID : {self.eid} \t, Dept : {self.dept} "
        

class Developer(Emp) :
    def __init__(self, name , eid ,project_id) :
        super().__init__(name, eid)
        self.project_id = project_id;
        
    def print_info(self) :
        return f"Name : {self.name} \t, ID : {self.eid} \t, Project : {self.project_id} "

 
e = Emp("prasad",141)
print(e.print_info())

m = Manager("kullu",142,"Consultancy")
print(m.print_info())

d = Developer("Boss",144,"crimson-21")
print(d.print_info())