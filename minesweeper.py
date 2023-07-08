
import random

A = ['*' for i in range(49)]
B = [i for i in range(0, 30)]
C=["*" for i in range (49)]
def clear_screen():
    print("\033[H\033[J") 

def board():
    i = 0
    n = 0
    for _ in range(5):
        for _ in range(5):
            print(f'| {A[i]:^3} |', end=' ')
            i += 1
        print(end='      ')
        for _ in range(5):
            print(f'| {B[n]:^3} |', end=' ')
            n += 1
        print()
        print('-' * 40,'    ','-'*40)


    


def set_bombs():
    for _ in range(6):
        while True:
            randomj = random.randint(0, 25)
            if A[randomj] != '&':
                A[randomj] = '&'
                break

   
def display_board():
    clear_screen()
    i = 0
    n = 0
    for _ in range(5):
        for _ in range(5):
            print(f'| {C[i]:^3} |', end=' ')
            i += 1
        print(end='      ')
        for _ in range(5):
            print(f'| {B[n]:^3} |', end=' ')
            n += 1
        print()
        print('-' * 40,'    ','-'*40)


def mechanics():
    count = 0
    display_board()
    a = int(input("Choose the number: "))
    if A[a] == '&':
        print("Game Over! You hit a bomb!")
        return False
    # Check for win condition
    if C.count('*') == 6:
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

    j = str(count)
    C[a] = j

    
    return True


def first_move():
    mechanics()
    
    for i in range(8):
        while True:
            randomj = random.randint(0, 24)
            if C[randomj] == '*':
                break
        count = 0
        if randomj % 5 != 0 and A[randomj - 1] == '&':
            count += 1
        if randomj % 5 != 4 and A[randomj + 1] == '&':
            count += 1
        if randomj >= 5 and A[randomj - 5] == '&':
            count += 1
        if randomj < 20 and A[randomj + 5] == '&':
            count += 1

        C[randomj] = str(count)

    display_board()

def lets_play():
   print("MINESWEEPER!!!!!!!!!!!!!!!!!!!!!!")

   set_bombs()
   first_move()
   while True:
        if not mechanics():
            break

lets_play()