' So here we start our programming journey with typing our first code.'  

print("hello World") # this is a print function to print any sentence , word , letter , digits.

# Now we need to know some things about this programming language

# 1. Python was created by Guido van Rossum, and first released on February 20, 1991.
 
# While you may know the python as a large snake, the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python's Flying Circus.

# 2. Features of Python language

# Easy to understand. 
# Free and Open source.
# Its a high level language.
# Portable with any oprating system we use.

# Now we learn that what are modules , comments and pip.

# A module is a file containing code written by somebody else (usually) which can be imported and used in our programs.
# here are two types of modules in Python.

# 1. Built in Modules (Preinstalled in Python)
# 2. External Modules (Need to install using pip)

# Some examples of built in modules are os, random etc.
# Some examples of external modules are tensorflow, flask etc.


# Pip is the package manager for python. You can use pip to install a module on your system.

# Now what is REPL (Read Evaluate Print Loop) Terminal also called REPL. 

# Comments
 
# Comments are used to write something which the programmer does not want to execute. This can be used to mark author
# name, date etc.

# There are two types of comments in python.

# 1. Single Line Comments: To write a single line comment just add a ‘#’ at the start of the line.

# This is a Single-Line Comment

# 2. Multiline Comments: To write multi-line comments you can use ‘#’ at each line 
# or you can use the multiline string (""" """)

"""This is an amazing
example of a Multiline
comment!"""

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Now we will learn about Variables and data types

# A variable is the name given to a memory location in a program it also called identifier.

# RULES FOR CHOOSING AN IDENTIFIER 

# • A variable name can contain alphabets, digits, and underscores.
# • A variable name can only start with an alphabet and underscores.
# • A variable name can’t start with a digit.
# • No while space is allowed to be used inside a variable name.

# Examples of a few variable names are: harry, one8, seven, _seven etc.

# For example:

x = 10 
y = 10

print(x+y) # The output will come 20.

# Some more examples: 

Name = "Sanchay Shukla"
Education = "Data Science"
Age = 20 
Gender = "Male"

# DATA TYPES

# Primarily these are the following data types in Python:

# 1. Integers (0-9 any digts) 

x1 = 123


# 2. Floating point numbers (numbers with decimals Eg: 1.12 , 20.7 , 0.45 , 234.2)

x2 = 1.23


# 3. Strings (Anything which we type in under double quotes will be a string Eg: "Car" , "122" , "Car122" "87.76") And Strings are immutable its too imoprtant to keep it in mind.

x3 = "There are 64 lions"


# 4. Booleans (Sometimes we need to store just two types of value in variable like is it true or false Eg: True and False)

x4 = True
x5 = False

# 5. None (None is just tells us that nothing is assign in a particular variable its empty.)

x6 = None 

# Python is a fantastic language that automatically identifies the type of data for us.

# As we know that python automatically identifies data for us but if we want to check the data type of any data so we can check it by using type function.

# Example : 

print(type(x1)) # Output - <class 'int'>

print(type(x3)) # Output - <class 'str'>

print(type(x5)) # Output - <class 'bool'>

print(type(x6)) # Output - <class 'NoneType'>


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# OPERATORS IN PYTHON 

# 1. Arithmetic operators: 

# Addition (+)

# Eg: x+y , 10 + 90     Output - 100


# Subtraction (-) 

# Eg: x-y , 90 - 10     Output - 80


# Multiplication (*) 

# Eg: x*y , 2*10        Output - 20


# Division (/)  

# Eg: x/y , 3/2        Output - 1.5


# Modulus (%)

# Eg: x%y , 3%2         Output - 1  [When we want to check the reminder value.]



# Floor division/Integer division (//)


# Eg: x//y , 3//2       Output - 1   [Output should be 1.5 but when we use floor division that means we just want an integer value as output.]

 
# Exponent (**)


# Eg: x**y , 5**2       Output - 25 [This operator raises the left operand (base) to the power of the right operand (exponent).]



# 2. Assignment operators: 

#  Simple Assignment Operator (=) [The simple assignment operator is the most commonly used operator in Python. It is used to assign a value to a variable.]

# Eg: x= Put the value , x = 10 , x = Sanchay , y = age 


# Addition Assignment Operator (+=)  [This operator is used to add the value on the right to the variable on the left and then update the value of the variable. 

# Eg: x+=y , x = x+y - x = 10+10 - x = 20     



# Subtraction Assignment Operator (-=) [This operator is used to subtract the right side value from the left side variable and then update the value of the variable.]

# Eg:x-=y , x = x-y , x = 10-10 , x = 0



