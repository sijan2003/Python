import random

A = ['▩' for _ in range(26)]
B = [i for i in range(0, 26)]
C = ['▩' for _ in range(26)]

def clear_screen():
    print("\033[H\033[J")

def board():
    i = 0
    n = 0
    for _ in range(5):
        for _ in range(5):
            print(f'| {A[i]:^2} |', end=' ')
            i += 1
        print(end='      ')
        for _ in range(5):
            print(f'| {B[n]:^2} |', end=' ')
            n += 1
        print()
    print('-' * 40, '    ', '-' * 40)

def set_bombs(initial_guess):
    bomb_indices = random.sample(range(len(A)), 6)
    if initial_guess in bomb_indices:
        bomb_indices.remove(initial_guess)
    for index in bomb_indices:
        A[index] = '&'

def display_board():
    clear_screen()
    i = 0
    n = 0
    for _ in range(5):
        for _ in range(5):
            print(f'| {C[i]:^2} |', end=' ')
            i += 1
        print(end='      ')
        for _ in range(5):
            print(f'| {B[n]:^2} |', end=' ')
            n += 1
        print()
    print('-' * 40, '    ', '-' * 40)

def mechanics():
    count = 0
    display_board()
    a = int(input("Choose a number: "))
    if A[a] == '&':
        print("Game Over! You hit a bomb!")
        return False
    # Check for win condition
    if C.count('▩') == 6:
        print("Congratulations! You won the game!")
        return False
    if a % 5 != 0 and A[a - 1] == '&':
        count += 1
    if a % 5 != 4 and A[a + 1] == '&':
        count += 1
    if a >= 5 and A[a - 5] == '&':
        count += 1
    if a < 20 and A[a + 5] == '&':
        count += 1
    if a % 5 != 0 and a >= 5 and A[a - 6] == '&':
        count += 1
    if a % 5 != 4 and a >= 5 and A[a - 4] == '&':
        count += 1
    if a % 5 != 0 and a < 20 and A[a + 4] == '&':
        count += 1
    if a % 5 != 4 and a < 20 and A[a + 6] == '&':
        count += 1
    C[a] = str(count)
    B[a] = 'X'
    return True

def first_move(ui):
    mechanics()

    for _ in range(8):
        while True:
            randomj = random.randint(0, 24)
            if C[randomj] == '▩' and randomj != ui:
                break

        count = 0
        row = randomj // 5
        col = randomj % 5

        if col > 0 and A[randomj - 1] == '&':
            count += 1
        if col < 4 and A[randomj + 1] == '&':
            count += 1
        if row > 0 and A[randomj - 5] == '&':
            count += 1
        if row < 4 and A[randomj + 5] == '&':
            count += 1
        if col > 0 and row > 0 and A[randomj - 6] == '&':
            count += 1
        if col < 4 and row > 0 and A[randomj - 4] == '&':
            count += 1
        if col > 0 and row < 4 and A[randomj + 4] == '&':
            count += 1
        if col < 4 and row < 4 and A[randomj + 6] == '&':
            count += 1

        C[randomj] = str(count)

    display_board()

def lets_play():
    print("MINESWEEPER!!!!!!!!!!!!!!!!!!!!!!")
    ui = int(input("Enter the initial guess (0-24): "))
    set_bombs(ui)
    first_move(ui)
    while True:
        if not mechanics():
            break

board()
lets_play()
