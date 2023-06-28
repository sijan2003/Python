def game_description():
    print('_[0]_|_[1]_|_[2]_')
    print("     |     |      ")
    print('_[3]_|_[4]_|_[5]_')
    print("     |     |      ")
    print(' [6] | [7] | [8] ')

    print('\n')

    print("********************\n")
    print("The users should have the understanding that they gonna put the 'X' and 'O' symbols in these compartments which are named above...")
    
A=['0' for x in range (10)]
for i in range (6):
    A[i]='_'
for i in range(6,9):
    A[i]=' '

def game():
    print(A[0],"|",A[1],"|",A[2])
    print(A[3],"|",A[4],"|",A[5])
    print(A[6],"|",A[7],'|',A[8])

def O():
    print("O's turn:")
    print('where do you want to place the O at:')
    x=(int(input()))
    A[x]='O'
    game()

def X():
    print("X's turn:")
    print('where do you want to place the X at:')
    a=(int(input()))
    A[a]='X'
    game()

def check_winner(symbol):
    if (A[0] == A[1] == A[2] == symbol) or \
       (A[3] == A[4] == A[5] == symbol) or \
       (A[6] == A[7] == A[8] == symbol) or \
       (A[0] == A[3] == A[6] == symbol) or \
       (A[1] == A[4] == A[7] == symbol) or \
       (A[2] == A[5] == A[8] == symbol) or \
       (A[0] == A[4] == A[8] == symbol) or \
       (A[2] == A[4] == A[6] == symbol):
        return True
    return False

def lets_play():
    game_description()
    while True:
        O()
        if check_winner('O'):
            print('O won! Game over!')
            break
        elif '_' not in A:
            print('Game tied!')
            break
        X()
        if check_winner('X'):
            print('X won! Game over!')
            break
        elif '_' not in A:
            print('Game tied!')
            break

lets_play()
