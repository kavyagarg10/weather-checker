class bankaccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

acc1 = bankaccount("rahul",100_000)

print(acc1.name,acc1.balance)
    


class employee:
    start_time = 10am
    end_time = 6pm
    
class teacher(employee):
    def __init__(self , salary , subject):
        self.salary = salary
        self.subject = subject

class admin(employee):
    def __init__(self , name , )
