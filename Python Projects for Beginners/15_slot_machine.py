# Ask the user for the starting balance
# Validate the balance
#   Positive number
# Loop (while balance > 0)
#   Print the current balance
#   Ask the user to bet
#   Validate the bet
#       Greater than 0
#       Less than the balance
#   Spin the reels
#       Generate three random symbos
#   Display the reels
#   Calculate the payout
#       If three symbols match, payout = bet X 10
#       If two symbols match, payout = bet X 2
#       Else, payout = 0
#   Recalculate the balance
#       balance += payout - bet
#   If balance <= 0
#       Print message
#       Break
#   Else
#       Ask the user if they want to continue playing?
#       If not
#           Break

import random


def get_starting_balance():
    while True:
        try:
            balance = int(input('Enter your starting balance: $'))
            if balance <= 0:
                print('Balance must be a positive number.')
            else:
                return balance
        except ValueError:
            print('Please enter a valid number.')


def get_bet_amount(balance):
    while True:
        try: 
            bet = int(input('Enter your bet amount: $'))
            if bet > balance or bet <= 0:
                print(f'Invalid bet amount. You can bet between $1 and ${balance}')
            else: 
                return bet
        except ValueError:
            print('Please enter a valid number for the bet amount.')


def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '⭐', '🍉']
    # reels = []
    # for _ in range(3):
    #     reels.append(random.choice(symbols))
    # return reels

    return [random.choice(symbols) for _ in range(3)]


def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}')


def calculate_payout(reels, bet):
    if reels[0] == reels[1] == reels[2]:
        return bet * 10
    
    if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet * 2
    
    return 0


def main():
    balance = get_starting_balance()
    
    print('Welcome to the Slot Machine Game!')
    print(f'You start with a balance of ${balance}.\n')

    while balance > 0:
        print(f'Current balance: ${balance}')

        bet = get_bet_amount(balance)
        reels = spin_reels()
        display_reels(reels)
        payout = calculate_payout(reels, bet)

        if payout > 0:
            print(f'You won ${payout}')
        else:
            print('You lost!')

        balance += payout - bet
        if balance <= 0:
            print('You are out of money! Game over.')
            break

        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print(f'You walk away with ${balance}')
            break

        


if __name__ == '__main__':
    main()