# CTI-110
# P3HW2 - Salary
# Nicholas Osterkamp
# 11/7/2023

employee_name = input("Enter employee's name: ")

hours_worked = float(input("Enter number of hours worked: "))

pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * (pay_rate * 1.5)

regular_pay = regular_hours * pay_rate

gross_pay = regular_pay + overtime_pay

print("Hours Worked   Pay Rate   Overtime Hours   Overtime Pay   Regular Hour Pay   Gross Pay")
print("--------------------------------------------------------------------------------------")
print(f"{hours_worked:<13.2f} {pay_rate:<12.2f} {overtime_hours:<17.2f} {overtime_pay:<17.2f} {regular_pay:<17.2f} {gross_pay:.2f}")


# 1. Ask the user to enter the employee's name and store it in the variable 'employee_name'.
# 2. Ask the user to enter the number of hours worked and store it as a float in the variable 'hours_worked'.
# 3. Ask the user to enter the employee's pay rate and store it as a float in the variable 'pay_rate'.
# 4. If 'hours_worked' is greater than 40, calculate overtime:
#    a. Set 'overtime_hours' to 'hours_worked' - 40
#    b. Set 'regular_hours' to 40
#    c. Calculate 'overtime_pay' by doing 'overtime_hours' * ('pay_rate' * 1.5)
# 5. If 'hours_worked' is not greater than 40, set 'overtime_hours' to 0 and 'regular_hours' to 'hours_worked'.
# 6. Calculate 'regular_pay' by doing 'regular_hours' * 'pay_rate'.
# 7. Calculate 'gross_pay' by doing 'regular_pay' + 'overtime_pay'.
# 8. Print the results.