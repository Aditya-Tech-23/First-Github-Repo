print("*"*150)
print()
print(f"{'NOTES APP':-^150}")
print()
print("*"*150)

names=[]
def create():
        global names
        name=input("Enter the name of the file: ").strip()
        names.append(name)
        f=open(f"{name}.txt","w")
        print("File Created Successfully")
        f.close()
def open_file():
        name=input("Enter the name of the file you want to open: ").strip()
        if name in names:
                f=open(f"{name}.txt","r")
                print(f.read())
                f.close()
        else:
                print("File Not Found")
def edit():
        name=input("Enter the name of the file you want to edit: ").strip()
        if name in names:
                f=open(f"{name}.txt","a")
                print("Enter the text you want to write: ")
                print("(Note: - You write maximum 10,000 lines\n      - At the end after writing is over enter '#savefile' to stop writing and save the file.)")
                for i in range(0,10000):
                        text=input()
                        if text.endswith("#savefile"):
                                f.write(f"{text[:(len(text) -9)]}")
                                print("File Saved Successfully")
                                break
                        else:
                                f.write(text+"\n")
                f.close()
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
        elif int(a)==2:
                open_file()
        elif int(a)==3:
                edit()
        elif int(a)==4:
                print()
                print("*"*150)
                print()
                print(f"{'THANK YOU':^150}")
                print()
                print("*"*150)
                break
        else:
                print("Invalid Input")
                       