# Multiplication Assignment Operator (*=) [Using the multiplication assignment operator , multiply the value on the right by the variable's existing value on the left.]

#  Eg: x*=y - x = x*y - x = 10*10 - x = 100
  
# Division Assignment Operator (/=)
 
 
# Eg: x/=y - x = x/y - x = 10/10 - x = 1
 

# Modulus Assignment Operator (%=) 

# Eg: x%=y - x = x%y - x = 10%10 - x = 0


# Floor Division Assignment Operator (//=)
#
# Eg: x//=y , x = x//y , x = 3//2 , x = 1
 
  
# Exponentiation Assignment Operator (**=)

# Eg: x**=y , x = x**y , x = 10**10 , x = 10000000000


# Bitwise AND Assignment Operator (&=) 
# Bitwise OR Assignment Operator (|=) 
# Bitwise XOR Assignment Operator (^=) 
# Bitwise Right Shift Assignment Operator (>>=) 
# Bitwise Left Shift Assignment Operator (<<=) 
# Walrus Operatorgo (:=)





# 3. Comparison operators:
  


# Equals to (==)  

#  Eg: x==y , 8==8 output - True , 8==6 Output - False [The Python equality operator ( == ) checks if two variables or values are equal. The result of the evaluation is either True or False.]


# Not equals to (!=) 

# Eg: x!=y , 5!=5 output - False , 5!=2 output - True [This operator checks the values that if these are not equal then it gives the output true and if its equal then false.]


# Grater than (>) 

# Eg: x>y , 10>15 output - False , 10>8 output - True [Greater than operator: In python, symbol '>' is used as greater than the operator. It returns True if the value on its left side is greater than the value on its right side, False otherwise.]


# Less than (<)

# Eg: x<y , 20<23 output - True , 78<32 output - False [Less than operator: In python, symbol '<' is used as less than operator. It returns True if the value on its right side is greater than the value on its left side, False otherwise.] 

   
# Greater than or Equals to (>=)
 
# Eg: x>=y , 10>=7 output - True , 10>=10 output - True , 9>=7 output - False [Greater than equal to: In python, symbol '>=' is used as greater than equal to operator. It returns True if the value on its left side is greater than or equal to the value on its right side, False otherwise] 


# Less than or Equals to (<=)

# Eg: x<=y , 61<=16 output - False , 61<=61 output - True , 61<=98 output - True [Less than equal to: In python, symbol '<=' is used as less than equal to operator. It returns True if the value on its left side is less than or equal to the value on its right side, False otherwise.]


#  4. Logical operators: and, or, not [In Python, logical operators are used to combine multiple conditions together and evaluate them as a single boolean expression. There are three types of logical operators in Python: `and`, `or`, and `not`. The `and` operator returns `True` if both conditions it is evaluating are true, otherwise it returns `False.]



# And - The `and` operator returns `True` if both conditions it is evaluating are true, otherwise it returns `False

# Or - The Or Operator returns True if either of the conditions is met. Not Operator inverts the result, i.e., True changes to False and Vice versa

# Not - The Python not operator is a logical operator that inverts the truth value of an expression. Using not , the value True becomes False and the other way around.



# 5. membership operators (In , Not in) [Membership Operator in Python: checks whether a given value is a member of a sequence such as strings, lists, and tuples. Two primary types: 'in' (returns True if specified value is found within a sequence) and 'not in' (returns True if specified value is not found within a sequence)]


# 6. Identity operators (is , is not) - [The identity operator is defined as a comparison operator in Python, used to determine whether two variables refer to the same object in memory. It has two forms: "is" and "is not". The "is" operator returns True if both variables point to the same object, while "is not" returns True if they point to different objects.]


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# STRING SLICING AND INDEXING.
# Now we will learn about string slicig.

# An index picks out a specific value from a list or a specific character from a string. But we can also pick out several values to a new list or string. We do this by specifiying two indexes, a start- and end-index.

# In any programming language counting starts from 0 and if we count from ending of the index then it will start from -1.


# For Example - "Sanchay" -  S A N C H A Y   OR   S  A  N  C  H  A  Y
#                            0 1 2 3 4 5 6       -7 -6 -5 -4 -3 -2 -1


# BY USING USING THIS CODE WE WILL GET THE LENGTH OF THE STRING - print(len(Your String))
# For Example

name = "Sanchay"

print(len(name)) # Output - 7



# The index in a string starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:


# sl = name[ind_start:ind_end] it means first index will include and end index will not include.
# For example

namecut = name[0:3]

print(namecut) # Output - San , Here we can see S [Start_index] is included but C [End_index] is not included. 

# S A N C H A Y
# 0 1 2 3 4 5 6

# Some more examples : 

