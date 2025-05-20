# Python slot machine

import random

symbols_value = {
    "🍒": 3, 
    "🍉": 4, 
    "🍋": 5, 
    "🔔": 10, 
    "⭐": 20
}

def spin_row():
    return [random.choice(list(symbols_value.keys())) for _ in range(3)]

def payment(spin, bet):
    if spin[0] == spin[1] == spin[2]:
        symbol = spin[0]
        winnings = symbols_value[symbol] * bet
        print(f"You won ${winnings}")
        return winnings
    return 0

def main():
    wallet = 100

    print("Welcome to the Python Slots!")
    print(f"You have ${wallet} to bet!")
    
    while wallet > 0:
        try:
            bet = int(input("Amount to bet: "))
            if bet <= 0 or bet > wallet:
                print("Invalid bet")
                continue
        except ValueError:
            print("Invalid bet")
            continue

        wallet -= bet

        spin = spin_row()
        print(" | ".join(spin))

        winnings = payment(spin, bet)
        
        wallet += winnings
        
        print(f"Your wallet has: ${wallet}")
        
        if wallet == 0:
            print("You don't have any money")
            break
        
        keep = input("Do you want to keep playing? (Y/N): ").lower().strip()
        if keep != "y":
            break

if __name__ == "__main__":
    main()

