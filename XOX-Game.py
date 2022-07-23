# Assignment 2
# Ensar Sonmez 21827794
# GoPy Game
board = []  # Game Board
move_records = []  # Records players moves


def get_size():
    row = int(input("What Size Game GoPy? "))
    if row < 3:
        print("Board size must be greater than or equal to 3")
        return get_size()
    else:
        return row


row = get_size()


def board_create(row):
    for i in range(row):
        board.append([])
        for j in range(row):
            board[i].append(row*i+j)
    return board


def board_print():
    for i in range(row):
        for j in range(row):
            output = "{:^3}".format(board[i][j])
            print(output, end="")
        print()


def get_index(bool):
    if bool:
        number = int(input("Player 1 turn--> "))
    else:
        number = int(input("Player 2 turn--> "))

    if number >= row**2 or number < 0:
        print("You must enter valid number")
        return get_index(not bool)
    move_records.append("1")
    first_index = number // row
    second_index = number % row
    if bool:
        return x_move(first_index, second_index, True)
    else:
        return o_move(first_index, second_index, False)


def x_move(first_index, second_index, queue):
    if board[first_index][second_index] != "X" and board[first_index][second_index] != "O":
        board[first_index][second_index] = "X"
    else:
        if board[first_index][second_index] == "X":
            print("You have made this choice before")
        else:
            print("The other player select this cell before")
        move_records.pop()
    return end_check(queue)


def o_move(first_index, second_index, queue):
    if board[first_index][second_index] != "X" and board[first_index][second_index] != "O":
        board[first_index][second_index] = "O"
    else:
        if board[first_index][second_index] == "O":
            print("You have made this choice before")
        else:
            print("The other player select this cell before")
        move_records.pop()
    return end_check(queue)


def end_check(queue):
    end_game = 0  # 0: game continues ; 1: game ends
    # Horizontal
    for i in range(row):
        if board[i][0] == "X" or board[i][0] == "O":
            letter = board[i][0]
            count = 0
            while count < row:
                if board[i][count] == letter:
                    count += 1
                else:
                    count = row + 2
            else:
                if count == row:
                    end_game = 1
                    break
    # Vertical
    for i in range(row):
        if board[0][i] == "X" or board[0][i] == "O":
            letter = board[0][i]
            count = 0
            while count < row:
                if board[count][i] == letter:
                    count += 1
                else:
                    count = row + 2
            else:
                if count == row:
                    end_game = 1
                    break
    # Diagonal
    if board[0][0] == "X" or board[0][0] == "O":
        letter = board[0][0]
        count = 0
        while count < row:
            if board[count][count] == letter:
                count += 1
            else:
                count = row + 2
        else:
            if count == row:
                end_game = 1

    inverse_count = row - 1
    if board[inverse_count][0] == "X" or board[inverse_count][0] == "O":
        letter = board[inverse_count][0]
        count = 0
        while count < row:
            if board[inverse_count][count] == letter:
                count += 1
                inverse_count -= 1
            else:
                count = row + 2
        else:
            if count == row:
                end_game = 1

    board_print()

    if end_game == 1:
        if queue:
            print("Winner X")
        else:
            print("Winner O")
    else:
        if len(move_records) == row**2:
            print("No Winner")
        elif queue:
            get_index(False)
        else:
            get_index(True)


board_create(row)
board_print()
get_index(True)
