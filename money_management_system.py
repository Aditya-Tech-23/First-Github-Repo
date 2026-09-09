file=open("expenses.txt","a+")
f=open("track.txt","a+")
f=open("track.txt","r")
d=f.read()
if d=="":
    cb=int(input("Enter your current balance: "))
    s=int(input("Enter your Savings: "))
    f=open("track.txt","w")
    f.write(f"Current balance: {cb}\n")
    f.write(f"Savings: {s}\n")
    f.close()
else:
    print()
f.close()
def reader():
    global f
    f=open("track.txt","r")
    
    lines=f.readlines()
    f.close()
    bal=int(lines[-2][lines[-2].index(":")+1:lines[-2].index("\n")])
    sv=int(lines[-1][lines[-1].index(":")+1:lines[-1].index("\n")])

        
    sl=[bal,sv]
    return sl
def save():
    global f
    ch=int(input("Enter 1 to save from current balance and 0 if received money externally: "))
    amt=int(input("Enter the amount to be saved: "))
    l=reader()
    if ch==1:
        l[1]+=amt
        l[0]-=amt
        f=open("track.txt","a")
        f.write(f"Current balance: {l[0]}\n")
        f.write(f"Savings: {l[1]}\n")
        f.close()
    elif ch==0:
        l[1]+=amt
        f=open("track.txt","a")
        f.write(f"Current balance: {l[0]}\n")
        f.write(f"Savings: {l[1]}\n")
        f.close()
    
def view_status():
    l=reader()
    print(f"Current balance: {l[0]}")
    print(f"Savings: {l[1]}")
def receive():
    global f
    l=reader()
    amt_r=int(input("Enter the amount received: "))
    ch=int(input("Enter 1 to put it in savings and 0 to not put in savings: "))
    if ch==1:
        l[1]+=amt_r
    elif ch==0:
        l[0]+=amt_r
    f=open("track.txt","a")
    f.write(f"Current balance: {l[0]}\n")
    f.write(f"Savings: {l[1]}\n")
    f.close()
def spend():
    global f
    global file
    exp_name=input("Enter expense name: ")
    exp_amt=int(input("Enter amount: "))
    l=reader()
    l[0]-=exp_amt
    file=open("expenses.txt","r")
    data=file.read()
    line=file.readlines()
    file.close()
    
    if data=="":
        file=open("expenses.txt","a")
        file.write(f"1. {exp_name} : {exp_amt}\n")
        file.close()
    else:
        file=open("expenses.txt","r+")
        
        lines=file.readlines()
    
        file.write(f"{int(lines[-1][0])+1}. {exp_name} : {exp_amt}\n")
        file.close()
    f=open("track.txt","a")
    f.write(f"Current balance: {l[0]}\n")
    f.write(f"Savings: {l[1]}\n")
    f.close()
def view_expenses():
    global file
    file=open("expenses.txt")
    print(file.read())
    file.close()
def borrow():
    amt_b=int(input("Enter the amount you want to borrow from savings: "))
    l=reader()
    l[0]+=amt_b
    l[1]-=amt_b
    f=open("track.txt","a")
    f.write(f"Current Balance: {l[0]}\n")
    f.write(f"Savings: {l[1]}\n")
    f.close()
print("*"*150)
print()
print(f"{'''ADITYA'S MONEY MANAGEMENT SYSTEM''':^150}")
print()
print("*"*150)
print()
while True:
    print()
    print("1. View money status")
    print("2. Saved money")
    print("3. Received Money")
    print("4. Spent Money")
    print("5. View Expenses")
    print("6. Borrow Savings")
    print("7. Exit")
    print()
    choice=int(input("Enter your choice: "))
    if choice==1:
        view_status()
    if choice==2:
        save()
    if choice==3:
        receive()
    if choice==4:
        spend()
    if choice==5:
        view_expenses()
    if choice==6:
        borrow()
    if choice==7:
        break
f.close()
file.close()
        
    
