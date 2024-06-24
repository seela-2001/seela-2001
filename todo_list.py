from datetime import datetime
class Task:
    def __init__(self,name,due_date,periority):
        self.name = name
        self.due_date = due_date
        self.periority = periority
    
    def __str__(self) :
        return f"Task : {self.name} , Due_date : {self.due_date} , Periority : {self.periority}"
    
    def edit_task(self,name = None , due_date = None , periority = None):
        if name :
            self.name = name
        if due_date:
            self.due_date = due_date
        if periority:
            self.priority = periority


class Todo_list:
    def __init__(self):
        self.tasks = []
    
    def add_task(self , task):
        self.tasks.append(task)

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def edit_task(self,task_name,new_name = None ,new_date = None,new_periority = None):
        for task in self.tasks :
            if task.name == task_name:
                task.edit_task(new_name ,new_date ,new_periority )
                break

    def display_task(self):
        if not self.tasks:
            print("there are no tasks to display.")
        for task in self.tasks :
            print(task)
    
def parse_date (date):
    return datetime.strptime(date,"%d-%m-%Y")


task1 = Task("reading",parse_date("5-10-2020"),"high")
task2 = Task("swimming",parse_date("5-10-2020"),"high")
task3 = Task("drawing",parse_date("5-10-2020"),"high")
todo = Todo_list()
todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)
todo.display_task()
print("==============================================")
todo.edit_task("drawing","photography",parse_date("5-10-2020"),"high")
todo.display_task()