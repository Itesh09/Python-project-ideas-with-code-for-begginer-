tasks=[]
def add_task():
    task=input("Please enter your task")
    tasks.append(task)
    print(f'task',{task},'has been added sucessfully')

def delete_task():
    list_task()
    try:
        tasktodelete=int(input("Enter the task number you want to delete:"))
        if tasktodelete>len(tasks):
            print("INVALID!!")
        elif tasktodelete<len(tasks):
            tasks.pop(tasktodelete)
            print(f'{tasktodelete}','has been delted')

    
    except:
        print("Invalid input")

def list_task():
    if not tasks:
        print("Current tasks:")
    else:
        for index, task in enumerate(tasks):
           print(f"Task{index}.{task}") 





while True:
    print("___________________________")
    print("welcome to your To do list:")
    print("1. To add new task")
    print("2. Delete task")
    print("3. list task")
    print("4. Quit")
   

    choice=int(input("Enter your choice"))
    if choice==1:
      add_task()
    if choice==2:
        delete_task
    if choice==3:
        list_task()
    if choice==4:
        break
    else:
        print("please input ")

