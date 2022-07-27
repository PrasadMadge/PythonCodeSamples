stock_prices = [('Apple', 200), ('Google', 500), ('Micorsoft', 100)]

for item in stock_prices:
    print(item)

# tuple unpacking
for company, price in stock_prices:
    print(company)

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 900)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    return (employee_of_month, current_max)  # returning tuple


print(employee_check(work_hours))

name, hours = employee_check(work_hours)
print(name)
print(hours )