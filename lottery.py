import structure as s
import compiller
import random
import string 
from random import choice
import data as q


def lottery_start():
    with open("_participans.csv", "r", encoding='utf-8') as f1:
        with open("_winners.csv", "w", encoding='utf-8') as f3:
            array_toys_value = compiller.lines_to_int_toys()
            array = []
            notes = f1.read().strip().split("\n")
            array_toys_names = compiller.toy_names_list()
            for n in notes:
                split_n = n.split(';')
                s.Note(id = split_n[0], title = split_n[1], body = split_n[2])
                split = int(split_n[1])
                if array_toys_value[1] > split >= array_toys_value[0]:      
                    array.append(s.Note(id = split_n[0], title = split_n[1], body = split_n[2] + ' - Выигрыш: ' + array_toys_names[0]))
                f3.seek(0)
                if array_toys_value[2] > split >= array_toys_value[1]:
                    array.append(s.Note(id = split_n[0], title = split_n[1], body = split_n[2] + ' - Выигрыш: ' + array_toys_names[1]))
                f3.seek(0)
                if split >= array_toys_value[2]:
                    array.append(s.Note(id = split_n[0], title = split_n[1], body = split_n[2] + ' - Выигрыш: ' + array_toys_names[2]))
                for notes in array:
                    f3.write(s.Note.to_string(notes))
                    f3.write('\n')
                f3.seek(0)
        
        f3.close

# def wins_random():
#     with open("_participans.csv", "r", encoding='utf-8') as f1:
#         with open("_winners.csv", "r", encoding='utf-8') as f2:
#             with open("_wins.csv", "w", encoding='utf-8') as f3:
#                 array_toys_value = compiller.lines_to_int_toys()
#                 array = []
#                 notes = f1.read().strip().split("\n")
#                 array_toys_names = compiller.toy_names_list()
#                 print(array_toys_value[0])
#                 print(array_toys_value[1])
#                 print(array_toys_value[2])
#                 print(array_toys_names[0])
#                 print(array_toys_names[1])
#                 print(array_toys_names[2])
#                 for n in notes:
#                     split_n = n.split(';')
#                     s.Note(id = split_n[0], title = split_n[1], body = split_n[2])
#                     split = int(split_n[1])
#                     if array_toys_value[1] > split >= array_toys_value[0]:      
#                         array.append(s.Note(id = split_n[0], title = split_n[1], body = split_n[2] + ' - Выигрыш: ' + array_toys_names[0]))
#                     f3.seek(0)
#                     if array_toys_value[2] > split >= array_toys_value[1]:
#                         array.append(s.Note(id = split_n[0], title = split_n[1], body = split_n[2] + ' - Выигрыш: ' + array_toys_names[1]))
#                     f3.seek(0)
#                     if split >= array_toys_value[2]:
#                         array.append(s.Note(id = split_n[0], title = split_n[1], body = split_n[2] + ' - Выигрыш: ' + array_toys_names[2]))
#                     for notes in array:
#                         f3.write(s.Note.to_string(notes))
#                         f3.write('\n')
#                     f3.seek(0)

#             f3.close


# def win_list():
#     with open('_winners.csv', 'r', encoding='utf-8') as f1:
#         with open('_wins.csv', 'r', encoding='utf-8') as f2:
#             array_toys_value = compiller.lines_to_int_toys()
#             array = []
#             notes = f1.read().strip().split("\n")
#             array_toys_names = compiller.toy_names_list()
#             for n in notes:
#                 split_n = n.split(';')
#                 s.Note(id = split_n[0], title = split_n[1], body = split_n[2])
#                 split = int(split_n[1])
#                 chance = f1.readlines()
#                 print(chance[1])
#                 winner_ticker = [choice(chance) for _ in range(len(array_toys_value))]      
#             print(winner_ticker)


    # print(*map(str.strip, lines))
    # cs = map(str.strip, lines)
    # print(cs)
        



# lottery_start()
# wins_random()
# win_list()




