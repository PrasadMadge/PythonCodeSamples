# two py

import one

print('Top level in two py file')

one.func()

if __name__ == "__main__":
    print('two is running directly')
else:
    print('Two is being imported')

