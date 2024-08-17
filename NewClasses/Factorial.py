#Nested loop = Combination if two loop
print("Welcome to Bank Of India ATM")
restart=('Y')
chances = 3
balance = 90
while chances >= 0:
    pin = int(input("Please Enter your 4 digit pin: "))
    if pin == (1234):
        print("Your Enterd pin is correct\n")
        while restart not in ('n','No','no','N'):
            print('Please press 1 for your balance:/n')
            print('Please press 2 to make a withdraw:/n')
            print('Please press 3 to pay:/n')
            print('Please press 4 to return card:/n')
            option = int(input('what would you like to choose?'))
            if option == 1:
                print('Your Balance is:', balance)
                restart = input('would you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('Y')
                withdrawl = float(input('how much would u like to withdraw?'))
                if withdrawl in [10, 20, 30, 40, 50, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('\nYour balance is now', balance)
                    restart = input('would you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 30, 40, 50, 60, 80, 100]:
                    print('Invalid Amount, please retry/n')
                    restart = ('Y')
                elif withdrawl == 1:
                    withdrawl = float(input('please enter valid amount:'))

            elif option == 3:
                Pay_in = int(input('how moch would you like to Pay in? '))
                Total = int(balance + Pay_in)
                print('\nYour balance is now:', Total)
                restart = input('would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option ==4:
                        print('please wait while your card is returned....\n')
                        print('Thank you For Your Services')
                        break
            else:
                print('Please Enter a Correct Number.\n')
                restart = ('Y')
    elif pin != ('1234'):
        print("incorrect password")
        chances = chances - 1
        if chances ==0:
            print('\nNO more tries')
            break