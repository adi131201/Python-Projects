import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 2,
    "B": 4,
    "C": 2,
    "D": 3
}

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, cnt in symbols.items():
        for _ in range(cnt):
            all_symbols.append(symbol)
    
    columns = []

    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()

def check_results(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else :
             winnings += values[symbol] * bet
             winning_line.append(line+1)
    
    return winnings, winning_line

#the amount which player deposits for playing.
def deposit():
    while True:
        amount  = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Enter a number")
    return amount

#number of lines player is willing to bet on.
def get_num_lines():
    while True:
        lines  = input("Enter number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter number of lines in specified range")
        else:
            print("Enter a number")
    return lines

#takes amount which player will put for each line.
def get_bet():
    while True:
        amount  = input("How much you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Enter a number")
    return amount

def spin(balance):
    lines = get_num_lines()
    while True:
        bet = get_bet()
        if bet*lines > balance:
            print(f"Insufficient balance.\nYour current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${bet * lines}.")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_results(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on: ", *winning_lines)

    return winnings - bet*lines

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to spin again or 'q' to quit.")
        if ans == "q" or ans=="Q":
            break
        balance+=spin(balance)
    print(f"Your balance is ${balance}")

main()