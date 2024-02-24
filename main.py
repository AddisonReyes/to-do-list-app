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
        self.tasks = np.append(self.tasks, [new_task], axis=0)

        self.df = pd.DataFrame(self.tasks)
        self.df.rename(columns={0: "Task"}, inplace=True)

        print("task added successfully")

    def remove_task(self, idx):
        pass

    def change_task(self, idx):
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
            my_list.add_task(str(input("Type the new task: ")))
        
        elif option == 'remove task':
            pass
        
        elif option == 'tasks':
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