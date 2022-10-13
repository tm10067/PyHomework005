# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# НАЧАЛЬНЫЕ УСЛОВИЯ:

from random import randint

total_candy = 150
min_turn = 1
max_turn = 28
player_switch = randint(1,2)
game_mode = 1
win_switch = 0

# ВЫБОР РЕЖИМА ИГРЫ:

def select_game_mode(game_mode):
    entry = ""
    while entry != "1" or entry != "2":
        entry = input("Для игры с ботом введите 1, для игры вдвоем введите 2: ")
        if entry == "1" or entry == "2":
            game_mode = int(entry)
            break
        else:
            print("некорректный ввод")
    if game_mode == 1:
            print("Режим игры с ботом")
    elif game_mode == 2:
        print("Режим игры вдвоем")
    else:
        print (f"game_mode error in select {game_mode}")
    return(game_mode)
    
# ПРОВЕРКА НА ВЫИГРЫШ:

def check_win(total_candy, win_switch, player_switch):
    if total_candy == 0:
        win_switch = player_switch
    return win_switch
    
# АЛГОРИТМ БОТА:

def bot_make_turn(total_candy, min_turn, max_turn):
    turn = randint(min_turn, max_turn)
    if total_candy < max_turn * 2 + min_turn:
        turn = max(total_candy - (max_turn  + min_turn), min_turn)
    if total_candy <= max_turn:
        turn = total_candy
    return turn
    
# ТЕЛО ИГРЫ: 

game_mode = select_game_mode(game_mode)
if player_switch == 2:
    player_switch = 3

print(f"На столе {total_candy} конфет")
while win_switch == 0:
    if player_switch == 1:
        current_turn = input("Игрок 1 сколько конфет возьмете: ")
        try:
            current_turn = int(current_turn) 
        except ValueError: 
            print("некорректный ввод (не число)")
            continue 
        if int(current_turn) > max_turn:
            print(f"вы не можете взять больше {max_turn}!)")
            continue 
        elif int(current_turn) < min_turn and total_candy > min_turn:
            print(f"вы не можете взять меньше {min_turn}!)")
            continue 
        else: 
            total_candy -= current_turn
            win_switch = check_win(total_candy, win_switch, player_switch)
            print(f"Осталось {total_candy} конфет")
            if game_mode == 1:
                player_switch = 3
            elif game_mode == 2:
                player_switch = 2
            else:
                print (f"game_mode error {game_mode}")
    elif player_switch == 2:
        current_turn = input("Игрок 2 сколько конфет возьмете: ")
        try: 
            current_turn = int(current_turn) 
        except ValueError: 
            print("некорректный ввод (не число)")
            continue 
        if int(current_turn) > max_turn:
            print(f"вы не можете взять больше {max_turn}!)")
            continue 
        elif int(current_turn) < min_turn and total_candy > min_turn:
            print(f"вы не можете взять меньше {min_turn}!)")
            continue 
        else: 
            total_candy -= current_turn
            win_switch = check_win(total_candy, win_switch, player_switch)
            print(f"Осталось {total_candy} конфет")
            player_switch = 1
    elif player_switch == 3:
        current_turn = bot_make_turn(total_candy, min_turn, max_turn)
        print(f"Бот взял {current_turn} конфет")
        if int(current_turn) > max_turn:
            print("ошибка бота")
            continue 
        elif int(current_turn) < min_turn and total_candy > min_turn:
            print("Ошибка бота")
            continue 
        else: 
            total_candy -= current_turn
            win_switch = check_win(total_candy, win_switch, player_switch)
            print(f"Осталось {total_candy} конфет")
            player_switch = 1
    else:
        print (f"player_switch error {player_switch}")
else: 
    if win_switch == 1 or win_switch == 2:
        print (f"Игрок {win_switch} победил")
    elif win_switch == 3:
        print (f"Бот победил")
    else:
        print (f"win_switch error {win_switch}")