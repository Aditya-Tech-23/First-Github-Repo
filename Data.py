import time
for i in  range(10,0,-1):
    print(i)
    time.sleep(1)
print(f"{'''Let's Start !!''':^90}")
    
print("*"*90)
print(f'{"Welcome to my data entry system":^90}')
print("*"*90)
print()
text="LET'S BEGIN"
print(f"{text:^50}")
print()
f=open("data entry.txt","w")
a=0
while True:
    a=a+1
    name=input("Enter your name- ")
    gen=input("Enter your gender- ")
    age=input("Enter your age- ")
    mob_no=input("Enter your phone number- ")
    occup=input("Enter your occupation- ")
    f.write(f"{a})   Name: {name}\n")
    f.write(f"     Gender: {gen}\n")
    f.write(f"     Age: {age}\n")
    f.write(f"     Phone number: {mob_no}\n")
    f.write(f"     Occupation: {occup}\n")
    res=int(input("Enter 1 to continue and 0 to stop- "))
    if res==0:
        print()
        print("To access the data entries follow the steps given below:- ")
        print("a) Click on the file option on the top-left corner of the screen.")
        print("b) Select the open option and search 'data entry.txt'")
        print("c) Open the file and see the data entries ")
        print()
        print("-"*90)
        print(f"{'THANK YOU':^90}")
        print("-"*90)
        f.close()
        break
    
    





    