print(name[1]) #Output - a

print(name[0]) #Output - S

print(name[0:4]) #Output - Sanc

print(name[1:5]) #Output - anch

print(name[:3]) #Output - San

print(name[:7]) #Output - Sanchay

print(name[1:]) #Output - anchay

print(name[0:]) #Output - Sanchay

print(name[:]) #Output - Sanchay

# NEGATIVE INDEXING EXAMPLES

# S  A  N  C  H  A  Y
#-7 -6 -5 -4 -3 -2 -1


print(name[-6:-1]) #Output - ancha

print(name[-5:-1]) #Output - ncha

print(name[-2:-1]) #Output - a

print(name[-7:-1]) #Output - Sancha

print(name[-1:-7]) #Output -


# We can also do one thing to find the output of negative indices so here we can covert negative indices into corresponding positve indices.

# for example: 

print(name[-6:-1])

# if we convert this into corresponding positve indices.then it will look like this:

print(name[1:6])

# So here we can see output is same as negative indices.

# NOW WE WILL SEE STRINGS SLICING WITH SKIP VALUE CONCEPT
print(name[1:6:3]) # S A N C H A Y
                   # 0 1 2 3 4 5 6

# some more examples 

AZ = "abcdefghijklmnopqrstuvwxyz"

print(AZ[1:9:4]) # Output - bf

print(AZ[3:12:5]) # Output - di

print(AZ[4:20:6]) #Output - ekq


# -------------------------------------------------------------------------------------------------


# STRING FUNCTIONS

# len() function - tells us the length  of the string

print(len(name)) 

# string.endswith() function - tells us that our string is ending with those characters which we typed in.

print(name.endswith("ay")) 

# capitalize() function - Converts the first character to uppercas.

s1 = "hello world"
print(s1.capitalize())  # Output: "Hello world"

# casefold() function - Converts the string to lowercase.

s2 = "Hello World"
print(s2.casefold())  # Output: "hello world"

# center(width, fillchar) function - Centers the string, padding it with a specified character.

s3 = "hello"
print(s3.center(10, '*'))  # Output: "**hello***"

# count(substring, start, end) function - Counts occurrences of a substring in the string.

s4 = "hello world"
print(s4.count("o"))  # Output: 2

# encode(encoding, errors) function - Encodes the string using the specified encoding.

s = "hello"
print(s.encode('utf-8'))  # Output: b'hello'

# endswith(suffix, start, end function - Checks if the string ends with a specified suffix.

s = "hello world"
print(s.endswith("world"))  # Output: True

# expandtabs(tabsize) function - Expands tabs in the string to multiple spaces.

# s = "hello\tworld"
print(s.expandtabs(4))  # Output: "hello   world"

# find(substring, start, end) function - Finds the first occurrence of a substring.

s = "hello world"
print(s.find("world"))  # Output: 6

# format(*args, **kwargs) function - Formats the string using a dictionary.

s = "Hello, {name}!"
print(s.format_map({"name": "world"}))  # Output: "Hello, world!"

# index(substring, start, end) function - Finds the first occurrence of a substring and raises an error if not found.

s = "hello world"
print(s.index("world"))  # Output: 6

# isalnum() function - Checks if all characters in the string are alphanumeric.

s = "hello123"
print(s.isalnum())  # Output: True

# isalpha() function - Checks if all characters in the string are alphabetic.

s = "hello"
print(s.isalpha())  # Output: True

# isascii() function - Checks if all characters in the string are ASCII.

s = "hello"
print(s.isascii())  # Output: True

# isdigit() function - Checks if all characters in the string are digits.

s = "12345"
print(s.isdigit())  # Output: True

# islower() function - Checks if all characters in the string are lowercase.

s = "hello"
print(s.islower())  # Output: True

# isnumeric()function - Checks if all characters in the string are numeric.

s = "12345"
print(s.isnumeric())  # Output: True


# isspace() function - Checks if all characters in the string are whitespace.

s = "   "
print(s.isspace())  # Output: True

# istitle() function - Checks if the string is titlecased.

s = "Hello World"
print(s.istitle())  # Output: True

# isupper() function - Checks if all characters in the string are uppercase.

s = "HELLO"
print(s.isupper())  # Output: True

# join(iterable) function - Joins elements of an iterable into a string.

s = "-"
print(s.join(["hello", "world"]))  # Output: "hello-world"


# ljust(width, fillchar) function - Left-justifies the string.

s = "hello"
print(s.ljust(10, '*'))  # Output: "hello*****"

# lower() function - Converts all characters to lowercase.

s = "Hello"
print(s.lower())  # Output: "hello"

# lstrip(chars) function - Removes leading characters.

