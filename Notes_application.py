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
                print()
                print("_"*150)
                print()
                print()
                f=open(f"{name}.txt","r")
                print(f.read())
                f.close()
                try:
                        f=open(f"{name}.txt","a")
                        choice=int(input("Enter 1 to write further and 0 to not write: "))
                        if choice==1:
                                print("Enter what you want to write further: ")
                                print()
                                print()
                                print("                          |***********************************************************************************************|")
                                print("                          |                                                                                               |")
                                print(f"{'''| IMPORTANT INSTRUCTION --> After completing the writing work type '#savefile' to save the file |''':^150}")
                                print("                          |                                                                                               |")
                                print("                          |***********************************************************************************************|")
                                print()
                                print()
                                for i in range(0,10000):
                                        t=input().strip()
                                        if t.endswith("#savefile") or t.endswith("'#savefile'"):
                                                f.write(f"{t[:len(t)-9]}")
                                                print("File Saved Successfully")
                                                break
                                        else:
                                                f.write(t+"\n")
                                f.close()
                except ValueError:
                        print()
                        print(f"{'Please enter numbers only':=^150} ")
                        print()
                print()
                print("_"*150)
                print()
                
        else:
                print("File Not Found")
def edit():
        name=input("Enter the name of the file you want to edit: ").strip()
        if name in names:
                f=open(f"{name}.txt","a")
                print("Enter the text you want to write: ")
                print("(Note: - At the end after writing is over enter '#savefile' to stop writing and save the file.)")
                for i in range(0,10000):
                        text=input().strip()
                        if text.endswith("#savefile"):
                                f.write(f"{text[:(len(text) -9)]}")
                                print("File Saved Successfully")
                                break
                        else:
                                f.write(text+"\n")
                f.close()
        else:
                print("File Not Found")
def view():
        print()
        print("_"*150)
        print()
        print()


        for i in range(0,len(names)):
                f=open(f"{names[i]}.txt","r")
                content=f.read()
                print(f"{i+1}. {names[i]}")
                print(f"Content: {content}")
                f.close()
        print()
        print("All files are displayed above ")
def delete_notes():
        print()
        d=input("Enter the name of the file whose notes you want to delete: ").strip()
        print()
        if d in names:
                f=open(f"{d}.txt","r")
                data=f.read()
                if data=="":
                        print("Notes Not Found")
                else:
                        f=open(f"{d}.txt","w")
                        f.close()
                        print("Notes deleted successfully")
                        print()
while True:
        print()
        print("-x-"*50)
        print()
        print("1. Create File")
        print("2. Open File")
        print("3. Edit File")
        print("4. View files")
        print("5. Exit")
        print()
        print("-"*150)
        print()
        try:
                a=int(input("Enter your choice: "))
                if a==1:
                   create()
                if a==2:
                   open_file()
                if a==3:
                   edit()
                if a==4:
                   view()
                if a==5:
                   print()
                   print("*"*150)
                   print()
                   print(f"{'> THANK YOU <':~^150}")
                   print()
                   print("*"*150)
                   break
        except ValueError:
                
                print()
                print(f"{'Please enter numbers only':=^150} ")
                print()
                
                
        
        
                       
