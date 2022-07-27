# LEGB Rule
# Local - names assigned in a func (def or lambda)
# E Enclosing funcs locals - Names in local scope of any and all enclosing funcs, from inner to outer.
# G Global (modeule) - Names assigned at the top level of a module, or declared global in a def within the file
# B Built in (Python) - Names preassigned in the build in names module: range open SyntaxError

# local variable example
lambda num: num ** 2

# num here is local

# Global one
name = 'This is a global string'


def greet():
    # Enclosing one
    name = 'Enclosing'

    def hello():
        # local one
        name = 'local'
        print('hello ' + name)

    hello()


greet()

# what if we comment internal name sammy

# Built in funcs, example len, should not overrite


# Brain fck, making global var changes via local var call, very interesting
# Using global keyword
varGlobal = 'Global Var'

def changing_global_var():
    global varGlobal
    print(f'Glolbal var is {varGlobal}')
#     local assignment on global var
    varGlobal = 'Local Var'
    print(f'Global var is now changed to {varGlobal}')

print(varGlobal)
changing_global_var()
print(varGlobal)

# Beginner should avoid using global
# Use return in the method and set it.
