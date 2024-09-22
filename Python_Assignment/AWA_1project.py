#!/usr/bin/env python
# coding: utf-8

# ### Python Assignment -  Variables, Operators, and Type Casting 
Name - Vaibhav Limkar 
Date - 03/09/2024
# <mark> 1. Understanding Variables 
# 
# a. Define a variable in Python. Provide an example of how to create a variable that 
# stores your name. 
# b. What is the difference between a variable and a constant? Can we have constants in 
# Python? </mark>
Ans a)  1 - Variables are containers for storing data values.
        2 - In Python - We do not need to declare variables before using them or declare their type
        3 - One Variable can store multiple value 
        4 - Variables can be reassigned to new values, even of a different data type.
        5 - Variable store their data in RAM which volatile means it
        Note - Variables in Python are created the moment you first assign a value to them. You use                  the = operator to assign values to variables.
# In[3]:


Var_1 = "Vaibhav"  #Var_1 is a Variable which store Data and Here Data is Vaibhav
print(Var_1)       #Here we are printing Data inside Var_1


# In[5]:


Var_1 = "Vaibhav","Python","Data" # In Python Variable can be reassign to a new value as mention in point 4
print(Var_1)                      # As mention in point no.4 and we can assign multiple value 


# <mark>b. What is the difference between a variable and a constant? Can we have constants in Python </mark>

# In[15]:


# Variable - Variable is used to store data and we can reassign a new value to variable 
Data = "Vaibhav"
print(Data)


# In[16]:


# Constant - Constant is used to store data and we can't change the value inside throught out the program 
#             and Constant is not applicable in Python but developer use Variable in uppercase to mention that 
#             it is not allow to change a value in that variable 

PI = 3.14 # Here PI is just used variable not constant variable but if needed we can write in comment 
print(PI) # Mention it as Constant variable and not to change data under that Variable 


# ## Working with Different Data Types
Different Data Type 
a. Create variables of the following types in Python: 
1. Integer 
2. Float 
3. String 
4. Boolean 
# In[24]:


# Integer - First_Value(variable) store a int datatype and we get the datatype using inbuilt function type
First_Value = 5
print(type(First_Value))

# Float - Second_Value(variable) store a float data and we get the datatype using inbuilt function type
Second_Value = 3.14
print(type(Second_Value))

# String - String is used to store data in text and mention in single,double and triple quote
Third_Value = "Vaibhav"
print(type(Third_Value))

# Boolean - Boolean is used to store data in True/False and intenally represent True = 1 and False = 2
Fourth_Value = True
print(type(Fourth_Value))

Fifth_Value = False
print(type(Fifth_Value))


# ## 3 - Arithmetic Operators 
# a. Explain the following arithmetic operators with examples: 
# 1. Addition (`+`) 
# 2. Subtraction (`-`) 
# 3. Multiplication (``) 
# 4. Division (`/`) 
# 5. Floor Division (`//`) 
# 6. Modulus (`%`) 
# 7. Exponentiation (``) 

# In[32]:


# Addition(+) -- (+) symbol is used to add 
Add = 2+3
print(Add)

# Subtraction(-) -- (-) symbol is used to subtract 
Sub = 5-3
print(Sub)

# Multiplication(*) -- (*) symbol is used to multplication
Mul = 3*5
print(Mul)

# Divison (/) -- (/) symbol is used to do Divison and gives Quotient
Div = 5/2
print(Div)

