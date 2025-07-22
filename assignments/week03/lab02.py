balance = 1000
pin = 1234

while True :
    try:
        entered_pin = int(input('Enter PIN: '))
        if entered_pin == pin:
            print('PIN accepted')
            break
        else:
            print ('Invaild PIN')
    except ValueError:
        print('Pleses enter PIN again.')
while True:
    try:
        print('\n1. Check Balance')
        print('2. withdraw')
        print('3. Deposit')
        print('4. Exit')

        choice = int(input('Choose option: '))
        if choice == 1:
            print(f'Your balance is: {balance}')
        elif choice == 2:
            amount = int (input('Enter amount to withdraw:'))
            if amount > balance:
                print(f'You have {balance}in your balance')
            elif amount <= 0:
                print('Amount must be positive')
            else:
                balance -= amount
                print(f'Withdraw {amount}. New balane: {balance}') 
        elif choice ==3 :
            amount = int(input('Enter amount to deposit:'))
            if amount <= 0:
                print('Amount must be positive')
            else:
                balance += amount
                print(f'Deposit {amount}. New balane: {balance}') 
        elif choice == 4:
            print('Thank you.')
            break
        else:
            print('Invalid choice.')
    except ValueError:
        print('Invalid choice. Please enter a number.')