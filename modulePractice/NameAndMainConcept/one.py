# one py file

# very imp
# In python all code at indentaiton level 1 are execute by default
# this is not the same as other programming languages
# in python there is an inbuilt var called __name__
# this var gets assigned a name based on how the script is executed
# if executed directly it gets __main__ name assigned

def func():
    print('func in one py')

print("Global level or identation level1  py call")

if __name__ == "__main__":
    print('one file is running directly')
else:
    print('One file is imported')



