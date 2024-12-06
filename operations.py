import structure as s

def toys_write_file(array, mode):
    file = open("_toys.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("_toys.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(s.Note.to_string(notes))
        file.write('\n')
    file.close


def toys_read_file():
    try:
        array = []
        file = open("_toys.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = s.Note(
                id = split_n[0], title = split_n[1], body = split_n[2])
            array.append(note)
    except Exception:
        print('\033[31mЕще нет записей\033[39m')
    finally:
        return array
    
def participans_write_file(array, mode):
    file = open("_participans.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("_participans.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(s.Note.to_string(notes))
        file.write('\n')
    file.close


def participans_read_file():
    try:
        array = []
        file = open("_participans.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = s.Note(
                id = split_n[0], title = split_n[1], body = split_n[2])
            array.append(note)
    except Exception:
        print('\033[31mЕще нет записей\033[39m')
    finally:
        return array    

def winners_write_file(array, mode):
    file = open("_winners.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("_winners.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(s.Note.to_string(notes))
        file.write('\n')
    file.close


def winners_read_file():
    try:
        array = []
        file = open("_winners.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = s.Note(
                id = split_n[0], title = split_n[1], body = split_n[2])
            array.append(note)
    except Exception:
        print('\033[31mЕще нет записей\033[39m')
    finally:
        return array   