# Создаем игровое поле 3x3
board = [[' ' for _ in range(3)] for _ in range(3)]


# Функция для отображения игрового поля
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


# Функция для проверки, есть ли выигрышная комбинация
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


# Главная функция игры
def main():
    current_player = 'X'

    for _ in range(9):
        display_board(board)
        print(f"Ходит игрок {current_player}")

        while True:
            try:
                row = int(input("Введите номер строки (0, 1 или 2): "))
                col = int(input("Введите номер столбца (0, 1 или 2): "))
                if board[row][col] == ' ':
                    break
                else:
                    print("Эта клетка уже занята. Попробуйте еще раз.")
            except (ValueError, IndexError):
                print("Неверный ввод. Попробуйте еще раз.")

        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Игрок {current_player} выиграл!")
            break

        current_player = 'O' if current_player == 'X' else 'X'
    else:
        display_board(board)
        print("Ничья!")


if __name__ == "__main__":
    main()
