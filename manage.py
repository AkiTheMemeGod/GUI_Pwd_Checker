import PySimpleGUI as pg
import Functions as fn
import encrypter as en
path = 'User Accounts/' + fn.whose_session()

def manager():
    global username, password
    en.encrypt_folder(path)

    entry_box1 = pg.InputText(tooltip="enter here", key="todo1", size=(35, 1))
    entry_box2 = pg.InputText(tooltip="enter here", key="todo2", size=(35, 1))
    button_edit1 = pg.Button("Edit Username")
    button_edit2 = pg.Button("Edit Password")
    button_generate = pg.Button("Auto Generate ?")
    button_delete = pg.Button("Delete")
    exit_button = pg.Button("Exit")
    clear_button = pg.Button('Clear all')
    pg.set_options(font=("Arial Bold", 14), icon='assets/image.ico')

    heading = ['UserName', 'Passwords']
    en.decrypt_folder(path)
    pds = fn.get_pd()
    usr = fn.get_usr()

    result_list = []

    for item1, item2 in zip(usr, pds):
        result_list.append([item1, item2])
    tbl1 = pg.Table(values=result_list, headings=heading,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='center', key='table',
                    selected_row_colors='red on #2cc985',
                    enable_events=True,
                    expand_x=True,
                    expand_y=True,
                    enable_click_events=True,
                    background_color='#c3c3c3',
                    header_background_color='#2cc985',
                    text_color='black')

    layout = [[tbl1], [entry_box1, button_edit1, button_delete],
              [entry_box2, button_edit2, button_generate], [clear_button, exit_button]]
    window = pg.Window("Manage",
                       layout,
                       resizable=True,
                       size=(880, 720),
                       background_color='#ebebeb',
                       button_color="#2cc985",
                       location=(500, 100))
    while True:
        event, values = window.read()
        print(values)
        us = list(event[2])
        try:

            username = usr[int(us[0])]
            password = pds[int(us[0])]
            print(username)
            print(password)
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            match event:
                case "Edit Username":
                    selected = username
                    new_todo = values['todo1']
                    ind = usr.index(selected)
                    usr[ind] = new_todo + "\n"
                    fn.put_usr(usr)
                    for item in result_list:
                        if item[0] == selected:
                            item[0] = new_todo
                    window['table'].update(values=result_list)

                    # window.update_animation(time_between_frames=0.2)
                case "Edit Password":
                    selected = password
                    new_todo = values['todo2']
                    ind = pds.index(selected)
                    pds[ind] = new_todo + "\n"

                    fn.put_pd(pds)
                    for item in result_list:
                        if item[1] == selected:
                            item[1] = new_todo
                    window['table'].update(values=result_list)
                case "Auto Generate ?":
                    new_password = fn.gen(24)
                    selected = password
                    new_todo = new_password
                    ind = pds.index(selected)
                    pds[ind] = new_todo + "\n"
                    fn.put_pd(pds)
                    result_list = []

                    for item1, item2 in zip(usr, pds):
                        result_list.append([item1, item2])
                    '''for item in result_list:
                        if item[1] == selected:
                            item[1] = new_todo'''
                    window['table'].update(values=result_list)
                case "Delete":

                    usr.remove(username)
                    pds.remove(password)

                    result_list = []
                    for item1, item2 in zip(usr, pds):
                        result_list.append([item1, item2])
                    fn.put_usr(usr)
                    fn.put_pd(pds)
                    window['table'].update(values=result_list)
                case "Clear all":
                    fn.clear()
                    v1 = fn.get_usr()
                    v2 = fn.get_pd()

                    result_list = []
                    for item1, item2 in zip(v1, v2):
                        result_list.append([item1, item2])
                    fn.put_usr(v1)
                    fn.put_pd(v2)
                    window['table'].update(values=result_list)
                case "Exit":
                    en.encrypt_all()
                    exit()
                    exit()
        except TypeError:
            pass

    window.close()
