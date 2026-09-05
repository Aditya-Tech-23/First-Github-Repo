import random
ch=""
def chance():
    global ch
    
   
    while True:
        print()
        print("="*150)
        print()
        ch=input("Do you want to play again ? (Yes/No) : ").strip().title()
        print()
        print()
        print("-"*150)
        print()
        print()
        if ch=="Yes":
            gaming()
        elif ch=="No":
            print()
            print("~"*150)
            print()
            print(f"{'THANK YOU':^150}")
            print()
            print("~"*150)
            print()
            break
        else:
            print("Invalid Input --> Enter Yes/No")

def gaming():
    
    print("*"*150)
    print()
    print(f"{'NUMBER GUESSING GAME':^150}")
    print()
    print("*"*150)
    print()
    num=random.randint(1,10)
    c=0
    while True:
        print()
        print("="*150)
        print()
        while True:
            try:
               a=int(input("Guess a no. from 1 to 10 :- "))
               if (str(a)).isdigit()==True:
                   break
            except ValueError:
               print("Please enter numbers only")
        if a not in range(1,11):
            print()
            print("Please guess a number from 1 to 10")
        elif num==a:
            c=c+1
            if c>1:
               print()
               print(f"You guessed the number in {c} steps !")
               
               chance()
               if ch=="No":
                    break
               
            else:
               print()
               print(f"You guessed the number in {c} step !")
               chance()
               if ch=="No":
                   break
               
               
               
               
               
            
        elif num<a:
            c=c+1
            print()
            print("Go a little lower")
        else:
            c=c+1
            print()
            print("Go a little higher")

            
gaming()