s = "   hello"
print(s.lstrip())  # Output: "hello"

# maketrans(x, y, z) function - Creates a translation table.

table = str.maketrans("aeiou", "12345")
s = "hello"
print(s.translate(table))  # Output: "h2ll4"

# partition(sep) function - Partitions the string into three parts.

s = "hello world"
print(s.partition(" "))  # Output: ('hello', ' ', 'world')

# replace(old, new, count) function - Replaces occurrences of a substring.

s = "hello world"
print(s.replace("world", "there"))  # Output: "hello there"

# rfind(substring, start, end) function - Finds the last occurrence of a substring.

s = "hello world world"
print(s.rfind("world"))  # Output: 12

# rindex(substring, start, end) function - Finds the last occurrence of a substring and raises an error if not found.

s = "hello world world"
print(s.rindex("world"))  # Output: 12

# rjust(width, fillchar) function - Right-justifies the string.

s = "hello"
print(s.rjust(10, '*'))  # Output: "*****hello"

# rpartition(sep) function - Partitions the string into three parts from the end.

s = "hello world"
print(s.rpartition(" "))  # Output: ('hello', ' ', 'world')

# rsplit(sep, maxsplit) function - Splits the string from the end.

s = "hello world"
print(s.rsplit(" ", 1))  # Output: ['hello', 'world']

# rstrip(chars) function - Removes trailing characters.

s = "hello   "
print(s.rstrip())  # Output: "hello"

# split(sep, maxsplit) function - Splits the string into a list.

s = "hello world"
print(s.split())  # Output: ['hello', 'world']

# splitlines(keepends) function - Splits the string at line breaks.

s = "hello\nworld"
print(s.splitlines())  # Output: ['hello', 'world']

#. startswith(prefix, start, end) function - Checks if the string starts with a specified prefix.

s = "hello world"
print(s.startswith("hello"))  # Output: True

# strip(chars) function - Removes leading and trailing characters.

s = "   hello   "
print(s.strip())  # Output: "hello"

# swapcase() function - Swaps case of all characters.

s = "Hello World"
print(s.swapcase())  # Output: "hELLO wORLD"

# title() function - Converts the first character of each word to uppercase.

s = "hello world"
print(s.title())  # Output: "Hello World"

# translate(table) function - Translates the string using a translation table.

table = str.maketrans("aeiou", "12345")
s = "hello"
print(s.translate(table))  # Output: "h2ll4"

# upper() function - Converts all characters to uppercase.

s = "hello"
print(s.upper())  # Output: "HELLO"

# zfill(width) function - Pads the string with zeros on the left.

s = "42"
print(s.zfill(5))  # Output: "00042"

# These methods provide powerful tools for working with and manipulating strings in Python.

# ----------------------------------------------------------------------------------------------

# ESCAPE SEQUENCE CHARACTERS

# 1. \\ - Inserts a backslash character.


print("This is a backslash: \\")  # Output: This is a backslash: \

# 2. \' - Inserts a single quote character.

print('It\'s a nice day.')  # Output: It's a nice day.

# 3. \" - Inserts a double quote character.

print("She said, \"Hello!\"")  # Output: She said, "Hello!"

# 4. \n - Inserts a newline.

print("Hello\nWorld")  # Output: Hello
                       #         World
# 5. \r - Inserts a carriage return.

print("Hello\rWorld")  # Output: World

# 6. \t - Inserts a tab.

print("Hello\tWorld")  # Output: Hello   World

# 7. \b - Inserts a backspace.

print("Hello\bWorld")  # Output: HellWorld

# 8. \f - Inserts a form feed.

print("Hello\fWorld")  # Output: Hello
                       #         World
# 9. \v - Inserts a vertical tab.

print("Hello\vWorld")  # Output: Hello
                       #         World
# 10. \a - Inserts a bell/alert sound.

print("\a")  # Output: (You may hear a beep sound, depending on your environment)
# 11. \0 - Inserts a null character.

print("Hello\0World")  # Output: HelloWorld

# 12. \ooo - Inserts a character based on its octal value.

print("\101")  # Output: A (since 101 in octal is 65 in decimal, which is 'A')

# 13. \xhh - Inserts a character based on its hexadecimal value.

print("\x41")  # Output: A (since 41 in hexadecimal is 65 in decimal, which is 'A')
# 14. \N{name} - Inserts a character based on its Unicode name.

print("\N{GREEK CAPITAL LETTER DELTA}")  # Output: Δ

# 15. \uFFFF - Inserts a Unicode character with a 16-bit hex value.

print("\u03A9")  # Output: Ω (Greek capital letter Omega)

