print("Salary System")
name = input("Enter employee name: ")
basic = float (input("Enter basic salary: "))
hra = float (input("Enter HRA: "))
da = float(input("Enter DA: "))

gross = basic + hra + da
tax = gross * 0.10
net = gross - tax

if net > 50000:
 print("High Salary")
elif net > 30000:
 print("Medium Salary")
else:
 print("Low Salary")
print("Gross:", gross)
print("Net:", net)

for i in range(5):
 print(i)
print("System Ended")