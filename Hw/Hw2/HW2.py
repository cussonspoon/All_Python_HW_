name = input("Enter employee's name: ")
hour = float(input("Enter number of hours worked in a week: "))
pay = float(input("Enter hourly pay rate: "))
ftax = float(input("Enter federal tax withholding rate: "))
stax = float(input("Enter state tax withholding rate: "))

tpay = float(hour*pay)
fw = tpay*ftax
sw = tpay*stax

print("Employee Name: " + name)
print("Hours Worked: " + str(hour) )
print("Pay Rate: $" + str(pay))
print("Gross pay: $" + str(hour*pay))
print("Deductions: ")
print("  Federal Withholding(" + format(ftax, "3.2%") + "): $ " + str(tpay*ftax))
print("  State Withholding(" + format(stax, "3.2%") + "): $ " + str(tpay*stax))
print("  Total Deduction : $" + str(fw+sw) )