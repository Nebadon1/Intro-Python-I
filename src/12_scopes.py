# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
  global x
  x = 99

change_x()

# *****Global Variables*****
#variable declared outside of the function or in global scope is known as a global variable. 
# This means that a global variable can be accessed inside or outside of the function.

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)
    #*****Nonlocal Variables******
    # Nonlocal variable are used in nested function whose local scope is not defined. 
    # This means that the variable can be neither in the local nor the global scope.

outer()
