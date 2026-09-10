# n = int(input('Enter the number of terms: '))
# print('Enter the numbers: ')
# x = [int(input(f'num{i+1}: '))for i in range(n)]
# total = sum(x)
# avg = total / n

# print(f'Average: {avg}')

# ATM SIMULATION

correct_pin = 1234
balance = 5000
attempt = 0

while attempt < 3:
    
    Ipin = input('Enter PIN (x for exit): ')
    
    if(Ipin == correct_pin):
    
        while True:
              print("Enter your choice (1,2,3,4): ")
              print("1.Check Balance")
              print("2.Deposit")
              print("3.Withdraw")
              print("4.Exit")
          
              choice = int(input(''))
          
              match choice:
                  case 1:
                      print(f'Your balance: {balance}')
                  case 2:
                      deposit = int(input("Enter amount to deposit:"))
                      balance = balance + deposit 
                  case 3:
                      withdraw = int(input('Enter amount to withdraw: '))
                      if withdraw <= balance:
                        balance = balance - withdraw
                        print("Withdraw successful")
                      else:
                         print("Insufficient balance")      
                  case 4:
                      print('Exit')
                      break;
                  case _:
                      print("Invalid choice!")  
    elif Ipin == "x":
        break
    else:
        print("Incorrect PIN")
        attempt += 1
        print(f'Number of attempts: {attempt} (max:3) {3-attempt} left')

if attempt == 3:
    print("Your card is blocked")    