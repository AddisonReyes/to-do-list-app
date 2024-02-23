import sys

commands = """
Commands:
 ~\'add task\'
 ~\'remove task\'
 ~\'tasks\'
 ~\'help\'
 ~\'exit\' """

class to_do_list():
    def __init__(self):
        self.idx = 000
        self.tasks = []
    
    def add_task(self, new_task):
        self.idx += 1
        self.tasks.append([self.idx, new_task])

    def remove_task(self):
        pass

    def change_task(self):
        pass

    def print_tasks(self):
        pass

    def __repr__(self):
        return str(self.tasks)


def main():
    my_list = to_do_list()
    run = True

    print("To Do List App")
    print(commands)

    while run:
        print("\n///////////////////////////////")
        option = str(input("Choose a option: "))

        if option == 'add task':
            my_list.add_task(str(input("Type the new task: ")))
        
        elif option == 'remove task':
            pass
        
        elif option == 'tasks':
            print(my_list)
        
        elif option == 'exit':
            run = False
        
        elif option == 'help':
            print(commands)

        else:
            pass


if __name__ == '__main__':
    main()