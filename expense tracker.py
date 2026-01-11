expenses = []

def add_expenses()
Date = input("enter the date")
category = input("enter the category")
amount = input("enter the amount")
note=input("enter the note")

expenses = date +","+ category +","+ amount+","+amount+","+note
expenses.append(expenses)

file = open("expenses.txt","a")
file.write(expenses+"\n")
file.close()

print("expenses added successfully")

def view_expenses()
try:
file=open("expenses.txt')
print("\nDate|Category|Amount|Note")
print("----------------------------")
for line in file:
data=line.strip().split(",")
print(data[0],"|",data[1],"|",data[2],"|",data[3])
file.close()
print()
except:
print("no such data is available")

def total_expenses()
total=0
try:
file.open("expenses.txt")
for line in file:
data = line.strip().split(",")
total = total+int(date[2])
file.close()
print("\ntotal expenses:",total,"\n")
expect:
print("no such expenses are found")

while true:
print("===Expense Tracker===")
print("1.Add expenses")
print("2.View expenses")
print("3.Total expenses")
print("4.Exit")

choice=input("enter the choices")

if choice==1
add_expenses()
elif 
choice==2
view_expenses()
elif
 choice==3
total_expenses()
elif
 choice==4
print("exit the program"
break
else:
print("Invalid choice.try again.\n")





	



