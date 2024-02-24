import pandas as pd
import numpy as np
import os


commands = """
Commands:
 ~\'add task\'
 ~\'remove task\'
 ~\'tasks\'
 ~\'clear\'
 ~\'help\'
 ~\'exit\' """


class to_do_list():
    def __init__(self):
        self.tasks = np.array([])
    
    def add_task(self, new_task):
        if new_task == '-1':
            return
        
        self.tasks = np.append(self.tasks, [new_task], axis=0)

        self.df = pd.DataFrame(self.tasks)
        self.df.rename(columns={0: "Task"}, inplace=True)

        print("task added successfully")

    def remove_task(self, idx):
        if idx == -1:
            return
        
        self.df.drop(index=idx, inplace=True)
        print("Task deleted successfully")

    def change_task(self, idx):
        pass

    def import_list(self):
        pass

    def export_liste(self):
        pass

    def print_tasks(self):
        print('\n', self.df)

    def __repr__(self):
        return str(self.df)


def main():
    my_list = to_do_list()
    run = True

    print("To Do List App")
    print(commands)

    while run:
        print("\n///////////////////////////////")
        option = str(input("Choose a option: ")).strip()

        if option == 'add task' or option == 'add':
            my_list.add_task(str(input("Type the new task, -1 to cancel: ")))
        
        elif option == 'remove task' or option == 'remove':
            my_list.print_tasks()

            try:
                my_list.remove_task(int(input("\nType the idx to remove, -1 to cancel: ")))
            
            except:
                print("Error: no index provided")
        
        elif option == 'tasks' or option == 'task':
            my_list.print_tasks()
        
        elif option == 'exit':
            run = False
        
        elif option == 'help':
            print(commands)
        
        elif option == 'clear':
            os.system('cls')

        else:
            pass


if __name__ == '__main__':
    main()