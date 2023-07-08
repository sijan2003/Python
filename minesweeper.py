def mechanics():
    count = 0
    display_board()
    a = int(input("Choose the number: "))
    if A[a] == '&':
        print("Game Over! You hit a bomb!")
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

    # Check for win condition
    if C.count('*') == 6:
        print("Congratulations! You won the game!")
        return False
    return True