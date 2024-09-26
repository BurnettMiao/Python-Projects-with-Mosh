# ATM
# Attribute:
#   - balance
# Methods
#   - check_balance()
#   - deposit()
#   _ withdraw()

class ATM:
    def __init__(self):
        self.balance = 0
    
    def check_balance(self):
        return self.balance
        

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        
        self.balance += amount
   
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')

        self.balance -= amount


def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print('Please enter a valid number.')


def main():
    atm = ATM()
    while True:
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

        choice = input('Please choose an option: ')
        if choice == '1':
            balance = atm.check_balance()
            print(f'Your current balance is: ${balance}')
        elif choice == '2':
            while True:
                try:
                    amount = get_number('Enter the amount to deposit: ')
                    atm.deposit(amount)
                    print(f'Successfully deposited ${amount}')
                    break

                except ValueError as error:
                    print(error)
        elif choice == '3':
            while True:
                try: 
                    amount = get_number('Enter the amount to withdraw: ')
                    atm.withdraw(amount)
                    print(f'Successfully withdrew ${amount}')
                    break
                    
                except ValueError as error:
                    print(error)
        elif choice == '4':
            print('Thank you for using the ATM.')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()