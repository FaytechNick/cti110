#CTI-110
#P4HW2 - Salary Calculator
#Nicholas Osterkamp
#11/28/23

total_overtime = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

while True:
    employee_name = input("Enter employee name or 'Done' to terminate: ")

    if employee_name.lower() == 'done':
        break

    hours_worked = float(input("How many hours did {} work? ".format(employee_name)))
    pay_rate = float(input("What is {}'s pay rate?".format(employee_name)))

    if hours_worked <= 40:
        regular_pay = pay_rate * hours_worked
        overpay = 0
    else:
        regular_pay = pay_rate * 40
        overpay = (hours_worked - 40) * 1.5 * pay_rate

    gross_pay = regular_pay + overpay

    total_regular_pay += regular_pay
    total_overtime += overpay
    total_gross_pay += gross_pay
    num_employees += 1

    print("\nEmployee Name: {}".format(employee_name))
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Hours Worked", "Pay Rate", "Regular Pay", "Overtime Pay", "Gross Pay"))
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("-" * 15, "-" * 15, "-" * 15, "-" * 15, "-" * 15))
    print("{:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f}".format(hours_worked, pay_rate, regular_pay, overpay, gross_pay))


print("Total number of employeesentered : {}".format(num_employees))
print("Total amount paid for overtime: ${:.2f}".format(total_overtime))
print("Total amount paid for regular hours: {:.2f}".format(total_regular_pay))
print("Total amount paid in gross: ${:.2f}".format(total_gross_pay))



# Initialize variables for totals
# Ask user for employee name
# Check if the user wants to terminate the program
# Ask user for pay rate and hours worked
# Calculate regular pay
# Calculate overtime pay for hours worked beyond 40
# Calculate gross pay
# Update totals
# Display results for the current employee
# Display overall results