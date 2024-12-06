import data as f
import lottery as l
import toys as t
import compiller

def menu():
    print("=" * 36)
    print(" Пожалуйста, введите код операции с клавиатуры\n")
    print(" [1] -- Показать условия розыгрыша игрушек")
    print(" [2] -- Принять участие в розыгрыше игрушек")
    print(" [3] -- Показать всех участников (админ)")
    print(" [4] -- Показать победителей (админ)")
    print(" [5] -- Изменить список рызыгруемых игрушек (админ)")
    print(" [7] -- Старт розыгрыша (админ)")
    print("\n [0] -- Выход")
    print("=" * 36)

def goodbuy():
    print("\033[32mСпасибо, что приняли участие в розыгрыше! Ждём Вас снова \033[33m;)\033[39m")

def conditions():
    toy_name = compiller.toy_names_list()
    toy_price = compiller.value_of_toys()
    print(f"\033[31m    Условия розыгрыша: \033[39m \n В розыгрыше могут принять участие все участники, совершившие покупку на более, чем {toy_price[0]} рублей. \n {toy_price[0]} рублей и более - {toy_name[0]} \n {toy_price[1]} рублей и более - {toy_name[1]} \n {toy_price[2]} рублей и более - {toy_name[2]}")

def run():
    input_from_user = ''
    while input_from_user != '7':
        menu()
        input_from_user = input().strip()
        if input_from_user == '1':                  # 1 Показать условия
            conditions()                          
        if input_from_user == '2':                  # 2 Внести участника
            f.add_participans()                                 
        if input_from_user == '3':                  # 3 Показать участников
            f.show_participans('all')                         
        if input_from_user == '4':                  # 4 Показать победителей
            f.show_winners('all')
        if input_from_user == '5':                  # 5 Изменить игрушку
            t.show_toys('all')
            t.edit_toys('edit')
        if input_from_user == '7':                  # 5 Старт розыгрыша
            l.lottery_start()
            f.show_winners('all')

        if input_from_user == '0':
            goodbuy()
            break