# 16. \UFFFFFFFF - Inserts a Unicode character with a 32-bit hex value.

print("\U0001F600")  # Output: 😀 (grinning face emoji)

# These escape sequences allow you to include special characters in strings that might otherwise be difficult to type directly or have special meaning in the context of your code.

# f string function is a new thing in python after upadte. So here is the example that how is it helpful for us :

name = input("Enter your name:  ")

print(f"Hello How are you ? {name} \nNice to meet you !")

print(s) 

# LISTS AND TUPLES 

# First we learn about list in python. So what is list ?

'''List is a collection which is ordered and changeable. Allows duplicate members. 
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 Set is a collection which is unordered, unchangeable*, and unindexed'''

# And keep one more thing in mind that lists are mutable

# Example: 

list = [10,100,50,500,"Sanchay","Nisha","Akshay"]


# LIST FUNCTIONS 

# 1. append() - Adds an element to the end in list.

# Example: 

list.append("Rohan") 

print(list) # Output - [10, 100, 50, 500, 'Sanchay', 'Nisha', 'Akshay', 'Rohan']

# 2. extend() - Adds all elements of a list (or any iterable) to the end of the current list.

# Example: 

list.extend(["Apple","Banana"])

print(list) # Output - [10, 100, 50, 500, 'Sanchay', 'Nisha', 'Akshay', 'Rohan', 'Apple', 'Banana']

# 3. insert() - Inserts an element at the specified position.

# Example: 

list.insert(4,800) # Here 4 is a indexed number to choose that at what index we want to put this elemnt.

print(list) # Output - [10, 100, 50, 500, 800, 'Sanchay', 'Nisha', 'Akshay', 'Rohan', 'Apple', 'Banana']

# 4. remove() - Removes the first occurrence of an element

# Example:

list.remove("Apple")

print(list) # Output - [10, 100, 50, 500, 800, 'Sanchay', 'Nisha', 'Akshay', 'Rohan', 'Banana']

# 5. pop() - Removes and returns the element at the specified position (default is the last element)

# Example: 

popped_element = list.pop()

print(list) # Output - [10, 100, 50, 500, 800, 'Sanchay', 'Nisha', 'Akshay', 'Rohan']

print(popped_element) # Output - Banana

# 6. clear() - Removes all elements from the list

# Example: 

'''list.clear()

print(list) Output - []'''

# 7. index() - Returns the index of the first occurrence of an element

# Example: 

indexing_of_Akshay = list.index("Akshay")

print(indexing_of_Akshay) # Output - 7

# 8. count() - Returns the number of occurrences of an element

# Example: 

count_of_Nisha = list.count("Nisha")

print(count_of_Nisha) # Output - 1

# 9. sort() - Sorts the list in ascending order (can be modified with reverse=True for descending order)

# Example: 

list1 = [8,6,2,5,1,0,9,10]

list1.sort()

print(list1) # Output - [0, 1, 2, 5, 6, 8, 9, 10]

list1.sort(reverse=True)

print(list1) # Output - [10, 9, 8, 6, 5, 2, 1, 0]
                                                        
# 10. reverse() - Reverses the order of the list         
                                                       
# Example:                                               

list1.reverse()

print(list1) # Output - [0, 1, 2, 5, 6, 8, 9, 10] 

# 11. copy() - Returns a shallow copy of the list 

# Example: 

copy_of_list = list.copy()

print(copy_of_list) # Output - [10, 100, 50, 500, 800, 'Sanchay', 'Nisha', 'Akshay', 'Rohan']


# Built-in Functions


# 12. len() - Returns the number of elements in the list

# Example: 

len_of_list = list.__len__()

print(len_of_list) # Output - 9

# 13. max() - Returns the maximum value in the list

max_value = max(list1)

print(max_value) # Output - 10

# 14. min() - Returns the minimum value in the list

# Example: 

min_value = min(list1)

print(min_value) # Output - 0

# 15. sum() - Returns the sum of all elements in the list

# Example: 

sum_of_list = sum(list1)

print(sum_of_list) # Output - 41

# 16. sorted() - Returns a new list containing all elements in sorted order

# Example: 

sorted_list = sorted(list1)

print(sorted_list) # Output - [0, 1, 2, 5, 6, 8, 9, 10]

# 17. List comprehensions - Provides a concise way to create lists

# Example: 


# TUPLES 

# Methods of Tuples

# 1. count(): Returns the number of times a specified value appears in the tuple.

# Example: 

t = (1, 2, 3, 2, 4, 2)

print(t.count(2))  # Output: 3

# 2. index(): Searches the tuple for a specified value and returns the position of where it was found.

print(t.index(3))  # Output: 2


