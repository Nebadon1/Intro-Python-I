# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
mylist= list(range(1,5))
y = mylist + y
print(y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
add =[9,10]
x.extend(add)
print(x)


# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE

print("This is the Length of X:", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

def Multiplication(n): 
    return n * 1000 

total = map(Multiplication, x)
print(list(total))
