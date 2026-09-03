import time
f=open("Expense tracker.txt","a+")


def add_expense():
	global f
	
	
	f=open("Expense tracker.txt","r")
	print()
	
	exp_name=input("Enter expense name- ")
	print()
	while True:
		try:
			
			amt=int(input("Enter amount:  "))
			if amt>0:
				
				break
			else:
				print("Negative amount not allowed")
				
				
			
			
		except:
			print("Please enter valid amount")
		
	
	
	
	
	if f.read=="":
		f=open("Expense tracker.txt","a")
		f.write(f"1. {exp_name} : {amt}\n")
		f.close()
	else:
		l=f.readlines()
		f=open("Expense tracker.txt","a")
		f.write(f"{len(l)+1}. {exp_name} : {amt}\n")
		f.close()
	f.close()
	
def view_expense():
	global f
	print()
	
	f=open("Expense tracker.txt")
	print(f.read())
	f.close()
def total():
	f=open("Expense tracker.txt")
	lines=f.readlines()
	f.close()
	print()
	print("-"*50)
	print()
	s=0
	for i in lines:
		s=s+int(i[len(i)-2:i.index(":"):-1][::-1])
	print("Total :",s)
	
def clear():
	f=open("Expense tracker.txt","w")
	f.close()
	print("All expenses cleared successfully !")
	
def highest():
	print()
	f=open("Expense tracker.txt")
	if f.read()!="":
		f.close()
		f=open("Expense tracker.txt")
		lines=f.readlines()
		f.close()
		greatest_calculate=[]
		for i in lines:
			greatest_calculate.append(int(i[len(i)-2:i.index(":"):-1][::-1]))
		print(f"Highest expense : {max(greatest_calculate)}")
	else:
		print("No expenses available(")
f.close()
# actual program begins	
print("-"*50)
print()
print(f"{'📒 Student Expense Traker 📒':^50}")
print()
print("-"*50)
print()
print("1. Add expense")
print("2. View expenses")
print("3. Calculate Total")
print("4. Clear Expenses")
print("5. Find Highest expense")
print("6. Exit")
while True:
	print()
	print("-"*50)
	print()
	while True:
		try:
			ch=int(input("Enter your choice: "))
			if ch>=1 and ch<=6:
				print()
				print("Loading.......")
				time.sleep(2)
				break
			else:
				print("Please enter a valid number")
		except:
			print()
			print("Please enter numbers only")
			print()
			
		
	
	if ch==1:
		add_expense()
	if ch==2:
		view_expense()
	if ch==3:
		total()
	if ch==4:
		clear()
	if ch==5:
		highest()
	if ch==6:
		print()
		print("-"*50)
		print()
		print(f"{' <--Thank you--> ':😊^35}")
		print()
		print("-"*50)
		print()
        
		break
