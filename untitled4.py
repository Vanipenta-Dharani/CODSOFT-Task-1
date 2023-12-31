# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13qaQNSmrZ8EtCRYWlE8CSjDKCrcYul9C
"""

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def show_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

def main():
    to_do_list = ToDoList()

    while True:
        print('\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Exit')
        choice = input('Enter your choice (1/2/3/4): ')

        if choice == '1':
            task = input('Enter the task: ')
            to_do_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to remove: ')
            to_do_list.remove_task(task)
        elif choice == '3':
            to_do_list.show_tasks()
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    main()