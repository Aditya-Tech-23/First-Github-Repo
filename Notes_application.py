print("*"*150)
print()
print(f"{'NOTES APP':-^150}")
print()
print("*"*150)

names=[]
def create():
        
        global names
        name=input("Enter the name of the file : ").strip()
        names.append(name)
        f=open(f"{name}.txt","w")
        print("File Created Successfully")
        f.close()
def open_file():
        name=input("Enter the name of the file you want to open : ").strip()
        if name in names:
                f=open(f"{name}.txt","r")
                print(f.read())
                f.close()
        else:
                print("File Not Found")
def edit():
    
    
    name=input("Enter name of the file you want to edit : ").strip()
    if name in names:
            
            f=open(f"{name}.txt","a")
            print("Enter the text you want to write :")
            while True:
               text=input()
               f.write(text)
               f.write("\n")
               while True:
                       n=input("Enter Y to go to next line or S to save the file : ").strip()
                       if n=="Y" or n=='y':
                               break
                       elif n=="S" or n=='s':
                               print("File Saved Successfully")
                               f.close()
                               break
                       else:
                               print("Invalid Input")
               if n=="Y" or n=="y":
                       continue
               else:
                       break
            
                    
               
        
            
            
    else:
        
            print("File Not Found")
            
while True:
    print("1. Create File")
    print("2. Open File")
    print("3. Edit File")
    print("4. Exit")
        
    a=input("Enter your choice: ")
    if int(a)==1:
                
                create()
                
        
    if int(a)==2:
        
        
        open_file()
        
    if int(a)==3:
        
        
        edit()
    if int(a)==4:
        print()
        print("*"*150)
        print()
        print(f"{'THANK YOU':^150}")
        print()
        print("*"*150)
        break
