import operations
import structure as s
import ui
import re

number = 2  # минимальное количество знаков в списке участника розыгрыша

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Введите более {n} символов\n')
        text = input('Введите значение: ')
    else:
        return text
    
def check_len_num_input():
    flag_text = True
    while flag_text:
        flag_text=False
        text = input('Введите сумму вашего чека: ')
        try:
            for i in text:
                if i.isdigit() is not True:
                    raise ValueError("Чек должен состоять из цифр! ")
        except Exception:
            print("Чек должен состоять из цифр! ")
            flag_text=True
        text = str(text)
    else:
        return text


def create_note(number):
    title = check_len_num_input()
    body = check_len_text_input(
        input('Введите Ваше имя и фамилию: '), number)
    return s.Note(title=title, body=body)

def add_participans():
    note = create_note(number)
    array = operations.participans_read_file()
    for notes in array:
        if s.Note.get_id(note) == s.Note.get_id(notes):
            s.Note.set_id(note)
    array.append(note)
    operations.participans_write_file(array, 'a')
    print('\033[32mЗаметка успешно добавлена!\033[39m')


def show_winners(text):
    logic = True
    array = operations.winners_read_file()
    if text == 'date':
        date = input('Введите дату в формате ДД.ММ.ГГГГ (например, 25.10.2020): ')
    for notes in array:
        if text == 'all':
            logic = False
            print(s.Note.map_note_winners(notes))
        if text == 'id':
            logic = False
            print('ID: ' + s.Note.get_id(notes))
        if text == 'date':
            logic = False
    if logic == True:
        print('На эту дату нет заметок')



def id_edit_del_show_toys(text):
    id = input('Введите ID необходимой заметки: ')
    array = operations.toys_read_file()
    logic = True
    for notes in array:
        if id == s.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = create_note(number)
                s.Note.set_title(notes, note.get_title())
                s.Note.set_body(notes, note.get_body())
                print('\033[32mЗаметка успешно изменена!\033[39m')
            if text == 'del':
                array.remove(notes)
                print('\033[31mЗаметка удалена\033[39m')
            if text == 'show':
                print(s.Note.map_note_toys(notes))
    if logic == True:
        print('С таким ID заметок нет, возможно ввели неверный ID')
    operations.toys_write_file(array, 'a')

def id_edit_del_show_participans(text):
    id = input('Введите ID необходимой заметки: ')
    array = operations.participans_read_file()
    logic = True
    for notes in array:
        if id == s.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = create_note(number)
                s.Note.set_title(notes, note.get_title())
                s.Note.set_body(notes, note.get_body())
                print('\033[32mЗаметка успешно изменена!\033[39m')
            if text == 'del':
                array.remove(notes)
                print('\033[31mЗаметка удалена\033[39m')
            if text == 'show':
                print(s.Note.map_note_participans(notes))
    if logic == True:
        print('С таким ID заметок нет, возможно ввели неверный ID')
    operations.toys_write_file(array, 'a')

def id_edit_del_show_winners(text):
    id = input('Введите ID необходимой заметки: ')
    array = operations.winners_read_file()
    logic = True
    for notes in array:
        if id == s.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = create_note(number)
                s.Note.set_title(notes, note.get_title())
                s.Note.set_body(notes, note.get_body())
                print('\033[32mЗаметка успешно изменена!\033[39m')
            if text == 'del':
                array.remove(notes)
                print('\033[31mЗаметка удалена\033[39m')
            if text == 'show':
                print(s.Note.map_note_winners(notes))
    if logic == True:
        print('С таким ID заметок нет, возможно ввели неверный ID')
    operations.toys_write_file(array, 'a')

def show_participans(text):
    logic = True
    array = operations.participans_read_file()
    if text == 'date':
        date = input('Введите дату в формате ДД.ММ.ГГГГ (например, 25.10.2020): ')
    for notes in array:
        if text == 'all':
            logic = False
            print(s.Note.map_note_participans(notes))
        if text == 'id':
            logic = False
            print('ID: ' + s.Note.get_id(notes))
        if text == 'date':
            logic = False

    if logic == True:
        print('На эту дату нет заметок')