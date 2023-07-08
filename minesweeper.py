import random

A = ['▩' for _ in range(25)]
B = [i for i in range(0, 25)]
C = ['▩' for _ in range(25)]

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
    # Use range(25) instead of range(len(A))
    bomb_indices = random.sample(range(25), 6)
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

def count_bombs(index):
    # Create a separate function that returns a count of bombs among the neighboring cells
    count = 0
    row = index // 5
    col = index % 5

    if col > 0 and A[index - 1] == '&':
        count += 1
    if col < 4 and A[index + 1] == '&':
        count += 1
    if row > 0 and A[index - 5] == '&':
        count += 1
    if row < 4 and A[index + 5] == '&':
        count += 1
    if col > 0 and row > 0 and A[index - 6] == '&':
        count += 1
    if col < 4 and row > 0 and A[index - 4] == '&':
        count += 1
    if col > 0 and row < 4 and A[index + 4] == '&':
        count += 1
    if col < 4 and row < 4 and A[index + 6] == '&':
        count += 1

    return count

def mechanics():
    display_board()
    
    # Use a try-except block to handle invalid inputs
    while True:
        try:
            a = int(input("Choose a number: "))
            if not (0 <= a < 25):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 24.")

    if A[a] == '&':
        print("Game Over! You hit a bomb!")
        return False

    # Check for win condition
    if C.count('▩') == 6:
        print("Congratulations! You won the game!")
        return False

    # Use the count_bombs function to get the count of bombs
    count = count_bombs(a)

    C[a] = str(count)
    B[a] = 'X'
    return True

def first_move(ui):
    mechanics()

    # Create a list of all the valid indices that are not the initial guess or a bomb
    valid_indices = [i for i in range(25) if i != ui and A[i] != '&']

    # Use random.sample to select eight of them to reveal
    reveal_indices = random.sample(valid_indices, 8)

    for index in reveal_indices:
        # Use the count_bombs function to get the count of bombs
        count = count_bombs(index)

        C[index] = str(count)

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