# Floor Divison (//) - (//) symbol is used to do Division and gives Quotient(Round Down)
Div = 5/2
print(5//2)

# Modulus (%) - (%) symbol is used to used to do Division and gives Remainder
Mod = 5%2
print(Mod)

# Exponentiation (**) - (**) symbol is used to raise to the power(eg - 2 to the Power 3)
Exp = 2**3
print(Exp)

# b. Write a Python script to calculate the area of a rectangle using variables `length` 
and `width` with values 5 and 10, respectively. Use the multiplication operator. 
# In[8]:


Length = 5                               # Assigning value 5 to Length variable
Width = 10                             # Assigning value 10 to Breadth variable
Area = Length*Width                    # Calculatig Area using Arthmetic Operator (Multiplication)
print("Area of Rectangle:",Area)


# <mark>  4 Comparison and Logical Operators  
# a. Explain the following comparison operators with examples: 
# 1. Equal to (`==`) 
# 2. Not equal to (`!=`) 
# 3. Greater than (`>`) 
# 4. Less than (`<`) 
# 5. Greater than or equal to (`>=`) 
# 6. Less than or equal to (`<=`) </mark>

# In[12]:


# Equal to (==)
Num1 = 5
Num2 = 10
Num1 == Num2 # Checking condition that Num2 is equal to Num1 - If not it will give O/P as False


# In[10]:


# Not Equal to (!=)
Num3 = 4
Num4 = 5
Num != Num2     # Checking condition that Num2 is not equal to Num1 - If not it will give O/P as True


# In[14]:


# Greater than (>)
Num5 = 105
Num6 = 101
Num5 > Num6   # Checking condition that Num6 is greater than Num5 - If yes it will give O/P as True


# In[15]:


# Less than (<)
Num7 = 56
Num8 = 89
Num7 < Num8   # Checking condition that Num7 is less than Num8 - If yes it will give O/P as True


# In[16]:


# Greater than or equal to (>=)
Num9 = 120
Num10 = 110
Num9 >= Num10  # Checking condition that Num10 is greater than or equal to Num9 - If yes it will give O/P as True


# In[18]:


# Less than or equal to (<=)
Num11 = 103
Num12 = 108
print(Num11 <= Num12)# Checking condition that Num11 is less than or equal to Num12 - If yes it will give O/P as True


# <mark> b. Using logical operators (`and`, `or`, `not`), write a Python script that checks if a 
# number is positive and even.</mark>

# In[ ]:


value = int(input("Enter any number"))

# Check if the value is positive and even
if value > 0:            #Here we are checking value is greater than 0 than go to next condition 
    if value % 2 == 0:   #Here we are checking if value divided by 2 then and remainder equal to zero then go to next step 
        print(f"{value} is positive and even.")
    else:
        print(f"{value} is positive but not even.") # If above condition is not satisfield then print this statement
else:
    print(f"{value} is not positive or value is zero.") # If above two conditon not satisfield then print this statement


# <mark> Q5)Type Casting in Python  
# a. What is type casting? Explain the difference between implicit and explicit type 
# casting with examples. 
# b. Write a Python script that: 
# 1. Converts a float to an integer. 
# 2. Converts an integer to a string. 
# 3. Converts a string to a float. 
Type Casting in Python
Type Casting helps in converting value of one data type into another data type as per the user's will for the execution of program

It can be Implicit or Explicit depending on whether the conversion is handled by Python itself or by the programmer
# In[ ]:


# Implicit type casting - Python automatically understnad datatype without using mention it like other language 
# When you perform operations between different types, Python will automatically convert one of the types to another as needed.
num_int = 5        # int
num_float = 3.0    # float

# Python automatically converts the int to float during the operation
result = num_int + num_float

print("Result:", result)          # Output - (float)
print("Type of result:", type(result))  # Output - <class 'float'


# In[ ]:


# Explicit type casting - Using in built function str(),float(),int(),bool(),list(),dicitonary(),tuple() > Programmer can convert the datatype
num1 = 5               # num1 is int datatypehere
num2 = float(num1)     # Here we convert int datatype using inbuilt dataype-float()
print(num1)            # O/P - 5(int)
print(num2)            # O/P- 5.0(float)


# In[16]:


# Write a Python script that:

# 1)Converts a float to an integer.
num3 = 5.0
num4 = int(num3)        # here we convert float to int using inbuilt function int()
print(num3,"We convert float to int:",num4) 
print(type(num3))
print(type(num4))


# In[23]:


# 2)Converts an integer to a string.
num5 = 5
num6 = str(num5)                  # here we convert int to string using inbuilt function str()
print(num5,"We convert int to float:",num6)
print(type(num5))
print(type(num6))


# In[21]:


# 3)Converts a string to a float.
num7 = "5"
num8 = float(num7) 
print(num7,"We convert string to float:",num8) # here we convert string to float using inbuilt function float()
print(type(num7))
print(type(num8))


# 6)Practical Exercise: Mini Calculator Write a Python script that asks the user to input two numbers and then:
# 1-Adds the two numbers and prints the result.
# 2-Subtracts the second number from the first and prints the result.
# 3-Multiplies the two numbers and prints the result.
# 4-Divides the first number by the second and prints the result (handle division by zero).
# 5-Converts the sum of the numbers to a string and prints the type of the result.

# In[28]:


# Mini Calculator Script

# Asking user to input two numbers
num1 = float(input("Enter the first number: ")) # Explicit convertion - If programmer enter any other data type it will convert it into float
num2 = float(input("Enter the second number: ")) # Explicit convertion - If programmer enter any other data type it will convert it into float

# Addition
sum_result = num1 + num2                        # sum of two number 
print(f"Sum of {num1} and {num2} is: {sum_result}") 

# Subtraction                                   # Substraction of two number
sub_result = num1 - num2
print(f"Difference when {num2} is subtracted from {num1} is: {sub_result}")

# Multiplication
mul_result = num1 * num2                        # Multiplication of two number
print(f"Product of {num1} and {num2} is: {mul_result}")

# Division (Handling division by zero)
if num2 != 0:                                   # If num2 is no tequal to 0 then 
    div_result = num1 / num2                    # we are dividing num1 by num2
    print(f"{num1} divided by {num2} is: {div_result}") 
else:
    print("Division by zero is not allowed!")   # If num1 is equal to 0 then execute this condition

# Converting the sum to a string and checking its type
sum_str = str(sum_result)                       # Here we are converting sum(result)variable in above calculation we used that > we are converting value store in sum(result) into string
print(f"The sum converted to string is: {sum_str}") # printing value store in sum_str
print(f"The type of the sum after conversion is: {type(sum_str)}") # Checking data type


# In[ ]:





# In[ ]:




