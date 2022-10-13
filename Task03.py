# НАЧАЛЬНЫЕ УСЛОВИЯ:

field = ["1", "2", "3", "4", "5", "6" ,"7", "8", "9"]
x = "X"
y = "0"
player_switch = 1
game_mode = 1
win_switch = 0

# ПЕЧАТЬ СЕТКИ:

def print_grid():
    print(f"{field[6]:^5}|{field[7]:^5}|{field[8]:^5}")
    print("-----------------")
    print(f"{field[3]:^5}|{field[4]:^5}|{field[5]:^5}")
    print("-----------------")
    print(f"{field[0]:^5}|{field[1]:^5}|{field[2]:^5}")
    return

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

def check_win(field, win_switch, player_switch, x, y):
    list_triplet = [(field[0], field[1], field[2]),
                    (field[3], field[4], field[5]),
                    (field[6], field[7], field[8]),
                    (field[0], field[3], field[6]),
                    (field[1], field[4], field[7]),
                    (field[2], field[5], field[8]),
                    (field[0], field[4], field[8]),
                    (field[2], field[4], field[6])] 
    sum_broken = 0
    for i in list_triplet:   
        if i[0] == i[1] and i[0] == i[2]:
            win_switch = player_switch
            break
        elif x in i and y in i:
            sum_broken += 1
            if player_switch == 1:
                if sum_broken == 8:
                    win_switch = 4
                    break
            elif player_switch == 2 or player_switch == 3:
                if sum_broken == 7:
                    win_switch = 4
                    break
            else:
                print (f"player_switch error (check_win) {player_switch}")
        else:
            continue
    return win_switch

# АЛГОРИТМ БОТА:

def bot_make_turn(field, x, y):
    list_triplet = [(field[0], field[1], field[2]),
                    (field[3], field[4], field[5]),
                    (field[6], field[7], field[8]),
                    (field[0], field[3], field[6]),
                    (field[1], field[4], field[7]),
                    (field[2], field[5], field[8]),
                    (field[0], field[4], field[8]),
                    (field[2], field[4], field[6])] 
    turn = 1
    if field[4] == "5":
        turn = field[4] 
    else: 
        for k in list_triplet: 
            if k[0] != x and k[1] != x and k[2] != x:
                if k[0] != y:
                    turn = k[0]
                    break
                elif k[2] != y:
                    turn = k[2]
                    break
                else:
                    turn = k[1]
                    break
            else:
                for l in field:
                    if l != x and l != y:
                        turn = l
                        break
    for j in list_triplet:
        if j[0] == x and j[1] == x and j[2] != y:
            turn = j[2]
            break
        elif j[0] == x and j[2] == x and j[1] != y:
            turn = j[1]
            break
        elif j[1] == x and j[2] == x and j[0] != y:
            turn = j[0]
            break
    for i in list_triplet:
        if i[0] == y and i[1] == y and i[2] != x:
            turn = i[2]
            break
        elif i[0] == y and i[2] == y and i[1] != x:
            turn = i[1]
            break
        elif i[1] == y and i[2] == y and i[0] != x:
            turn = i[0]
            break
    return turn

# ТЕЛО ИГРЫ:  

game_mode = select_game_mode(game_mode)
print_grid()
while win_switch == 0:
    if player_switch == 1:
        current_turn = input("Игрок 1 введите номер клетки: ")
        try: 
            current_turn = int(current_turn) 
        except ValueError: 
            print("некорректный ход (не число)")
            continue 
        if int(current_turn) > 9:
            print("некорректный ход (больше 9)")
            continue 
        elif str(current_turn) == field[int(current_turn) - 1]:
            field[int(current_turn) - 1] = x
            print_grid()
            win_switch = check_win(field, win_switch, player_switch, x, y)
            if game_mode == 1:
                player_switch = 3
            elif game_mode == 2:
                player_switch = 2
            else:
                print (f"game_mode error {game_mode}")
        else: 
            print("некорректный ход (клетка занята)")
    elif player_switch == 2:
        current_turn = input("Игрок 2 введите номер клетки: ")
        try: 
            current_turn = int(current_turn) 
        except ValueError: 
            print("некорректный ход (не число)")
            continue 
        if int(current_turn) > 9:
            print("некорректный ход (больше 9)")
            continue 
        elif str(current_turn) == field[int(current_turn) - 1]:
            field[int(current_turn) - 1] = y
            win_switch = check_win(field, win_switch, player_switch, x, y)
            print_grid()
            player_switch = 1
        else:
            print("некорректный ход (клетка занята)")
    elif player_switch == 3:
        current_turn = bot_make_turn(field, x, y)
        print(f"Ход бота: {current_turn}")
        if current_turn == field[int(current_turn) - 1]:
            field[int(current_turn) - 1] = y
            win_switch = check_win(field, win_switch, player_switch, x, y)
            print_grid()
            player_switch = 1
        else:
            print("ошибка бота")
    else:
        print (f"player_switch error {player_switch}")
else: 
    if win_switch == 1 or win_switch == 2:
        print (f"Игрок {win_switch} победил")
    elif win_switch == 3:
        print (f"Бот победил")
    elif win_switch == 4:
        print (f"Ничья")
    else:
        print (f"win_switch error {win_switch}")