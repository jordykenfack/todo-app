import functions
import FreeSimpleGUI as sg


label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter a todo here', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',enable_events=True,size=[45,10])
Edit_button = sg.Button('Edit')
Complete_button = sg.Button('Complete')
Exit_button = sg.Button('Exit')
window = sg.Window('My To-Do App',
                   layout= [[label],[input_box,add_button],[list_box,Edit_button,Complete_button],[Exit_button]],
                   font= ('Helvetica',18))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo'].update(value = todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo =  values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break


window.close()
