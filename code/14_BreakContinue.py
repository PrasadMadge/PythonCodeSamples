# break -> breaks out of current closest enclosing loop
# continue -> goes to the top of the closest enclosing loop
# pass -> does nothing at all 😅

n = [1, 2, 3, 4]

for item in n:
    pass  # place holder to avoid syntax error, to deal later or do nothing

name = 'sammy'


# what if we dont want a letter
print('what if we dont want a letter')
for n in name:
    if (n == 'a'):
        continue
    print(n)

# what if we used break here
for n in name:
    if (n == 'a'):
        break
    print(n)


# break with while

x = 0;

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
