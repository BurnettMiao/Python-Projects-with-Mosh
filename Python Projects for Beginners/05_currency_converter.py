# Loop
    # Ask the user for an amount
    # If invalid
    #   Print an error

# Loop
    # Ask for the source currency
    # If invalid
    #   Print an error

# Loop
    # Ask for the target currency
    # If invalid
    #   Print an error

# Do the conversion
# Print the result

def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <=0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amout')

def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        if currency not in currencies:
            print('Invalid currency')
        else:
            return currency
        
def convert(amount, source_currency, target_currency):
    exchange_rates = {
        'USD': {'EUR': 0.85, 'CAD': 1.25},
        'EUR': {'USD': 1.18, 'CAD': 1.47},
        'CAD': {'EUR': 0.80, 'CAD': 0.68},
    }

    if source_currency == target_currency:
        return amount
    
    return amount * exchange_rates[source_currency][target_currency]


def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f}')


if __name__ == "__main__":
    main()