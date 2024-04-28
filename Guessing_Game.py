import random
def play_game():
    n=random.randint(1,100)
    chance=10
    count=1
   
    while chance!=0:
            try:
                num=int(input("Enter your guess nummber less than 100 and greater than 1\n"))
                if num < 1 or num >100:
                    print("Invalid input please enter  number between 1 to 100")
                    continue

                if n!=num:
        
                    if num<n:
                        print("You guess is small try again")
                    elif num>n:
                        print("your  guess is greater try again")
                    else:
                     print("YOUR WON Correct guess")
                     return True

                    chance-=1
                    print("remaining chances  are\n ",chance)
                    if chance==0:
                     print("YOU LOSE  try again the corect number was",n)
                     return False
            except ValueError():
             print("Invalid input")
response=input("Press y to play")
while response.lower() == 'y':
    if play_game():
        response = input("Do you want to play again? (y/n): ")
    else:
        response = input("Do you want to try again? (y/n): ")
print("THank you ")


    

    
 

    
    






