from functions import get_todos,write_todos
import time
print('Im a big boy')
print('Today is',time.strftime("%B %d, %Y %H:%M:%S"))
while True:
    user_action = input("Type add, edit, show, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip()
        todos = get_todos()
        todo = todo.capitalize() + '\n'
        todos.append(todo)
        write_todos('todos.txt',todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            print(f"{index + 1} - {item.strip()}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()
            number = int(user_action[5:].strip()) - 1
            if 0 <= number < len(todos):
                new_item = input(f"Type the new item to replace '{todos[number].strip()}': ").capitalize()
                todos[number] = new_item + "\n"
                write_todos(todos, 'todos.txt')

            else:
                print("Number out of range.")
        except ValueError:
            print('Invalid input. Please enter a number.')

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()
            item_todelete = int(user_action[9:].strip()) - 1
            if 0 <= item_todelete < len(todos):
                print(f"'{todos[item_todelete].strip()}' was successfully marked as completed.")
                todos.pop(item_todelete)
                write_todos(todos, 'todos.txt')

            else:
                print('Number is out of range.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    elif user_action.startswith("exit"):
        break

    else:
        print('Invalid command')

print("End of program")
