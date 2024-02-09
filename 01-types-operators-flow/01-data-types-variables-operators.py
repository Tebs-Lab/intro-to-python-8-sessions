# We can create variables by giving them a name, and
# using the assignment operator, the equals sign (=)
# to give them a value.

# Data comes in a variety of types. These two versions
# of the number one are not the same. One is a number, 
# the other is a piece of text.
x = 1
y = '1'

# We can print the "type" of our two variables like this:
print('\n===quotes===')
print(type(x))
print(type(y))

# There are three kinds of numbers in python: integers, floats, and complex numbers
integer_example = 2
float_example = 0.1
complex_example = 4+3j # These are rarely important for most programmers... 

print('\n===number types===')
print(type(integer_example))
print(type(float_example))
print(type(complex_example))

# We can do math with numbers
z = integer_example + float_example

# WAIT: Predict what type and value z has.
print(type(z), z)

# Micro Exercise: create two new variables and assign them:
#  1) the result of dividing z by float_example
#  2) the result of of multiplying z by float_example



# Booleans are either True or False
t = True
f = False

print('\n===booleans===')
print(type(t))
print(type(f))

# Comparison operations result in booleans
# comparisons operators are: <, <=, >, >=, ==, !=
print('1 < 2', 1 < 2)       # True
print('10 >= 10', 10 >= 10) # True
print('10 > 10', 10 > 10)   # False

# There is a special value that means "nothing"
nothing = None

print('\n===None===')
print(type(nothing))

# Micro Exercise: perform three comparisons using the special None value, what are the results?



# And textual data, called strings, are wrapped in quotes
text = "This is a string."
print(type(text))

# Strings have operators too, for example:
# Strings are compared pseudo-alphabetically for greater than / less than
print('"albert" < "bill"', "albert" < "bill") # True

# HOWEVER, in python ALL capital letters come before ANY lowercase letters
print('"B" < "a"', "B" < "a") # True

# FYI: There are additional rules for other characters like $, %, ., and so on
# that we're ignoring for now.

# Strings also have 
x = "hello " + "world." # Concatenation, x is "hello world."
y = "a" * 4 # Duplication, y = "aaaa"

print("===String Operator Results===")
print(x)
print(y)

# Usually, values with different types can't be combined with operators.
# These lines of code raise errors:
x = 1 + '1'
y = 'False' + True


# Sometimes data of one type can be "coerced" into data of another type
text_number = "20"
coerced_int = int(text_number)
coerced_float = float(text_number)

print("\n===Coercion===")
print(type(text_number), text_number)
print(type(coerced_int), coerced_int)
print(type(coerced_float), coerced_float)

# Which allows us to use operators on them
new_result = coerced_int + coerced_float
print(new_result)

# But, not everything can be coerced
int("This will cause an error")

# Micro-Exercise: Coerce both boolean types to int types. What happened?



# Python also provides a function that can report whether or not a string
# can be coerced to an int without actually attempting the coercion.
can_convert = "123"
print(can_convert, can_convert.isnumeric())

cannot_convert = "I'm not a number"
print(cannot_convert, cannot_convert.isnumeric())

# Finally, we can combine the assignment operator and these math operations
# using the following shorthands:
x = 4
x += 3 #  x = x + 3
x -= 1 #  x = x - 1
x *= 2 #  x = x * 2
x /= 4 #  x = x / 4

# Micro-Exercise: predict the value of x. Then write a comparison statement 
# involving x that evaluates to False. Print the result of that comparison.