# Functions Applicable to Tuples

# 1. len(): Returns the number of items in a tuple.

# Example:

t1 = (1, 2, 3, 4, 5)
print(len(t1))  # Output: 5

# 2. max(): Returns the largest item in the tuple.

t2 = (1, 2, 3, 4, 5)
print(max(t2))  # Output: 5

# 3. min(): Returns the smallest item in the tuple.

# Example: 

t3 = (1, 2, 3, 4, 5)
print(min(t3))  # Output: 1

# 4. sum(): Returns the sum of all items in the tuple.

# Example: 

t4 = (1, 2, 3, 4, 5)
print(sum(t4))  # Output: 15

# 5. sorted(): Returns a sorted list of the tuple's items.

# Example:

t5 = (3, 1, 4, 2)
print(sorted(t5))  # Output: [1, 2, 3, 4]

# 6. any(): Returns True if any item in the tuple is true.

# Example: 

t6 = (0, False, 5)
print(any(t6))  # Output: True

# 7. all(): Returns True if all items in the tuple are true.

# Example:

t7 = (1, True, 3)
print(all(t7))  # Output: True

# 8. tuple(): Converts an iterable (e.g., list) to a tuple.

# Example:

lst = [1, 2, 3]
t = tuple(lst)
print(t)  # Output: (1, 2, 3)


# Other tuple oprations

# 1. Indexing: Accessing an element in a tuple.

# Example: 

tt = (1, 2, 3)
print(tt[1])  # Output: 2

# 2. Slicing: Accessing a range of elements in a tuple.

# Example: 

ta = (1, 2, 3, 4, 5)
print(ta[1:4])  # Output: (2, 3, 4)

# 3. Concatenation: Combining two tuples.

# Example:

t111 = (1, 2, 3)
t222 = (4, 5)
t333 = t111 + t222
print(t333)  # Output: (1, 2, 3, 4, 5)

# 4. Repetition: Repeating a tuple.

# Example: 

ty = (1, 2)
t28 = ty * 3
print(t28)  # Output: (1, 2, 1, 2, 1, 2)


# 5. Membership: Checking if an item exists in a tuple.

# Example:

tw = (1, 2, 3)
print(2 in tw)  # Output: True
print(4 in tw)  # Output: False



# Dictionaries and Sets 



# dictionaries are mutable data structures that allow you to store key-value pairs.



marks = {
    "Sanchay" : 100,
    "Neha" : 90,
    "Rohan" : 100,
    "Sneha" : 95

}

print(type(marks), marks) 


# Dictionary Methods 

# 1. dict.clear() - Removes all items from the dictionary.

# Example: 

zen = {"Tony": 9788709098,"kuku":546456}

zen.clear()

print(zen) # Output - {}

# 2. dict.copy() -  Returns a shallow copy of the dictionary.

# Example:

sonu = {"Tony": 12 ,"Shila":7}

sonu_copy = sonu.copy()
print(sonu_copy) # Output - {'Tony': 12, 'Shila': 7}

# 3.dict.fromkeys(iterable, value=None) -  Creates a new dictionary with keys from iterable and sets all values to value

# Example:

keys = ('a', 'b', 'c')
d = dict.fromkeys(keys, 0)
print(d)  # Output: {'a': 0, 'b': 0, 'c': 0}

# 4. dict.get(key, default=None) -  Returns the value for key if key is in the dictionary; otherwise, returns default.

# Example: 

d = {'a': 1, 'b': 2}
print(d.get('a'))      # Output: 1
print(d.get('c', 3))   # Output: 3


# 5. dict.items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs.

# Example:

d = {'a': 1, 'b': 2}
print(d.items())  # Output: dict_items([('a', 1), ('b', 2)])

# 6. dict.keys() - Returns a view object that displays a list of all the dictionary's keys.

# Example: 

d = {'a': 1, 'b': 2}
print(d.keys())  # Output: dict_keys(['a', 'b'])

# 7. dict.pop(key, default=None) - Removes and returns the value associated with key. If key is not found, default is returned if provided

# Example: 

d = {'a': 1, 'b': 2}
print(d.pop('a'))     # Output: 1
print(d.pop('c', 3))  # Output: 3

# 8. ict.popitem() - Removes and returns the last key-value pair as a tuple. Raises a KeyError if the dictionary is empty

# Example: 

d = {'a': 1, 'b': 2}
print(d.popitem())  # Output: ('b', 2)

# 9. dict.setdefault(key, default=None) - Returns the value of key if key is in the dictionary. If not, inserts key with a value of default and returns default

# Example:

d = {'a': 1}
print(d.setdefault('a', 2))  # Output: 1
print(d.setdefault('b', 3))  # Output: 3

