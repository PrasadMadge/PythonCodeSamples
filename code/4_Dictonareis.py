# syntax
employee = {'prasad': 123, 'Rahul': 1234}
print(employee)

print(employee.get('prasad'))

# to get paring
print(employee)

# iterating an dictonarie

print('for each with employee')
for employ in employee:
    print(employ)

# interesting, by default while iteration a dictonary you only iterate in keys
# to iterate in items, both key value

print('for each in items')
for employ in employee.items():
    print(employ) # returns tuples,

# hence same tuple unpacking technique could be used to unpack it.
for (key, value) in employee.items():
    print(value)