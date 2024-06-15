def add_task(tasks):
    task=input("enter a task:")
    tasks.append(task)
    print("Task added successfully")

def view_task(tasks):
    if len(tasks)==0:
        print("List of tasks is empty")
    for a,b in enumerate(tasks): #for printing with index value we use enumerate()
        print(a,b)
     
           

def delete_task(tasks):
    view_task(tasks)
    delete=int(input("enter any index no to  remove:"))
    tasks.pop(delete)
    print("task removed successfully"'\n')
    print("updated tasks list:")
    view_task(tasks)

tasks=[]
while True:
    print("choose your option:")
    print("1.Add task")
    print("2.View task")
    print("3.Delete task")
    print("4.Quit")
    choice=int(input("enter any choice:"))
    if(choice==1):
        add_task(tasks)
    elif(choice==2):
        view_task(tasks)
    elif(choice==3):
        delete_task(tasks)
    elif(choice==4):
        print("you decided to quit 😢")
        break
     