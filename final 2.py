# TASK MANAGER
list_task = []
done_tasks = []
import os
def clean():#Credits to the author :)
    os.system("cls")
    print("Name: Andres Felipe")
    print("Age: 17 years old")
    print("City: Apartado")

def fnt_show():#Here is the list
    if list_task:
        print("Pending Tasks:")
        for i, task in enumerate(list_task, 1):
            print(f"{i}. {task}")
    else:
        print("No pending tasks.")

def fnt_show_done():
    if done_tasks:#completed tasks are validated here
        print("Completed Tasks:")
        for i, task in enumerate(done_tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No completed tasks.")

sw = True

def selector(option):
    global sw
    if option == '0':
        sw = False
    elif option == '1':
        task = input('Enter the task you want to add: ')
        if task:
            list_task.append(task)
            input("Task added successfully. Press Enter to continue.")
        else:
            input('Enter a valid task. Press Enter to continue.')
    elif option == '2':#HERE THE PROCESS OF DELETING SOME TASK IS DONE
        if list_task:
            fnt_show()
            task_num = input("Enter the number of the task you want to delete: ")
            if task_num.isdigit() and 1 <= int(task_num) <= len(list_task):
                list_task.pop(int(task_num) - 1)
                input("Task deleted successfully. Press Enter to continue.")
            else:#HERE IS THE MESSAGE THAT THE USER HAS CHOSEN AN INVALID NUMBER TO DELETE
                input("Invalid task number. Press Enter to continue.")
        else:
            input("No tasks to delete. Press Enter to continue.")
    elif option == '3':#here it is validated to mark a task as done
        if list_task:
            fnt_show()
            task_num = input("Enter the number of the task you want to mark as done: ")
            if task_num.isdigit() and 1 <= int(task_num) <= len(list_task):
                done_tasks.append(list_task.pop(int(task_num) - 1))
                input("Task marked as done. Press Enter to continue.")
            else:
                input("Invalid task number. Press Enter to continue.")
        else:
            input("No tasks to mark as done. Press Enter to continue.")
    elif option == '4':
        fnt_show()
        input("Press Enter to continue.")
    elif option == '5':
        fnt_show_done()
        input("Press Enter to continue.")
    else:
        input("Invalid option. Press Enter to continue.")

while sw == True:
    clean()
    option = input('Choose an option:\n\n0.Exit\n1.Add task\n2.Delete task\n3.Mark task as done\n4.Show pending tasks\n5.Show completed tasks\n->')
    selector(option)