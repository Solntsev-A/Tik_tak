def print_table():
    print("", 0, 1, 2)
    for index_id, row in enumerate(playing_field):
        print(f"{index_id}{'|'.join(row)}")


def winner_list():
    cort = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
    for line in cort:
        combo = []
        for dot in line:
            elem = playing_field[dot[1]][dot[0]]
            combo.append(elem)
        if combo == ["x", "x", "x"]:
            return "x"
        elif combo == ["0", "0", "0"]:
            return "0"

def play_start(start_symbol):
    global print_table
    global playing_field
    count = 0
    while True:
        if start_symbol == "x":
            step1 = int(input("Введите координату по горизонтали от 0 до 2-ух для х: "))
            step2 = int(input("Введите координату по вертикали от 0 до 2-ух для х: "))
            if (step1 < 0 or step1 > 2) or (step2 < 0 or step2 > 2):
                print("Попробуйте другие координаты! ")
            else:
                if playing_field[step1][step2] == "-":
                    playing_field[step1][step2] = start_symbol
                    print_table()
                    start_symbol = "0"
                else:
                    print("Позиция занята, введите другую!")
        elif start_symbol == "0":
            step1 = int(input("Введите координату по горизонтали от 0 до 2-ух для 0: "))
            step2 = int(input("Введите координату по вертикали от 0 до 2-ух для 0: "))
            if (step1 < 0 or step1 > 2) or (step2 < 0 or step2 > 2):
                print("Попробуйте другие координаты! ")
            else:
                if playing_field[step1][step2] == "-":
                    playing_field[step1][step2] = start_symbol
                    print_table()
                    start_symbol = "x"
                else:
                    print("Позиция занята, введите другую!")
        else:
            print('Некорректный символ, перезапустите игру.')
        # winner_list()
        if winner_list() == "x":
            print("Победа крестиков")
            print("Конец игры, вы молодец")
            break
        elif winner_list() == "0":
            print("Победа ноликов")
            print("Конец игры, вы молодец")
            break

        count += 1
        if count == 9:
            print("Ничья!")
            break


print("Добро пожаловать в игру, крестики нолики")
print()
start = input("Начало игры, выберите с какого символа хотите начать(x/0):")
playing_field = [["-", "-", "-"] for i in range(3)]
print_table()


if start == "x":
    play_start("x")
elif start == "0":
    play_start("0")
else:
    print('Некорректный символ, перезапустите игру.')



