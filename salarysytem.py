print("Salary System")
name = input("Enter employee name: ")
basic = input("Enter basic salary: ")
hra = input("Enter HRA: ")
da = input("Enter DA: ")
gross = basic + hra + da
tax = gross * 0.1
net = gross - tax
if net > 50000
 print("High Salary")
elif net > 30000
 print("Medium Salary")
else
 print("Low Salary")
print("Gross:", gross)
print("Net:", netsalary)
for i in range(5):
print(i)
print("System Ended")