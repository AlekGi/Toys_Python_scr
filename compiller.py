import toys as t
import random
import structure as s



def lines_to_int_toys():  
    array = value_of_toys()
    int_list = [int(i) for i in array]
    toy1 = int(int_list[0])
    toy2 = int(int_list[1])
    toy3 = int(int_list[2])
    array = [toy1, toy2, toy3]
    return array

def lines_to_int_chances():
    with open('_chance.csv', "r", encoding='utf-8') as f:
        array = []
        lines = f.readlines()
        int_list = [int(i) for i in lines]
        chance1 = int(int_list[0])
        chance2 = int(int_list[1])
        chance3 = int(int_list[2])
        array = [chance1, chance2, chance3]
        return array   

def toy_names_list():
        f2 = open("_toys.csv", "r", encoding='utf-8')
        array = []
        notes = f2.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            s.Note(id = split_n[0], title = split_n[1], body = split_n[2])
            array.append(split_n[2])
        return array

def value_of_toys():
        f2 = open("_toys.csv", "r", encoding='utf-8')
        array = []
        notes = f2.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            s.Note(id = split_n[0], title = split_n[1], body = split_n[2])
            split = int(split_n[1])
            array.append(split)
        return array


def show_chance():
    with open("_chance.csv", "r", encoding='utf-8') as f2:
        array_toys_names = toy_names_list()
        chances = f2.readlines()
        print ('Список и количество разыгруемых игрушек: ' + '\n')
        print(array_toys_names[0] + ' - ' + chances[0])
        print(array_toys_names[1] + ' - ' + chances[1])
        print(array_toys_names[2] + ' - ' + chances[2])

def add_chance():
    with open("_chance.csv", "w", encoding='utf-8') as f2:
        flag_text = True
        array = []
        array_toys_names = toy_names_list()
        while flag_text:
            flag_text = False        
            text1 = input('Введите шанс выигрыша игрушки: ' + array_toys_names[0])   
            text2 = input('Введите шанс выигрыша игрушки: ' + array_toys_names[1])
            text3 = input('Введите шанс выигрыша игрушки: ' + array_toys_names[2])
            try:
                for i in text1:
                    if i.isdigit() is not True:
                        raise ValueError('Ошибка! Вы ввели не число')
                for i in text2:
                    if i.isdigit() is not True:
                        raise ValueError('Ошибка! Вы ввели не число')
                for i in text3:
                    if i.isdigit() is not True:
                        raise ValueError('Ошибка! Вы ввели не число')
                array.append(text1)
                array.append(text2)
                array.append(text3)
            except Exception:
                print("Ошибка! Вы ввели не число! ")
                flag_text=True
            f2.write("\n".join(array))

# show_chance()
# add_chance()
# value_of_toys()
# toy_names_list()