# 10. dict.update(other) - Updates the dictionary with the key-value pairs from other, overwriting existing keys.

# Example: 

d = {'a': 1}
d.update({'b': 2, 'c': 3})
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 11. dict.values() -  Returns a view object that displays a list of all the dictionary's values.

# Example: 

d = {'a': 1, 'b': 2}
print(d.values())  # Output: dict_values([1, 2])



# Built-in Dictionary Functions


# 1. len(dict) - Returns the number of items in the dictionary.

# Example: 

d = {'a': 1, 'b': 2}
print(len(d))  # Output: 2

# 2. dict(key=..., ...) - Creates a new dictionary from keyword arguments or from an iterable of key-value pairs.

# Example:

d1 = dict(a=1, b=2)
print(d1)  # Output: {'a': 1, 'b': 2}

d2 = dict([('a', 1), ('b', 2)])
print(d2)  # Output: {'a': 1, 'b': 2}

# 3. dict(**kwargs) - Creates a new dictionary from keyword arguments.

# Example: 

d = dict(a=1, b=2)
print(d)  # Output: {'a': 1, 'b': 2}

# 4. dict(iterable) - Creates a new dictionary from an iterable of key-value pairs.

# Example:

pairs = [('a', 1), ('b', 2)]
d = dict(pairs)
print(d)  # Output: {'a': 1, 'b': 2}


# SETS IN PYTHON.

# Set is a collection of non-repetitive elements.

# PROPERTIES OF SETS

# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# Set Methods

# 1. set.add(elem)

# Description: Adds an element elem to the set. If elem is already in the set, it has no effect.

# Example:

s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# 2.set.clear()

# Description: Removes all elements from the set.

# Example:

s = {1, 2, 3}
s.clear()
print(s)  # Output: set

# 2.set.copy()

# Description: Returns a shallow copy of the set.

# Example:

s = {1, 2, 3}
s_copy = s.copy()
print(s_copy)  # Output: {1, 2, 3}

# 3.set.discard(elem)

# Description: Removes the element elem from the set if it is present. Does nothing if elem is not present.
 # Example:

s = {1, 2, 3}
s.discard(2)
print(s)  # Output: {1, 3}

# 4.set.pop()

# Description: Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.

# Example:

s = {1, 2, 3}
elem = s.pop()
print(elem)  # Output: 1 (or 2 or 3, since it's arbitrary)
print(s)     # Output: {2, 3} (or {1, 3} or {1, 2})

# 5.set.remove(elem)

# Description: Removes the element elem from the set. Raises a KeyError if elem is not present.

# Example:

s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}

# 6.set.discard(elem)

# Description: Removes elem from the set if present. Does nothing if elem is not present.

# Example:

s = {1, 2, 3}
s.discard(4)  # Does nothing
print(s)  # Output: {1, 2, 3}

# 7.set.update(*others)

# Description: Updates the set, adding elements from all others iterables.

# Example:

s = {1, 2}
s.update([3, 4], {5, 6})
print(s)  # Output: {1, 2, 3, 4, 5, 6}

# 8.set.intersection_update(*others)

# Description: Updates the set to keep only elements found in all others iterables.

# Example:

s = {1, 2, 3, 4}
s.intersection_update([2, 3], {3, 4})
print(s)  # Output: {3}

# 9.set.difference_update(*others)

# Description: Updates the set to remove elements found in others iterables.

# Example:

s = {1, 2, 3, 4}
s.difference_update([2, 4])
print(s)  # Output: {1, 3}

# 10.set.symmetric_difference_update(other)

# Description: Updates the set to keep only elements that are in exactly one of the sets.

# Example:

s = {1, 2, 3}
s.symmetric_difference_update([3, 4, 5])
print(s)  # Output: {1, 2, 4, 5}

# 11.set.union(*others)

# Description: Returns a new set with elements from the set and all others iterables.

# Example:

s = {1, 2}
u = s.union([3, 4], {5, 6})
print(u)  # Output: {1, 2, 3, 4, 5, 6}

# 12.set.intersection(*others)

# Description: Returns a new set with elements found in all others iterables.

# Example:

s = {1, 2, 3, 4}
i = s.intersection([2, 3], {3, 4})
print(i)  # Output: {3}

# 13.set.difference(*others)

# Description: Returns a new set with elements in the set that are not in others iterables.

# Example:

s = {1, 2, 3, 4}
d = s.difference([2, 4])
print(d)  # Output: {1, 3}

# 14.set.symmetric_difference(other)

# Description: Returns a new set with elements that are in either the set or other, but not in both.

# Example:

