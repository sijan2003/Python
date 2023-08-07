import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

symbol_count={
   "A":2,
   "B":3,
   "C":4,
   "D":5
}

symbol_values={
   "A":5,
   "B":4,
   "C":3,
   "D":2
}
def check_winnings(columns,lines, bet, values):
   winnings=0
   winning_lines=[]
   for line in range(lines):
      symbol=columns[0][line]
      for column in columns:
         symbol_to_check=column[line]
         if symbol!= symbol_to_check:
            break
      else:
         winnings+=values[symbol]*bet
         winning_lines.append(line+1)
   return winnings, winning_lines

def get_slotmachine_spin(rows, cols, symbols):
   all_symbols=[]
   for symbol, symbol_count in symbols.items():
      for _ in range(symbol_count):
         all_symbols.append(symbol)
   columns=[]
   for _ in range(cols):
      column=[]
      current_symbols=all_symbols[:]# creating the copy of all_symbols because we don't want the repetition of the already used symbols
      for _ in range (rows):      # what it does is changes in current_symbol won't be implemented in the all_symbols
         value=random.choice(current_symbols)
         current_symbols.remove(value)
         column.append(value)
      columns.append(column)
   return columns


def print_slot_machine(columns):
   for row in range(len(columns[0])):
      for i,column in enumerate(columns):
         if i!=len(columns)-1:

          print(column[row],"|",end='')
         else:
            print(column[row])
   print()
         

def deposit():
    while True:

         amount=input("Enter the amount you want to deposit: ")
         if amount.isdigit():
            amount=int(amount)
            if amount>0:
               break
            else:
               print("Enter amount greater than 0")
         else:
            print("Enter a number:")
    return amount
    
 
     
def get_number_of_lines():
   while True:
    lines=input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")?") # this is the method first how we can CONVERT OTHER VARIABLE INTO STRING
    if lines.isdigit():
       lines=int(lines)
       if 1<= lines<= MAX_LINES:
          break
       else :
        print("Invalid input! ")
    else:
       print("Enter a number :")
   return lines

def get_bet():
   while True:
    bet=input(f"Enter your bet on each line ( ${MIN_BET}-${MAX_BET}) ?")      # WE CAN DO THE SAME BY ADDING 'F' AT THE BEGINNING AND WRITING THE VARIABLE INSIDE CURLY BRACES
    if bet.isdigit():
       bet=int(bet)
       if MIN_BET<= bet<= MAX_BET:
          break
       else :
        print("Invalid input! ")
    else:
       print("Enter a number :")
   return bet
def spin(balance):
    
    lines=get_number_of_lines()
    while True:

        bet_amount=get_bet()
        total_bet= lines*bet_amount
        if total_bet<balance:
           break
        else:
           print("Insufficient balance!!!")
   
    print(f'you are betting ${bet_amount} on {lines} lines . So the total bet is  ${total_bet}')
    slots=get_slotmachine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet_amount,symbol_values)
    print(f"you won $ {winnings}")
    print(f"you won on lines: ",*winning_lines)
    return winnings-total_bet


def main():
   balance=deposit()
   while True:
      print(f"current balance is ${balance}")
      ans=input("press enter to spin  (h to quit )")
      if ans=='h':
         break
      
      balance+=spin(balance)
   print(f"you left with ${balance}")
main()