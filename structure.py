from datetime import datetime
import uuid


class Note:
    def __init__(self, id = str(uuid.uuid1())[0:4],  title = "текст", body = "текст"):
        self.id = id
        self.body = body
        self.title = title        

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title  

    def get_body(note):
        return note.body

    def set_id(note):
        note.id = str(uuid.uuid1())[0:4]

    def set_title(note, title):
        note.title = title 

    def set_body(note, body):
        note.body = body

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body

    def map_note_toys(note):
        return '\n\033[31mID\033[39m: ' + note.id + '\n' + '\033[32mСумма по чеку\033[39m: ' + note.title + '\n' + 'Игрушка\033[39m: ' + note.body

    def map_note_participans(note):
        return '\n\033[31mID\033[39m: ' + note.id + '\n' + '\033[32mСумма по чеку\033[39m: ' + note.title + '\n' + 'Участник\033[39m: ' + note.body

    def map_note_winners(note):
        return '\n\033[31mID\033[39m: ' + note.id + '\n' + '\033[32mСумма по чеку\033[39m: ' + note.title + '\n' + 'Игрушка\033[39m: ' + note.body