s = {1, 2, 3}
sd = s.symmetric_difference([3, 4, 5])
print(sd)  # Output: {1, 2, 4, 5}

# 15.set.isdisjoint(other)

# Description: Returns True if the set has no elements in common with other, otherwise False.

# Example:

s = {1, 2, 3}
print(s.isdisjoint([4, 5]))  # Output: True
print(s.isdisjoint([2, 4]))  # Output: False

# 16.set.issubset(other)

# Description: Returns True if all elements of the set are in other.

# Example:

s = {1, 2}
print(s.issubset({1, 2, 3}))  # Output: True
print(s.issubset({1, 3}))     # Output: False

# 17.set.issuperset(other)

# Description: Returns True if all elements of other are in the set.

# Example:

s = {1, 2, 3}

print(s.issuperset([1, 2]))  # Output: True
print(s.issuperset([1, 4]))  # Output: False

# 18.set.pop()

# Description: Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.

# Example:

s = {1, 2, 3}

elem = s.pop()
print(elem)  # Output: 1 (or 2 or 3, since it's arbitrary)
print(s)     # Output: {2, 3} (or {1, 3} or {1, 2})


# Built-in Set Functions


# 1. len(set)

# Description: Returns the number of elements in the set.

# Example:

s = {1, 2, 3}
print(len(s))  # Output: 3

# 2.set(iterable)

# Description: Creates a new set from an iterable, removing duplicates.

# Example:

lst = [1, 2, 2, 3]
s = set(lst)
print(s)  # Output: {1, 2, 3}

# 3.set.union(*iterables)

# Description: Returns a new set with all elements from the set and all iterables.

# Example:

s = {1, 2}
u = s.union([3, 4], {5, 6})
print(u)  # Output: {1, 2, 3, 4, 5, 6}

# 4.set.intersection(*iterables)

# Description: Returns a new set with elements found in all iterables.

# Example:

s = {1, 2, 3, 4}
i = s.intersection([2, 3], {3, 4})
print(i)  # Output: {3}

# 5.set.difference(*iterables)

# Description: Returns a new set with elements in the set that are not in iterables.

# Example:

s = {1, 2, 3, 4}
d = s.difference([2, 4])
print(d)  # Output: {1, 3}

# 6.set.symmetric_difference(other)

# Description: Returns a new set with elements in either the set or other, but not in both.

# Example:

s = {1, 2, 3}
sd = s.symmetric_difference([3, 4, 5])
print(sd)  # Output: {1, 2, 4, 5}

# 6.set.isdisjoint(other)

# Description: Returns True if the set has no elements in common with other, otherwise False.

# Example:

s = {1, 2, 3}
print(s.isdisjoint([4, 5]))  # Output: True
print(s.isdisjoint([2, 4]))  # Output: False

# 7.set.issubset(other)

# Description: Returns True if all elements of the set are in other.

# Example:

s = {1, 2}
print(s.issubset({1, 2, 3}))  # Output: True
print(s.issubset({1, 3}))     # Output: False

# 8.set.issuperset(other)

# Description: Returns True if all elements of other are in the set.

# Example:

s = {1, 2, 3}
print(s.issuperset([1, 2]))  # Output: True
print(s.issuperset([1, 4]))  # Output: False




# CONDITIONAL EXPRESSION

# if,elif,else 

# Conditional statements (if, else, and elif) are fundamental programming constructs that allow you to control the flow of your program based on conditions that you specify.
# They provide a way to make decisions in your program and execute different code based on those decisions.

# Example:

xcx = int(input("Enter Your Age: "))

if(xcx>18):
    print("Yes You are eligible for the ticket.")
    print("Thanks for cominf.")

elif(xcx==18):
    print("Yes Your are just eligible.")

elif(xcx==0):
    print("You haver entered an invalid age.")


else:
    print("Sorry to say but you are  not eligible for this.")
    print("See you soon.")



# LOOPS IN PYTHON

# Looping means repeating something over and over until a particular condition is satisfied. A for loop in Python is a control flow statement 
# that is used to repeatedly execute a group of statements as long as the condition is satisfied. Such a type of statement is also known as an iterative statement.

# There are 2 types of loops. While loop and for loop. 

# Example:

for l in range(1,11): # range(stop) -> range object range(start, stop[, step]) -> range object

 print(l)


men = 0

while(men<15):
   print("men")
   men+=2


enz = [1, "hello", 3.14, True]

i = 0 

while(i<len(enz)):
   print(enz[i])

   i += 1 
print("End of the program")

for k in range(100):
   if(k==77):
      break
   print(k)


for p in range(60):
   pass

tuv = 18

print   
 


 

 





























