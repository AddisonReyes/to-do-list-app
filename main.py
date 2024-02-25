import pandas as pd
import numpy as np
import os


commands = """
Commands:
 ~\'add task\'
 ~\'remove task\'
 ~\'Import list\'
 ~\'Export list\'
 ~\'list\'
 ~\'clear\'
 ~\'help\'
 ~\'exit\' """


class to_do_list():
    def __init__(self):
        self.tasks = np.array([])
        self.df = pd.DataFrame(self.tasks)
    
    def tasks_to_dataframe(self):
        self.df = pd.DataFrame(self.tasks)
        self.df.rename(columns={0: "Task"}, inplace=True)

    def add_task(self, new_task):
        if new_task == '-1':
            return
        
        self.tasks = np.append(self.tasks, [new_task], axis=0)
        self.tasks_to_dataframe()

        print("task added successfully")

    def remove_task(self, idx):
        if idx == -1:
            return
        
        self.df.drop(index=idx, inplace=True)
        self.tasks = self.df['Task'].values

        self.tasks_to_dataframe()
        print("Task deleted successfully")

    def import_list(self):
        list_path = 'lists/' + input("Write the name of the list: ")
        if os.path.exists(list_path):
            self.df = pd.read_json(list_path)
            self.tasks = self.df['Task'].values
            print("List imported successfully.")

        else:
            print("That list does not exist.")

    def export_list(self):
        if self.df.empty:
            print("There is no list created.")
        else:
            list_path = 'lists/' + input("Write the name of the list: ")
            self.df.to_json(list_path)#, orient='records')
            print("List exported successfully.")

    def print_tasks(self):
        if self.df.empty:
            print("There is no list created.")
            return False
        
        else:
            print('\n', self.df)
            return True

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
            can_remove = my_list.print_tasks()

            if can_remove:
                try:
                    my_list.remove_task(int(input("\nType the idx to remove, -1 to cancel: ")))
            
                except:
                    print("No index written.")
        
        elif option == 'import list' or option == 'import':
            my_list.import_list()

        elif option == 'export list' or option == 'export':
            my_list.export_list()

        elif option == 'tasks' or option == 'task' or option == 'list':
            my_list.print_tasks()
        
        elif option == 'exit':
            run = False
        
        elif option == 'help':
            print(commands)
        
        elif option == 'clear':
            os.system('cls')

        else:
            print("Unknown command")


if __name__ == '__main__':
    main()