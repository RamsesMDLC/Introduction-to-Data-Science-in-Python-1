# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#GENERAL INFORMATION ABOUT PYTHON

    #"Python Interpreter": takes the code that we write and converts it...
    #...into the language that the computer’s hardware understands (0s and...
    #...1s, bits and bytes), due to the fact that the computer doesn’t...
    #...actually understand Python at the lowest level. This process is done..
    #...every time you run a Python script.
    
    #"Process to run a code and get an answer":
        #First, it processes the statements of the script and checks for...
        #...correct syntax.
        #Then it compiles the source code to bytecode.
        #Next, it ships that code off for execution, and this is where the..
        #..."Python Virtual Machine" comes into play (which actually runs the...
        #...code that you’ve written at the lowest level).

#WEEK 1 (TRIAL VIDEOS)

#Topic 0.1: Python Functions
def addnum (x1,y1,z1=None):
    r1 = x1+y1+z1
    print (r1)
    return r1

addnum (1,2,4)
print("\n")

#Topic 0.2: Python Types and Sequences
# It is important to say that we can use Python to know the type of variable...
#...we are dealing with the code "type". For instance: We can know if we are...
#...dealing with "int", "float", "string", "function" or "NoneType" as a...
#...result to apply the code "type".
x2 = 23
y2= type (x2)
print(y2)
print("\n")

x3 = 123.4534
y3= type (x3)
print(y3)
print("\n")

x4 = "XXX"
y4= type (x4)
print(y4)
print("\n")

x5 = addnum
y5= type (x5)
print(y5)
print("\n")

x6 = None
y6= type (x6)
print(y6)
print("\n")

#Topic 0.3: Python Types and Sequences
# It is important to say that we can use Python to know the type of sequence...
#...(collection type) we are dealing with the code "type". For instance: We..
#...can know if we are dealing with "list", "tuple" or "dictionary" as a...
#...result to apply the code "type".

#In the case of the "tuple":
    #it is important to say that they are a collection of inmutable data. 
    #One way to recognize that we are working with "tuple" is the parentheses ().
    #We can mix in "tuple": "int", "float", "string", "function" and "NoneType.
    #It is iterable (loops), it means that we can use the code "For"or "while".
    #We can concatenate several tuples.
    #We can repeat a tuple (Work with thee code like a multiplication).
    #We can check if there is a specific item in a tuple.
    #It has an order.

x7 = (3,6,3,"ZXXXX",45.666)
y7= type (x7)
print(y7)
print("\n")

#In the case of the "list":
    #It is important to say that they are a collection of mutable data. 
    #One way to recognize that we are working with "list" is the square...
    #...brackets [].
    #We can mix in "list": "int", "float", "string", "function" and "NoneType".
    #It is iterable (loops), it means that we can use the code "For"or "while"
    #We can concatenate several lists.
    #We can repeat a list (Work with thee code like a multiplication).
    #We can check if there is a specific item in a list.
    #It has an order.

x8 = [3,6,3,"ZXXXX",45.666]
y8= type (x8)
print(y8)
print("\n")

    #In this case we modify the list, when we append the value "1000".

x8.append (1000)
print(x8)
print("\n")
    
    #In this case we apply a loop ("For").

for x9 in x8:
    print (x9)
print("\n")

    #In this case we apply a loop using indexing operator (i.e. square...
    #...bracket to know the position or index) in the "while" loop.

x10 =0
while (x10 != len (x8)):
    print (x8[x10])
    x10= x10 +1
print("\n")

    #In this case we concatenate lists.

x11 = [45,46,78,89]
x12 = [100,200,300,400]
x13 = x11+x12
print (x13)
print("\n")

    #In this case we repeat a list.

x14 = [45,46,78,89]
x15 = x14*3
print (x15)
print("\n")

    #In this case we check if there is a specific item in a list.

x16 = [45,46,78,89]
x17 = 46 in x16
print (x17)
print("\n")

#Topic 0.4: Python Types and Sequences
#We can apply through the indexing operator (i.e. square bracket to know the..
#...position or index) the slicing of string, list or tuple. 

#It is important to say that we can apply the slicing with positive numbers...
#...(slicing from left to right) or with negative numbers (slicing from right...
#...to left).

#Also, it is important to say that when we apply slicing with two values [1:4]...
#...the first value (index value) is inclusive and the second value (index...
#...value) is exclusive.

x18 = "c'est la vie"
x19 = x18[0]
print (x19)
print("\n")

x18 = "c'est la vie"
x20 = x18[0:1]
print (x20)
print("\n")
   

x18 = "c'est la vie"
x21 = x18[0:2]
print (x21)
print("\n") 

x18 = "c'est la vie"
x22 = x18[-1]
print (x22)
print("\n") 

x18 = "c'est la vie"
x22 = x18[-4:-1]
print (x22)
print("\n") 
    
x23 = [30,31,32,33,34]
x24 = x23[2]
print (x24)
print("\n") 

#Topic 0.5: Python Types and Sequences
#We can apply a code to concatenate string.

x25 = "Thomas"
x26 = "Piketty"
x27 = x25+x26
print (x27)
print("\n") 

#We can apply a code to concatenate string (inlcuding a space between the words).

x25 = "Thomas"
x26 = "Piketty"
x27 = x25+" "+x26
print (x27)
print("\n") 

#We can apply a code to search a specific text in a string.

x25 = "Thomas"
x28 = "om" in x25
print (x28)
print("\n") 

#We can apply a code (to be specific, the code "split") to search a specific...
#...text in a string group.

    #Split: returns a word, certain words or all the words that...
    #...belong to a string.

x29op1 = "Thomas Piketty - Capital 21 Century".split(" ")[1:3]
print (x29op1)
print("\n") 

x29op2 = "Thomas Piketty - Capital 21 Century".split(" ")[3]
print (x29op2)
print("\n") 

#Topic 0.6: Python Types and Sequences
# It is important to say that we can use Python to know the type of sequence...
#...(collection type) we are dealing with the code "type". For instance: We..
#...can know if we are dealing with "list", "tuple" or "dictionary" as a...
#...result to apply the code "type".

#In the case of the "dictionary":
    #it is important to say that they are a collection of mutable data. 
    #It is compound by a key and a value. They are in the following way:...
    #...{key:value}.
    #One way to recognize that we are working with "dictionary" is the curly braces {}.
    #We can mix in "dictionary": "int", "float", "string", "function" and "NoneType.
    #It is iterable (loops), it means that we can use the code "For"or "while"...
    #...in the keys o in the values.
    #It has no order.
    
#In this case we are interested in get a value by using the indexing operator.

x30 = {"Christopher Brooks": "brooksch@umich.edu", "Bill Gates": "billg@microsoft.com"}
x31 = x30["Christopher Brooks"]
print(x31)
print("\n") 

#Iterate over all of the values of the dictionary

x30 = {"Christopher Brooks": "brooksch@umich.edu", "Bill Gates": "billg@microsoft.com"}
for email in x30.values():
    print(email)
print("\n") 

#Iterate over all of the items in the dictionary (keys and values).

x30 = {"Christopher Brooks": "brooksch@umich.edu", "Bill Gates": "billg@microsoft.com"}
for name, email in x30.items():
    print(name)
    print(email)
print("\n") 

#Topic 0.7: Python Types and Sequences
#We can unpack a sequence of strings into different variables, like we show...
#...in the folloeing code:
x31 = ("Christopher", "Brooks", "brooksch@umich.edu")
fname, lname, email = x31
print(fname)
print(lname)
print(email)
print("\n") 

#Topic 0.8: Python Types and Sequences
#We can organize or select a a string or a sequence of strings and then put...
#...them in other sequence of strings in the order that we want it, with the...
#...code "format".
sales_record = {"price": 3.24,"num_items": 4,"person": "Chris"}

sales_statement = "{} bought {} item(s) at a price of {} each for a total of {}"

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

print("\n") 

#Topic 0.8: Python Types and Sequences
#We can organize or select a string (in this case the values of the...
#...dictionary through the keys of the dictionary) or a sequence of strings..
#...and then put them in other sequence of strings in the order that we want..
#...it, with the code "format".

#it is imporant to say that the "format" code also allow us to do:.
    #Control a number of different things like decimal places, for floating...
    #...point numbers
    #Put in the positive numbers the plus sign
    #Set the alignment of strings to left or right justified.
    #Use of scientific notation and etc.
    
sales_record = {"price": 3.24,"num_items": 4,"person": "Chris"}

sales_statement = "{} bought {} item(s) at a price of {} each for a total of {}"

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

print("\n")

#Topic 1: String Format
Dictio1 = {"Name":"Ramses","Lastname":"MDLC", "Age":29}
Statement1 = "{} is my name, {} is my lastname and {} is my age"
FinalStatement = Statement1.format(Dictio1["Name"],Dictio1["Lastname"],Dictio1["Age"])
print(FinalStatement)
print("\n") 

#Topic 2: Date and Time.In this case we import the "Datatime" and "Time" modules.
import datetime as dt
import time as tm

#This code returns the current time in seconds since the Epoch (January 1st, 1970)
print(tm.time())
print("\n") 

#2.1: Printing the date from today (year, month, day, hour, minute, second,...
#...milisecond) in a single line. In other words we convert the "timestamp" to...
#..."datetime".
datenow = dt.datetime.fromtimestamp(tm.time())
print(datenow)
print("\n") 

#2.2: Printing one or more values related to the date from today (year, month,...
#...day, hour, minute, second, milisecond) in a single line.
#For instance:
    #dtnow.year
    #dtnow.month
    #dtnow.day
    #dtnow.hour
    #dtnow.minute
    #dtnow.second
                                                                  
print(datenow.year)
print(datenow.year, datenow.month)
print("\n") 

#2.3: We can establish a span of days from today (although I think that...
#...there are more ways to play with the time code) and then can do an addition...
#:..or a sustracion from today of that span of days.

#2.3.1.Establishing the span of days or "Delta Time".
deltatime1 = dt.timedelta(days = 100)
print (deltatime1)
print("\n") 

#2.3.2.Establishing the date of today (year, month, day)
todaydate = dt.date.today()
print (todaydate)
print("\n") 

#2.3.3.Doing the addition of days, in this case the date of today plus the...
#...Deltatime (year, month, day)
print(todaydate + deltatime1)
print("\n") 

#Topic 0.9: Python Basics

#Object-oriented programming (OOP): is a method of structuring a program by...
#...bundling (compactando) related properties and behaviors into individual...
#...objects. 

#Objects: contains data and behavior.

    #Example 1: OOP models real-world entities as software objects that have....
    #...some data associated with them and can perform certain functions.
    
    #Example 2: an object could represent a person with properties like a...
    #...name, age, and address and behaviors such as walking, talking,...
    #...breathing, and running. 

#Class: is used to create user-defined data structures. 

    #Define "functions" called "Methods", which identify the behaviors and...
    #...actions that an object created from the Class can perform with its data.
    #Is a blueprint for how something should be defined (It doesn’t actually..
    #...contain any data). 
    #Python class names are written in Capitalized Words notation by convention.
    
    #Example 3: The "Dog Class" specifies that a name and an age are...
    #...necessary for defining a dog, but it doesn’t contain the name or age...
    #...of any specific dog.

#Instance: is an object that is built from a Class and contains real data. 

    #Example 4: An instance of the Dog Class is not a blueprint anymore...
    #..It’s an actual dog with a name, like Miles, who’s 4 years old.
    
    #Example 5: Put another way, a class is like a form or questionnaire. An...
    #...instance is like a form that has been filled out with information...
    #...Just like many people can fill out the same form with their own...
    #...unique information, many instances can be created from a single class.

#Topic 3: Map Function. Example 1

#The "map function" is one of the basis for functional programming in Python.

#Functional programming is a programming paradigm in which you explicitly...
#... declare all parameters which could change through execution of a given...
#...function.

#It is a way of making lists.

#It's not uncommon to see a parameter for a function, be a function itself. The...
#...map built-in function is one example of a functional programming feature
#...of Python.

#You pass inside "map()" a "function and an iterable", then "map()" will...
#...create an object. This "object" contains the output you would get from...
#...running each iterable element through the supplied function.

#The map function signature looks like this "map(function, iterable)":
    #The first parameter, the function that you want executed, and the second...
    #...parameter, and every following parameter, is something which can be..
    #...iterated upon (all the iterable arguments are unpacked together, and...
    #...passed into the given function)
    
#Map() is iterable, so we can use like a for loop to look at all of the values...
#... or items in the map(). 
    
#In this instance we can see that the "Map function" select the "min value" (a...
#...Python function) from the comparison of every column of "Store 1" and...
#..."Store 2" and stored in the object "A". Finally, we convert this map...
#...object "A" into a list using list(). If the list of one of the stores is...
#...larger or shorter than the other (i.e. having more o less items), then...
#...we are going to see only as a result the comparison between the values...
#...that correspond each other (in matter of list length).

store1 = [1,100,65798]
store2 = [3,6,34]
A = map(min,store1,store2)
print(list(A))
print("\n")

store1b = [1,100,65798]
store2b = [3,6]
Ab = map(min,store1b,store2b)
print(list(Ab))
print("\n")  

#Topic 3: Map Function {without the map() code, but with the map() concept...
#...through a function with several arguments}. Example 3.1

EmptyList = []

def word_search(people, keyword):
    for X in people:
        if keyword in X:
            especificword = X.split()
            especificword1 = especificword[0]
            especificword2 = especificword[-1]
            especificword3 = especificword1 + especificword2
            EmptyList.append(especificword3)
    print(EmptyList) 
    print("\n") 
    return EmptyList
                       
people = ["Dr. Christopher Brooks", "Dr. Kevyn Collins-Thompson", "Dr. VG Vinod Vydiswaran", "Dr. Daniel Romero"]
keyword = "Dr."
word_search(people, keyword)

#Topic 3.01: Map Function. Example 3.1 (Option Coursera - Version 1)

#In this case we can put as an argument in the function the variable "person"...
#...which represent the variable "people" that belong to the "map function"...
#...and also represent the list called "people".

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

print(list(map(split_title_and_name, people)))
print("\n")

#Topic 3.02:
    
#In this case we can put as an argument in the function the variable "peoplex"...
#...which represent the variable "peoplex" that belong to the "map function"...
#...and also represent the list called "peoplex".
    
peoplex = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_namex(peoplex):
    titlex = peoplex.split()[0]
    lastnamex = peoplex.split()[-1]
    return '{} {}'.format(titlex, lastnamex)

print(list(map(split_title_and_namex, peoplex)))
print("\n")

#Topic 3.03:
    
#In this case we can put as an argument in the function the variable "peoplexx"...
#...which represent the list called "peoplex".

def split_title_and_namexx(peoplexx):
    titlexx = peoplexx.split()[0]
    lastnamexx = peoplexx.split()[-1]
    return '{} {}'.format(titlexx, lastnamexx)

peoplexx = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

##############################################################################

##############################################################################

##############################################################################

#Topic 4.1: Lambda Function. (RMDLC)

#Lambda (some features or properties):
    #The "lambda function" is an expression; therefore, it can be named (i.e...
    #...through a variable).
    
    #It is Python's way of creating anonymous functions.
    
    #These are the same as other functions, but they have no name.
    
    #They're simple or short lived and it's easier just...
    #...to write out the function in one line instead of going to the trouble...
    #...of creating a named function (in contrast to a normal function, a...
    #...Python lambda function is a single expression). 
        #Although, in the body of a lambda, we can spread the expression over...
        #...several lines using parentheses or a multiline string (i,e. """ """...
        #...), it remains a single expression.
    
    #It can only contain expressions and can’t include statements (like...
    #..."return", "pass", "assert", or "raise") in its body.
    
    #Are really much more limited than full function definitions.
    
    #They're very useful for simple little data cleaning tasks. 
    
    #In the lambdas, the arguments ("bound variable) don’t have parentheses...
    #...around them (usually). However, we can also have the option (not...
    #...usual) to surround the Lambda function itself and its argument with...
    #...parentheses.
    
    #It can take a single argument or multi-arguments. It is important to say...
    #...that Lambdas that take more than one argument list arguments and...
    #...separating them with a comma (,) but without surrounding them with...
    #...parentheses.
    
    #When we talk about arguments, it is important to say Lambda expressions...
    #...support all the different ways of passing arguments. This includes:
        #Positional arguments
        #Named arguments (sometimes called keyword arguments)
        #Variable list of arguments (often referred to as varargs)
        #Variable list of keyword arguments
        #Keyword-only arguments
    
    #Lambda functions are frequently used with "higher-order functions" (this...
    #...kind of function can take one or more functions as arguments or...
    #...return one or more functions). In essence, lambda function can...
    #...take a function (normal or lambda) as an argument.
    #Some Python higher-order functions include: <-- EXTREMELY IMPORTANT
        #map()
        #filter()
        #functools.reduce()
        #sort()
        #sorted()
        #min()
        #max()
        
    #A disavantage of "Lambda" is that "traceback of an exception" (i.e. the...
    #:..message of error sent by Python when the code is wrong). After the...
    #...execution of the failed or wrong lambda function, the "traceback"...
    #...only identify the function causing the exception as <lambda> (without...
    #...detail in comparison wiht a normal o regular function).
    
    #Lambda has the following components:
        #The keyword: lambda
        
        #A "bound variable" or variables located before the colon (:). It is an...
        #...argument to a lambda function. In contrast, a "free variable" is...
        #...not bound and may be referenced in the body of the expression. A...
        #...free variable can be a constant or a variable defined in the...
        #...enclosing scope of the function.
        
        #A body located after the colon (:).
        
    #Interesting topic Lambdas and in normal functions:
    # Use of "Decorators"
    # Print the name of a function "{f.__name__}"

#Example 4.1.1:
Lambda1 = lambda X:X*2
print(Lambda1(3))
print("\n")

#Example 4.1.2:
Numbers = [5,6,7]

D = map(Lambda1,Numbers)
print(list(D))
print("\n")

#Example 4.1.3:Using Lambdas with map() function.
people = ["Dr. Christopher Brooks", "Dr. Kevyn Collins-Thompson", "Dr. VG Vinod Vydiswaran", "Dr. Daniel Romero"]

Lambda1 = lambda person:"{}{}".format(person.split()[0],person.split()[-1])
print(Lambda1("Dr. Christopher Brooks"))
print("\n")
 
E = map(Lambda1,people)
print(list(E))
print("\n")

#Example 4.1.4:Using Lambdas with map() function.
peopley = ["Dr. Christopher Brooks", "Dr. Kevyn Collins-Thompson", "Dr. VG Vinod Vydiswaran", "Dr. Daniel Romero"]

Lambda1y = lambda persony:"{}{}".format(persony.split()[0],persony.split()[-1])
 
Ey = map(Lambda1y,peopley)
print(list(Ey))
print("\n")

#Example 4.1.5: Using Lambdas with parentheses.
Lambda2 = (lambda x, y: x + y)(15, 5)
print(Lambda2)
print("\n")

#Example 4.1.6: Using Lambdas with other functions (even Lambda) as arguments...
#...Similar to the use of map().

  #First, we establish the Lambda with their arguments (variables and/or...
  #...functions).
    #...For instance, in this case the arguments are:
      #Variable "x1"
      #The function "func1"
high_ord_func1 = lambda x1, func1: x1 + func1(x1)

  #Second, we describe the arguments (variables and/or functions) of the Lambda...
  #...For instance, in this case:
      #The value of "x1" = 2
      #The function "func1(x)" = lambda x1: x1 * x1
high_ord_func1(2, lambda x1: x1 * x1)

#Example 4.1.7: Using Lambdas with other functions as arguments. Similar to...
#...the use of map().

  #First, we establish the Lambda with their arguments (variables and/or...
  #...functions).
    #...For instance, in this case the arguments are:
      #Variable "x2"
      #The function "func2"
high_ord_func2 = lambda x2, func2: x2 + func2(x2)

  #Second, we describe the arguments (variables and/or functions) of the Lambda...
  #...For instance, in this case:
      #The value of "x2" = 9
      #The function "func2(x2)" = xproof2 = x2**x2
def func2(x2):
    xproof2 = x2**x2
    return xproof2

high_ord_func2(9, func2)

#Example 4.1.8: Using Lambdas. The code over several lines (with parentheses)
Lambda3 = (lambda x, y
           : x + y)(5, 5)
print(Lambda3)
print("\n")

#Example 4.1.9: Using Lambdas wiht arguments (to be specific: Positional arguments).

   #Positional arguments are values that are passed into a function based...
   #...on the order in which the parameters were listed during the function...
   #...definition. Here, the order is especially important. And also it is...
   #...important to correspond the same quantity of parameters and arguments...
   #...passed (i.e. fixed function arguments).
   
Lambda4 = (lambda x, y, z: x + y + z)(1, 2, 3)
print(Lambda4)
print("\n")

Lambda5 = (lambda x, y, z=3: x + y + z)(1, 2)
print(Lambda5)
print("\n")

#Example 4.1.10: Using Lambdas wiht arguments (to be specific:Named arguments...
#...{sometimes called Keyword Arguments}).

   #Parameters: are the input variables bounded by parentheses when defining...
   #...a function.
   
   #Arguments: are the values assigned to the Parameters (defined in the...
   #...previous line) when passed into a function or method during a...
   #...function call.
   
       #Default arguments: are keyword arguments whose values are assigned...
       #...at the time of function definition.
   
   #Named arguments (or Keyword Arguments) are values that, when passed into...
   #...a function, are identifiable by specific parameter name, previously defined...
   #...A "keyword argument" is preceded by a parameter and the assignment...
   #...operator (=). In some way the "Keyword arguments (or named arguments)"...
   #...look like a dictionary. Here, the order (of the arguments) is not...
   #...especially important. And also it is important to correspond the same...
   #...quantity of parameters and arguments passed (i.e. fixed function...
   #...arguments).
   
       #It is important to take in count that the Named arguments (or Keyword...
       #...Arguments), when they are listed (before passed into a function. In...
       #...essence, in a "function call") do have to come after "positional...
       #...arguments" and before "default arguments".
       
           #In the example "Lambda6" we put the arguments in the right order...
           #...(positional argument, then the Keyword Argument) If we do not...
           #...follow the right order (Keyword Argument, then the positional...
           #...argument) , we are going to get an syntax error message like...
           #...in the example "Lambda7".
                                               
Lambda6 = (lambda x, y, z=3: x + y + z)(1, y=2)
print(Lambda6)
print("\n")

Lambda7 = (lambda x, y, z=3: x + y + z)(y=2, 1)
print(Lambda7)
print("\n")

#Example 4.1.11: Using Lambdas wiht arguments (to be specific: Variable list...
#...of arguments {often referred to as varargs}).

   #Instead of use "fixed function arguments" (like we from Example 4.1.1 to...
   #...Example 4.1.10), Python allows us to use certain special syntaxes that...
   #...are collectively known as "arbitrary arguments" (or "variable-length...
   #...arguments" or "special symbols"). Those syntaxes, which represent the...
   #...iterables items that would be accessed during a function call, are of...
   #...the forms:

       #*args: for non-keyworded/positional arguments
           # A single asterisk signifies elements of a tuple.
           #Using the *, the variable that we associate with the * becomes an...
           #...iterable (meaning that we can iterate over it, run some...
           #...higher-order functions such as map and filter, etc).
           
   #In essence, we are going to pass into a function an unkown quantity of...
   #...arguments. Those arguments listed during the function definition are...
   #...in the form of elements of a tuple. Here, the order is not especially..
   #...important.                  

Lambda8 = (lambda *args: sum(args))(1,2,3)
print(Lambda8)
print("\n")

#Example 4.1.12: Using Lambdas wiht arguments (to be specific: Variable list...
#...of keyword arguments).

   #Instead of use "fixed function arguments" (like we from Example 4.1.1 to...
   #...Example 4.1.11), Python allows us to use certain special syntaxes that...
   #...are collectively known as "arbitrary arguments" (or "variable-length...
   #...arguments" or "special symbols"). Those syntaxes, which represent the...
   #...iterables items that would be accessed during a function call, are of...
   #...the forms:
           
       # **kwargs: for keyworded arguments.
           # Double asterisks signify elements of a dictionary.                                            
           #Using the **, the variable that we associate with the * becomes an...
           #...iterable (meaning that we can iterate over it, run some...
           #...higher-order functions such as map and filter, etc).
           
   #In essence, we are going to pass into a function an unkown quantity of...
   #...arguments. Those arguments listed during the function definition are...
   #...in the form of a dictionary. Here, the order is not especially important.                    
                         
Lambda9 = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
print(Lambda9)
print("\n")

#Topic 4.2: Lambda Practices (W3 Resources)
# https://www.w3resource.com/python-exercises/lambda/index.php
#Problem 1
#Write a Python program to create a lambda function that adds 15 to a...
#..given number passed in as an argument, also create a lambda function...
#...that multiplies argument x with argument y and print the result.

LambdaP1p1 = lambda X:X+15
print(LambdaP1p1(10))
print("\n")

LambdaP1p2 = lambda X,Y:X*Y
print(LambdaP1p2(10,2))
print("\n")

#Problem 2 (old fashion way - Option 1)
#Write a Python program to create a function that takes one argument,...
#...and that argument will be multiplied with an unknown given number.
def LambdaP2o1 (xrandom):
    xnew1 = 2*xrandom
    print("Double the number", xrandom, "=", xnew1)
    xnew2 = 3*xrandom
    print("Triple the number", xrandom, "=", xnew2)
    xnew3 = 4*xrandom
    print("Quadruple the number", xrandom, "=", xnew3)
    xnew4 = 5*xrandom
    print("Quintuple the number", xrandom, "=", xnew4)
    return xnew1, xnew2, xnew3, xnew4

LambdaP2o1 (15)

#Problem 2 (new fashion way - Option 2)
LambdaP2o2 = lambda F,G:F*G
print("Double the number of 15 =", LambdaP2o2(15,2))
print("\n")

#Problem 2 (new fashion way - Option 3)
LambdaP2o3 = lambda F:15*F
print("Double the number 15 =", LambdaP2o3(2))
print("Triple the number 15 =", LambdaP2o3(3))
print("Quadruple the number 15 =", LambdaP2o3(4))
print("Quintuple the number 15 =", LambdaP2o3(5))
print("\n")

#Problem 3
#Write a Python program to sort a list of tuples using Lambda.

#We use the syntax of the function "sort" for "List" --> list.sort(reverse=True|False, key=myFunc) 
    # reverse (Optional): reverse=True will sort the list descending. Default...
    #...is reverse=False
    # key (Optional): A function to specify the sorting criteria(s)
    
    #In this case the sorting criteria of the function is the second item (of...
    #...the tuple) from every item of the list.
ListGrades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
ListGrades.sort(key = lambda x: x[-1])
print(ListGrades)
print("\n")

#Problem 4 - Option 1
#Write a Python program to sort a list of dictionaries using Lambda.

#We use the syntax of the function "sorted" --> sorted(iterable, key=key, reverse=reverse) 
    # iterable: 	Required. The sequence to sort, list, dictionary, tuple, etc
    # key (Optional): A Function to execute to decide the order. Default is None.
    # reverse (Optional): A Boolean. False will sort ascending, True will sort descending. Default is False.
    
    #In this case the sorting criteria of the function is the second item (of...
    #...the tuple) from every item of the list.
ListCell = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Cell = sorted(ListCell, key = lambda x: x['color'])
print(Cell)
print("\n")

#Problem 4 - Option 2
#We use the syntax of the function "sorted" --> sorted(iterable, key=key, reverse=reverse) 
    # iterable: 	Required. The sequence to sort, list, dictionary, tuple, etc
    # key (Optional): A Function to execute to decide the order. Default is None.
    # reverse (Optional): A Boolean. False will sort ascending, True will sort descending. Default is False.
    
    #In this case the sorting criteria of the function is the second item (of...
    #...the tuple) from every item of the list.
ListCell = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Cell = sorted(ListCell, key = lambda x: x['model'], reverse=True)
print(Cell)
print("\n")

#Problem 5 - Option 1
#Write a Python program to filter a list of integers using Lambda.

#It is important to say that due to the fact that the result of apply the...
#..."Filter Function" is an object called "Filter", I was forced to create...
#..."blank lists" and also "for loops" to append the blank lists.
NewListEven1 = []
NewListEven2 = []
OriginalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NewList1 = filter(lambda x: x%2 !=1, OriginalList)
for w in NewList1:
    NewListEven1.append(w)
print(NewListEven1)
print("\n")
NewList2 = filter(lambda y: y%2 !=0, OriginalList)
for z in NewList2:
    NewListEven2.append(z)
print(NewListEven2)
print("\n")

#Problem 5 - Option 2
#It is important to say that due to the fact that the result of apply the...
#..."Filter Function" is an object called "Filter", I was forced to create...
#...in a direct way a "list" that catch thee result of the "Filter Function".

    #filter(function, iterable)
    #The filter() function returns an iterator were the items are filtered...
    #...through a function to test if the item is accepted or not.
OriginalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NewList1 = list(filter(lambda x: x%2 !=1, OriginalList))
print(NewList1)
print("\n")
NewList2 = list(filter(lambda y: y%2 !=0, OriginalList))
print(NewList2)
print("\n")

#Problem 6
#Write a Python program to square and cube every number in a given list of...
#...integers using Lambda.

#In this case I use "map()" function as  a way to apply a function (i.e. a..
#...."Lambda Funcion") in a list of data. 

 #It is important to remember that function "map()" give us back an "map...
 #...object"; therefore, we need to apply a "list" code to the answer of...
 #...from function map().

OriginalList3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LambdaP6p1 = map(lambda x:x**2,OriginalList3)
print(list(LambdaP6p1))
LambdaP6p2 = map(lambda x:x**3,OriginalList3)
print(list(LambdaP6p2))
print("\n")  

#Problem 7 - Option 1
#Write a Python program to find if a given string starts with a given...
#...character using Lambda. Go to the editor

#In this case I use the code "in", which acts like a boolean.
String1 = "Yazidi is good"
LambdaP7p1 = lambda x:"e" in x
print(LambdaP7p1(String1))
print("\n")

#Problem 7 - Option 2
#Write a Python program to find if a given string starts with a given...
#...character using Lambda. Go to the editor

#In this case I use the code "startswith" (to figure out if a string begin...
#...with a certain word or letter) which acts like a boolean.
String2 = "Sanaa is good"
LambdaP7p2 = lambda x: x.startswith("h") 
print(LambdaP7p2(String2))
print("\n")

#Problem 7 - Option 3
#Write a Python program to find if a given string starts with a given...
#...character using Lambda. Go to the editor

#In this case I use the code "startswith" (to figure out if a string begin...
#...with a certain word or letter) which acts like a boolean (using the...
#...word "True" and "False" in a explicty way).
String3 = "Turmeric is good"
LambdaP7p3 = lambda x: True if x.startswith("w") else False
print(LambdaP7p3(String3))
print("\n")

#Problem 8 - Option 1
#Write a Python program to extract year, month, date and time using Lambda....
#...Go to the editor.

#In this case instead of write the date like a string, I get the date from...
#...Python code "datetime". Then I apply several subcodes from "datetime"...
#...to get in a separete way the:
    #year
    #month
    #day
    #time (hour, minutes, second). In this specific case I use...
    #...a method is called "strftime()", which takes one parameter (hour,...
    #...minutes and second) and returned in a string format.

import datetime
DateToday = datetime.datetime.now()
LambdaP8p1 = lambda x: x.year
LambdaP8p2 = lambda x: x.month
LambdaP8p3 = lambda x: x.day
LambdaP8p4 = lambda x: x.strftime("%X")
print(LambdaP8p1(DateToday))
print(LambdaP8p2(DateToday))
print(LambdaP8p3(DateToday))
print(LambdaP8p4(DateToday))
print("\n")

#Problem 8 - OPtion 2
#Write a Python program to extract year, month, date and time using Lambda....
#...Go to the editor.

#In this case instead of write the date like a string, I get the date from...
#...Python code "datetime". Then I apply several subcodes from "datetime"...
#...to get in a separete way the:
    #year
    #month
    #day
    #time (hour, minutes, second and milisecond). In this specific case I use...
    #...a method is called "time()", which returned "hour, minutes, second...
    #...and milisecond.
    
import datetime
DateToday = datetime.datetime.now()
LambdaP8p1 = lambda x: x.year
LambdaP8p2 = lambda x: x.month
LambdaP8p3 = lambda x: x.day
LambdaP8p4 = lambda x: x.time()
print(LambdaP8p1(DateToday))
print(LambdaP8p2(DateToday))
print(LambdaP8p3(DateToday))
print(LambdaP8p4(DateToday))
print("\n")

#Problem 9
#Write a Python program to check whether a given string is number or not...
#...using Lambda.

#In this case I use the function "isdigit()".
String4 = "8"
LambdaP9 = lambda x:x.isdigit()
print(LambdaP9(String4))
print("\n")

#Problem 10
#Lazy becase was Fibonacci.

#Problem 11- Option 1
#Write a Python program to find intersection of two given arrays using Lambda.
EmptyArray = []
OriginalArray1 = [1, 2, 3, 5, 7, 8, 9, 10]
OriginalArray2 = [1, 2, 4, 8, 9]

for w in OriginalArray1:
    if w in OriginalArray2:
        EmptyArray.append(w)
print(EmptyArray)
print("\n")

#Problem 11- Option 2
#Write a Python program to find intersection of two given arrays using Lambda.

#It is important to say that due to the fact that the result of apply the...
#..."Filter Function" is an object called "Filter", I was forced to create...
#...in a direct way a "list" that catch thee result of the "Filter Function".

OriginalArray3 = filter(lambda x: x in OriginalArray1, OriginalArray2)
print(list(OriginalArray3))
print("\n")

#Problem 12 - Option 1
#Write a Python program to rearrange positive and negative numbers in a...
#...given array using Lambda.

#Idea 1 (use lists, filter, sorted())
    #Split the list in two lists (positive an negatives)
    #Order both lists.
    #Then join the ordered lists

#It is important to say that due to the fact that the result of apply the...
#..."Filter Function" is an object called "Filter", I was forced to create...
#...in a direct way a "list" that catch thee result of the "Filter Function".

    #filter(function, iterable)
    #The filter() function returns an iterator were the items are filtered...
    #...through a function to test if the item is accepted or not.
    
#It is important to say that work very different the codes:
    #list.sort()
        #List objects have a sort() method that will sort the list...
        #..alphanumerically, numerically in ascending (by default) or..
        #...descending.
        
    #sorted(iterable, key=key, reverse=reverse) <-- I applied this
        #iterable (required) = The sequence to sort, list, dictionary, tuple,...
        #...etc.
        #key (optional) = A Function to execute to decide the order. Default...
        #...is None
        #reverse (optional)= A Boolean. False will sort ascending, True will..
        #...sort descending. Default is False
        
        #It is a Python Built in Function.                                                   
OriginalList3 = [-1, 2, -3, 5, 7, 8, 9, -10]
NewList3 = sorted(list(filter(lambda x: x>0, OriginalList3)))
print(NewList3)

OriginalList4 = [-1, 2, -3, 5, 7, 8, 9, -10]
NewList4 = sorted(list(filter(lambda x: x<0, OriginalList4)))
print(NewList4)

OriginalList5 = lambda X,Y: X+Y
print(OriginalList5(NewList3, NewList4))

#Problem 12 - Option 2
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print(result)

#Problem 13
#Write a Python program to count the even, odd numbers in a given array of...
#...integers using Lambda.

#Idea
    #-Use a filter, create a list, and then use len() to know the number...
    #:..of items of a list.
OriginalList6 = [1, 2, 3, 5, 7, 8, 9, 10]
OriginalArray6 = len(list(filter(lambda x: x%2==0, OriginalList6)))
print(OriginalArray6)
print("\n")

OriginalList7 = [1, 2, 3, 5, 7, 8, 9, 10]
OriginalArray7 = len(list(filter(lambda x: x%2!=0, OriginalList7)))
print(OriginalArray7)
print("\n")

#Problem 14 - Option 1
#Write a Python program to find the values of length six in a given list...
#...using Lambda.

#Idea
    #Use a filter for every string with the size of 6, allowing pass to only...
    #...string of 6 characters and avoid the pass of the strings...
    #...that surpass the 6 characters or are less than 6 characters .
    #Then print only the strings (not in a list way) of the results (strings...
    #...with 6 characters).

OriginalList8 = ["Monday", "Friday","Sunday", "Domingo", "Sigfried"]
OriginalArray8 = list(filter(lambda x: len(x) == 6,OriginalList8)) 
for x in OriginalArray8:
    print(x)
print("\n")

#Problem 14 - Option 2
#Write a Python program to find the values of length six in a given list...
#...using Lambda.

#Idea
    #Use a filter for every string with the size of 6, allowing pass to only...
    #...string of 6 characters and avoid the pass of the strings...
    #...that surpass the 6 characters or are less than 6 characters .
    #Then print only the strings (not in a list way) of the results (strings...
    #...with 6 characters).

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)
print("\n")

#Problem 15
#Write a Python program to add two given lists using map and lambda

#Idea:
    #Create the list (every list works like a Lambda variable) and them add...
    #..those variables.
OriginalList9 =[1, 2, 3]
OriginalList10 =[4, 5, 6]
LambdaP15 = map(lambda X,Y:X+Y,OriginalList9, OriginalList10)
print(list(LambdaP15))
print("\n") 

#Problem 16
#Write a Python program to find the second lowest grade of any student(s)...
#...from the given names and grades of each student using lists and lambda.
#...Input number of students, names and grades of each student.

#Ideas
    #Work like a list.
    #Iterate over the second element of every sublist.
    
ListStudGrad = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
LambdaP16 = lambda X:X
StudGrad = LambdaP16(ListStudGrad)
for W in StudGrad:
    for Grade in W:
        if Grade == 2:
            print(W[0])
            print(W[1])

#Problem 17
#Write a Python program to find numbers divisible by nineteen or thirteen...
#...from a list of numbers using Lambda.

#Idea
    #-Use a filter, create a list, and then use % to know the numbers...
    #...of a the list that are divisible by 13 or 19.
    
OriginalList11 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
OriginalFilter12 = list(filter(lambda x: x%13==0 or x%19==0, OriginalList11))
print(OriginalFilter12)
print("\n")

#Problem 18 - Option 1 (Without Lambda Function)
#Write a Python program to find palindromes in a given list of strings using...
#... Lambda.

#Idea
    #Create a list of invert words
    #Contrast the list of invert words vs the original list
    #Print the filtered list of the common words.
OriginalList18 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
EmptyList1 = []
EmptyList2 = []
for W in OriginalList18:
    Z = W[::-1]
    EmptyList1.append(Z)
    if Z in OriginalList18:
        EmptyList2.append(Z)
print(EmptyList2)
print("\n")

#Problem 18 - Option 2
#Write a Python program to find palindromes in a given list of strings using...
#... Lambda.

#Idea
    #Create a list with a filter.
    #The filter contrast (without a "For Loop") the value of the variable "x"...
    #...versus the reverse version {using the function "reverse()"} of the...
    #...value of the variable "x". It is important to say that we also use...
    #...the function "join()" with the space "", because the function...
    #..."reverse()" iterate over every single character of the strings and...
    #...we are intersted in do the filter contrasting words no strings...
    #...More info about the codes join() and reversed():
        #The join() method takes all items in an iterable and joins them...
        #...into one string (a string must be specified as the separator).
        #iterable: object where all the returned values are strings
            #string.join(iterable) 
        #The reverse() The reversed() function returns a reversed iterator..
        #..object.
        #sequence: Any iterable object
            #reversed(sequence)
OriginalList18 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
result = list(filter(lambda x: (x == "".join(reversed(x))), OriginalList18)) 
print(result)
print("\n")

#Problem 19 
#Write a Python program to find all anagrams of a string in a given list of...
#...strings using lambda.

#Idea:
    #In a surprise move, we import "Counter" from the module "collections"
    
    #This module implements specialized container datatypes providing..
        #...alternatives to Python’s general purpose built-in containers,...
        #...dict, list, set, and tuple.
        
        #A "Counter" is a dict subclass for counting hashable objects (i.e...
        #...characters in a single string). It is a collection where...
        #...elements (characters in a single string) are stored as dictionary...
        #...keys and their counts (numbers of time the characters appears)...
        #...are stored as dictionary values. 
        
    #In a simple way the "counter" code used to contrast the keys and values...
    #...(i.e. characters in a single string and numbers of time the..
    #...characters appears in that single string) vs the keys and values...
    #...(i.e. characters in every element of the list of strings and numbers..
    #...of time the characters appears in in every element of the list of...
    #...strings). Therefore, is just like do the count of characters (no...
    #...matter the order of the characters in the string).
   
    #Then make a list only with the strings that have the same type and...
    #...quantity of characters (no matter the order).
    
from collections import Counter  
OriginalList19 = ['bcda', 'abce', 'cbdaa', 'cbea', 'adcb']
OriginalString = "abcd"
result = list(filter(lambda x: (Counter(OriginalString) == Counter(x)), OriginalList19))
print(result)
print("\n")

#Problem 20 
#Write a Python program to find the numbers of a given string and store....
#...them in a list, display the numbers which are bigger than the length...
#...of the list in sorted form. Use lambda function to solve the problem.

#Idea
    #Find the numbers of the text splited (getting from that split a list of...
    #...strings) with the code split(" ").
    #After that, from the previous list we are going to filter numbers from...
    #...the text with the code "isdigit()"and finally create a list.
    #In a separate Lambda (i.e. first time I work with 2 lambdas at the same...
    #...time) I apply a filter to get a new list that capture the result of...
    #...contrasting numbers in a string version from the previous list...
    #...(transformed in integers) versus the length of the previous list.
    #Finally, I make sure that the result of the final list is sorted (from...
    #...lower o higher).
OriginalString ="sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
result1 = list(filter (lambda x: x if x.isdigit() else "", OriginalString.split(" ")))
result2 = sorted(list(filter (lambda y: y if int(y) > len(result1) else "", result1)))
print(result1)
print(result2)
print("\n")

#Problem 21 
#Write a Python program that multiply each number of given list with...
#...a given number using lambda function. Print the result.

#Idea
    #I create a Lambda that include the "map() function". The "map()...
    #...function" allow me to iterate or apply a function inside a given...
    #...list.
    #Due to the fact that we will get a "map object" of the "map()...
    #...function" we need to apply the "list" code.
    #Finally we iterate (outside the Lambda) with a "For Loop" through..
    #...the list created for the "map object" with the purpose to get...
    #...thee values outside of a list.
OriginalList21 = [2, 4, 6, 9, 11]
Given_number = 2
result21 = list(map(lambda X:X*Given_number,OriginalList21))
print(result21)
for Y in result21:
  print(Y)
print("\n")

#Problem 22 - Option 1
#Write a Python program that sum the length of the names of a given list...
#...of names after removing the names that starts with...
#...an lowercase letter. Use lambda function.

#Ideas:
    #First, I use the Lambda Function to create a filter (to detect the...
    #...the words that have only lower case letters in the original list)...
    #...and then a list.
    #Second, I use other Lambda Function to create a filter (to detect...
    #...the words that starts with upper case letters in the...
    #...original list in contrast with the previously created list).
    #Finally I apply a "for loop" that allow me to know the sum of length...
    #...of every element of the recent create list.
OriginalListNames = ["Gucci", "Spacex", "bandera", "Bitcoin", "pain"]
result221 = list(filter(lambda x: x if x.islower() else "",OriginalListNames))
result222 = list(filter(lambda y: len(y) if y not in result221  else "",OriginalListNames))
print(result221)
print(result222)
w1=0
for z in result222:
    w = len(z)
    w1+=w
print(w1)
print("\n")

#Problem 22 - Option 2
#Write a Python program that sum the length of the names of a given list...
#...of names after removing the names that starts with...
#...an lowercase letter. Use lambda function.

#Ideas:
    #First, I use the Lambda Function to create a filter (to detect the...
    #...the words that have the first letter as a upper case and the rest...
    #...of the letters of the same word with lower case in the original...
    #...list).
    #Then I create a list of that filter.
    #Finally I join all the words of the previously created list and then...
    #...calculate the length.
sample_names = ["Gucci", "Spacex", "bandera", "Bitcoin", "pain"]
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print(len(''.join(sample_names)))
print("\n")

#Problem 23 - Option 1
#Write a Python program to calculate the sum of the positive and negative...
#...numbers of a given list of numbers using lambda function.

#Ideas
    #Filter the "numbers > 0" and "numbers < 0" and the apply a code...
    #...(to be specific a "For Loop") that add the values of every list...
    #...in a separate way.
OriginalList23 = [2, 4, -6, -9, 11, -12, 14, -5, 17]
result231=list(filter(lambda X:X if X<0 else "",OriginalList23))
result232=list(filter(lambda F:F if F>0 else "",OriginalList23))
print(result231)
print(result232)
w1=0
for y in result231:
    w1+=y
print(w1)
w2=0
for z in result232:
    w2+=z
print(w2)
print("\n")

#Problem 23 - Option 2
#Write a Python program to calculate the sum of the positive and negative...
#...numbers of a given list of numbers using lambda function.

#Ideas
    #Filter the "numbers > 0" and "numbers < 0" and the apply a code...
    #...(to be specific a "sum() code") that add the values of every list...
    #...in a separate way.
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))
print(sum(total_negative_nums))
print(sum(total_positive_nums))

#Problem 24 
#Write a Python program to find numbers within a given range where...
#...every number is divisible by every digit it contains.

#REMEMBER:
    #In Python strings, the backslash "\" is a special character, also...
    #...called the "escape" character. It is used in representing...
    #...certain whitespace characters:
        #"\t" is a tab
        #"\n" is a newline
        #"\r" is a carriage return. 
        
    #Python "any()" function returns True if any of the elements of a...
    #...given iterable( List, Dictionary, Tuple, set, etc) are True else...
    #...it returns False. 
    
    #Python operator modulus "%" it is the remainder (i.e. residuo de la...
    #...división).
    
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
        if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))

#Problem 25 - Option 1 
#Write a Python program to create the next bigger number by...
#...rearranging the digits of a given number. 

#Ideas
    #Convert the "int" values into "str" values.
    #Then I switch the positions of every component of the number and then...
    #...contrast that new number (as a result of the new position)....
    #...against a higher value..
    #This idea only work for number with 2 digits; therefore is incomplete.

Original_Number = 56
Next_bigger_number = lambda X:(str(X)[-1]+str(X)[0]) if int(str(X)[-1]+str(X)[0])>X else (str(X)[0]+str(X)[-1])
print(Next_bigger_number(Original_Number))   

#Problem 25 - Option 2
#Write a Python program to create the next bigger number by...
#...rearranging the digits of a given number. 
def rearrange_bigger(n):
    #Break the number into digits and stored in a list.
    nums = list(str(n))
    #The "negative step" in the "range()" code will reverse the order of the....
    #...values iterated of the list. In this case:
        #Start = 3-2 = 1 (i.e. number = 1)
        #Stop = -1 (i.e. position -1)
            #The range() never includes the stop number in its result.
        #Step = -1
    #Therefore, the "i" in the first iteration is "1".
    for i in range(len(nums)-2,-1,-1):
        print("A",i)
        
        #TurnPoint: from this point we work only with two numbers.

        #This condition "nums[i] < nums[i+1]" is always true.
        #"i" means a position
        if nums[i] < nums[i+1]:
            print("B",nums[i])
            print("C",nums[i+1])
            #"z" is a list extracted from the list "nums" (that begin in...
            #..."i" and finish...
            #...putting all the numbers that follow it in the original...
            #...list "nums"), and I use lambda function in that list "z".
            z = nums[i:]
            print("D",z)
            
        #TurnPoint: from this point we separate the two numbers an switch...
        #...their positions.
            
            #I use the "min" because I am working with a list. The filter...
            #...get the "min" value in the list which is also greater....
            #...than z[0]. Therefore, "z[0] = 2" and "x=3 is greater than 2"
            y = min(filter(lambda x: x > z[0], z))
            print("E",y)
            #The "remove code" remove the "min" value in the list which...
            #...is also greater than z[0]. Therefore, remove "3" list "z" .
            z.remove(y)
            #Order the leftlovers. In this case sort the list "z" that...
            #...only has the number "2".
            z.sort()
            print("F",z.sort())
           
        #TurnPoint: from this point we concatenate and the join the numbers...
        #...in their new positions.
            
            #In this step I concatenate the list [Y] (the number "3") and...
            #...the list Z (the number "2").
            nums[i:] = [y] + z
            print("G",nums[i:])
            #Finally I join the elements of the recently created list. 
            return int("".join(nums))
        return False
n = 123
print("Original number:",n)
print("Next bigger number:",rearrange_bigger(n))

#Problem 26 - Option 1
#Write a Python program to find the list with maximum and minimum...
#...length using lambda.

#Ideas:
    #I create a sorted list, which was filtered according to the size of...
    #...the length of sublists tha belong to the main list.
    #Afterwards, I choose the first and last element of that sorted list...
    #...(i.e. the short and longest elements) and finally print them...
    #...as a tuple with their respective length.
OriginalList26 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
result261=sorted(list(filter(lambda X:X if len(X)>0 else "",OriginalList26)))
result262=result261.pop(0)
result263=result261.pop(-1)
print(result261)
print(tuple((len(result262),result262)))
print(tuple((len(result263),result263)))

#Problem 26 - Option 2
#Write a Python program to find the list with maximum and minimum...
#...length using lambda.

#Ideas:
    #I create a for loop according to the length of sublists tha belong...
    #...to the main list.
    #Afterwards, I use a conditional (knowing the size of the sub-lists,...
    #...which is like a lil trap) and finally print them as a tuple...
    #...with their respective length.
OriginalList26 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
for X in OriginalList26:
    if len(X) < 2:
        print(tuple((len(X),X)))
OriginalList26 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
for X in OriginalList26:
    if len(X) > 2:
        print(tuple((len(X),X)))       

#Problem 26 - Option 3
#Write a Python program to find the list with maximum and minimum...
#...length using lambda.

#Ideas:
    #I create a function in which through a for loop I find:
        #First, the element with the maximum length in the list, and as...
        #...consequence we print the length of that element.
        #Second, the element with the maximum length in the list, and as...
        #...consequence we print that element. To be specific, we use...
        #...the function max(iterable, function).
        #Finally, the function return a tuple with the length's element...
        #...and the element.
        
    #I create another function in which through a for loop I find:
        #First, the element with the minimum length in the list, and as...
        #...consequence we print the length of that element.
        #Second, the element with the maximum length in the list, and as...
        #...consequence we print that element. To be specific, we use...
        #...the function min(iterable, function).
        #Finally, the function return a tuple with the length's element...
        #...and the element.
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))
    print(max_length)
    print(max_list)
    return(max_length, max_list)
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print(max_length_list(list1))

def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    print(min_length)
    print(min_list)
    return(min_length, min_list)
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print(min_length_list(list1))
   
#Problem 26 - Option 4
#Write a Python program to find the list with maximum and minimum...
#...length using lambda.

    #I create a function in which through a for loop I find:
        #First, the element with the maximum length in the list, and as...
        #...consequence we print the length of that element.
        #Second, the element with the maximum length in the list, and as...
        #...consequence we print that element. To be specific, we use...
        #...the function max(iterable, function).
        #Finally, the function return a tuple with the length's element...
        #...and the element.
        
    #I create another function in which through a for loop I find:
        #First, the element with the minimum length in the list, and as...
        #...consequence we print the length of that element.
        #Second, the element with the maximum length in the list, and as...
        #...consequence we print that element. To be specific, we use...
        #...the function min(iterable, function).
        #Finally, the function return a tuple with the length's element...
        #...and the element.
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list) 
    print(max_length)
    print(max_list)
    return(max_length, max_list)
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print(max_length_list(list1))

def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list)
    print(min_length)
    print(min_list)
    return(min_length, min_list)
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print(min_length_list(list1))
     
#Problem 27 - Option 1
#Write a Python program to sort each sublist of strings in a given list...
#...of lists using lambda. 

#Ideas
    #I used the code map() to apply a function to all the elements of...
    #...a list. 
    #In this case the function is the code "sorted()" 
        #The sorted() function returns a sorted list of the specified...
        #...iterable object.
        # sorted(iterable, key=key{optional}, reverse=reverse{optional})
            #iterable: The sequence to sort, list, dictionary, tuple etc.
            #key: A Function to execute to decide the order. Default...
            #..is None.
            #reverse: A Boolean. False will sort ascending, True will...
            #...sort descending. Default is False.
OriginalList27 = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
result27=map(lambda X:sorted(X),OriginalList27)
print(list(result27)) 

#Problem 27 - Option 2
#Write a Python program to sort each sublist of strings in a given list...
#...of lists using lambda. 

#Ideas
    #Create a "for loop", then iterate and sort elements of the sublist.
    #Print the new sorted list.
    #In this option we can see clearly how affected is the original list...
    #...due to the "sort()" code applied inside the "for loop". 
        #sort() is a list  method.
        #The sort() method sorts the list ascending by default. 
        #You can also make a function to decide the sorting criteria(s).
        # list.sort(reverse=True|False {optional}, key=myFunc {optional}) 
OriginalList27 = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
for X in OriginalList27:
    X.sort()
print(OriginalList27)

#Problem 27 - Option 3
#Write a Python program to sort each sublist of strings in a given list...
#...of lists using lambda. 

#Ideas
    #I create a blank list.
    #Create a "for loop", then iterate and sort elements of the sublist.
    #Then I append the sorted elements to the new list.
    #Print the new sorted list.
    #In this case the function is the code "sorted()" 
        #The sorted() function returns a sorted list of the specified...
        #...iterable object.
        # sorted(iterable, key=key{optional}, reverse=reverse{optional}) 
            #iterable: The sequence to sort, list, dictionary, tuple etc.
            #key: A Function to execute to decide the order. Default...
            #..is None.
            #reverse: A Boolean. False will sort ascending, True will...
            #...sort descending. Default is False.
BlankList = []
OriginalList27 = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
for X in OriginalList27:
    Y = sorted(X)
    W = BlankList.append(Y)
print(BlankList)

#Problem 28 - Option 1
#Write a Python program to sort a given list of lists by length and value...
#...using lambda. 

#Ideas
    #First, I create several blank lists.
    #Then I create a "for loop" over the original list, and then ...
    #...through a conditional we check the length every sublist of the...
    #...original list, added in a specific blank list and finally...
    #...ordered that sub-lists that fall in every blank list.
    #Finally we print the a new main list that concatenate the previous...
    #...blank lists.
BlankList1 = []
BlankList2 = []
BlankList3 = []
OriginalList28 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
for X in OriginalList28:
    if len(X) == 1:
        W1 = BlankList1.append(X)
        W11 = sorted(BlankList1)
    elif len(X) == 2:
        W2 = BlankList2.append(X)
        W22 = sorted(BlankList2)
    elif len(X) == 3:
        W3 = BlankList3.append(X)
        W33 = sorted(BlankList3)
BlankList4 = W11 + W22 + W33
print(BlankList4)

#Problem 28 - Option 2
#Write a Python program to sort a given list of lists by length and value...
#...using lambda.

#Ideas
    #First, I create several blank lists.
    #Second, I create a function that have the following:
        #Then I create a "for loop" over the original list, and then ...
        #...through a conditional we check the length every sublist of the...
        #...original list, added in a specific blank list and finally...
        #...ordered that sub-lists that fall in every blank list.
        #Finally we print the a new main list that concatenate the previous...
        #...blank lists.
    
    #What we described previously is supported with lambda function with...
    #...map() {to apply a function to every element of the original list}...
    #...with the function recenlty created.
    #Finally to adjust the values printed (because we get as an answer...
    #...the correct answer repetead six times {six is the number of ...
    #...sublists that belong to original list}) we delete all the values,...
    #...except the printe value number [0].
BlankList1 = []
BlankList2 = []
BlankList3 = []
def myfunctionorder(Y):
    for X in OriginalList28:
        if len(X) == 1:
            W1 = BlankList1.append(X)
            W11 = sorted(BlankList1)
        elif len(X) == 2:
            W2 = BlankList2.append(X)
            W22 = sorted(BlankList2)
        elif len(X) == 3:
            W3 = BlankList3.append(X)
            W33 = sorted(BlankList3)       
    BlankList5 = W11 + W22 + W33
    return BlankList4

OriginalList28 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
result28=map(lambda Z:myfunctionorder(Z),OriginalList28)
finalresult = list(result28)
del finalresult[1:6]
print(finalresult)

#Problem 28 - Option 3  
#Write a Python program to sort a given list of lists by length and value...
#...using lambda.

#Ideas
    #First, I create a function that have the following:
        #I use the "sorted()" function.
            #The sorted() function returns a sorted list of the...
            #...specified iterable object.
        #Inside the "sorted()" function I use the "lamdba function" to...
        #...apply the "sorted()" function to every element (i.e. sublists)...
        #...according to their length.
        #Finally we print the result o the function.
def sort_sublists(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print(sort_sublists(list1))

#Problem 29 - Option 1
#Write a Python program to find the maximum value in a given heterogeneous...
#...list using lambda. 

#Ideas
    #I create a "if" conditional inside the "lambda function" in which I...
    #...remove only the values (transformed to "str") that has a length...
    #...longer than one.
    #Then I create a list of the filter ("if" conditional) applied...
    #...previously.
    #Finally I choose and print the maximum value of the previous list...
    #...with the code "max()"
OriginalList29 = ['Python', 3, 2, 4, 5, 'version']
result29=max(list(filter(lambda X:X if len(str(X))==1 else "",OriginalList29)))
print(result29) 

#Problem 29 - Option 2
#Write a Python program to find the maximum value in a given heterogeneous...
#...list using lambda. 

def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print(max_val(list_val))

##############################################################################

##############################################################################

##############################################################################

#Topic 5: List Comprenhesion (RMDLC)

#It is:
    #A condense way to write a loop (for) and conditionals (if) in...
    #...just one line.
    
    #A way of making lists. 
    
#Other forms to make a list are the followings:...
    #Option 1 (Using "For Loops") to create a list of elements in three...
    #...steps:
            #Instantiate an empty list.
            #Loop over an iterable or range of elements.
            #Append each element to the end of the list.
    #Option 2 (Using "Map()") to create a list of elements:
            #Provides an alternative approach that’s based in functional...
            #...programming. You pass in a function and an iterable, and...
            #...map() will create an object. This object then is converted....
            #...into a list using list().

#Rather than creating an empty list and adding each element to the end,...
#...we simply define the list and its contents at the same time by following...
#...this format: "new_list = [expression for "member in iterable"]"
    
#Every list comprehension in Python includes three elements:
    #Expression: is the member itself, or a call to a method, or any other valid...
    #...expression that returns a value. 
    #Member: is the object or value in the list or iterable. 
    #Iterable: is a list, set, sequence, generator, or any other object that...
    #...can return its elements one at a time.
    
#The only distinction between "list comprehension" and map() is that the...
#...list comprehension in Python returns a list, not a map object.

#Benefits of Using List Comprehensions:

    #In addition to standard list creation, list comprehensions can also be...
    #...used for mapping and filtering. 
    #List comprehensions are also more declarative than loops, which means...
    #...they’re easier to read and understand. Loops require you to focus on...
    #...how the list is created. You have to manually create an empty list,..
    #...loop over the elements, and add each of them to the end of the list...
    #...With a list comprehension in Python, you can instead focus on what you...
    #...want to go in the list and trust that Python will take care of how the...
    #...list construction takes place.

#List Comprenhesion (Supercharge)

#List Comprenhesion Normal format is: "new_list = [expression for member in iterable]"

#List Comprenhesion Supercharge format N°1 is: "new_list = [expression for member in iterable(if conditional)]"

        #A more complete description of the comprehension formula adds support...
        #...for optional conditionals. The most common way to add conditional..
        #...logic to a list comprehension is to add a conditional to the end..
        #..of the expression. 
        
#List Comprenhesion Supercharge format N°2 is: "new_list = [expression (if conditional) for member in iterable]"

        #Conditionals are important because they allow...
        #...list comprehensions to filter out unwanted values, which would...
        #...normally require a call to filter(). With this formula, we can...
        #...use conditional logic to select from multiple possible output...
        #...options that came from the "expression".

#Other Objects Comprenhesion ("Set" and "Dictionary")

#Set Comprenhesion format N°1 is "new_set = {expression for member in iterable (if conditional)}"

#Set Comprenhesion format N°2 is "new_set = {expression (if conditional) for member in iterable}"

        #Is almost exactly the same as a list comprehension in Python. The...
        #...difference is that set comprehensions make sure the output...
        #.."contains no duplicates". You can create a set comprehension by...
        #...using curly braces {} instead of brackets [].
        
        #Unlike lists, sets don’t guarantee that items will be saved and...
        #...printed in any particular order.

#Dictionary comprehensions are similar, with the additional requirement of...
#...defining a key.

#Dictionary Comprenhesion format N°1 is "new_set = {expression:expression for member in iterable (if conditional)}"

#Dictionary Comprenhesion format N°2 is "new_set = {expression:expression (if conditional) for member in iterable}"
   
#When Not to Use a List Comprehension:
            
    #Nested Comprehension (can be complicated to understand).
    
    #They might make your code run more slowly or use more memory. 
        #A list comprehension in Python works by loading the entire output...
        #...list into memory. For small or even medium-sized lists, this is...
        #...generally fine. But if we want to sum the squares of the first...
        #...billion integers we are going to notice that our computer becomes...
        #...non-responsive (that’s because Python is trying to create a list..
        #...with one billion integers, which consumes more memory than our...
        #...computer would like). Our computer may not have the resources it...
        #...needs to generate an enormous list and store it in memory. Then...
        #...the size of a list becomes problematic, it’s often helpful to use..
        #...a "generator" or "map()" instead of a "list comprehension" in Python.
        
            #A "generator" doesn’t create a single, large data structure in...
            #...memory, but instead returns an iterable. Your code can ask...
            #...for the next value from the iterable as many times as...
            #...necessary or until you’ve reached the end of your sequence,...
            #...while only storing a single value at a time.
            
            #We can identify a generator because the expression isn’t...
            #...surrounded by brackets or curly braces. Optionally,...
            #...generators can be surrounded by parentheses.

#Topic 5: List Comprenhesion. Example 5.1 (Normal Version - Just a Function)

lst = []
    
def times_tables():
    for j in range (10):
        n=j*2
        lst.append(n)
    print(lst)
    print("\n")        
    return lst

times_tables()

#Topic 5: List Comprenhesion. Example 5.2.

#We can see in this example very interesting things like:

#1. When we apply the "List Comprenhension", everything inside the code WWW...
#...is expicitly wrote inside a list (it means inside square brackets []). In...
#...other words we are creating a list.

    #Expression: is the member itself, a call to a method, or any other valid...
    #...expression that returns a value. <---IMPORTANT

#2. Inside the code WWW we declare the function that we want to apply, in this...
#...case the function "times_tables2()".

    #Member: is the object or value in the list or iterable. <---IMPORTANT

#3. Inside the code WWW we declare the variable in which...
#...we will apply the function, in this the variable "i" inside the function...
#..."times_tables2(i)".

    #Iterable: is a list, set, sequence, generator, or any other object that...
    #...can return its elements one at a time. <---IMPORTANT

#4. Inside the code WWW we declare the iterable in which we run the member "i"
#...and the function "times_tables2(i)", in this the iterable is "for i in z" 
                                  
#5. Then We describe:
    #The Iterable, in this case "z=[1,2]"
    #The function, in this case "times_tables2(YY)"
            #It is important to say that it is not necesssary to apply another...
            #...for loop inside the function "times_tables2(YY)"
            #It is important to say that the variable "YY "inside the function...
            #..."times_tables2(YY)" is the value that will take the member "i"...
            #...when we invoke the function "times_tables2(i)"
            
#Topic 5. Finally we just print the list comprenhension, in this case "WWW".
z=[1,2]

def times_tables2(YY):
    Z2= YY*2
    print("5.2",Z2)
    print("\n")        
    return Z2

WWW = [times_tables2(i) for i in z]
print("5.3",WWW)
print("\n") 

#Topic 5: List Comprenhesion (Supercharge). Example 5.3
 
#In this case we apply a filter to only get the number that are "2".
numbers2 = [1,2,674,2,6746,2,8978]
only2 = [i for i in numbers2 if i ==2]
print(only2)
print("\n") 

#Topic 5: List Comprenhesion (Supercharge). Example 5.4

#If we need a more complex filter, then we can even move the conditional...
#..logic to a separate function

#In this case we create a function to apply a filter (this filter will allow...
#...us to get only the vowels of the "sentence"). It is important to say...
#...that we put this filter function (in this case called "onlyvowels (i)")...
#... at then end of list comprenhension.

#Finally, the method "isalpha()" (built in function of Python) returns True...
#...if all characters in the string are alphabets. If not, it returns False.
sentence = 'the rocket came back from mars'
def onlyvowels (XXX):
    vowelsXXX = "aeiou"
    return XXX.isalpha() and XXX.lower() in vowelsXXX

vowels = [i for i in sentence if onlyvowels (i)]
print(vowels)
print("\n") 

#Topic 5: List Comprenhesion (Supercharge). Example 5.5
#To be honest, in this case was impossible to apply the "List Comprenhesion...
#...Supercharge format N°2 is: "new_list = [expression (if conditional) for member in iterable]"

#Therefore, I create a function (with a "if" conditional), and then create a...
#...create the "list comprenhension" that called that function recently created.
       
numbers3 = [1,2,674,2,6746,2,8978]

def equal2(YY):
    if YY == 2:
        z = YY 
        return z

only3 = [equal2(i) for i in numbers3]
print(only3)
print("\n") 

#Topic 5: List Comprenhesion vs Set Comprenhesion. Example 5.6

#We can see the differenc in the printed answer because there are...
#...not duplicated items (to be specific, using the "Set Comprenhesion" code)...
#...in comparison with the printed duplicated items (to be specific, in the...
#..."Set Comprenhesion" code). Also,  unlike "lists", "sets" don’t guarantee...
#...that items will be saved and printed in any particular order. 

quote1 = "life, uh, finds a way"
unique_vowels1 = [i for i in quote1 if i in 'aeiou']
print(unique_vowels1)
print("\n") 

quote2 = "life, uh, finds a way"
unique_vowels2 = {i for i in quote2 if i in 'aeiou'}
print(unique_vowels2)
print("\n") 

#Topic 5: Dictionary Comprenhesion. Example 5.7

squares = {i:i**i for i in range(10)}
print(squares)
print("\n") 

#Topic 5: Generator (this is not a "List Comprenhesion"). Example 5.8

sumbig = sum(i for i in range(10000))
print(sumbig)
print("\n") 

#Topic 5.2: List Comprenhesion Practices
#https://towardsdatascience.com/beginner-to-advanced-list-comprehension-practice-problems-a89604851313
#https://bbookman.github.io/Python-list-comprehension1/

#Problem 1
#Find all of the numbers from 1–1000 that are divisible by 8

#Idea
    #I create a loop from 1 to 1001 (1001 due to fact that the last value of...
    #...a range is excluded and we are interested in 1000) for the variables..
    #...divisible by 8 (using the Modulus operator "%" wich means "residuo de...
    #...división = 0").
Numberdivv8 = [i for i in range(1,1001) if i%8 == 0]
print(Numberdivv8)
print("\n") 

#Problem 2 - Option 1 (almost correct)
#Find all of the numbers from 1–1000 that have a 6 in them

#Idea
    #I create a loop from 6 to 1001 (1001 due to fact that the last value of...
    #...a range is excluded and we are interested in 1000) for the variables..
    #...every 10 numbers. This options is almost correct due to the fact that..
    #...missed values that belong to 61-69, 601...)
Number6 = [i for i in range(6,1001,10)]
print(Number6)
print("\n") 

#Problem 2 - Option 2
#Find all of the numbers from 1–1000 that have a 6 in them

#Idea
    #I create a loop from 6 to 1001 (1001 due to fact that the last value of...
    #...a range is excluded and we are interested in 1000) for the variables.
    #...This options put the conditional if the number 6 is inside the...
    #..."transformed number to string" analyzed.
Number6 = [i for i in range(6,1001) if "6" in str(i)]
print(Number6)
print("\n") 

#Problem 3 - Option 1
#Count the number of spaces in a string (use string above)

#Idea
    #I create a loop in the string that measure the length of every element...
    #...of the string (charachter and space) with the conditional to detect...
    #...empty elements (spaces). Then measure the quantity of empty elements...
    #...(spaces) that the list has.
    
String3 = "Horror Movie, Castlevanie, Dieter, Zombie, Morgen"
Len3 = len([len(i) for i in String3 if " " in i])
print(Len3)
print("\n") 

#Problem 3 - Option 2
#Count the number of spaces in a string (use string above)

#Idea
    #I create a loop in the string that count every element...
    #...of the string (charachter and space) with the conditional to detect...
    #...empty elements (spaces). Then measure the quantity of empty elements...
    #...(spaces) that the list has.
String3 = "Horror Movie, Castlevanie, Dieter, Zombie, Morgen"
Len3 = len([i.count(" ") for i in String3 if " " in i])
print(Len3)
print("\n") 

#Problem 4 - Option 1
#Remove all of the vowels in a string (use string above)

#Idea
    #I create a loop in the string that replace every vowel...
    #...of the string with a blank space. Then, I proceed to put together... 
    #...with the method "join()" every ripped element of the string.
        #string.join(iterable) 
            #It takes all items in an iterable and joins them into one string.
            #...In this case the string is the blank space "", which works...
            #...like the element that ut together every iterable (i.e. every..
            #...word).
String4 = "Horrer, osos perros, asa iglesia murcielago"
Removevowel = [i.replace("a", "") and i.replace("e", "") and i.replace("i", "") and i.replace("o", "") and i.replace("u", "") for i in String4]
print("".join(Removevowel))
print("\n")

#Problem 4 - Option 2
#Remove all of the vowels in a string (use string above)
String4 = "Horrer, osos perros, asa iglesia murcielago"
q4_answer = "".join([char for char in String4 if char not in ["a","e","i","o","u"]])
print("".join(q4_answer))
print("\n")

#Problem 5
#Find all of the words in a string that are less than 5 letters (use string...
#...above)

#Ideas
    #"Split()" the string into substrings (in this case we are interested in...
    #...substrings that are separated by commas or blank spaces; and also...
    #...strings that have less than 5 characters)
    #Then we apply the "Split()" twice (one considering the commas and the...
    #...other considering the blank spaces).
    #Finally I concatenate every list and print it.
String5 = "Horrer er,car, osos perros, asa ver iglesia murcielago"
CountLetters1 = [i for i in String5.split(" ") if len(i)<5]
CountLetters2 = [i for i in String5.split(",") if len(i)<5]
CountLetters3 = CountLetters1 + CountLetters2
print(CountLetters3)
print("\n")

#Problem 6 
#Use a dictionary comprehension to count the length of each word in a...
#..sentence (use string above).

#Idea
    #Check every word and count its length
    #"Split()" the string into substrings (in this case we are interested in...
    #...substrings that are separated by commas.
    #Then we apply the "Split()" (considering the commas).
    #Then print every word together with its length in a dictionary
String6 = "Horrer, car, osos, perros, murcielago"
CountLengthWord = {i:len(i) for i in String6.split(", ")}
print(CountLengthWord)
print("\n")

#Problem 7 - Option 1
#Use a nested list comprehension to find all of the numbers from 1–1000...
#...that are divisible by any single digit besides 1 (2–9)

#Idea
    #I believe that they want to generate 9 separate lists with only one...
    #...row of code dedicated to one number.
    #Then we concatenate every list.
    #The downside of this method is that repeat values that are divisble by...
    #...more than one number.
Numberdivv82 = [i for i in range(1,1001) if (i%2 == 0)]
Numberdivv83 = [i for i in range(1,1001) if (i%3 == 0)]
Numberdivv84 = [i for i in range(1,1001) if (i%4 == 0)]
Numberdivv85 = [i for i in range(1,1001) if (i%5 == 0)]
Numberdivv86 = [i for i in range(1,1001) if (i%6 == 0)]
Numberdivv87 = [i for i in range(1,1001) if (i%7 == 0)]
Numberdivv88 = [i for i in range(1,1001) if (i%8 == 0)]
Numberdivv89 = [i for i in range(1,1001) if (i%9 == 0)]
print(Numberdivv82+Numberdivv83+Numberdivv84+Numberdivv85+Numberdivv86+Numberdivv87+Numberdivv88+Numberdivv89)
print("\n") 

#Problem 7 - Option 2
#Use a nested list comprehension to find all of the numbers from 1–1000...
#...that are divisible by any single digit besides 1 (2–9)

#Idea
    #We create a list that move from 1 to 1001
    #Then we create conditional "if clause" that send us to a list that...
    #...that only works and contains variable (divisor) that moves from...
    #..the range from 2 to 10 to check if there is a number ("num") that...
    #...is divisible.
    #The greatness of this method is that it does not repeat values that are...
    #...divisble by more than one number.
q7_answer = [num for num in range(1,1001) if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(q7_answer)
print("\n")

#Problem 8
#For all the numbers 1–1000, use a nested list/dictionary comprehension to...
#...find the highest single digit any of the numbers is divisible by

#Idea:
    #We are looking for the maximum value numbers (that range from 1 to 10)...
    #...that can divide a list of numbers that range from 1 to 1000.
    #Therefore, we create a dictionary / list nested (i.e. a list inside a...
    #...dictionary).
q810_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in range(1,1001)}
print(q810_answer)
print("\n")

#Problem 9
#Create a list of all the consonants in the string “Yellow Yaks like yelling..
#...and yawning and yesturday they yodled while eating yuky yams”

#Ideas
    #Apply a "for loop" in the string then filter the vowels to get the...
    #...list of consonants only. 
    #I was hurry; therefore, I lef the blanl spaces.
quote9 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
unique_consonant9 = [i for i in quote9 if i not in 'aeiou']
print(unique_consonant9)
print("\n")  

#Problem 10 
#Get the index and the value as a tuple for items in the list...
#...“hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). 
#Result would look like (index, value), (index, value)

#Ideas:
    #For the first time I work with several list comprehension at the...
    #...same time (although I am not sure if it is the most efficient,...
    #...optimus or fastest way work with them).
    #First I create a list comprehension to only get the index values of...
    #...every element of the original list.
    #Second I create a list comprehension to only get the values of...
    #...every element of the original list.
    #Third I create a list comprehension to only get the tuples that...
    #...couple every element of the first list and second list according...
    #...to the loop that runs in the original list.
List10 = ["hi", 4, 8.99, "apple", ("t,b","n")]
TupleIndexValue1 = [List10.index(i) for i in List10]
TupleIndexValue2 = [str(i) for i in List10]
TupleIndexValue3 = [((TupleIndexValue1[List10.index(i)], TupleIndexValue2[List10.index(i)])) for i in List10]
print(TupleIndexValue1)
print(TupleIndexValue2)
print(TupleIndexValue3)
print("\n") 

#Problem 11
#Find the common numbers in two lists (without using a tuple or set)...
#...list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

#Idea
    #Iterate over a "List A" and contrast every value of the "List A" ...
    #...against the values of the "List_B" (i.e. checking is the value....
    #...of "List A" is in "List_B").
list_a = [1, 2, 3, 4]
list_b = [99, 3, 88, 5]
commonvalue = [i for i in list_a if i in list_b]
print(commonvalue)
print("\n")  

#Problem 12
#Get only the numbers in a sentence like ‘In 1984 there were 13 instances...
#...of a protest with over 1000 people attending’.

#Idea:
    #I iterate over a separates elements of a string (using the critera...
    #...of blank space (" ").
    #Then I create a list filter only of the numbers that belong to that.
    #...string. Finally I print that list (only formed by numbers) and..
    #...then I print every element of that list separately.
quote12 = "In 1984 there were 13 instances of a protest with over 1000 people attending"
onlynumber12 = [i for i in quote12.split(" ") if i.isdecimal()]
print(onlynumber12)
for X in onlynumber12:
    print(X)
print("\n")  

#Problem 13
#Given numbers = range(20), produce a list containing the word ‘even’ if..
#...a number in the numbers is even, and the word ‘odd’ if the number is...
#...odd. Result would look like ‘odd’,’odd’, ‘even’

#Ideas
  #I used the "conditional if" with the code "i%2!=0" to know if a number...
  #...is "even or odd" inside the "for loop".
#
OddEven13 = ["odd" if i%2!=0 else "even" for i in range(20)]
print(OddEven13)
print("\n")  

##############################################################################

##############################################################################

##############################################################################

#Topic 6: Numpy (RMDLC)

#Topic 6.0.1 - NumPy (Introduction):
    #"NumPy" stands for "Numerical Python".   

    #NumPy is a Python library used for working with arrays.  It also has...
    #...functions for working in domain of linear algebra, fourier...
    #...transform, and matrices.
    
    #In Python we have lists that serve the purpose of arrays, but they are...
    #...slow to process. Therefore, NumPy aims to provide an "array object"...
    #...(called "ndarray") that is up to 50x faster than traditional..
    #...Python lists.
    
        #NumPy arrays are stored at "one continuous place in memory" unlike...
        #...lists, so processes can access and manipulate them very...
        #...efficiently (this behavior is called "locality" of reference...
        #...in computer science.
        
    #NumPy is a Python library and is written partially in Python, but...
    #...most of the parts that require fast computation are written in...
    #...C or C++.

#Topic 6.0.2 - NumPy (Getting Started):
    #NumPy is usually imported under the "np" alias. Therefore, the NumPy...
    #...package can be referred to as np instead of numpy. 

#Topic 6.0.3 - NumPy (Creating Arrays):
    #NumPy is used to work with arrays. The array object in NumPy is called...
    #..."ndarray". We can create a NumPy "ndarray" object by using the...
    #..."array()" function.
    
    #To create an ndarray, we can pass:
        #A list, tuple or any array-like object into the array() method,...
        #...and it will be converted into an "ndarray".
        
    #The array is represented in the printed format by square brackets []...
    #...like a list (this comment not apply for 0-D arrays).

#Example 6.0.3.1:
#In this case a tuple is converted in an array.
import numpy as np
arr = np.array((1, 2, 3, 4, 5))       
print(arr)
print("\n")

    #Dimensions in Arrays: A dimension in arrays is one level of array...
    #...depth (nested arrays). Can be O-D, 1-D, 2-D, 3-D, 4-D,...etc. Where:
        #0-D: It is just one value (scalar).
        #1-D: It is like a vector (colum or row). Also called "2nd order...
        #...tensors".
        #2-D: It is like a matrix. Also called "3nd order tensors". It is...
        #...importantet say that NumPy has a whole sub module dedicated...
        #...towards matrix operations called "numpy.mat".
        #3-D: It is like mix of matrices (i.e. we put in several layer or...
        #...dimensions the matrices).
    
#Example 6.0.3.2:
#In this case we are very interested in write a 0D array.
import numpy as np
arr1 = np.array(5)       
print(arr1)
print("\n")    

#Example 6.0.3.3:
#In this case we are very interested in write a 1D array. In this case a...
#...tuple and then a list.
import numpy as np
arr2 = np.array((1,2,3,7))       
print(arr2)
print("\n")  

import numpy as np
arr2 = np.array([1,2,3,7])       
print(arr2)
print("\n")  

#Example 6.0.3.4:
#In this case we are very interested in write a 2D array. In this case lists.
import numpy as np
arr3 = np.array([[1,2,3,7], [12, 20, 30, 40]])       
print(arr3)
print("\n")  

#Example 6.0.3.5:
#In this case we are very interested in write a 3D array. In this case lists.
#To be specific we are writing an array that is formed by two 2D matrices...
#...arranged in two layers, where the first layer is...
#...[[1,2,3,7], [12, 20, 30, 40]] an the second layer is...
#...[[10,20,30,70], [12, 20, 30, 40]].
import numpy as np
arr4 = np.array([[[1,2,3,7], [12, 20, 30, 40]], [[10,20,30,70], [12, 20, 30, 40]]])       
print(arr4)
print("\n")  

    #We can check the dimensions of arrays with the code ".ndim"
import numpy as np
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)     
    
#Topic 6.0.4 - NumPy (NumPy Array Indexing): 
    #We are going to basically find certain values that belong to the...
    #...arrays trough their index position (like in Python, starting...
    #:..with zero). We can use also negative index values.
    
    #We use commas "," to do the Indexing.

#Example 6.0.4.1:
#In this case we are very interested get the the value "40" of...
#... this 3D array (using positive and negative values of indexes).
#In this case (index position like in Python):
    #Layer 0
    #Row 1
    #Column 3
import numpy as np
arr4 = np.array([[[1,2,3,7], [12, 20, 30, 40]], [[1,2,3,7], [12, 20, 30, 50]]])       
print(arr4[0, 1, 3]) 
print("\n")    
     
#In this case (index position like in Python):
    #Layer 0
    #Row 1
    #Column -1                                       
import numpy as np
arr4 = np.array([[[1,2,3,7], [12, 20, 30, 40]], [[1,2,3,7], [12, 20, 30, 50]]])       
print(arr4[0, 1, -1]) 
print("\n")        
    
#Topic 6.0.5 - NumPy (NumPy Array Slicing):  
    #We are going to basically find and extract certain values that...
    #...belong to the arrays trough their index position (like in Python,...
    #...starting with zero). We can use also negative index values.    
    
    #We pass slice instead of index like this: [start:end].
    #We can also define the step, like this: [start:end:step]
        #If we don't pass start its considered 0
        #If we don't pass end its considered the length of array in that...
        #...dimension
        #If we don't pass step its considered 1
    #The result includes the start index, but excludes the end index.
    
    #We use colon ":" to do the Slicing.
    
#Example 6.0.5.1:
#In this case we are very interested to slice in 1D.
import numpy as np
arr4 = np.array([1, 2, 3, 4, 5, 6, 7])       
print(arr4[0:3]) 
print("\n")    

import numpy as np
arr4 = np.array([1, 2, 3, 4, 5, 6, 7])       
print(arr4[:3]) 
print("\n") 

import numpy as np
arr4 = np.array([1, 2, 3, 4, 5, 6, 7])       
print(arr4[3:]) 
print("\n") 

import numpy as np
arr4 = np.array([1, 2, 3, 4, 5, 6, 7])       
print(arr4[0:5:2])
print("\n") 

import numpy as np
arr4 = np.array([1, 2, 3, 4, 5, 6, 7])       
print(arr4[-3:-1]) 
print("\n") 

#Example 6.0.5.2: 
#In this case we are very interested to slice in 2D. It is important to...
#...see that we first located the element in which we are interested...
#...through the index and then we do the slicing.
#In this case (index position like in Python):
    #Certain Elements of Row 1
import numpy as np
arr3 = np.array([[1,2,3,7], [12, 20, 30, 40]])       
print(arr3[1,0:2])
print("\n")  

#Example 6.0.5.3:
#In this case we are very interested to slice in 2D. It is important to...
#...see that we first located the element in which we are interested...
#...(in a range form) then we do the slicing in the elements...
#...(specific index) in which we are interested.
#In this case (index position like in Python):
    #All Elements of Column 3
import numpy as np
arr3 = np.array([[1,2,3,7], [12, 20, 30, 40]])       
print(arr3[0:2,3])
print("\n")  

#Example 6.0.5.4:
#In this case we are very interested to slice in 2D. It is important to...
#...see that we first located the element in which we are interested...
#...(in a range form) then we do the slicing in the elements...
#...(specific index in a range form) in which we are interested.
#In this case (index position like in Python):
    #Row 1 and 2
    #Column 0
import numpy as np
arr3 = np.array([[1,2,3,7], [12, 20, 30, 40]])       
print(arr3[0:99,0:1])
print("\n")  

#Example 6.0.5.5:                
#In this case we are very interested to slice in 3D. It is important to...
#...see that we first located the dimension in which we are interested...
#...(in a index form. In this case formed by [1,2,3,7], [12, 20, 30, 40]),..
#...then locate the row in which we are interested (in a index form. In..
#...this case formed by [12, 20, 30, 40]), finally we do the slicing in...
#...the elements (in a index form) in which we are interested.  
#In this case (index position like in Python):
    #Layer 0
    #Row 1
    #Column -1                                       
import numpy as np
arr4 = np.array([[[1,2,3,7], [12, 20, 30, 40]], [[1,2,3,7], [12, 20, 30, 50]]])       
print(arr4[0, 1, -1]) 
print("\n")  

#Example 6.0.5.6:                
#In this case we are very interested to slice in 3D. It is important to...
#...see that we first located the dimension in which we are interested...
#...(in a index form. In this case formed by [1,2,3,7], [12, 20, 30, 50]),..
#...then locate the row in which we are interested (in a index form. In..
#...this case formed by [1,2,3,7]), finally we do the slicing in...
#...the elements (in a index form) in which we are interested.     
#In this case (index position like in Python):
    #Layer 1
    #Row 0
    #Column 2
import numpy as np
arr4 = np.array([[[1,2,3,7], [12, 20, 30, 40]], [[1,2,3,7], [12, 20, 30, 50]]])       
print(arr4[1, 0, 2]) 
print("\n")  

#Example 6.0.5.7:                
#In this case we are very interested to slice in 3D. It is important to...
#...see that we first located the dimension in which we are interested...
#...(in a range form. In this case formed by [[[1,2,3,7],...
#...[12, 20, 30, 40]], [[1,2,3,7], [12, 20, 30, 50]]]), then locate the...
#...row in which we are interested (in a index form. In this case formed...
#...by [12, 20, 30, 40] and [12, 20, 30, 50]), finally we do the slicing..
#...in the elements (in a index form) in which we are interested.  
#In this case (index position like in Python):
    #All elements of Layer 0 and 1
    #Row 0
    #Column 2                                        
import numpy as np
arr4 = np.array([[[1,2,3,7], [12, 20, 30, 40]], [[1,2,3,7], [12, 20, 30, 50]]])       
print(arr4[0:, 1, 2]) 
print("\n")  

#Topic 6.0.6 - NumPy (NumPy Data Types):
  #Below is a list of all data types in NumPy and the characters used...
  #...to represent them.
    #"i" - integer
        #(normally either int64 or int32)
    #"b" - boolean
    #"u" - unsigned integer
    #"f" - float
    #"c" - complex float
    #"m" - timedelta
    #"M" - datetime
    #"O" - object
    #"S" - string
    #"U" - unicode string
        #(normally "U1" for only strings and "U11" for strings mixed with...
        #...numbers).
    #"V" - fixed chunk of memory for other type ( void )

#Example 6.0.6.1:                
#In this case we are checking the "type of data" of our arrays.
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
print("\n")       
    
import numpy as np
arr = np.array(["a","b","c"])
print(arr.dtype)  
print("\n")  

import numpy as np
arr = np.array([1, "a", 3, 4])
print(arr.dtype)     
print("\n")  
    
#Example 6.0.6.2:                
#In this case we are creating an array with a specific "type of data" (in..
#..this case the "integer").
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i')
print(arr)
print(arr.dtype) 
print("\n")  
    
#Example 6.0.6.3:                
#In this case we are changing the "type of data" of an array using...
#... the function "astype()" that allow us to create a copy of the...
#...array and specify the data type as a parameter.
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(arr)
print(newarr)
print(newarr.dtype) 
print("\n")  
    
#Topic 6.0.7 - NumPy (NumPy Array Copy vs View):
  #The main difference between a "copy of an array" and a "view of an...
  #...array" is:
      #The "copy" is a new array.
      #The "copy" owns the data and any changes made to the "copy" will...
      #...not affect original array, and any changes made to the...
      #...original array will not affect the copy.

      #The "view" is just a view of the original array.
      #The "view" does not own the data and any changes made to the...
      #...view will affect the original array, and any changes made to...
      #...the original array will affect the view.

#Example 6.0.7.1:                
#In this case we are checking that a change in the "original array" does...
#...not affect the "copy".
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)                    
print("\n")  
                     
#Example 6.0.7.2:                
#In this case we are checking that a change in the "original array" does...
#...affect the "view".
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)                    
print("\n")  
                                     
#Example 6.0.7.3:                
#In this case we are checking that a change in the "view" does...
#...affect the "original array".
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 42
print(arr)
print(x)                    
print("\n")                       
                     
#Topic 6.0.8 - NumPy (NumPy Array Shape):
  #The "shape" allow us to know the number of elements in each dimensions...
  #...of an array.

#Example 6.0.8.1:                
#In this case we are checking the shape (the number of elements in each...
#...dimensions) in...
#...an "array". We get a 2D array with a shape of: 2 rows and 4 columns...
#...(another way to say this: outermost dimension {which can be indentified...
#...with the outer square brackets} will have 2 arrays, each array with...
#...4 elements).
#In this case (shape):
    #Rows: 2
    #Columns: 4
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)                      

#Example 6.0.8.2:                
#In this case we are checking the shape (the number of elements in each...
#...dimensions) in...
#...an "array". We get a 3D array with a shape of: 2 matrices with 2 rows...
#...and 4 columns (another way to say that is: outermost dimension will...
#...have 2 arrays that contains 2 arrays, each array with with 4 elements). 
#In this case (shape):
    #Layer: 2
    #Rows: 2 (in each layer)
    #Columns: 4 (in each layer)                  
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])
print(arr.shape)                         

#Topic 6.0.9 - NumPy (NumPy Array Reshaping):
  #The "reshape" allow us to change (add or remove dimensions or change..
  #...number of elements in each dimension) the shape of an array.
  
  #The "reshaped array" is a "view", not a "copy"; therefore, modify the...
  #...original dataframe.

#Example 6.0.9.1: 
#In this case we are changing the shape of an "array". We get a 2D array...
#...with a shape of 1 matrix with 4 rows and 3 columns from a 1D array.   
#In this case we get a shape:
    #Layer: 1
    #Rows: 4
    #Columns: 3
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)         
print("\n")             
                    
#Example 6.0.9.2: 
#In this case we are changing the shape of an "array". We get a 3D array...
#...with a shape of 2 matrices with 2 rows and 3 columns from a 1D array.  
#In this case we get a shape:
    #Layer: 2
    #Rows: 2 (in each layer)
    #Columns: 3 (in each layer)              
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 2, 3)
print(newarr)                        
print("\n")  

#Example 6.0.9.3: 
#In this case we are changing the shape of an "array". We get a 3D array...
#...with a shape of 2 matrices with 2 rows the number of columns is...
#...unkown (therefor I put the value "-1" and the machine automatically...
#...calculate the unkown dimension) from a 1D array.
#In this case we get a shape:
    #Layer: 2
    #Rows: 2 (in each layer)
    #Columns: 2 (in each layer)  
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr) 

#Example 6.0.9.4: 
#In this case we are changing the shape of an "array". We get a 1D array...
#...(i.e. we flat an array) from a 3D array.
#In this case we get a shape:
    #Rows: 1  
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])
newarr = arr.reshape(-1)
print(newarr) 

#Topic 6.0.10 - NumPy (NumPy Array Iterating):
  #We can iterate on an array in two ways:
      #Through a "for loop". In this case we need to be careful because...
      #...we can get the elements of an array or even the sub-array of...
      #..sub-arrays (depending of the quantity of dimensions of an array...
      #...and the quantity of "for loop" that we use).
      
        #The main divantage of "for loops", is that iterating through each...
        #...scalar of an array we need to use "n" for loops (equal to the...
        #...quantity of dimnensions of an array) which can be...
        #...difficult to write for arrays with very high dimensionality.
      
      #Through the function "nditer()". In this case we are using the...
      #...most efficient techinque to iterate in Numpy.
          #The function "nditer()" allow change the "data type" through:
            #We can use "op_dtypes" argument and pass it the expected...
            #...datatype to change the existing datatype of elements...
            #...while iterating.
            #It is important to remember that NumPy does not change the..
            #...data type of the element in-place (where the element is...
            #...in array) so it needs some other space to perform this...
            #...action, that extra space is called "buffer", and in order...
            #...to enable it in "nditer()" we pass "flags=['buffered']".
            
          #The function "nditer()" allow iterating with different step...
          #...size.

#Example 6.0.10.1: 
#In this case we are interating over an 1D array using a simple "for loop"...
#...and getting the scalars.
import numpy as np
arr = np.array([1, 2, 3, 4])
for x in arr:
    print(x) 

#Example 6.0.10.2: 
#In this case we are interating over an 3D array using a simple "for loop"...
#...and getting the subarrays of the arrays,
#In this case we interate in the following order (two levels of three):
    #Layer --> Rows
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]]])
for x in arr:
    for y in x:
        print(y) 

#Example 6.0.10.3: 
#In this case we are interating over an 3D array using a simple "for loop"...
#...and getting the scalars
#In this case we interate in the following order (three levels of three):
    #Layer --> Rows --> Scalars
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]]])
for x in arr:
    for y in x:
        for z in y:
            print(z) 

#Example 6.0.10.4: 
#In this case we are interating over an 3D array using the function...
#..."nditer()" and getting the scalars.
#In this case we interate in the following order (three levels of three),...
#...but in a very efficent and fast way:
    #Layer --> Rows --> Scalars
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]]])
for x in np.nditer(arr):
    print(x) 

#Example 6.0.10.5: 
#In this case we are interating over an 1D array using the function...
#..."nditer()" and flags=['buffered'] to transform the integers of the...
#...array to strings trough code "op_dtypes=['S']".
    #We will see the lowercase letter "b" (for data type "bytes88") at...
    #...the right side of every transformed element when we print.
import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x) 

#Example 6.0.10.6: 
#In this case we are interating over an 2D array using the function...
#..."nditer()" and putting a step of 2.
#In this case we interate in the following order (three levels of three):
    #All Rows
    #All columns (but in stepp of 2)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x) 

#Topic 6.0.11 - NumPy (NumPy Joining Array):
  #In a simple way we are going to see several codes that will allow...
  #...us to merge arrays of data.
    
  #There are axis (like cartesians coordinates) in the Numpy.
  #In a simple way the axis are the directions along rows and columns.
  #The axis for the 1D array are different for the 2D array, because...
  #..1D array works a little differently (technically, 1D arrays do..
  #...have only axis "0" that runs horizontally).
  #The array axes in NumPy are numbered like a Python list.
  
  #We need to be careful with the behavior of certain functions when we...
  #...use them in combination with axis (for instance: "sum(), mean(),...
  #...min(), median(), and other statistical functions") that aggregate...
  #...(i.e. collapsed the axis) the data of an axis.
  
  #We need to be careful with the behavior of certain functions when we...
  #...use them in combination with axis (for instance: "concatenate()"...
  #...that stack (i.e. "apilar valores") values of the dataframes (below or...
  #...at the right of the first dataframe) based on axis selected. In...
  #...this case, the code "concatenate()" does not sum or add any value...
  #...(i.e. this function does not collapsed the axis).
  
  #The axis for the 2D array are:
      #"Axis 0": It is the axis that represent the rows (and move in a...
      #...vertical way). It is the axis by default.
      #"Axis 1":It is the axis that represent the columns (and move in a...
      #...horizontal way).
      
  #Stacking:
      #It is similar as concatenation, the only difference is that stacking...
      #...is done along a new axis.
      #We pass a sequence of arrays that we want to join to the stack()...
      #...method along with the axis. If axis is not explicitly passed it...
      #...is taken as 0.
      
      #With "stack()" we do not mix the values of the arrays (thing that...
      #...happen with "concatenate()") in other arrays.
      
      #We have other codes derive from stack(), that give us result with...
      #...a different shape and arrange of data:
              #hstack(): to stack along rows.
              #vstack(): to stack along columns.
              #dstack(): to stack along height, which is the same as depth.
      
   #As a result of applying "concatenation", "stacking" and other "math...
   #...operations" the shape of the final array is different from the...
   #...original arrays (we can see how diminish or increase the dimensions...
   #...of the resultant array).

#Examples applying sum()
#Example 6.0.11.1: 
#In this case we are applying the function sum (i.e. aggregating = ...
#...collapsing) over the rows (axis =0) in a 2D array. As an answer we...
#...see how we go from 2 rows (original data) to 1 row (answer showing...
#...the rows collapsed).
import numpy as np          
np_array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d_sum = np.sum(np_array_2d, axis = 0)
print(np_array_2d_sum) 
print(np_array_2d_sum.shape)

#Example 6.0.11.2: 
#In this case we are applying the function sum (i.e. aggregating = ...
#...collapsing) over the columns (axis =1) in a 2D array. As an answer we...
#...see how we go from 2 rows (original data) to 1 row (answer showing...
#...the columns collapsed).
import numpy as np          
np_array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d_sum = np.sum(np_array_2d, axis = 1)
print(np_array_2d_sum) 
print(np_array_2d_sum.shape)


#Examples applying concatenate()
#Example 6.0.11.3: 
#In this case we are applying the function concatenate(), and saw in the...
#...printed result the stacked values of one 2D array (the second array...
#...below of the first 2D array) based on axis chosen (in this case...
#..."axis 0").
import numpy as np          
np_array_2d1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
np_array_2d21 = np.concatenate([np_array_2d1, np_array_2d2], axis = 0)
print(np_array_2d21) 
print(np_array_2d21.shape)

#Example 6.0.11.4:
#In this case we are applying the function concatenate(), and saw in the...
#...printed result the stacked values of the 2D array (at the right of...
#...the first 2D array in every row) based on axis chosen (in this case...
#..."axis 1").

   #This code apply the fusion of the rows of every array at the...
   #...respective level.
import numpy as np          
np_array_2d1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
np_array_2d21 = np.concatenate([np_array_2d1, np_array_2d2], axis = 1)
print(np_array_2d21) 
print(np_array_2d21.shape)

#Example 6.0.11.5.1: 
#In this case we are applying the function concatenate(), and saw in the...
#...printed result the stacked values of the 1D array (at the right of...
#...the first 1D array) based on axis chosen (in this case "axis 0").

  #This function cause a fusion of values, just like the concatenation...
  #...of 2D arrays in axis 1 (see Example 6.0.11.4).
import numpy as np          
np_array_1d1 = np.array([1, 2, 3, 4])
np_array_1d2 = np.array([10, 20, 30, 40])
np_array_1d12 = np.concatenate([np_array_1d1, np_array_1d2], axis = 0)
print(np_array_1d12)
print(np_array_1d12.shape)


#Examples applying stack() 
#Example 6.0.11.6: 
#In this case we are applying the function stack(), and saw in the...
#...printed result the stacked values of the 1D array (below of the...
#...first 1D array) based on axis chosen (in this case "axis 0").

    #The shape of the arrange of an 1D array with function stack()...
    #...is different from shape of the arrange of an 1D array with function...
    #...concatenate().
    
    #In  this case the behavior of the 1D array is according to the axis=0...
    #...(move in a vertical way).
import numpy as np          
np_array_1d1 = np.array([1, 2, 3, 4])
np_array_1d2 = np.array([10, 20, 30, 40])
np_array_1d12 = np.stack((np_array_1d1, np_array_1d2), axis = 0)
print(np_array_1d12)
print(np_array_1d12.shape)

#Example 6.0.11.7: 
#In this case we are applying the function stack(), and saw in the...
#...printed result the stacked values of the 1D array (making couples...
#...from every value of the colums of the 1D array). In this case "axis 1".

    #In  this case the behavior of the 1D array is according to the axis=1...
    #...(move in a horizontal way). It looks like we are grouping the rows...
    #...of vertical vectors.
import numpy as np          
np_array_1d1 = np.array([1, 2, 3, 4])
np_array_1d2 = np.array([10, 20, 30, 40])
np_array_1d12 = np.stack((np_array_1d1, np_array_1d2), axis = 1)
print(np_array_1d12)
print(np_array_1d12.shape)

#Example 6.0.11.8:     
#In this case we are applying the function stack(), and saw in the...
#...printed result the stacked values of the 2D array.In this case "axis 0".

    #In  this case the behavior of the 2D array is according to the axis=0...
    #...(move in a vertical way). The result is a 3D array (the rows of...
    #...the first array above the of rows of the next array).
import numpy as np                  
np_array_2d1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
np_array_2d21 = np.stack([np_array_2d1, np_array_2d2], axis = 0)
print(np_array_2d21)                    
print(np_array_2d21.shape)               

#Example 6.0.11.9:  
#In this case we are applying the function stack(), and saw in the...
#...printed result the stacked values of the 2D array.In this case "axis 1".

    #In  this case the behavior of the 2D array is according to the axis=1...
    #...(move in a horizontal way). The result is a 3D array (the first...
    #...row of the first array above the first row of the second array....
    #...in a goup, then following rows and so on in other group).
import numpy as np                  
np_array_2d1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
np_array_2d21 = np.stack([np_array_2d1, np_array_2d2], axis = 1)
print(np_array_2d21)   
print(np_array_2d21.shape)

#Examples applying others stack()        
#Example 6.0.11.10:
#In this case we are applying the function hstack() that do the same thing...
#...that concatenate(), and saw in the printed result the stacked values...
#...of the 1D array (at the right of the first 1D array). This function...
#...cause a fusion of values.

    #"hstack()" apply to stack along rows.

    #This printed result (to be specific the shape) is different from the...
    #...result got when we applied the function "stack()".
import numpy as np          
np_array_1d1 = np.array([1, 2, 3, 4])
np_array_1d2 = np.array([10, 20, 30, 40])
np_array_1d12 = np.hstack([np_array_1d1, np_array_1d2])
print(np_array_1d12)
print(np_array_1d12.shape)

#Example 6.0.11.11:     
#In this case we are applying the function hstack(), that don´t do...
#...the same thing that concatenate(). And we saw in the printed result...
#...the stacked values of every row of the second 2D array (at the...
#...right of the row of the first 2D array). This function cause a...
#...fusion of values.

    #This printed result (to be specific the shape) is different from the...
    #...result got when we applied the function "stack()".
import numpy as np                  
np_array_2d1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
np_array_2d21 = np.hstack([np_array_2d1, np_array_2d2])
print(np_array_2d21)                    
print(np_array_2d21.shape)                
                     
#Example 6.0.11.12:
#In this case we are applying the function vstack(), and saw in the...
#...printed result the stacked values of the 1D array (below of the...
#...first 1D array) based on axis chosen (in this case "axis 0").

    #"vstack()" apply to stack along columns.

    #The shape of the arrange of an 1D array with function stack()...
    #...is different from shape of the arrange of an 1D array with function...
    #...concatenate().
    
    #This printed result (to be specific the shape) is the same of the...
    #...result got when we applied the function "stack()".
    
    #In this case the behavior of the 1D array is according to the axis=0...
    #...(move in a vertical way).
import numpy as np          
np_array_1d1 = np.array([1, 2, 3, 4])
np_array_1d2 = np.array([10, 20, 30, 40])
np_array_1d12 = np.vstack([np_array_1d1, np_array_1d2])
print(np_array_1d12)
print(np_array_1d12.shape)

#Example 6.0.11.13:     
#In this case we are applying the function vstack(), and saw in the...
#...printed result the stacked values of the 2D array.In this case "axis 1".

    #In  this case the behavior of the 2D array is according to the axis=1...
    #...(move in a horizontal way). The result is a 2D array (the rows of...
    #...first array stacked over the rows of the following arrays and so...
    #...on in other group).
    
    #This printed result (to be specific the shape) is not the same of the...
    #...result got when we applied the function "stack()".
import numpy as np                  
np_array_2d1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
np_array_2d21 = np.vstack([np_array_2d1, np_array_2d2])
print(np_array_2d21)                    
print(np_array_2d21.shape)   

#Example 6.0.11.14:
#In this case we are applying the function dstack(), and saw in the...
#...printed result the stacked values of the 1D array (making couples...
#...from every value of the colums of the 1D array).

    #"dstack()" apply to stack along height, which is the same as depth.

    #In  this case the behavior of the 1D array is according to the axis=1...
    #...(move in a horizontal way). It looks like we are grouping the rows...
    #...of vertical vectors.
import numpy as np          
np_array_1d1 = np.array([1, 2, 3, 4])
np_array_1d2 = np.array([10, 20, 30, 40])
np_array_1d12 = np.dstack([np_array_1d1, np_array_1d2])
print(np_array_1d12)
print(np_array_1d12.shape)

#Example 6.0.11.15:
#In this case we are applying the function dstack(), and saw in the...
#...printed result the stacked values of the 2D array (making couples...
#...from every value of the colums of the 2D array). For instance: the...
#....values of the of the first row of the first array is grouped...
#...vertically with the first row of the following array,
import numpy as np                  
np_array_2d1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np_array_2d2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
np_array_2d21 = np.dstack([np_array_2d1, np_array_2d2])
print(np_array_2d21)                    
print(np_array_2d21.shape)   

#Topic 6.0.12 - NumPy (NumPy Splitting Array):
  #In a simple way we are going to see several codes that will allow...
  #...us to split arrays of data.
  
  #We use the code "array_split()":
      #For splitting arrays, we pass it the array we want to split...
      #...the number of splits and the axis of the split (by default...
      #...axis=0). This can be applied in 1D, 2D, 3D, etc. arrays.
      
      #If the array has less elements than required, it will adjust...
      #...from the end accordingly. In constrat with method "split()"...
      #...which will not adjust the elements when elements are less...
      #...in source array for splitting.
      
      #We can specify which axis you want to do the split around "axis=1"...
      #...or "axis=0".
      
      #We can also use the codes {taking in count that this codes will....
      #...behave in the same way of the code "split" [sending error...
      #...messages when the quantity of elements of the array it is not...
      #...according to the quantity of slips that we want to do]:
          #"vsplit()": generating results equals of the code...
          #..."array_split()" in axis 0.
          #"hsplit()": generating results equals of the code...
          #..."array_split()" in axis 1.
          #"dsplit()": generating results or arrays in 3D or more.

# ONE DIMENSION (1D)

#Example 6.0.12.1.1:
#In this case we are applying the function array_split(), to split a 1D...
#...array in 3 1D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) 

#Example 6.0.12.1.2:
#In this case we are applying the function array_split(), to split a 1D...
#...array in 3 1D arrays in the "axis 1", getting as an answer an error...
#...because for a tuple the split in the "axis 1" is out fo range.
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3, axis =1)
print(newarr) 

#Example 6.0.12.1.3:
#In this case we are applying the function "hsplit()", to split a 1D...
#...array in 3 1D arrays.

    #We get the same result of "Example 6.0.12.1.1" (split a 1D...
    #...array in 3 1D arrays in the "axis 0" (axis by default).)
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.hsplit(arr, 3)
print(newarr) 

#Example 6.0.12.1.4:
#In this case we are applying the function "dsplit()", to split a 1D...
#...array in 3 1D arrays.

    #Getting as an answer an error due to the fact that "dsplit()" only...
    #...works on arrays of 3 or more dimensions.
    
    #"dsplit()" is for split in depth of arrays.
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.dsplit(arr, 3)
print(newarr) 

#Example 6.0.12.1.5:
#In this case we are applying the function "vsplit()", to split a 1D...
#...array in 3 1D arrays.

    #Getting as an answer an error due to the fact that "vsplit()" only...
    #...works on arrays of 2 or more dimensions.
    
    #"vsplit()" is for split in high of arrays.
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.vsplit(arr, 3)
print(newarr) 

#Example 6.0.12.2:
#In this case we are applying the function array_split(), to split a 1D...
#...array in 5 1D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 5)
print(newarr) 

# TWO DIMENSIONS (2D)

#Example 6.0.12.3.1:
#In this case we are applying the function array_split(), to split a 2D...
#...array in 3 2D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([[1, 2, 3], [50, 60, 70],[500, 600, 700]])
newarr = np.array_split(arr, 3)
print(newarr) 

#Example 6.0.12.3.2:
#In this case we are applying the function array_split(), to split a 2D...
#...array in 3 2D arrays in the "axis 1".
import numpy as np 
arr = np.array([[1, 2, 3], [50, 60, 70],[500, 600, 700]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr) 

#Example 6.0.12.3.3: 
#In this case we are applying the function "hsplit()", to split a 2D...
#...array in 3 2D arrays.

#We get the same result of "Example 6.0.12.3.2" (i.e.split split a 2D...
#...array in 3 2D arrays in the "axis 1".
import numpy as np 
arr = np.array([[1, 2, 3], [50, 60, 70],[500, 600, 700]])
newarr = np.hsplit(arr, 3)
print(newarr) 

#Example 6.0.12.3.4:
#In this case we are applying the function "vsplit()", to split a 2D...
#...array in 3 2D arrays.

#We get the same result of "Example 6.0.12.3.1" (i.e.split split a 2D...
#...array in 3 2D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([[1, 2, 3], [50, 60, 70],[500, 600, 700]])
newarr = np.vsplit(arr, 3)
print(newarr) 

#Example 6.0.12.3.5: 
#In this case we are applying the function "dsplit()", to split a 2D...
#...array in 3 2D arrays.

    #Getting as an answer an error due to the fact that "dsplit()" only...
    #...works on arrays of 3 or more dimensions.                                        
import numpy as np 
arr = np.array([[1, 2, 3], [50, 60, 70],[500, 600, 700]])
newarr = np.dsplit(arr, 3)
print(newarr) 

#Example 6.0.12.4: 
#In this case we are applying the function array_split(), to split a 2D...
#...array in 7 2D arrays in the "axis 0" (axis by default).

    #In this case we can see that will appear in the answer from the...
    #...fourth to the seventh array that they are blank arrays with the....
    #....shape of the original array. To avoid this we need to be sure...
    #...that the same number of splits is less or equal to the same...
    #...number of subarrays that belong to the main array.
    
    #Also we need to be careful about the dimension of the original array.
import numpy as np 
arr = np.array([[1, 2, 3, 4, 5], [50, 60, 70, 80, 90],[500, 600, 700, 800, 900]])
newarr = np.array_split(arr, 7)
print(newarr) 

#Example 6.0.12.5:
#In this case we are applying the function array_split(), to split a 2D...
#...array in 3 2D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([[1, 2, 3, 4, 5], [50, 60, 70, 80, 90],[500, 600, 700, 800, 900]])
newarr = np.array_split(arr, 3)
print(newarr) 

# THREE DIMENSIONS (3D)

#Example 6.0.12.6: 
#In this case we are applying the function array_split(), to split a 3D...
#...array in 4 3D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]], [[100, 200, 300, 400], [500, 600, 700, 800]]])
newarr = np.array_split(arr, 4)
print(newarr) 

#Example 6.0.12.7:
#In this case we are applying the function split(), to split a 3D...
#...array in 4 3D arrays, but we get an error message due to the fact...
#...that the code "np.split()" do not know how to handle splits that...
#...are not compatible or adjustable to the quantity of elements...
#...of the original array.
import numpy as np 
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]], [[100, 200, 300, 400], [500, 600, 700, 800]]])
newarr = np.split(arr, 4)
print(newarr) 

#Example 6.0.12.8.1:
#In this case we are applying the function split(), to split a 3D...
#...array in 3 3D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]], [[100, 200, 300, 400], [500, 600, 700, 800]]])
newarr = np.split(arr, 3)  
print(newarr) 

#Example 6.0.12.8.2:
#In this case we are applying the function split(), to split a 3D...
#...array in 3 3D arrays in the "axis 1", but we get an error message...
#...due to the fact that the code "np.split()" do not know how to....
#...handle splits that are not compatible or adjustable to the quantity...
#...of elements of the original array (array split does not result in an...
#...equal division).
import numpy as np 
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]], [[100, 200, 300, 400], [500, 600, 700, 800]]])
newarr = np.split(arr, 3, axis =1)  
print(newarr) 

#Example 6.0.12.9.1:
#In this case we are applying the function hsplit(), to split a 3D...
#...array in 3 3D arrays, but we get an error message...
#...due to the fact that the code "np.hsplit()" do not know how to....
#...handle splits that are not compatible or adjustable to the quantity...
#...of elements of the original array (array split does not result in an...
#...equal division).
import numpy as np 
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 20, 30, 40], [50, 60, 70, 80]], [[100, 200, 300, 400], [500, 600, 700, 800]]])
newarr = np.hsplit(arr, 3)  
print(newarr) 

#Example 6.0.12.9.2:
#In this case we are applying the function hsplit(), to split a 3D...
#...array in 3 3D arrays.
import numpy as np 
arr = np.array([[[1, 2], [5, 6], [8, 9]], [[10, 20], [50, 60], [70, 90]], [[100, 200], [500, 600], [700, 800]]])
newarr = np.hsplit(arr, 3)  
print(newarr) 

#Example 6.0.12.10:
#In this case we are applying the function vsplit(), to split a 3D...
#...array in 3 (this 3 is according to the number of columns of the...
#...sub-arrays) 3D arrays.

#We get the same result of "Example 6.0.12.8.1" (i.e.split split a 3D...
#...array in 3 3D arrays in the "axis 0" (axis by default).
import numpy as np 
arr = np.array([[[1, 2], [5, 6], [8, 9]], [[10, 20], [50, 60], [70, 90]], [[100, 200], [500, 600], [700, 800]]])
newarr = np.vsplit(arr, 3)  
print(newarr) 

#Example 6.0.12.11:
#In this case we are applying the function dsplit(), to split a 3D...
#...array in 2 (this 2 is according to the number of columns of the...
#...sub-arrays) 3D arrays.
import numpy as np 
arr = np.array([[[1, 2], [5, 6], [8, 9]], [[10, 20], [50, 60], [70, 90]], [[100, 200], [500, 600], [700, 800]]])
newarr = np.dsplit(arr, 2)  
print(newarr) 

#Topic 6.0.13 - NumPy (NumPy Searching Arrays):
  #The website said that we could search an array for a certain value,...
  #...and get as a return the indexes that get a match (thar index is..
  #...like a Python index).
    #We use to do that the "where()" method.

#Example 6.0.13.1:
#In this case we are applying the function "where()", to find the index...
#...of a specific element (in this case is the number "4") of an array.
   #Be careful in this instance, because several times appears the number....
   #..."4"; therefore, the answer shows several index.
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) 

#Example 6.0.13.2:
#In this case we are applying the function "where()", to find the index...
#...of a specific element (in this case is the word "dog") of an array.
import numpy as np 
arr = np.array(["cat", "dog", "mouse"])
x = np.where(arr == "dog")
print(x) 

#Example 6.0.13.3:
#In this case we are applying the function "where()", to find the index...
#...of a specific element (in this case is the word "astra") of an array.

   #Due to the fact that the word "astra" does not apper in the array....
   #...we get as an answer a blank array.
import numpy as np 
arr = np.array(["cat", "dog", "mouse"])
x = np.where(arr == "astra")
print(x) 

#Example 6.0.13.4:
#In this case we are applying the function "where()", to find the index...
#...of a specific element (in this case the number greater than 4) of...
#...an array.
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr > 4)
print(x) 

#Topic 6.0.14 - NumPy (NumPy Sorting Arrays):
  #This code is very helpful to sort elements of an array (str, float,...
  #..int, boolean) in ordered sequence (ascending or descending,...
  #...or alphabetically).
  #We use to do that the "sort()" function.
    #It is important to say that this code generate a new array and do...
    #...not modify the original array.
    #If we mix in the array different type of data (str, float, int,....
    #...or boolean) there is no problem.
    
#Example 6.0.14.1:
#In this case we are applying the function "sort()", to order sequentially...
#...the elements of an array.
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) 

#Example 6.0.14.2:
#In this case we are applying the function "sort()", to order sequentially...
#...the elements of an array.
import numpy as np
arr = np.array(["dog", "bitcoin", "polygon", "ether"])
print(np.sort(arr))                     
                      
#Example 6.0.14.2:
#In this case we are applying the function "sort()", to order sequentially...
#...the elements of an array.
import numpy as np
arr = np.array(["dog", "bitcoin", "polygon", 4])
print(np.sort(arr))                          

##############################################################################

##############################################################################

##############################################################################                      
                      
#Numpy 6.1:
    #It is the fundamental package for numeric computing with Python.
    #It provides powerful ways to create, store and manipulate data, which...
    #...makes it able to seamlessly and speedily integrate with a wide variety...
    #...of databases and data formats.
    #This is also the foundation that Pandas is built on which is a high....
    #...performance data-centric package.
    
import numpy as np

#Numpy 6.2 (Arrays):
    #Arrays: are displayed as a list or lists of lists.
    #When creating an array, we pass into it a list as an argument.
    
array1 = np.array([1,2,3])
print(array1)
print("\n") 

    #Dimensiones of Arrays.
    
    #"Dimension" is not equal to "Shape" of an array. 
    
    #"Dimension": give us through a scalar value the quantity of...
    #...dimensions of an array (1D, 2D, 3D,...)
    
    #"Shape": give us through a tuple the quantity of elements...
    #...of an array no matter its dimension.

print(array1.ndim)
print("\n")     
    
    #When we are creating an array as a list of list, we are creating a...
    #...multidimensional list; therefore, we can see multiple square brackets...
    #...(i.e. several inner lists) inside a single square bracket (i.e. the ...
    #...main list).
import numpy as np   
array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2)
print("\n")

print(array2.ndim)
print("\n") 

    # We can print out the length of each dimension of the list or main list...
    #...(in the case we have several lists) by calling the "shape attribute",...
    #...which returns a tuple (it is easy to see that because the parentheses...
    #...in the printed result).

print(array2.shape)
print("\n") 

    #We can also check the type of items in the array. 
    #Integers = int32
    #Floats = float64. (It will happen if we have at least one value with...
    #...decimales inside the array).
    
print(array2.dtype)
print("\n") 

array3 = np.array([[1,2.6,3],[4,5,6]])

print(array3.dtype)
print("\n") 

   #When we see the printed result of an array with one or more decimales,...
   #...Numpy automatically converts integers, up to floats (in the data...
   #...type result). Numpy will give us...
   #...the best data type format possible to keep your data types homogeneous...
   #...which means all the same, in the array.
   
   # When manipulating arrays of different types, the type of the resulting..
   #...array will correspond to the more general of the two types. This is...
   #..called "upcasting".

print(array3)
print("\n") 

    #Numpy offers several functions to create arrays with placeholders, such...
    #...as zero's or one's.

array4 = np.zeros((2,3))
print(array4)
print("\n") 

array5 = np.ones((2,3))
print(array5)
print("\n") 

    #Numpy offers several functions to create arrays with placeholders, such...
    #...random numbers (from 0 to 1)

array6 = np.random.rand(2,3)
print(array6)
print("\n") 

    #We can also create a sequence of numbers in an array with the "arrange()"...
    #...function. The fist argument is the starting bound (inclusive)...
    #...and the second...
    #...argument is the ending bound (exclusive), and the third argument is...
    #...the difference between each consecutive numbers.

array7 = np.arange(10, 50, 2)
print(array7)
print("\n") 

    #If we want to generate a sequence of floats, we can use the "linspace()...
    #...function. The fist argument is the starting bound (inclusive)...
    #...and the second...
    #...argument is the ending bound (inclusive). In this function the third...
    #...argument is the total number of items you want to generate.
    
array8 = np.linspace(0, 2, 15)
print(array8)
print("\n") 

#Numpy 6.3 (Arrays Operations):
    #We can do: mathematical manipulation (addition, subtraction, square,...
    #...exponents) as well as use boolean arrays, which are binary values. We...
    #...can also do matrix manipulation such as product, transpose, inverse, etc.
    
    # Arithmetic operators on array apply elementwise.
    
    #Elementwise = it means that we add, substract, product, etc of one element...
    #...of an array to other element in the same position of other array.
array9 = np.array([10,20,30,40])
array10 = np.array([1, 2, 3,4])
array11= array9 - array10
print(array11)
print("\n") 

array12= array9 * array10
print(array12)
print("\n") 

    #We can apply an operator (boolean operator like <,>,==,!=) on an array, and..
    #...a boolean array will be returned for any element in the original, with...
    #..."True" being emitted if it meets the condition and "False" oetherwise.

array13 = np.array([10,20,30,40])
array14 = (array13 > 25)
print(array14)
print("\n") 
    
    #Matrix Manipulation (For Elementwise Product, we use the symbol *)
array15 = np.array([[1,1],[0,1]])
array16 = np.array([[2,0],[3,4]])
print(array15*array16)
print("\n") 

    #Matrix Manipulation (For Matrix Product, also called dot function, we use...
    #....the symbol @). It is importante to see that this result is very...
    #...different from the "Elementwise Product".
    
    #Matrix Product, also called dot function: We need to be careful of the...
    #...dimension of every vector or matrix.
print(array15@array16)
print("\n") 

    # Numpy arrays have many interesting aggregation functions on them, such...
    #...as  sum(), max(), min(), and mean()
array17 = np.array([100,200,300,400,500])
print(array17.sum())
print(array17.max())
print(array17.min())
print(array17.mean())
print("\n") 

    #We can change the shape (quantity of rows and columns) of an array wih...
    #...the code "reshape".
array18 = np.arange(1,16,1)
array19 = np.arange(1,16,1).reshape(3,5)
print(array18)
print(array19)
print("\n")

#Numpy 6.4 (Indexing):

    #This index in Numpy works exactly like Python Index (it means, starts in...
    #...0,1,2,3 and so on). In this case we can see the Indexing in a one...
    #...dimensional array.
array20 = np.array([10,20,30,40,50])
print(array20[3])
print("\n") 

    #This index in Numpy works exactly like Python Index (it means, starts in...
    #...0,1,2,3 and so on). In this case we can see the Indexing in a two...
    #...dimensional array.
    
    #In this case the first value (integer) is the row and the second value...
    #...(integer) is the the column
array21 = np.array([[1,2], [3, 4]])
print(array21[1,1])
print("\n") 

    #If we want to get multiple elements for example, "1, 4, and 100" and put...
    #...them into a one-dimensional array we can enter the indices directly...
    #...into an array function
import numpy as np  
array22 = np.array([[1,2], [3, 4],[100,45]])
array23 = np.array([array22 [0, 0],array22 [1, 1],array22 [2, 0]])
print(array23)
print("\n") 

    #We can also get multiple elements by using the following form array...
    #...indexing, which essentiall "consolidate" the first list and the second list.
print(array22[[0, 1, 2], [0, 1, 0]])
print("\n") 

#Numpy 6.5 (Boolen Indexing)

    # Boolean indexing allows us to select arbitrary elements based on conditions. 
    
    #We can apply an operator (boolean operator like <,>,==,!=) on an array, and..
    #...a boolean array will be returned, with "True" being emitted if it...
    #...meets the condition and "False" oetherwise.
array24 = np.array([[1,2], [3, 4],[100,45]])
array25 = (array24 > 25)
print(array25)
print("\n") 

#Numpy 6.6 (Slicing):

   # Slicing is a way to create a sub-array based on the original array. When...
   #...we do slice, for instance (2:5), the first number is inclusive and...
   #...the second number is exclusive.
   
   #Option 1: For one-dimensional arrays, slicing works in similar ways to...
   #...a list. (i.e that we get a piece of the array).
array26 = np.array([0,1,2,3,4,5])
print(array26[:3])
print("\n") 

    #Option 2: For multi-dimensional arrays, it works similarly. With this...
    #...kind of examples we get a complete array of the group of arrays.
        #For instance, the first and second value of the slice are related with...
        #...the rows.
array27 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(array27[:2])
print("\n") 

    #Option 3: For multi-dimensional arrays, it works similarly. With this...
    #...kind of examples we get a piece of the severals arrays that belong to...
    #...group of arrays. 
        #For instance, the first and second value of the slice are related with...
        #...the rows an the third and fourth value are related with columns.
array28 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(array28[:2,0:2])
print("\n") 

    #With slicing, we can change the values of the members of the array..

array29 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
array29[0] = 1000000
print(array29)
print("\n") 

#Numpy 6.7 (Load Data):

# To load a dataset in Numpy, we can use the genfromtxt() function: 
    #We can specify data file name, delimiter (which is optional but often...
    #...used), and number of rows to skip if we have a header row.
    #This function has a parameter called dtype for specifying data types..
    #...of each column (this parameter is optional). Without specifying the...
    #...types, all types will be casted the same to the more general/precise type

wines = np.genfromtxt("datasets/winequality-red.csv", delimiter=";", skip_header=1)
print(wines)
print("\n") 

#If we want several non-consecutive columns, we can place the indices of the...
#...columns that we want into an array and pass the array as the second...
#...argument.
array30 = wines[:, [0,2,4]]
print(array30)
print("\n") 

# We can also do some basic summarization of this dataset (in this case we...
#...want to know the mean value of the column). For example, to...
#...find out the average (mean value) quality of red wine, we can select the quality...
#...column. 
array31 = wines[:,-1].mean()
print(array31)
print("\n") 

##############################################################################

##############################################################################

##############################################################################

#Regular Expressions (also called RegEx) - 7: (RMDLC)
    
#Usually when we do string matching, instead of RegEx (more sophisticated...
#...pattern-matching capabilities) we use:
    #Option 1: Strings operators
    #OPtion 2: Built-in string methods like ".find() and .index()"

#Regex functionality in Python resides in a module named "re". 
    #The "re" module contains many useful functions and methods. One of the...
    #...most important functinos es "re.search()".
        #re.search(regex, string):
            
            #It works looking for the first location where the pattern...
            #..."regex" matches. If a match is found, then "re.search()"...
            #...returns a "match object". Otherwise, it returns "None". 
                                             
#Metacharacter:
    #It is important to say that the "regex parser" regards any character...
    #...not listed as a "Metacharacter" an ordinary character that matches..
    #...only itself.
        #Apparently the "regex parser" (in spanish the "analizador regex")...
        #...is considered the part of the code in charge of to find the....
        #...characters. Usually has the form or shape of "re.function()" code.
    
        #When the "regex parser" encounters one of the metacharacter...
        #...sequences, a match happens if the character at the current...
        #...parsing position fits the description that the sequence describes.
    
    #The real power of RegEx matching in Python emerges when "regex" contains...
    #...metacharacters. Some instances of metacharacters are the followings:
        
        #Square brackets []: This metacharacter...
        #...matches any single character that is inside. Square brackets can...
        #...be used to indicate a characters or set of characters, so...
        #...for instance [abc] matches 'a' or 'b' or 'c'. with the exception...
        #...that dot "." just means a literal dot.
        
        #A "character class" is represented by one or more characters...
        #...surrounded by square brackets ([]). When Python encounters a...
        #...character class in a regular expression, it will be matched by...
        #...an occurrence of any of the characters within the character class.

#Topic 7: Example 7.1

#We can see as an answer "<_sre.SRE_Match object; span=(3, 6), match='123'>".
  #This show us that in fact the code "re.search" return a match object...
  #...rather than "None". (in other words, the specified "regex" {object...
  #...of interest} is present inside the "string".
  
  #This show us that the span=(3, 6) indicates the indexes of portion of...
  #...the "string" (i.e. "123") in which the match was found.

import re
s = 'foo123bar'
print(re.search("123", s))
print("\n") 

#Topic 7: Example 7.2.1

#We can see as an answer "<_sre.SRE_Match object; span=(3, 6), match='123'>".
  #This show us the same result of Example 7.1, but in this case we use the...
  #...Metacharacter "Square brackets" []. To be specific [0-9] matches any...
  #...single decimal digit character (any character between '0' and '9',...
  #...inclusive). The full expression [0-9][0-9][0-9] matches any sequence...
  #...of three decimal digit characters.

import re
s = 'foo123bar'
print(re.search("[0-9][0-9][0-9]", s))
print("\n") 

import re
s = 'foo123.45564bar'
print(re.search("[0-9. ]+", s))
print("\n") 

import re
s = '123-456-7890'
print(re.search("(\(\d{3}\)|\d{3}-)\d{3}-\d{4}", s))
print("\n") 

#Topic 7: Example 7.2.2

#Square brackets can be used to indicate a set of characters, so [abc] matches...
#...'a' or 'b' or 'c'. 
import re
s = 'foo123bar'
print(re.search("[123]", s))
print("\n") 

import re
s = 'foo123bar'
print(re.search("[0-9]", s))
print("\n") 

  #If the string does not has or does not match the quantity decimal...
  #...digit character (established in through "Square brackets" []) we are...
  #...going to get as an answer "None".

import re
t = 'foo13bar'
print(re.search("[0-9][0-9][0-9]", t))
print("\n") 


#Metacharacters

#Topic 7: Example 7.3

#We can see as an answer "<_sre.SRE_Match object; span=(3, 6), match='123'>".

  #Number N°0
  #The dot regex "." matches all characters except the newline character "\n".
  #Combined with the asterisk quantifier in the pattern '.*', the dot regex...
  #...matches an arbitrary number of symbols except newline characters.
  
  #Every "dot" search for a single charachter (i.e. 3 "dots"search for 3...
  #...characters of the text).

import re
s = 'foo123bar'
print(re.search("1.3", s))
print("\n") 

s = 'foo123bar'
print(re.search(".", s))
print("\n") 

s = 'foo123bar'
print(re.search("....", s))
print("\n") 

s = 'foo123bar'
print(re.search(".*", s))
print("\n") 

import re
s = 'foocarropazulbar'
print(re.search("carro.azul", s))
print("\n") 

  #If in the metacharacter {inside the "re.search()"} we omit the value...
  #...at the right side of the "dot" the match will be automatically...
  #...the left side and any character or value inmeditely at the right...
  #...side. It is interesting that we will see how the span showed in...
  #...answer take in count the "dot".
import re
s = 'foo16bar'
print(re.search("1.", s))
print("\n") 

  #If in the metacharacter {inside the "re.search()"} we omit the value...
  #...at the left side of the "dot" the match will be automatically...
  #...the right side and any character or value inmeditely at the left...
  #...side. It is interesting that we will see how the span showed in...
  #...answer take in count the "dot".
import re
s = 'foo16bar'
print(re.search(".6", s))
print("\n") 

  #If the string does not has or does not match the quantity of three...
  #...characters we are going to get as an answer "None".
import re
s = 'foo16bar'
print(re.search("1.6", s))
print("\n") 

  #If the string has newline (described has "\n" inside the string) we are...
  #...going to get as an answer "None".
import re
s = 'foo1\n6bar'
print(re.search("1.6", s))
print("\n") 

import re
s = 'foo1\n6bar'
print(re.search(".", s))
print("\n") 

    #Number N°1
    #The metacharacter sequences wrote inside square brackets [] is for...
    #...match a single character from the searched string. When the regex...
    #...parser encounters one of these metacharacter sequences, a match....
    #...happens.
    
        #Square brackets can be used to indicate a set of characters, so...
        #...[abc] matches 'a' or 'b' or 'c'. 
        
        #A "character class" is represented by one or more characters...
        #...surrounded by square brackets ([]). When Python encounters a...
        #...character class in a regular expression, it will be matched by...
        #...an occurrence of any of the characters within the character class.
        
#Topic 7: Example 7.4.1
#In this case we are very interested in found inside a string the word that...
#...begin with the letters "ba" and continue with the letters "a" or "r" or...
#..."t" or "z"; therefore, it is trying to match the words "baa", "bar",...
#..."bat" and "baz", matching finally the word "bar". 
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('ba[artz]', 'foobarqux'))
print("\n")

#We get the same result using quotation marks.
import re
print(re.search('bar', 'foobarqux'))
print("\n")

#Topic 7: Example 7.4.2
#In this case we are very interested in found inside a string the word that...
#...begin with the letters "a" or "r" or "t" or "z" and finish with the...
#...letters "qu" ; therefore, it is trying to match the words "aqu", "rqu",...
#..."tqu" and "zqu", matching finally the word "rqu". 
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('[artz]qu', 'foobarqux'))
print("\n")

#Topic 7: Example 7.4.3
#In this case we are very interested in found a string with the letter "a"...
#...without putting the word outside the square bracket.
    #As a result, get only the position of the letter "a".
import re
print(re.search('[artz]', 'foobarqux'))
print("\n") 

import re
print(re.search('[ar]', 'foobarqux'))
print("\n") 

import re
print(re.search('[a]', 'foobarqux'))
print("\n") 

#Topic 7: Example 7.5 
#In this case we are very interested in found inside a string the word that...
#...begin with the letters "ba" and continue with the letters "a" or "r" or...
#..."t" or "z"; therefore, it is trying to match the words "baa", "bar",...
#..."bat" and "baz", matching finally the word "baz".
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('ba[artz]', 'foobazqux'))
print("\n") 

    #Number N°2
    #A "character class" can also contain a range of characters separated...
    #...by a hyphen "-", in which case it matches any single character...
    #..within the range. It is important to say that this code only...
    #...match one character; therefore, if we want to match more characters...
    #...we need to write more square brackets.
        #For example, [a-z] matches (only one) any lowercase alphabetic...
        #...character between 'a' and 'z' (inclusive "a" and "z"). 
        
    #Note: the return value is always the leftmost possible matched by...
    #..."re.search()". This code search string from left to right, and as...
    #...soon as it locates a match for <regex>, it stops scanning and...
    #...returns the match.

#Topic 7: Example 7.6.1
#In this case we are very interested in found inside a string the first...
#...characters in lowercase in the range from "a" to "z".
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('[a-z]', 'FOObar'))
print("\n") 

#Topic 7: Example 7.6.2
#In this case we are very interested in found inside a string the first...
#...characters in lowercase  in the range from "e" to "f".
    #In essence, get as an answer "None" because there is no lowercase..
    #...letter in the range from "e" to "f".
import re
print(re.search('[e-f]', 'FOOzzr'))
print("\n") 

#Topic 7: Example 7.7.1
#In this case we are very interested in found inside a string the first...
#...characters number in the range from "0" to "9".
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('[0-9]', 'foo123bar'))
print("\n") 

#Topic 7: Example 7.7.2
#In this case we are very interested in found inside a string the first...
#...characters number in the range from "4" to "7".
    #In essence, get as an answer "None" because there is no lowercase..
    #...letter in the range from "4" to "7".
import re
print(re.search('[4-7]', 'foo123bar'))
print("\n") 

#Topic 7: Example 7.8
#In this case we are very interested in found inside a string the first...
#...two characters numbers
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('[0-9][0-9]', 'foo123bar'))
print("\n") 

    #Number N°3
    #A "character class" can also contain the "^" which matches the first...
    #...character that do not start with the "character class" listed inside...
    #...the square brackets (as long as they are wrote as range with...
    #...hyphen). 
    
    #A "character class" can also contain the "^" which matches the first...
    #...character that start with the "character class" (that is a string)...
    #...listed inside the square brackets (as long as they are not wrote...
    #...as range with hyphen). 
    
    #If the "^" character appears in a character class but isn’t the first...
    #...character, then it has no special meaning and matches a literal "^"...
    #...character.

#Topic 7: Example 7.9
#In this case we are very interested in found inside a string the first...
#...character that it is not a number in the range from "0" to "9".
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('[^0-9]', 'foo123bar'))
print("\n") 

#Topic 7: Example 7.9.1
#In this case we are very interested in found inside a string the first...
#...characters that it is not a letter.
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('[^a-z]', 'foo129bar'))
print("\n") 

#Topic 7: Example 7.9.2
#In this case we are very interested in found inside a string the first...
#...characters that it is a letter.
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
import re
print(re.search('[^a]', 'foo129bar'))
print("\n") 

    #Number N°4
    #If we want to find literally in a string a hyphen character "-" (i.e...
    #...we are not interested in used like a range), we can:
        #Place the hyphen as first or last character
        #Escape the hyphen with a backslash "\"
        #Put the hyphen alone between square brackets
        #Put the hyphen alone between quotation marks.

#Topic 7: Example 7.10
#In this case we are very interested in found inside a string the first...
#...characters that it is not a letter.
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
    
    #It is important to say that the metacharacter "\" espaces a...
    #...metacharacter of its special meaning.
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.
import re
print(re.search('[-abc]', 'foo-123bar'))
print("\n") 

import re
print(re.search('[a-]', 'foo-123bar'))
print("\n") 

import re
print(re.search('[-]', 'foo-123bar'))
print("\n") 

import re
print(re.search('-', 'foo-123bar'))
print("\n") 

import re
print(re.search('[ab\-c]', 'foo-123bar'))
print("\n") 

import re
print(re.search('[\-]', 'foo-123bar'))
print("\n") 

    #Number N°5 
    #If we want to find literally in a string a piece of square bracket...
    #...character, we can place the piece of square bracket as first or...
    #...last character or with a backslash "\".

#Topic 7: Example 7.11.1
#In this case we are very interested in found inside a string the first...
#...characters that it is a square bracket "]" or this "[" using square....
#...brackets [].
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.
import re
print(re.search('[[]', 'foo[123bar'))
print("\n") 

import re
print(re.search('[ab\]c]', 'foo]123bar'))  
print("\n") 

import re
print(re.search('[\]]', 'foo]123b]ar'))  
print("\n") 

#Topic 7: Example 7.11.2
#In this case we are very interested in found inside a string the first...
#...characters that it is a square bracket "]" or this "[" using quotation....
#...marks "".
    #In essence, we confirm that what we are looking for is inside the...
    #...string when we get the position of the object and also the character...
    #...matched.
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.
    
import re
print(re.search('\]', 'foo]123bar'))  
print("\n") 

    #Number N°6 
    #We used "\w" if we want to find any alphanumeric word character (a word...
    #...characters are uppercase and lowercase letters, digits, and the...
    #...underscore (_) character. If there is not an alphanumeric word...
    #...character the printed answer will be "None".
    
    #It only matches a single word char, not a whole word.
    
    #We can use "square brackets []" or "quotation marks"
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.
    
    #What is the difference of "\w" (without the space and without..
            #...square brackets) instead of "[\w ]"?
                #First it is important to remember that the square brackets...
                #...without the outside company of other characters like...
                #..."+,*,?" just match a single character. Therefore, if...
                #...we use several square brackets (for instance: "[][][]"...
                #...3 square bracketsto match 3 characters) we are going to...
                #...match several characters.
                
                #A "character class" is represented by one or more characters...
                #...surrounded by square brackets ([]). When Python...
                #...encounters a character class in a regular expression, it...
                #...will be matched by an occurrence of any of the characters...
                #...within the character class. 
                
                #The space " " is important to be considered in the match if we...
                #...are interested in match text that has one or more spaces.
                
                #The code"[\w ]*" try to match any quantity of characters and...
                #...spaces.
  
            #What is the difference of "\w" (without square brackets) instead...
            #...of "[\w ]"?
                #We are going to get the same match result with and without...
                #...the square bracket when we use "\w " and "[\w ]". However...
                #...we need to consider:
                    #Use "\w*" for a single word or string that is not...
                    #...located after a newline "\n".
                    #Use "[\w]*" for a single word or string that is...
                    #...located after a newline "\n".

#Topic 7: Example 7.12.1   
import re
print(re.search('[\w]', '###_/()'))  
print("\n") 

import re
print(re.search('[\w]', '###a/()'))  
print("\n") 

import re
print(re.search('[\w]', '###L/()'))  
print("\n")

import re
print(re.search('[\w]', '###0896/()'))  
print("\n") 

import re
print(re.search('[\w][\w]*', '###0896/()'))  
print("\n")   

import re
print(re.search('[\w][\w]', '###0896/()'))  
print("\n")  

import re
print(re.search('\w\w', '###0896/()'))  
print("\n")  

import re
print(re.search('\w\w*', '###0896/()'))  
print("\n")  

import re
print(re.search('\w', '###0896/()'))  
print("\n") 

import re
print(re.search('[\w]', '###/()'))  
print("\n")  

import re
print(re.search('\w *', 'I know that this is OK'))  
print("\n") 

import re
print(re.search('[\w ]*', 'I know that this is OK'))  
print("\n") 

import re
print(re.search('\w*', 'Ih know that this is OK'))  
print("\n") 

import re
print(re.search('[\w]*', 'Ih know that this is OK'))  
print("\n")   

import re
print(re.search('\w', 'Ih know that this is OK'))  
print("\n") 

import re
print(re.search('[\w]', 'I know that this is OK'))  
print("\n")   

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("[\w]", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("\w", s))
print("\n") 
        
import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("[\w ]*", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("\w  *", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("[\w ]", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("\w ", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("[\w]*", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("\w*", s))
print("\n") 


    #Number N°7 
    #We used "\W" if we want to find any non-alphanumeric word character...
    #...(a word characters are uppercase and lowercase letters, digits, and...
    #...the underscore (_) character. If there is only alphanumeric word...
    #...characters the printed answer will be "None".
    
    #We can use "square brackets []" or "quotation marks"
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.
    
#Topic 7: Example 7.13                  
import re
print(re.search('[\W]', 'aaa#gjhg683t742'))  
print("\n") 

import re
print(re.search('\W', 'aaa#gjhg683t742'))  
print("\n") 

import re
print(re.search('[\W]', 'aaagjhg683t742'))  
print("\n")

    #Number N°8 
    #We used "\d" if we want to find any decimal digit character. (i.e. "\d"...
    #...is essentially equivalent to [0-9]). If there is not decimal...
    #...digit character characters the printed answer will be "None".
    
    #We can use "square brackets []" or "quotation marks"
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.

#Topic 7: Example 7.14.1
import re
print(re.search('[\d]', 't742'))  
print("\n") 

import re
print(re.search('\d', 't742'))  
print("\n") 

import re
print(re.search('[\d]', 'abcusX'))  
print("\n") 

#Topic 7: Example 7.14.2
#We are mixing the "Number N°8" and "Number N°1".
import re
print(re.search('7[\d]', 't742'))  
print("\n") 

import re
print(re.search('http\/[\d]', 'thttp/42'))  
print("\n") 

#Topic 7: Example 7.14.3
#We trying to fin a "dot" a two numbers in the range from 0 to 9 after...
#...the "dot".
import re
print(re.search('\.\d{2}', 'The bill is $742.35, therefore you need to pay'))  
print("\n") 


    #Number N°9 
    #We used "\D" if we want to find any non-decimal digit character.(i.e...
    #..."\d" is essentially equivalent to [^0-9]).If there is not a letter...
    #...or other special character the printed answer will be "None".
    
    #We can use "square brackets []" or "quotation marks"
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.

#Topic 7: Example 7.15  
import re
print(re.search('[\D]', '742t'))  
print("\n") 

import re
print(re.search('\D', '#t'))  
print("\n") 

import re
print(re.search('[\D]', '563456'))  
print("\n")

    #Number N°10 
    #We used "\s" if we want to find any blank spaces.
    
    #Unlike the dot metacharacter, "\s" does match a newline "\n" character...
    #...(i.e. the newline "\n" character is considered a blank space;...
    #...therefore, is detected by the "\s" metacharacter). If there is...
    #...not blank spaces or newline "\n" character the printed answer...
    #...will be "None".
    
    #We can use "square brackets []" or "quotation marks"
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.

#Topic 7: Example 7.16  
import re
print(re.search('[\s]', '742 t'))  
print("\n") 

import re
s = 'foo1\n6bar'
print(re.search('[\s]', s))
print("\n") 

import re
print(re.search('\s', '742 t'))  
print("\n") 

import re
s = 'foo1\n6bar'
print(re.search('\s', s))
print("\n") 

import re
s = 'foo1ar'
print(re.search('[\s]', s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search('[\s]', s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search('\s', s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search('\sbe\s', s))
print("\n") 

    #It is important to see that there are more than one way to search and...
    #...match fo the blank spaces. Those are:
        #Using explicitly the blank spaces. In essence "text text text"
        
        #Using the metacharacter "\s". In essence "text\stext\stext".
        
        #Using the metacharacter "\". In essence "text\ text\ text".
import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search('will be amazing', s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search('will\sbe\samazing', s))
print("\n") 


import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("will\ be\ amazing", s))
print("\n") 
 

    #Number N°11 
    #We used "\S" if we want to find any character that is not a blank space.
    
    #Unlike the dot metacharacter, "\S" does not match a newline "\n" character...
    #...(i.e. the newline "\n" character is considered a blank space;...
    #...therefore, is not detected by the "\S" metacharacter). If there is...
    #...not any character that is not a blank space or newline "\n"...
    #...character the printed answer will be "None".

    #We can use "square brackets []" or "quotation marks"
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.
    
#Topic 7: Example 7.17
import re
print(re.search('[\S]', '742 t'))  
print("\n") 

import re
print(re.search('[\S]', ' 742t'))  
print("\n")

import re
s = 'foo1\n6bar'
print(re.search('[\S]', '  \n foo  \n  '))
print("\n") 

import re
s = 'foo1\n6bar'
print(re.search('\S', '  \n foo  \n  '))
print("\n") 

import re
s = 'foo1\n6bar'
print(re.search('\S', ' '))
print("\n") 

    #Number N°12
    #We can mix metacharacters.
    
#Topic 7: Example 7.18  
#In this case we are interested in find a character that is: 
    #Any blank spaces (We use "\s")
    #Any decimal digit character equivalent to [0-9]). (We used "\d")
    #Any alphanumeric word character (a word characters are uppercase...
    #...and lowercase letters, digits, and the underscore (_) character...
    #...If there is not an alphanumeric word character the printed...
    #...answer will be "None". (We used "\w")
    
    #We need to use only "square brackets []" in this case of mixing...
    #...because with the "quotation marks" the answer that we get is "None".
    
    #It is important to say that it will stop inmediately the first match...
    #...its done.
    
import re
print(re.search('[\d\w\s]', '---5---'))  
print("\n")   
    
import re
print(re.search('[\d\w\s]', '- -5---'))  
print("\n")  

import re
print(re.search('[\d\w\s]', '--r5---'))  
print("\n")  

import re
print(re.search('\d\w\s', '--r5---'))  
print("\n")  

    #Number N°13  
    #If we want to include a metacharacter in our regex, withour carrying its...
    #...special meaning (i.e. represent itself as a literal character) we...
    #...use the backslash "\", which in simply words removes the special...
    #...meaning of a metacharacter (In other words, a metacharacter...
    #...preceded by a backslash; therefore, we need to put the backslash...
    #...before the special metacharacter).
    
    #It is important to say that there are few exceptions to application of...
    #...backslash "\". Those metacharacter classes (exceptions) are the...
    #...followings:
        #word       --> [\w] and [\W]
        #digit      --> [\d] and [\D]
        #whitespace --> [\s] and [\S]
    
    #It is important to say that there are few exceptions to application of...
    #...backslash "\". Those metacharacter sequences (exceptions) are the...
    #...followings:
        #Anchors

#Topic 7: Example 7.19.
#In this case we are going to see how the metacharacter "^" "a-z"...
#...preceded by a backslash; therefore, stop to work "^" and we get as...
#...an answer the match resulted only from the code "a-z".
import re
print(re.search('[\^a-z]', 'foo123bar'))  
print("\n") 

import re
print(re.search('[a-z]', 'foo123bar'))  
print("\n") 

#Topic 7: Example 7.20
    #In this case we are going to see how the metacharacter "a-z" works...
    #...normally therefore, we get as an answer the number "1" as the that...
    #...first character that it is not a letter.
import re
print(re.search('[^a-z]', 'foo123bar'))  
print("\n")   

#Topic 7: Example 7.21 
#In this case we are going to see how the metacharacter "." works normally.

  #The dot regex "." matches all characters except the newline character "\n".
  #Combined with the asterisk quantifier in the pattern '.*', the dot regex...
  #...matches an arbitrary number of symbols except newline characters.
  
  #Every "dot" search for a single charachter (i.e. 3 "dots"search for 3...
  #...characters of the text).
import re
print(re.search('.', 'foo.bar'))
print("\n")   

import re
print(re.search('b.r', 'foo.bar'))
print("\n")  

import re
print(re.search('b.', 'foo.bar'))
print("\n")  

import re
print(re.search('.a', 'fao.bar'))
print("\n")  

#Topic 7: Example 7.22
#In this case we are going to see how the metacharacter "." preceded by...
#...a backslash stop to work, therefore, we get as an answer the location...
#...of the simple dot in the string (not acting like metacharacter).

   #We can use "square brackets []" or "quotation marks"
import re
print(re.search('\.', 'foo.bar'))
print("\n")  

import re
print(re.search('[\.]', 'foo.bar'))
print("\n")    

#Topic 7: Example 7.23 - Option 1 
#In this case we are going to see how the metacharacter "\" preceded by...
#...a backslash stop to work, therefore, we get as an answer the location...
#...of the simple backslash in the string (not acting like metacharacter).
    #The backslash is itself a special character in a regex, so to specify...
    #...a literal backslash, you need to escape it with another four...
    #...backslashess.
    
    #The "Python Interpreter" sees '\\\\' as a pair of escaped backslashes....
    #...It reduces each pair to a single backslash and passes '\\' to...
    #..the regex parser.
    #The "regex parser" then sees "\\" as one escaped backslash. As a...
    #..."regex" that matches a single backslash character. 
    
    #We need to use the "Raw string" (i.e. the lowercase letter "r" before...
    #...the first quotation mark of the analyzed string), because if we...
    #...omit that we are going to get as an answer "None". In this case...
    #...we only use the "Raw string" in the analyzed string and not with...
    #....the metacharacter.
import re
print(re.search('\\\\', r'foo\bar'))
print("\n")   

import re
print(re.search('[\\\\]', r'foo\bar'))
print("\n") 

import re
print(re.search('\\\\', "foo\bar"))
print("\n")   

import re
print(re.search('[\\\\]', "foo\bar"))
print("\n") 

#Topic 7: Example 7.23 - Option 2 
#In this case we are going to see how the metacharacter "\" preceded by...
#...a backslash stop to work, therefore, we get as an answer the location...
#...of the simple backslash in the string (not acting like metacharacter).
    #The backslash is itself a special character in a regex, so to specify...
    #...a literal backslash, you need to escape it with another four...
    #...backslashess.
    
    #The second, and probably cleaner, way to handle this situation is...
    #...to specify the "regex" using a "raw string".
        #Raw string: This suppresses the escaping at the "Python...
        #...Interpreter level (i.e. we are going directly to the "regex...
        #...parser"). The string '\\' gets passed unchanged to...
        #...the "regex parser", which again sees one escaped backslash...
        #...as desired. 
        
        #It’s good practice to use a "raw string" to specify a regex in...
        #...Python whenever it contains backslashes.
        
        #Raw string: To use the raw string in this case, the string is...
        #...prefixed with an "r" and also the methacharacter is prefixed ...
        #...with an "r", because if we omit that we are going to get as an...
        #...answer "None".
import re
print(re.search(r'\\', r'foo\bar'))
print("\n")   

import re
print(re.search(r'[\\]', r'foo\bar'))
print("\n") 

import re
print(re.search(r'\\', 'foo\bar'))
print("\n")   

import re
print(re.search(r'[\\]', 'foo\bar'))
print("\n") 

    #In the following printed strings we will see the effect of the "raw...
    #...string" "r" in the metacharacter "\", maintaining the entire text...
    #...(including metacharacter "\") in the string intact when we use...
    #...the "raw string" "r".
        #The raw string means that the newline character is not...
        #...interpreted by "print()" and is left intact.
    
    #Without the use of "raw string" "r" in strings that have the...
    #...metacharacter "\" the printed result will show the text incomplete.
print(r'foo\bar')

print('foo\bar')

print(r'foobar')

print('foobar')

    #Number N°14 - Part 1  
    #Anchors: It is a special metacharacter sequences that can be...
    #...represented in two ways:
        #"\A" (with a backslash).
        #"^"
    #Anchors are zero-width matches. They don’t match any actual...
    #...characters in the search string. Instead, an "anchor" dictates a...
    #...particular location in the search string where a match must...
    #...occur.
    #When the regex parser encounters "^" or "\A", the parser’s current...
    #..position must be at the beginning of the search string for it to...
    #...find a match (i.e. to find the the character that we are interested).
    
    #It is importantto say that if the character that we are interested...
    #...is not located at the beginning of the search string we are going...
    #...to get as an answer the word "None" when we apply the "anchor". 
    
    #"^" and "\A" behave slightly differently from each other in..."
    #..."multiline mode". 
    
#Topic 7: Example 7.24
#In those cases we are checking the answers when we apply with a number,...
#...letter and other characters (like newline or underscore):
    #"\A" (with a backslash).
    #"^"
import re
print(re.search('^foo', 'foobar'))
print("\n") 

import re
print(re.search('^9', '9barfoo'))
print("\n") 

import re
print(re.search('^\n', '\nbarfoo'))
print("\n") 

import re
print(re.search('^_', '_barfoo'))
print("\n") 

import re
print(re.search('^foo', 'barfoo'))
print("\n") 

import re
print(re.search('\Afoo', 'foobar'))
print("\n") 

    #Number N°14 - Part 2 
    #Anchors: It is a special metacharacter sequences that can be...
    #...represented in two ways:
        #"\Z" (with a backslash).
        #"$"
    #Anchors are zero-width matches. They don’t match any actual...
    #...characters in the search string. Instead, an "anchor" dictates a...
    #...particular location in the search string where a match must...
    #...occur.
    #When the regex parser encounters "$" or "\Z", the parser’s current...
    #..position must be at the end of the search string for it to...
    #...find a match (i.e. to find the the character that we are interested).
    #Whatever precedes "$" or "\Z" must constitute the end of the search..
    #..string.
    
    #It is importantto say that if the character that we are interested...
    #...is not located at the end of the search string we are going...
    #...to get as an answer the word "None" when we apply the "anchor".
    
    #As a special case, "$" (but not "\Z") also matches the text just...
    #...before a the newline.
    
    #"$" and "\Z" behave slightly differently from each other in..."
    #..."multiline mode". 

#Topic 7: Example 7.25
#In those cases we are checking the answers when we apply with a number,...
#...letter and other characters (like newline or underscore):
    #"\Z" (with a backslash).
    #"$"
import re
print(re.search('bar$', 'foobar'))
print("\n") 

import re
print(re.search('9$', 'barfoo9'))
print("\n") 

import re
print(re.search('\n$', 'barfoo\n'))
print("\n") 

import re
print(re.search('_$', 'barfoo_'))
print("\n") 

import re
print(re.search('bar$', 'barfoo'))
print("\n") 

import re
print(re.search('bar\Z', 'foobar'))
print("\n") 

#Topic 7: Example 7.26
#In this cases we are checking how the special case, "$"...
#...(but not "\Z") also matches just before a single newline at the...
#...end of the search string (as long as after the newline there is no...
#...any character).
import re
print(re.search('bar$', 'foobar\n'))
print("\n") 

import re
print(re.search('bar$', 'foobar\n88888'))
print("\n") 

import re
print(re.search('bar\Z', 'foobar\n'))
print("\n") 

    #Number N°14 - Part 3
    #Anchors: It is a special metacharacter sequences that can be...
    #...represented in the following way:
        #"\b" (with a backslash).
        
    #Anchors are zero-width matches. They don’t match any actual...
    #...characters in the search string. Instead, an "anchor" dictates a...
    #...particular location in the search string where a match must...
    #...occur.
    
    #When the regex parser encounters "\b", it match to a word boundary...
    #...("a word boundary" means that it needs to be a blank space o a...
    #...special symbol or characters before or after {depends of the...
    #...case} the sequence of alphanumeric characters that we try to find).
    
    #"\b" points out that the regex parser’s current position must be at..
    #...the beginning or end of a "word". A "word" consists of a...
    #...sequence of alphanumeric characters or underscores.
    
    #It is important to remember the use of the "raw string".
        #Because '\b' is an escape sequence for both string literals...
        #...and regexes in Python, each use above would need to be...
        #...double escaped as '\\b' if we didn’t use raw strings.
    
    #It is important say that if the character that we are interested...
    #...is not located we are going to get as an answer the word...
    #..."None" when we apply the "anchor".

#Topic 7: Example 7.27
#In this cases we are checking if there is the string "bar" located...
#...after a blank space o a special symbol or character. It is important...
#...to see that we use the "r" of the "raw string" only with the anchor. 
import re
print(re.search(r'\bbar', 'foo bar'))
print("\n") 

#Topic 7: Example 7.28
#In this cases we are checking if there is the string "bar" located...
#...after a blank space o a special symbol or character. It is important...
#...to see that we use the "r" of the "raw string" with the anchor and with...
#...string.

    #We get the same answer if we put or not the "r" of the "raw string"...
    #...with the string". But we need to put always the "r" of the "raw...
    #...string" with the anchor.  
    
    #The newlinw "\n" and the underscore "_" does not count like...
    #...special symbol or metacharacters; therefore we get as an answer...
    #...the word "None" (#There is not a word boundary in the string;...
    #...therefore, the answer is "None".)
import re
print(re.search(r'\bbar', r'foo bar'))
print("\n") 

import re
print(re.search(r'\bbar', r'foo.bar'))
print("\n") 

import re
print(re.search(r'\bbar', r'foo-bar'))
print("\n") 

import re
print(re.search(r'\bbar', r'foo+bar'))
print("\n") 

import re
print(re.search(r'\bbar', r'foo#bar'))
print("\n") 

import re
print(re.search(r'\bbar', r'foo*bar'))
print("\n") 

import re
print(re.search(r'\bbar', r'foo\nbar'))
print("\n") 

import re
print(re.search(r'\bbar', r'foo_bar'))
print("\n") 

#In this cases we are checking if there is the string "foo" located...
#...before a blank space o a special symbol or character. It is important...
#...to see that we use the "r" of the "raw string" with the anchor and with...
#...string.
import re
print(re.search(r'foo\b', r'foo bar'))
print("\n") 

import re
print(re.search(r'foo\b', r'foo.bar'))
print("\n") 

#Topic 7: Example 7.29
#In this cases we are checking if there is the string "bar" located...
#...after a blank space o a special symbol or character. 

    #We get the same answer if we put or not the "r" of the "raw string"...
    #...with the string". But we need to put always the "r" of the "raw...
    #...string" with the anchor.   
import re
print(re.search('\bbar', r'foo bar'))
print("\n") 

import re
print(re.search(r'\bbar', 'foo bar'))
print("\n") 

#Topic 7: Example 7.30.1
#In this cases we are checking if there is the string "bar" located...
#...after a blank space o a special symbol or character. It is important...
#...to see that we use the double slash (also called "double escaped")...
#...as '\\b' instead of raw strings.

    #It is important to say that we do not need to worry about the..
    #...to put "r" of the "raw string".
import re
print(re.search('\\bbar', 'foo bar'))
print("\n") 

#Topic 7: Example 7.30.2
#In this cases we are checking if there is the string "bar" located...
#...after a blank space o a special symbol or character. It is important...
#...to see that we use the double slash (also called "double escaped")...
#...as '\\b' instead of raw strings.

    #It is important to say that we do not need to worry about the..
    #...to put "r" of the "raw string".
import re
print(re.search('\\bfoo', 'foo bar'))
print("\n") 

#Topic 7: Example 7.31
#In this cases we are checking if there is the string "bar" and "foo" located...
#...after a blank space o a special symbol or character. It is important...
#...to see that we use the "r" of the "raw string" with the anchor and with...
#...string.

#There is not a word boundary in the string; therefore, the answer is "None".
import re
print(re.search(r'\bbar', r'foobar'))
print("\n") 

import re
print(re.search(r'foo\b', 'foobar'))
print("\n") 

    #Number N°14 - Part 4
    #Anchors: It is a special metacharacter sequences that can be...
    #...represented in the following way:
        #"\B" (with a backslash).
        
    #Anchors are zero-width matches. They don’t match any actual...
    #...characters in the search string. Instead, an "anchor" dictates a...
    #...particular location in the search string where a match must...
    #...occur.
    
    #When the regex parser encounters "\B", it is not match to a word boundary...
    #...("a word boundary" means that it needs to be a blank space o a...
    #...special symbol or characters before or after {depends of the...
    #...case} the sequence of alphanumeric characters that we try to find).
    
    #"\B" do the opposite of "\b"
    
    #"\B" points out that the regex parser’s current position no need to be...
    #...be at the beginning or end of a "word". A "word" consists of a...
    #...sequence of alphanumeric characters or underscores.
    
    #It is important to remember the use of the "raw string".
        #Because '\b' is an escape sequence for both string literals...
        #...and regexes in Python, each use above would need to be...
        #...double escaped as '\\b' if we didn’t use raw strings.
    
    #It is important say that if the character that we are interested...
    #...is not located we are going to get as an answer the word...
    #..."None" when we apply the "anchor".

#Topic 7: Example 7.32
#In this cases we are checking if there is the string "bar" and "foo" located...
#...in the string. 

    #It is not important to see that we use the "r" of the...
    #..."raw string" with the anchor and with string.
import re
print(re.search(r'\Bbar', r'foobar'))
print("\n") 

import re
print(re.search(r'foo\B', 'foobar'))
print("\n") 

#Topic 7: Example 7.33
#In this cases we are checking if there is the string "bar" and "foo" located...
#...in the string. It is not important to see that we use the "r" of the...
#..."raw string" with the anchor and with string.
       
    #The newline "\n" and the underscore "_" does not count like...
    #...special symbol or metacharacters; however ".", "-", "+", "#"...
    #..."*" are special symbol or metacharacters; therefore, we get as...
    #...an answer the word "None".
import re
print(re.search(r'\Bbar', r'foo.bar'))
print("\n") 

import re
print(re.search(r'foo\B', 'foo-bar'))
print("\n") 

import re
print(re.search(r'\Bbar', r'foo+bar'))
print("\n") 

import re
print(re.search(r'\Bbar', r'foo#bar'))
print("\n") 

import re
print(re.search(r'\Bbar', r'foo*bar'))
print("\n") 

import re
print(re.search(r'\Bbar', r'foo\nbar'))
print("\n") 

import re
print(re.search(r'\Bbar', r'foo_bar'))
print("\n") 

import re
print(re.search(r'\Bbar', r'foo bar'))
print("\n") 

    #Number N°15   
    #Quantifiers: means how much / how often. We tell the...
    #....regex engine how often you want to match a given pattern.
    #We implicitly don’t define any quantifier; therefore, no...
    #..."quantifier" means to match the regular expression exactly once.
    #It is a special metacharacter sequences that can be...
    #...represented in the following way:
        
        #It is important to say that the character that we want to..
        #...find need to be the first character in the entire...
        #...string. 
            #"A?" = Match regular expression "A" zero or one times.
            #"A*" = Match regular expression "A" zero or more times.
        #It is important to say that the character that we want to..
        #...find do not need to be the first character in the entire...
        #...string. 
            #"A+" = Match regular expression "A" one or more times.
            #"A{m}" = Match regular expression "A" exactly "m times.
            #"A{m,n}" = Match regular expression "A" between "m" and "n"...
            #...times (included)
     
     #It is important to say that the character that we want to find....
     #...need to be the first character in the entire string. If there...
     #...is not in that way we are going to get as an answer the...
     #...match "" in the span(0,0).
     
#Topic 7: Example 7.34.1 <--ONGOING
#In this case we are checking if "a" appears zero or one times. To be...
#....specific "a" appears at least one time and is located automatically...
#...the first time it appears using:
    #"A?" = Match regular expression "A" zero or one times.
import re
print(re.search('a?', 'aaaa'))
print("\n") 

import re
print(re.search('a?', 'a/345aaa'))
print("\n")  

#It is important to say that the character could be also a number.
import re
print(re.search('54?', '54aa'))
print("\n") 

#It is important to say that the character that we want to find need to...
#...be the first character in the entire string. If there is not in that...
#...way we are going to get as an answer the match "" in the span(0,0).
import re
print(re.search('a?', 'ppaaaa'))
print("\n") 

import re
print(re.search('a?', '54\n aaaa'))
print("\n")

#Topic 7: Example 7.34.2
#In this case we are checking if "a" appears zero or one times. To be...
#....specific "a" does not appear in the string; therefore we get as an...
#...answer the match "" in the span(0,0).
#...using:
    #"A?" = Match regular expression "A" zero or one times.
import re
print(re.search('a?', 'b123'))
print("\n")   

#Topic 7: Example 7.35.1
#In this case we are checking if "a" appears zero or more times. To be...
#....specific "a" appears four times and is located automatically...
#...the first time it appears using:
    #"A*" = Match regular expression "A" zero or more times.
import re
print(re.search('a*', 'aaaa'))
print("\n")  

import re
print(re.search('a*', 'aaaabn6ea'))
print("\n")  

import re
print(re.search('a*', 'aaaa a'))
print("\n")

#It is important to say that the character could be also a number.
import re
print(re.search('5*', '5aaaaa55a'))
print("\n") 

#In this case we use the metacharacter "Number N°2: hyphen -", useful...
#...to contain a range of characters. Therefore, we get as an answer all...
#...the characters between "abej" and "bar" including  "abej" and "bar".

    #Also, it is importante to take in count that "*" match if...
    #...the character appears zero or more times of "-".
    
    #Also, it is importante to take in count that in this case we are...
    #...going to see how the metacharacter "-" is not preceded by a...
    #...backslash (therefore, it does nor stop to work and still act...
    #...like a metacharacter).
import re
print(re.search('abej-*bar', '777abejbar') ) 
print("\n")  

import re
print(re.search('abej-*zar', 'abej-zar') ) 
print("\n")  

import re
print(re.search('abej-*bar', 'abej----bar') ) 
print("\n") 

#In this case we use the metacharacter "Number N°0: dot .", useful...
#...to get all the characters between other two specific characters....
#...Therefore, we get as an answer all the characters between "abej"...
#...and "bar" including  "abej" and "bar".

    #Also, it is importante to take in count that "*" match if...
    #...the character appears zero or more times of ".".
    
    #Also, it is importante to take in count that in this case we are...
    #...going to see how the metacharacter "." is not preceded by a...
    #...backslash (therefore, it does nor stop to work and still act...
    #...like a metacharacter).
import re
print(re.search('abej.*zar', 'abej83-zar') ) 
print("\n")  
 
#In this case we use the metacharacter "Number N°0: dot .", useful...
#...to get all the characters between other two specific characters....
#...Therefore, we get as an answer all the characters between "abej"...
#...and "bar" including  "abej" and "bar".
    #Remember that the dot "." wildcard metacharacter doesn’t match..
    #...a newline "\n"; therefore, we get as an answer the word  "None"
import re
print(re.search('abej.*zar', 'abej8\n3-zar') ) 
print("\n")  
 
import re
print(re.search('.*', 'abej8\n3-zar') ) 
print("\n")  

#Topic 7: Example 7.35.2 
#In this case we are checking if "a" appears zero or more times. To be...
#....specific "a" appears one time and is located automatically...
#...the first time it appears using:
    #"A*" = Match regular expression "A" zero or more times.
import re
print(re.search('a*', 'a aaaa '))
print("\n")  

#It is important to say that the character that we want to find need to...
#...be the first character in the entire string. If there is not in that...
#...way we are going to get as an answer the match "" in the span(0,0).
   #Be careful about this because it is not 100% truth.
import re
print(re.search('a*', '545aaaa'))
print("\n")  

#Topic 7: Example 7.36.1 <--ONGOING
#In this case we are checking if "a" appears one or more times. To be...
#....specific "a" appears four times and is located automatically...
#...the first time it appears using:
    #"A+" = Match regular expression "A" one or more times.
import re
print(re.search('a+', 'aaaa'))
print("\n")  

import re
print(re.search('a+', 'aaaabn6ea'))
print("\n")  

import re
print(re.search('a+', 'aaaa a'))
print("\n") 

#In this case we use the metacharacter "Number N°2: hyphen -", useful...
#...to contain a range of characters. Therefore, we get as an answer all...
#...the characters between "abej" and "bar" including  "abej" and "bar".
    
    #Also, it is importante to take in count that "+" match if...
    #...the character appears one or more times of "-".
    
    #Also, it is importante to take in count that in this case we are...
    #...going to see how the metacharacter "-" is not preceded by a...
    #...backslash (therefore, it does nor stop to work and still act...
    #...like a metacharacter).
    
    #If there is no match, we get as an answer he word "None".
import re
print(re.search('abej-+bar', '777abejbar') ) 
print("\n")  

import re
print(re.search('abej-+zar', 'abej-zar') ) 
print("\n")  

import re
print(re.search('abej-+bar', 'abej----bar') ) 
print("\n") 

#It is important to say that the character could be also a number.
import re
print(re.search('5+', 'a55abn6ea5555'))
print("\n")  

#Topic 7: Example 7.36.2
#In this case we are checking if "a" appears one or more times. To be...
#....specific "a" appears one time and is located automatically...
#...the first time it appears using:
    #"A+" = Match regular expression "A" one or more times.
import re
print(re.search('a+', 'a aaa a'))
print("\n") 

#It is important to say that the character that we want to find do not...
#..need to be the first character in the entire string. 
import re
print(re.search('a+', '545aaaa'))
print("\n") 

import re
print(re.search('a+', '545\naaaa'))
print("\n")  
 
import re
print(re.search('a+', '545aa\naaaa'))
print("\n")  
 
#Topic 7: Example 7.37.1
#In this case we are checking if "a" appears "m" times. To be...
#....specific "a" appears one or more times and is located automatically...
#...the first time it appears {as long as the quantity of character of...
#...interest be the same of the "m". If that conditions is not met...
#...we are going to get as answer the word "None".} using:
    #"A{m}" = Match regular expression "A" exactly "m" times.
import re
print(re.search('a{3}', 'aaaaaaa'))
print("\n")  

import re
print(re.search('a{3}', 'aa'))
print("\n")  

import re
print(re.search('a{6}', 'aaaabn6eaa'))
print("\n")  

import re
print(re.search('a{6}', 'aaaa aa'))
print("\n")

#It is important to say that the character could be also a number.
import re
print(re.search('5{4}', 'a55abn6ea5555'))
print("\n")  

#Topic 7: Example 7.37.2
#In this case we are checking if "a" appears "m" times. To be...
#....specific "a" appears one or more times and is located automatically...
#...the first time it appears {as long as the quantity of character of...
#...interest be the same of the "m". If that conditions is not met...
#...we are going to get as answer the word "None".} using:
    #"A{m}" = Match regular expression "A" exactly "m" times.
    
#It is important to say that the character that we want to find do not...
#..need to be the first character in the entire string. 
import re
print(re.search('a{3}', '545aaaa'))
print("\n") 

import re
print(re.search("a{3}", '545\naaaa'))
print("\n")  
 
import re
print(re.search('a{3}', '545aa\naaaa'))
print("\n")  

#Topic 7: Example 7.38.1 
#In this case we are checking if "a" appears in the range of "m" and "n"...
#...times. To be specific "a" appears one or more times and is located...
#...automatically the first time it appears {as long as the times...
#...range of character of interest (not the index position) be the...
#...same of the range "m,n". If that conditions is not met we are going...
#...to get as answer the word "None".} using:
    #"A{m,n}" = Match regular expression "A" between "m" and "n"...
    #...times (included)
import re
print(re.search('a{1,2}', 'aaaa'))
print("\n")  

import re
print(re.search('a{1,2}', 'aa'))
print("\n")  

import re
print(re.search('a{7,8}', 'aaaabn6eaa'))
print("\n")  

import re
print(re.search('a{1,2}', 'aaaa aa'))
print("\n")

#It is important to say that the character could be also a number.
import re
print(re.search('5{1,2}', 'a55abn6ea5555'))
print("\n")  

#Topic 7: Example 7.38.2
#In this case we are checking if "a" appears in the range of "m" and "n"...
#...times. To be specific "a" appears one or more times and is located...
#...automatically the first time it appears {as long as the times...
#...range of character of interest (not the index position) be the...
#...same of the range "m,n". If that conditions is not met we are going...
#...to get as answer the word "None".} using:
    #"A{m,n}" = Match regular expression "A" between "m" and "n"...
    #...times (included)
    
#It is important to say that the character that we want to find do not...
#..need to be the first character in the entire string. 
import re
print(re.search('a{1,2}', '545aaaa'))
print("\n") 

import re
print(re.search("a{1,2}", '545\naaaa'))
print("\n")  
 
import re
print(re.search('a{1,2}', '545aa\naaaa'))
print("\n")  

#Number N°16 

##############################################################################

##############################################################################

##############################################################################

#Regular Expressions allow us to do pattern matching in strings using regular...
#...expressions. 
 
#Regular Expressions are written in a condensed formatting language. 

#Regular expression is a pattern which you give to a "regex processor"...
#...(apparently the "Regular Expression") with "some source data" (the...
#...text, paragraph, email, book or any type of content). The "regex...
#...processor" then parses that "source data" using that pattern, and...
#...returns chunks of text back to the a data scientist.

#The 3 main reasons to apply Regular Expressions is:
    #To check whether a pattern exists within some source data
    #To get all instances of a complex pattern from some source data
    #To clean your source data using a pattern generally through string...
    #...splitting.

#Importing the "re" module, which is where python stores "regular expression"...
#...libraries.

import re

    #"match()" checks for a match that is at the beginning of the string and...
    #...returns a boolean. This match need to exactly (even wiht the capital...
    #...letters and lowercases.)
text = "This is a good day."
if re.match("This", text): 
    print("Wonderful!")
    print("\n") 
else:
    print("BAD")
    print("\n") 

    #Similarly, search(), checks for a match anywhere in the string, and...
    #...returns a boolean.This match need to exactly (even wiht the capital...
    #...letters and lowercases.)
import re
text = "This is a good day."
if re.search("Is", text): 
    print("Wonderful!")
    print("\n") 
else:
    print("BAD")
    print("\n") 

    #We can segment a string. The work that regex does here is called...
    #..."tokenizing", where the string is separated into substrings based on...
    #...patterns. Tokenizing is a core activity in natural language processing.

    # The "split()" functions will parse the string for us and return chunks. We...
    #...will se that the printed result (by the way, as a "list[]" with the...
    #...first member empty) is the text that is located after the selected...
    #...word to apply "spilt()".This match need to exactly (does matter...
    #...the capital letters and lowercases.
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."
print(re.split("Amy", text))
print("\n") 

    #If we wanted to count how many times we have talked about a word, we could..
    #...use the function "findall()".This match need to exactly (does matter..
    #...the capital letters and lowercases.)
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."
print(re.findall("Amy", text))
print("\n")

grades="ACAAAABCBCBA777A,50924839B"
grades1= re.findall("B",grades)
print(grades1) 
print("\n")  

#Regular Expressions - Patterns and Character Classes - 7.1:

    #Option 1:
    # If we want to count the number of certain characters's strings in a list...
    # (i.e. count more than one character) we put the specific...
    #...characters inside square brackets (wich means [characters and characters and ...]),...
    #...and we will get as an answer all the characters printed the order...
    #...they are presented in the original string, in a list. 
    
    #In this option, does not matter the position of the characters in the...
    #original string, when we apply the function "findall()"
    
    #This is code is used to detect all letters "A" and "B" (no matter capital...
    #...letters and lowercases.), in addition to detect the number "7". 
    
    #It is important...
    #...to say that also does not matter if we put inside the square brackets...
    #...(also called "set operator") a letter or number that do not appear in...
    #...the original string, because that letter or number will not be detected.
    
    #When we are using square brackets (also called "set operator"), we are...
    #...doing "character-based matching". So we are matching individual...
    #...characters not words, not senteces, not phrases.
import re
grades="ACAAAABCBCBA777A,50924839B"
grades1= re.findall("[AB7]",grades)
print(grades1) 
print("\n") 

grades="ACAAAAbCbCbA777A"
grades1= re.findall("[An7b]",grades)
print(grades1) 
print("\n")   

grades="ACAAAarrozbCbCbA777A"
grades1= re.findall("[arroz]",grades)
print(grades1) 
print("\n")   

    #Option 2 (This is called the "Set Operator []") plus ( - means "RANGE" ):
    # If we want to count the number of certain characters's strings in a list...
    # (i.e. count more than one character) we put the specific...
    #...characters inside square brackets (wich means [characters and characters and ...]),...
    #...and we will get as an answer all the characters printed the order...
    #...they are presented in the original string, in a list. 
    
    #In this option, does matter the position of the characters in the...
    #original string, when we apply the function "findall()".
    
    #Range
        #In this option, the characters that will complement the main characters,...
        #...need to ordered alphanumerically and not mixed, (it means...
        #...A-B or 1-3).
    
        #In this option, the second square brackets means [string - string]),...
        #..(in other word is "Range") refer to the complement strings ordered...
        #...alphanumerically.
    
    #This match need to exactly (even wiht the capital letters and lowercases.)
    
    #This is code is used to detect all letters "A" (does matter capital...
    #...letters and lowercases.) that are in group (in this case at the left...
    #...) with another string, in this case range of numbers from "1" to "7". 
grades2="ACAAAABCBCBA777A1,UDFHYSIDUFA1C,HDOHASDOFSDIUA2C"
grades3= re.findall("[A][1-7]",grades2)
print(grades3) 
print("\n")  

grades2="ACAAAABCBCBA777A1,UDFHYSIDUFA1C,HDOHASDOFSDIUA2C"
grades3= re.findall("[a][1-7]",grades2)
print(grades3) 
print("\n") 

    #This is code is used to detect all letters "A" (does matter capital...
    #...letters and lowercases.) that are in group (in this case at the left...
    #...) with another characters, in this case range of numbers from "B" to "H"... 
    #...(does matter capital letters and lowercases.)
grades4="ACAAZABAHDEFGHAE777A1"
grades5= re.findall("[A][B-H]",grades4)
print(grades5) 
print("\n") 

grades4="ACAAZABAHDEFGHAE777A1"
grades5= re.findall("[A][b-H]",grades4)
print(grades5) 
print("\n") 
    #Option 3 (This is called the "Set Operator []") plus (| means "OR" ):
    # If we want to count the number of certain characters's strings in a list...
    # (i.e. count more than one character) we put the specific...
    #...characters inside square brackets (wich means [characters and characters and ...]),...
    #...and we will get as an answer all the characters printed the order...
    #...they are presented in the original string, in a list. 
    
    #In this option, does matter the position of the characters in the...
    #original string, when we apply the function "findall()".
    
    #In this option, the characters that will complement the main string,...
    #...not need to ordered alphanumerically and dos not matter if it is mixed.
    
    #In this option, the vertical line "characters|characters" means "characters OR...
    #...characters" (also called the "pipe character").
                                                         
    #This match need to exactly (does matter capital letters and lowercases.)
grades6="ACAAAABCBCBA777A1,UDFHYSIDUFA1C,HDOHASDOFSDIUA2C"
grades7= re.findall("A2|A1",grades6)
print(grades7) 
print("\n")  

grades6="ACAAAABCBCBA777A1,UDFHYSIDUFA1C,HDOHASDOFSDIUA2C"
grades7= re.findall("a2|A1",grades6)
print(grades7) 
print("\n")  

    # We can use the caret symbol "^" inside the square bracket [] to negate...
    #...our results. For instance, if we want to parse out only the grades...
    #...which were not A's
grades8="CAAAABCBCBA"
grades9 = re.findall("[^A]",grades8)
print(grades9) 
print("\n") 

    # We can use the caret symbol "^" matched to the beginning of a characters as..
    #...an anchor point. For instance, if we want to parse out only the grades...
    #...which were not A's in a string that begin with different characters from...
    #... vowel A, in this case the consonant C, we use the caret symbol "^"...
    #..inside and outside of the square bracket.
    
        #Anchors: specify the start and/or the end of the string that you are...
        #...trying to match. 
            #"The caret character" ^ means start.
            #"The dollar sign" character $ means end. 
grades8="CAAAABCBCBA"
grades10 = re.findall("^[^A]",grades8)
print(grades10) 
print("\n") 

grades8="AAAABCBCB"
grades10 = re.findall("^[^A]",grades8)
print(grades10) 
print("\n") 

grades8="AAAABCBCBA"
grades10 = re.findall("$[^A]",grades8)
print(grades10) 
print("\n") 

#Regular Expressions - Quantifiers - 7.2:

#Quantifiers are the number of times you want a pattern to be matched in order..
#...to match. The most basic quantifier is expressed as "e{m,n}", where:
    
    #"e" is the expression or character we are matching.
    #"m" is the minimum number of times you want to see it repeated join together...
    #...(i.e. the minimm number of times the "e" needes to show repeated join...
    #...together to be accounted)
    #"n" is the maximum number of times the item could be repeated join together...
    #...(i.e. the maximum number of times the "e" needes to show repeated to...
    #...be accounted)

    #For example: In this case we are accounting only the A's that are in groups...
    #...from two (AA) to three (AAA). No matter the quantity of groups and also..
    #....no matter of the quantity of elements in a group is greater than "n"...
    #...because the code automatically separate this huge groups in small groups....
    #...that can be in a size range from "m" to "n".
grades11="CAAAABCBCBAA,UOIUFIOAAAIUOIUOIAAOIUIOUAAAAAAAOI56OI"
grades12 = re.findall("A{2,3}",grades11) 
print("grades12",grades12) 
print("\n")

grades11="CAAAABCBCBAA,UOIUFIOAAAIUOIUOIAAOIUIOUAAAAAAAOI56OI"
grades12 = re.findall("A{2,9}",grades11) 
print("grades12",grades12) 
print("\n")

grades11="CAAAABCBCBAA\nAAAAAAAA"
grades12 = re.findall("A{2,9}",grades11) 
print("grades12",grades12) 
print("\n")

    #For example:We are looking for two A's back to back (similar when we apply...
    #..."Regular Expressions - Patterns and Character Classes"), so it sees one...
    #...A followed immediately by one more A.

    # It's important to note that the regex quantifier syntax does not allow you...
    #...to deviate from the {m,n} pattern. In particular, if you have an extra...
    #...space in between the interested characters (i.e "A A" instead of "AA")...
    #...this will not be account.
grades13="CBAAAABBCBCBAA,UOIUFIOBAAABBBBBBBBBCIUOIUO IA BAOIUIOUAABCCCCAAOII"
grades14 = re.findall("A{1,1}A{1,1}",grades13)
print(grades14) 
print("\n")

    #This is other way to do the previous instance.
grades15 = re.findall("A{2,2}",grades13)
print(grades15) 
print("\n")

    #If we don't include a quantifier then the default is {1,1}
grades16 = re.findall("AA",grades13)
print(grades16) 
print("\n")

    # Oh, and if you just have one number in the braces, it's considered to...
    #..be both "m" and "n"
grades17 = re.findall("A{2}",grades13)
print(grades17) 
print("\n")

    #In this case the code will find, account and print all the values of A´s...
    #...that are previous and join immediately to B's, then will find, account...
    #...and print all the values of B´s that are previous and join immediately..
    #...to C's and so on.
grades18 = re.findall("A{1,10}B{1,10}C{1,10}",grades13)
print(grades18) 
print("\n")

#There are 3 other quantifiers that are used as short hand:
    #Asterix " * " : to match 0 or more times
    #Question mark " ? ": to match one or more times
    #plus sign " +  ":to match one or more times. 
    
#Complex Instance:
#We'll read that into a variable called wiki and lets print.
with open("ferpa.txt","r") as file:
    wiki=file.read()
print(wiki)
print("\n")

    #Instance (Option 1 - Complex Way):
        
    # Scanning through this document one of the things we notice is that the...
    #...headers all have the words [edit] behind them, followed by a newline...
    #...character. So if we wanted to get a list of all of the headers we apply:
        
    #We are tryig to find all alphanumeric values that appear just before...
    #...the text [edit] and also the text [edit].
        
    # "\" Escapes special characters or denotes character classes. In..
    #...this case we escapes special characters [].
import re
wiki1 = re.findall("[A-Za-z]{1,100}\[edit\]",wiki)
print(wiki1)
print("\n")

import re
wiki1 = re.findall("[A-Za-z]{1,100}\[edit]",wiki)
print(wiki1)
print("\n")

import re
wiki1 = re.findall("[A-z]{1,100}\[edit]",wiki)
print(wiki1)
print("\n")

    #Instance (Option 2 - Easy Way):    
    
    #" \w " is a metacharacter, and indicates a special pattern of any letter...
    #...or number. 
    
    #" \s " matches any whitespace character.

    #Next, there are three other quantifiers we can use which shorten up the...
    #...curly brace syntax. We can use an asterix " * " to match 0 or more...
    #...times, so let's try that.
    
    #We are tryig to find all alphanumeric values that appear just before...
    #.. the text [edit] and also the text [edit].
    
    # "\" Escapes special characters or denotes character classes. In..
    #...this case we escapes special characters [].
wiki2 = re.findall("[\w]*\[edit\]",wiki)
print(wiki2)
print("\n") 

wiki2 = re.findall("[\w ]*\[edit\]",wiki)
print(wiki2)
print("\n")     

wiki2 = re.findall("[\w\s]*\[edit\]",wiki)
print(wiki2)
print("\n")     

#It is important to say:
    # "\" Escapes special characters or denotes character classes. In..
    #...this case we escapes special characters [].
    
    #We are tryig to find all alphanumeric values that appear just before...
    #... the text [edit] and also the text [edit].

    #In this instance we print the entire text (number or letter) without...
    #...space that is located just before the string "[edit]".
    
    #In this example. It is important to say the effect of the metacharacter...
    #..."[\w]" without space at the end of "w".

wiki23 = "A B C, ODSI%&¨*!!!¡?FN[edit], 490R32409F, FOWERNNLK[edit]MFVNSO[edit]"
wiki3 = re.findall("[\w]*\[edit]",wiki23)
print(wiki3)
print("\n")

#It is important to say:
    # "\" Escapes special characters or denotes character classes. In..
    #...this case we escapes special characters [].
    
    #We are tryig to find all alphanumeric values that appear just before...
    #... the text [edit] and also the text [edit].

    #In this instance we print the entire text (number or letter) with...
    #...space that is located just before the string "[edit]".
    
    #In this example. It is important to say the effect of the metacharacter...
    #..."[\w]" with space at the end of "w".
    
wiki24 = "A B C, OD SI%&¨*!!!¡?FN[edit], 490R32409F, FOWERN NLK[edit]MFV NSO[edit]"
wiki4 = re.findall("[\w ]*\[edit]",wiki24)
print(wiki4)
print("\n")

#In this case we apply the "split code" inside a "for loop" to print what is...
#...located before (using the index [0]) or after the symbol "[" (using the...
#...index [1]).If we do no use the code index position, we are going to get...
#...entire text without the "[".

    #Instance 1: Only printing every element found by the for loop.

for title in re.findall("[\w ]*\[edit\]",wiki):
    print(title)

    #Instance 2: Printing every element found by the for loop, located in the...
    #...index position [1] (after the symbol "[").
    #In essence, now we will take that intermediate result and split on the...
    #...square bracket [ just taking the second result.
for title in re.findall("[\w ]*\[edit\]",wiki):
    print(re.split("[\[]",title)[1])

    #Instance 3: Printing every element found by the for loop, located in the...
    #...index position [0] (before the symbol "[").
    #In essence, now we will take that intermediate result and split on the...
    #...square bracket [ just taking the first result.

for title in re.findall("[\w ]*\[edit\]",wiki):
    print(re.split("[\[]",title)[0])
    
    #Instance 4: Printing every element found by the for loop, eliminating...
    #...only the symbol "[".
for title in re.findall("[\w ]*\[edit\]",wiki):
    print(re.split("[\[]",title))

#Regular Expressions - Groups - 7.3:

#Groups
    
#To this point we have been talking about a regex as a single pattern which...
#...is matched.
#We can match different patterns, called "groups", at the same time. To "group..
#...patterns" together we use parentheses "()".

#When we are using square brackets (also called "set operator"), we are...
#...doing "character-based matching". So we are matching individual...
#...characters not strings, no words, not sentences, not phrases.
          
    #Instance 1: 
        #The first group is just to find all alphanumeric values that appear...
        #...zero or more time with the code --> ([\w ]*)
        #The second group is just to find the text [edit] with the....
        #...code -->(\[edit\])
            # "\" Escapes special characters or denotes character classes. In..
            #...this case we escapes special characters [].
            
        #We get as a result a list of tuples (i.e. groups).
import re
wiki5 = re.findall("([\w ]*)(\[edit\])",wiki)    
print(wiki5)
print("\n") 

    #Instance 2: 
        #The first group is just to find all alphanumeric values that appear...
        #...zero or more time with the code --> ([\w ]*)
        #The second group is just to find the text [edit] with the....
        #...code -->(\[edit\])
            # "\" Escapes special characters or denotes character classes. In..
            #...this case we escapes special characters [].
                
        #We get as a result another way to get a list of tuples (i.e. groups)...
        #...of Match objects
        
        #The sequence or order of printed groups (0, 1, 2, ...) are...
        #...determined by the groups that we try to match trough the...
        #..."for loop" and the code "re.finditer".
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())
print("\n") 


    #Instance 3: 
        #The first group is just to find all alphanumeric values that appear...
        #...zero or more time with the code --> ([\w ]*)
        #The second group is just to find the text [edit] with the....
        #...code -->(\[edit\])
            # "\" Escapes special characters or denotes character classes. In..
            #...this case we escapes special characters [].
            
        #We see previously that the "groups()" method returns a tuple of the...
        #...group. We can get an individual group using "group(number)",...
        #...where "group(0)" is the whole match, and each other number is the...
        #...portion of the match we are interested in. In this case, we want...
        #..."group(1)" and "group(2)".
        
        #The sequence or order of printed groups (0, 1, 2, ...) are...
        #...determined by the groups that we try to match trough the...
        #..."for loop" and the code "re.finditer".
import re

with open("ferpa.txt","r") as file:
    wiki=file.read()
print(wiki)
print("\n")

for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(1))    
print("\n") 
    
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(0))      
print("\n") 
    
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(2))      
print("\n") 
    
#Another good idea is labeling or naming groups. In the previous examples I...
#...use the "position of the group". But giving them a label and looking...
#...at the results as a dictionary (where the name of the dictionary´s key...
#...is the "<name>" and the value of the dictionary is the matched group)..
#...is pretty useful. For that we use the syntax "(?P<name>)", where the...
#...parethesis starts the group, the "?P" indicates that this is an...
#...extension to basic regexes, and "<name>" is the dictionary key we want...
#...to use wrapped in "<>".

    #It is important to say that without the "?P", we only detect the text but...
    #...we cannot print it.

    #Instance 4: 
        # We can get the value of the dictionary printed (i.e. the value...
        #...for every item of the "for loop") using the code "groupdict()"...
        #...and the name of the "key" of the group that we are interested....
        #...to print.
            #In this case we are only interested in the "value" of the group...
            #..."title"
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    print(item.groupdict()['title'])    
    
    #Instance 5: 
        # We can get the value of the dictionary printed (i.e. the value...
        #...for every item of the "for loop") using the code "groupdict()"...
        #...to get the value of all groups.
            #In this case we are interested in the "value" of the group...
            #..."title" and the group "edit_link" (i.e. we are interested...
            #...in all groups)
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    print(item.groupdict())       
    
    #Instance 6: 
        #We can see the effect of "(?)" in grouping:
            #Without the "(?)" we find every text that has space,....
            #...alphanumeric values andd underscore. In this case the...
            #...printed value stop in the comma.
            
            #With the "(?=text)" we find the text (word, numbers, space,...
            #...symbol, etc) located before the "text" establish in the...
            #....group (?=).
            
            #With the "(?:text)" we find the text (word, numbers, space,...
            #...symbol, etc) located before the "text" establish in the...
            #....group (?:) and also the "text" establish in the...
            #....group (?:)
import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("(?P<title>[\w ]*)", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("(?P<title>[\w ]*)(?:buy)", s))
print("\n") 

import re
s = 'This will be amazing; therefore, it is important to buy Bitcoins'
print(re.search("(?P<title>[\w ]*)(?=buy)", s))
print("\n")     
    
    
#Regular Expressions - Look Ahead and Look Behind - 7.4: 

#Look Ahead and Look Behind 
  
#"Look ahead" and "look behind" is a tecnhique for matching. In this case, the...
#...pattern being given to the regex engine is for text either before or...
#...after the text we are trying to isolate.

    #Instance 1: 
        # For example, we want to isolate text which comes...
        #...before the text "[edit]", but we actually don't care about the...
        #..."[edit]" text itself. If we want to use "[edit]" text to match...
        #...but don't want to capture (i.e. printed) we could put "[edit]"...
        #...text in a group and use "look ahead" instead with "?=" syntax.
        
        #What this regex says is match two groups, the first will be named....
        #...and called "title", will have any amount of whitespace or...
        #...regular word characters, the second will be the characters....
        #..."[edit]" but we don't actually want this "[edit]" put and...
        #...printed in our output match objects.
import re

with open("ferpa.txt","r") as file:
    wiki=file.read()
print(wiki)
print("\n")


for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])",wiki):
    print(item)
   
#Regular Expressions - Example: Wikipedia Data - 7.5:

#Example: Wikipedia Data

with open("budhist.txt","r") as file:
    wikibu=file.read()
print(wikibu)
print("\n")

    #Instance 1: 
        #We can use the "verbose mode" of python regexes (taking advantage...
        #...that the text of the file is in a fairly similar pattern. In this...
        #...case the "university name" followed by an "–" then the words...
        #..."located in" followed by the city and state's name). 
        
        #The "verbose mode" allows us to write multi-line regexes and....
        #...increases readability. For this mode, we have to:
            #Explicitly indicate all whitespace characters, either by...
            #...prepending them with a "\" or by using the "\s" special...
            #...value. We can even include comments with "#".
            
        # Now when we call "finditer()" we just pass the "re.VERBOSE" flag...
        #...as the last parameter, this makes it much easier to understand...
        #...large regexes.
        
        # We can get the dictionary returned for the item with "groupdict()".
        
        #We need to be aware of the following:
            #Maybe some symbols or characters will avoid to open...
            #...the file in python. In this case were strange indian symbols.
            
            #Maybe the symbols or some characters will change when we open...
            #...the file in python (i.e. the symbols or some characters will...
            #...look different in the "txt" and in "python").
            
            #We are going to see different ways to apply the "pattern code".
            
            #Why do I use the "." instead of "[\w ]? <--- OK 1.5
                #I get the same result.
                #The dot regex "." matches all characters except the newline...
                #...character "\n". Combined with the asterisk quantifier...
                #...in the pattern '.*', the dot regex matches an arbitrary...
                #...number of symbols except newline characters.
                
            #The presence of symbols like "," , ";" and even the newlines...
            #...can affect the match or search.

            #What is the difference of "\w" (without the space and without..
            #...square brackets) instead of "[\w ]"? <--- OK 1.6
                #First it is important to remember that the square brackets...
                #...without the outside company of other characters like...
                #..."+,*,?" just match a single character. Therefore, if...
                #...we use several square brackets (for instance: "[][][]"...
                #...3 square bracketsto match 3 characters) we are going to...
                #...match several characters.
                
                #A "character class" is represented by one or more characters...
                #...surrounded by square brackets ([]). When Python...
                #...encounters a character class in a regular expression, it...
                #...will be matched by an occurrence of any of the characters...
                #...within the character class. 
                
                #The space " " is important to be considered in the match if we...
                #...are interested in match text that has one or more spaces.
                
                #The code"[\w ]*" try to match any quantity of characters and...
                #...spaces.
  
            #Why do I use the "\" instead of "\s"? <--- OK 1.7
                #It is important to see that there are more than one way...
                #...to search and match fo the blank spaces. Those are:
                    #Using explicitly the blank spaces. In essence "text text text"
        
                #Using the metacharacter "\s". In essence "text\stext\stext".
        
                #Using the metacharacter "\". In essence "text\ text\ text".

            #What is the difference of "\w" (without square brackets) instead...
            #...of "[\w ]"? <--- OK 1.8
                #We are going to get the same match result with and without...
                #...the square bracket when we use "\w " and "[\w ]". However...
                #...we need to consider:
                    #Use "\w*" for a single word or string that is not...
                    #...located after a newline "\n".
                    #Use "[\w]*" for a single word or string that is...
                    #...located after a newline "\n".
        
#Instance OK 1.8
for item in re.finditer("(?P<title>[\w ]*)(â€“\ located\ in\ )(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")  

#Instance OK 1.7
for item in re.finditer("(?P<title>[\w ]*)(â€“\ located\ in\ )(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")  

for item in re.finditer("(?P<title>[\w ]*)(â€“\slocated\sin\s)(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")

for item in re.finditer("(?P<title>[\w ]*)(â€“ located in )(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")    
          
#Instance OK 1.6
for item in re.finditer("(?P<title>\w *)(â€“\ located\ in\ )(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")

for item in re.finditer("(?P<title>[\w ]*)(â€“\ located\ in\ )(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")  

#Instance OK 1.5
for item in re.finditer("(?P<title>[\w ]*)(â€“\ located\ in\ )(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")   

#Instance OK 1.4
pattern="""
(?P<title>.*)           #the university title
(â€“\ located\ in\ )    #city the university is in
(?P<city>\w*)(,\ )      #separator for the state
(?P<state>\w*)          #the state the city is located in
"""       
for itemx in re.finditer(pattern,wikibu,re.VERBOSE):
    print(itemx.groupdict())
print("\n")

#Instance OK 1.3
pattern="""
(?P<title>.*)
(â€“\ located\ in\ )
(?P<city>\w*)(,\ )
(?P<state>\w*)"""       

for itemx in re.finditer(pattern,wikibu,re.VERBOSE):
    print(itemx.groupdict())
print("\n")


#Instance OK 1.2
pattern="(?P<title>.*)(â€“\ located\ in\ )(?P<city>\w*)(,\ )(?P<state>\w*)"       

for itemx in re.finditer(pattern,wikibu,re.VERBOSE):
    print(itemx.groupdict())
print("\n")

#Instance OK 1.1
import re

for item in re.finditer("(?P<title>.*)(â€“\ located\ in\ )(?P<city>\w*)(,\ )(?P<state>\w*)",wikibu):
    print(item.groupdict())
print("\n")

#Regular Expressions - Example: New York Times and Hashtags - 7.6:

#Example: New York Times and Hashtags
    #The file opened is a partial copy of the original file due to the fact....
    #...that the file do not want to open (apparently for the presence of...
    #...strange characters).

with open("Ebola2.txt","r") as file:
    health=file.read()
print(health)
print("\n")

    #Finding the hastags (Option 1):
        #So here we can see there are tweets with fields separated by pipes |...
        #...Lets try and get a list of all of the hashtags that are included...
        #...in this data. A hashtag begins with a pound sign (or hash mark)...
        #...and continues until some whitespace is found.
for item in re.finditer("(#)([\w])*",health):
    print(item.group())    
print("\n") 
   
    #Finding the hastags (Option 2):
        #So here we can see there are tweets with fields separated by pipes |...
        #...Lets try and get a list of all of the hashtags that are included...
        #...in this data. A hashtag begins with a pound sign (or hash mark)...
        #...and continues until some whitespace is found. 
        
        # So lets create a pattern:
            #We want to include the hash sign first.
            #Then include any number of alphanumeric characters.
            #Notice that the ending is a look ahead (using "?=" syntax.)...
            #...We're not actually interested in matching whitespace in...
            #...the return value.
                    # For example, we want to isolate text which comes...
                    #...before the blank space " ", but we actually don't...
                    #...care about the blank space " " itself. If we want...
                    #...to use the blank space " " to match but don't want...
                    #...to capture (i.e. printed) we could put blank space...
                    #..." " in a group and use "look ahead" ("?=" syntax.)
pattern = '#[\w]*(?=\s)'
re.findall(pattern, health)

#Regular Expressions - Quiz - 7.6:

import re
s = 'ramses@gmail.com'
t = '8ramses.m_def9@gmail.com.co'

#Quiz 7.6.1 - Option 1 (Good with only "s")
#--> @ + * \w \. (\w+\.) (\w*\.) 
s = 'ramses@gmail.com'
print(re.search("\w*@\w*\.\w*", s))
print("\n")     

#Quiz 7.6.1 - Option 2 (Good with only "s")
s = 'ramses@gmail.com'       
print(re.search("\w*@(\w*\.)\w*", s))
print("\n")     

#Quiz 7.6.2 - Option 1 (Good with only "t")
#--> @ + * \w \. (\w+\.) (\w*\.) 
t = '8ramses.m_def9@gmail.com.co'
print(re.search("\w*\.+\w*@\w*\.+\w*\.+\w*", t))
print("\n")

#Quiz 7.6.2 - Option 2 (Good with only "t" and "s")
#--> @ + * \w \. (\w+\.) (\w*\.) 
t = '8ramses.m_def9@gmail.com.co'
print(re.search("\w+\.*\w+@\w+\.*\w+\.+\w+", t))
print("\n")

#Quiz 7.6.3 - Option 1 (Good with only "t" and "s")
s = 'ramses@gmail.com'
print(re.search("\w+\.*\w+@\w+\.*\w+\.+\w+", s))
print("\n")    

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#Assignment 1 - January 20, 2021 (RMDLC)

#1.1 Part A
#Find a list of all of the names in the following string using regex.

# <--WINNER (Option without function)
import re
simple_string = """Amy is 5 years old, and her sister Mary is 2 years old.
Ruth and Peter, their parents, have 3 kids."""
Result1 = re.findall("[A-Z][a-z]+", simple_string)
print(Result1)
print(len(Result1))
print("\n")

# <--WINNER (Option with function)
import re
def names(simple_string):
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old.
    Ruth and Peter, their parents, have 3 kids."""
    Result1 = re.findall("[A-Z][a-z]+", simple_string)
    print(Result1)
    print(len(Result1))
    return Result1
    print("\n")
names(simple_string)

#1.2 Part B
#The dataset ﬁle in assets/grades.txt contains a line separated list...
#...of people with their grade in a class. Create a regex to generate...
#...a list of just those students who received a B in the course.

# <--WINNER (Option without function)
import re
with open("assets-grades.txt","r") as file:
    grades=file.read()
print(grades)
print("\n")

pattern="(?P<Name>[\w ]+)(\: \ )(?P<Grade>[B])"       

for itemx in re.finditer(pattern,grades,re.VERBOSE):
    print(itemx.groupdict())
print("\n")

# <--WINNER (Option with function)
import re
with open("assets-grades.txt","r") as file:
    grades1=file.read()
print(grades1)
print("\n")

WhiteList = []
def grades(grades1):
    pattern="(?P<Name>[\w ]+)(\: \ )(?P<Grade>[B])"  
    for itemx in re.finditer(pattern,grades1,re.VERBOSE):
        ax = itemx.groupdict()
        print(ax)
        WhiteList.append(ax)
    print(len(WhiteList))
    return(WhiteList)

grades(grades1)

#1.3 Part C 
#Consider the standard web log ﬁle in assets/logdata.txt. This ﬁle...
#...records the access a user makes when visiting a web page (like...
#...this one!). Each line of the log has the following items: 
    #*a host (e.g., ‘146.204.224.152’) 
    #* a user_name (e.g., ‘feest6811’ note: sometimes the user name is...
    #...missing! In this case, use ‘-’ as the value for the username.)
    #* the time a request was made (e.g.,‘21/Jun/2019:15:45:24 -0700’)
    #* the post request type (e.g., ‘POST /incentivize HTTP/1.1’ note:...
    #...not everything is a POST!)
#Your task is to convert this into a list of dictionaries, where each...
#...dictionary looks like the following:

 #example_dict = {"host":"146.204.224.152",
                  #"user_name":"feest6811",
                  #"time":"21/Jun/2019:15:45:24 -0700",
                  #"request":"POST /incentivize HTTP/1.1"}

# <--WINNER (Option without function)  
import re
with open("assets-logdata.txt","r") as file:
    logdata=file.read()
print(logdata)
print("\n")

patternx="""
(?P<host>\d{1,10}\.\d{1,10}\.\d{1,10}\.\d{1,10})
(\ \- \ )
(?P<user_name>[\w]+|\-+)
(\ \[)
(?P<time>[\w]+\/[\w]+\/[\w]+\:[\w]+\:[\w]+\:[\w]+\ \-[\w]+)
(\] \ \")
(?P<request>POST [\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+\")"""
     
for itemx2 in re.finditer(patternx,logdata,re.VERBOSE):
    print(itemx2.groupdict())
print("\n")

# <--WINNER (Option with function)
import re
with open("assets-logdata.txt","r") as file:
    logdata=file.read()
print(logdata)
print("\n")

WhiteList2 = []
def logdatafunc(logdata):
    patternx="""
    (?P<host>\d{1,10}\.\d{1,10}\.\d{1,10}\.\d{1,10})
    (\ \- \ )
    (?P<user_name>[\w]+|\-+)
    (\ \[)
    (?P<time>[\w]+\/[\w]+\/[\w]+\:[\w]+\:[\w]+\:[\w]+\ \-[\w]+)
    (\] \ \")
    (?P<request>POST [\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+|POST [\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*[\W]+[\w ]*\/[\d]+\.[\d]+\")"""
    for itemx2 in re.finditer(patternx,logdata,re.VERBOSE):
        var = itemx2.groupdict()
        print(var)
        WhiteList2.append(var)
    print(WhiteList2)
    return(WhiteList2)

logdatafunc(logdata)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
    
#Quiz 1 - January 20, 2021 (RMDLC)

    
#PROB #1  <--WINNER 
import re
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print("Q1:",result)
print("\n")

#PROB #2  <--WINNER 
#def l2_dist(a, b):
#     result = ((a - b) * (a - b)).sum()
#     result = result ** 0.5
#     print("Q2:",result)
#     return result
#print("\n")

#a = (20, 20, 20)
#b= (20, 20, 20)
#l2_dist(a.T,b.T)

#PROB #3  <--WINNER 
import numpy as np
a1 = np.random.rand(4)
print(a1)
print(a1.shape)
print("\n")
a2 = np.random.rand(4, 1)
print(a2)
print(a2.shape)
print("\n")
a3 = np.array([[1, 2, 3, 4]])
print(a3)
print(a3.shape)
print("\n")
a4 = np.arange(1, 4, 1)
print(a4)
print(a4.shape)
print("\n")
a5 = np.linspace(1 ,4, 4)
print(a5)
print(a5.shape)
print("\n")

a213 = (a5.shape == a1.shape)
print("Q3:",a213)
print("\n")

#PROB #5  <--WINNER 
old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0
print("Q4:",old) 
print("\n")

#PROB #5  <--WINNER 
Q5 = np.random.randint(36, size=(6,6))
print(Q5)
newQ5 = Q5[2:4,2:4]
print("Q5:",newQ5)
print("\n")

#PROB #6  <--WINNER 
s = 'ACBCAC'
ss = re.findall("^AC",s)
print("Q6:",ss)
print("\n")

#PROB #7  <--WINNER 
sss = 'ACAABAACAAAB'
result = re.findall('A{1,2}', sss)
print(result)
L = len(result)
print("Q7:",L)
print("\n")

#PROB #8  <--WINNER 
Text8 = "Office of Research Administration: (734) 647-6333 | 4325"
Text8Ans = re.findall("[(]\d{3}[)]\s\d{3}[-]d{4}",Text8)
print("Q8:",Text8Ans)
print("\n")

#PROB #9  <--WINNER 
Text9 = "'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'"
Text9Ans = re.findall("(?<=[https]:\/\/)([A-Za-z0-9.]*)",Text9)
print("Q9:",Text9Ans)
print("\n")

#PROB #10  <--WINNER 
text=r'''Everyone has the following fundamental freedoms:
(a) freedom of conscience and religion;
(b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
(c) freedom of peaceful assembly; and
(d) freedom of association.
'''
X10 = "\(.\)"
pattern = X10
print("Q10:",len(re.findall(pattern,text)))
print("\n")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

##############################################################################

##############################################################################

##############################################################################

#Topic 8: Pandas (RMDLC)

#Topic 8.0.1 - Pandas (Introduction):
    #The name "Pandas" has a reference to both "Panel Data", and "Python...
    #...Data Analysis".

    #Pandas is a Python library Pandas used for working with data sets.
    #It has functions: for analyzing, cleaning, exploring, and manipulating..
    #...data.

#Topic 8.0.2 - Pandas (Getting Started):
    #OK.
    #The main differences between Pandas and Numpy are:
        #Pandas
            #1- When we have to work on Tabular data, we prefer the Pandas...
            #...module.	
            #2- The powerful tools of Pandas are Data frame and Series.
            #3- Pandas consume more memory. 
            #4- Pandas has a better performance when number of rows is...
            #...500K or more.	
            #5- Indexing of the Pandas series is very slow as compared to...
            #...numpy arrays (Data rows are by default indexed in...
            #...Pandas series and dataframes).
            #6- Pandas offers 2d table object called DataFrame.
            #7- Pandas is popularly used for data analysis and visualization.
            #8- Pandas provide support for working with tabular data...
            #...(CSV, Excel etc).
            #9- Usage in Deep Learning and Machine Learning: Pandas series...
            #...and dataframes cannot be directly fed as input in these...
            #..toolkits (we have to run them through several steps of...
            #...preprocessing before feeding them to a machine learning....
            #...module.)
            #10- Pandas uses R language as its reference language...
            #...and hence provide many similar functions.
        
        #Numpy
            #1- When we have to work on Numerical data, we prefer the...
            #...Numpy module.
            #2- The powerful tools of Numpy is Arrays.
            #3- Numpy is memory efficient. 
            #4- Numpy has a better performance when number of rows is...
            #...50K or less (It is insanely faster than pandas when it...
            #...comes to calculations such as solving linear algebra,...
            #...finding gradient descent, matrix multiplications and...
            #...vectorization of data etc).
            #5- Indexing of Numpy Arrays is very fast (there is no default...
            #...indexing of data rows in numpy arrays).
            #6- Numpy is capable of providing multi-dimensional arrays.
            #7- NumPy is popularly used for numerical calculations.
            #8- NumPy by default support data in the form of arrays and..
            #...matrix.
            #9- Usage in Deep Learning and Machine Learning: Toolkits...
            #...for machine/deep learning like Tensorflow, Scikit Learn...
            #...can only be fed using numpy arrays.
            #10- NumPy is written in the C programming language and...
            #...hence uses multiple functionalities from it.
    
#Topic 8.0.3 - Pandas (Pandas Series and Dataframes):
    #A Pandas Serie is like a column in a table. It is a 1D array...
    #...holding data of any type (str, int, float...)
    
    #A Serie has an index (also called "label") which by default starts...
    #...at zero or can be established by us in a "simple way" (i.e. first...
    #...define the elements of the serie and in another line define the...
    #...then index) or in a "key/value" way - like a dictionary).
    
    #A Pandas Dataframe is like a table with several columns (i.e. several...
    #...Series). It is like a 2D array holding data of any type (str,...
    #...int, float, object...)
        #It also has labels.

#Example 8.0.3.1: 
#In this cases we are printing a serie. In this case we see that the type...
#...of data is "int64" because all the elements are integers.
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

    #In this cases we are watching a specific element of the serie...
    #...trough the index [0].
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar[0])

#Example 8.0.3.2: 
#In this cases we are printing a serie. In this case we see that the type...
#...of data is "float64" because at least one of the elements (which are...
#...all numbers) is a float
import pandas as pd
a = [1, 7, 2.6]
myvar = pd.Series(a)
print(myvar)

#Example 8.0.3.3: 
#In this cases we are printing a serie. In this case we see that the type...
#...of data is "object" because at least one of the elements (which are...
#...a mix of numbers and string) is a string.
import pandas as pd
a = [1, 7.3, "jaba"]
myvar = pd.Series(a)
print(myvar)

#Example 8.0.3.4:
#In this cases we are detailing the index of the serie.
import pandas as pd
a = ["a", 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

    #In this cases we are watching a specific element of the serie...
    #...trough the index ["z"].
import pandas as pd
a = ["a", 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar["z"])

#Example 8.0.3.5:
#In this cases we are create a serie using a "key/value" way - like a...
#...dictionary (i.e. another way to detail the index of the serie).
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

    #The keys of the dictionary become the labels
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar["day2"])

#Example 8.0.3.6:
#Creating Dataframes with the concept of serie "key/value" way - like a...
#...dictionary. In this case 3 rows and 2 columns.
    #It is important to see the use of the square brackets when we are...
    #...listing the data that belong to a specific column.
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

#Creating Dataframes with the concept of serie "key/value" way - like a...
#...dictionary. In this case 1 row and 2 columns.
    #It is important to see the use of the square brackets when we are...
    #...listing the data that belong to a specific column.
import pandas as pd
data = {
  "calories": [420],
  "duration": [50]
}
myvar = pd.DataFrame(data)
print(myvar)

#Topic 8.0.4 - Pandas (Dataframes): 
    #A Pandas Dataframe is like a table with several columns (i.e. several...
    #...Series). It is like a 2D array holding data of any type (str,...
    #...int, float, object...)
        #It also has labels.
    
    #The main purpose of this is to apply certain techniques when we are...
    #...handling data. 
        #Each row in your data frame represents a data sample.
        #Each column is a variable or feature (and is usually named).
        #Select relevant rows from the data frame for modelling and...
        #...visualisation activities.
        
    #The two main options to achieve the selection and indexing (i.e....
    #...operations for retrieving data from Pandas dataframes) activities...
    #...in Pandas are: 
        #Selecting data by row numbers (.iloc):
            #Entire rows or columns
            #Slice of rows or columns
            #Single value of a row or a column
            #The "iloc" indexer for Pandas Dataframe is used for...
            #...integer-location based indexing / selection by position.
            
        #Selecting data by label or by a conditional statement (.loc)
            #Index or label value for row. Also name of column.
            #List of label value for rows. List of names of columns.
            #Logical / boolen index for rows. Slice of columns.
        
#Using "iloc" ("slice" or "single value")
#Example 8.0.4.1: 
#In this cases we are printing a DataFrame and a specific row (based in...
#...Python Index) of the datafame (i.e. we are printing a Serie). In this...
#...case we see that the type of data of the printed row is "int64"...
#...because all the elements are integers.
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
print(myvar.iloc[2])

#Example 8.0.4.2: 
#In this cases we are printing a DataFrame and a specific rows (based in...
#...Python Index) of the  of the datafame (i.e. we are printing a datafame).
  #It is important to say that is not a range of rows. I this case, to be...
  #...specific we are very interested in the row N°2 and N°4 (based in...
  #...Python Index).
import pandas as pd
data = {
  "calories": [420, 380, 390, 500, 6000, 700, 800],
  "duration": [50, 40, 45, 55, 65, 75, 85]
}
myvar = pd.DataFrame(data)
print(myvar)
print(myvar.iloc[[2,4]])

#Example 8.0.4.3: 
#In this cases we are printing a DataFrame and a specific rows (based in...
#...Python Index) of the  of the datafame (i.e. we are printing a datafame).
  #It is important to say that is not a range of rows.I this case, to be...
  #...specific we are very interested in the row N°2, N°3, N°4 (based in...
  #...Python Index).
import pandas as pd
data = {
  "calories": [420, 380, 390, 500, 6000, 700, 800],
  "duration": [50, 40, 45, 55, 65, 75, 85]
}
myvar = pd.DataFrame(data)
print(myvar)
print(myvar.iloc[[2,3,4]])

#Example 8.0.4.4: 
#In this cases we are printing a dataFrame with specific names for the...
#...index values of every row.
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday"])
print(myvar)

#Example 8.0.4.5:
#In this cases we are printing a specific row based in its position inside...
#...the dataframe. In this case the position is based in Python Index.
import pandas as pd
datax = {
  "calories": [420, 380, 390, 400, 500, 600, 700, 800],
  "duration": [50, 40, 45, 55, 66, 77, 88, 99]
}
myvar = pd.DataFrame(datax)
locate = myvar.iloc[7]
print(locate)

#Example 8.0.4.6:
#In this cases we are printing a specific range (not including the number....
#...position located after the semicolon) of rows based in its ...
#...position inside the dataframe. In this case the position is based...
#...in Python Index.
import pandas as pd
datax = {
  "calories": [420, 380, 390, 400, 500, 600, 700, 800],
  "duration": [50, 40, 45, 55, 66, 77, 88, 99]
}
myvar = pd.DataFrame(datax)
locate = myvar.iloc[:4]
print(locate)

#Example 8.0.4.7:
#In this cases we are printing a specific range (not including the number....
#...position located after the semicolon) of rows based in its ...
#...position inside the dataframe. In this case the position is based...
#...in Python Index.
import pandas as pd
datax = {
  "calories": [420, 380, 390, 400, 500, 600, 700, 800],
  "duration": [50, 40, 45, 55, 66, 77, 88, 99]
}
myvar = pd.DataFrame(datax)
locate = myvar.iloc[2:4]
print(locate)

#Example 8.0.4.8:
#In this cases we are printing a specific non-consecutive rows (using...
#...square brackets). In this case the position is based in Python Index.
import pandas as pd
datax = {
  "calories": [420, 380, 390, 400, 500, 600, 700, 800],
  "duration": [50, 40, 45, 55, 66, 77, 88, 99]
}
myvar = pd.DataFrame(datax)
locate = myvar.iloc[[2,4]]
print(locate)

#Example 8.0.4.9:
#In this cases we are printing a specific colum based in its position inside...
#...the dataframe. In this case the position is based in Python Index.
import pandas as pd
datax = {
  "calories": [420, 380, 390, 400, 500, 600, 700, 800],
  "duration": [50, 40, 45, 55, 66, 77, 88, 99],
  "energy": [5, 4, 6, 7, 8, 9, 10, 1],
  "stamina": [5000, 4000, 6000, 7000, 8000, 9000, 10000, 11000]
}
myvar = pd.DataFrame(datax)
locate = myvar.iloc[:,1]
print(locate)

#Example 8.0.4.10:
#In this cases we are printing a specific range (not including the number....
#...position located after the colon) of columns based in its ...
#...position inside the dataframe. In this case the position is based...
#...in Python Index.
import pandas as pd
datax = {
  "calories": [420, 380, 390, 400, 500, 600, 700, 800],
  "duration": [50, 40, 45, 55, 66, 77, 88, 99],
  "energy": [5, 4, 6, 7, 8, 9, 10, 1],
  "stamina": [5000, 4000, 6000, 7000, 8000, 9000, 10000, 11000]
}
myvar = pd.DataFrame(datax)
locate = myvar.iloc[:,0:2]
print(locate)

#Example 8.0.4.11:
#In this cases we are printing a specific non-consecutive columns (using...
#...square brackets). In this case the position is based in Python Index.
import pandas as pd
datax = {
  "calories": [420, 380, 390, 400, 500, 600, 700, 800],
  "duration": [50, 40, 45, 55, 66, 77, 88, 99],
  "energy": [5, 4, 6, 7, 8, 9, 10, 1],
  "stamina": [5000, 4000, 6000, 7000, 8000, 9000, 10000, 11000]
}
myvar = pd.DataFrame(datax)
locate = myvar.iloc[:,[0,-1]]
print(locate)


#Using "loc" ("Index or label value" and "List of label value")
#Example 8.0.4.12:
#In this cases we are printing a specific row based in its label...
#...value of the dataframe.
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc["Friday"]
print(locate)

#Example 8.0.4.13: 
#In this cases we are printing a specific non-consecutive rows (using...
#...square brackets for the row label values). 
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[["Friday", "Saturday"]]
print(locate)

#Example 8.0.4.14:
#In this cases we are printing a specific range (using row label values).
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc["Monday":"Saturday"]
print(locate)

#Example 8.0.4.15:
#In this cases we are printing a specific range (using row label values)...
#...with a specific column (using name of the column).
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc["Monday":"Saturday","duration"]
print(locate)

#Example 8.0.4.16: 
#In this cases we are printing a specific non-consecutive rows (using...
#...square brackets for the row label values) with specific columns...
#...(using name of the columns).
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[["Friday", "Saturday"],["duration","energy"]]
print(locate)

#Example 8.0.4.17: 
#In this cases we are printing a specific non-consecutive rows (using...
#...square brackets for the row label values) with specific range of...
#...columns (using name of the columns).
   #Be careful about the range of the columns, because the range apparently...
   #...is managed alphabetically; therefore, is covenient to list the...
   #...specific names of the columns that we want to see.
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[["Friday", "Saturday"],"duration":"power"]
print(locate)


#Using "loc" ("Logical and Boolean")
#Example 8.0.4.18: 
#In this cases we are printing specific rows (using...
#...square brackets for the chosen column label) and the specific value...
#...that belong to the column that need to be true to show in printed....
#...result specific rows and all columns.
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8],
  "vitamin":["A","A","B","C","A"]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[myvar["vitamin" ] =="A"]
print(locate)

#Example 8.0.4.19: 
#In this cases we are printing specific rows (using...
#...square brackets for the chosen column label) and the specific value...
#...that belong to the column that need to be true to show in printed....
#...result specific rows and all columns.
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8],
  "vitamin":["A","A","B","C","A"]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[myvar["power" ] <5000]
print(locate)

#Example 8.0.4.20:
#In this cases we are printing specific rows (using...
#...square brackets for the chosen column label) and the specific value...
#...that belong to the column that need to be true to show in printed....
#...result specific rows and specific columns.
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8],
  "vitamin":["A","A","B","C","A"]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[myvar["power" ] <5000, ["calories", "duration"]]
print(locate)

#Example 8.0.4.21:
#In this cases we are printing a specific row (not using...
#...square brackets for the chosen column label) and the specific value...
#...that belong to the column that need to be true to show in printed....
#...result a specific rows and specific column (in a Serie shape,...
#...because I use quotation marks to write the specific alone column).
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8],
  "vitamin":["A","A","B","C","A"]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[myvar["power"]<5000,"vitamin" ]
print(locate)

#Example 8.0.4.22:
#In this cases we are printing a specific row (using...
#...square brackets for the chosen column label) and the specific value...
#...that belong to the column that need to be true to show in printed....
#...result a specific rows and specific column (in a dataframe shape,...
#...because I use square brackets to write the specific alone column).
import pandas as pd
data = {
  "calories": [420, 380, 390, 400, 500],
  "duration": [50, 40, 45, 55, 65],
  "power": [5000, 4000, 4500, 5500, 6500],
  "energy": [5, 4, 6, 7, 8],
  "vitamin":["A","A","B","C","A"]
}
myvar = pd.DataFrame(data, index = ["Monday", "Tuesday", "Friday", "Saturday", "Sunday"])
locate = myvar.loc[myvar["power"]<5000,["vitamin"]]
print(locate)

#Topic 8.0.5 - Pandas (pandas Read CSV):
    #We can use Pandas to load data into a DataFrame. for instance a...
    #...load a comma separated file (CSV) from MS Excel into a DataFrame.
    
    #It its important to know in what folder is the MS Excel file,...
    #...located because the Python Panda code may send some error messages...
    #...pointing out that the file does not exist (i.e. does not exist...
    #...the file because the Python Panda code does not find it). To...
    #...avoid the previous situation we need to do the following things:
        #Option #1: Put the MS Excel file (in the format of CSV) in the...
        #...folder located inside the default path:
            #Disco Local (C) --> Usuario Folder --> USUARIO Folder...
            #...--> pokemondata.csv
            
        #Option #2: Put the MS Excel file (in the format of CSV) in the...
        #...folder located inside the specific path:
            #Desktop --> M --> COURSERA --> Applied Data Science with...
            #...Python --> Introduction to Data Science in Python -->...
            #...Week 1 --> pokemondata.csv
            
#Example 8.0.5.1:
    #In this case we are reading a MS Excel file (in the format of CSV)...
    #...using the default file path to find it.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
print(dfpokemon) 

#Example 8.0.5.2:
    #In this case we are reading a MS Excel file (in the format of CSV)...
    #...using the created file path to find it.
import pandas as pd
dfpokemon = pd.read_csv('Desktop/M/COURSERA/Applied Data Science with Python/Introduction to Data Science in Python/Week 1/pokemondata.csv')
print(dfpokemon) 

#Example 8.0.5.3:
    #In this case we are reading a MS Excel file (in the format of CSV)...
    #...using the default file path to find it.
    
    #The main difference with the previous examples (#Example 8.0.5.1...
    #...and #Example 8.0.5.2) is that we are going to watch the entire...
    #...data and not just a part of the data printed. (i.e. we are going to...
    #...watch the entire printed data). We can see cleary that we print...
    #...a part of the data because there are several points in the...
    #...middle of the printed data.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
print(dfpokemon.to_string()) 

#Topic 8.0.6 - Pandas (pandas Read JSON):
  #Big data sets are often stored, or extracted as JSON.
  
  #JSON:
      #JSON is a syntax for storing and exchanging data.
      #JSON is text, written with "JavaScript object notation".
      #Python has a built-in package called "json", which can be used to...
      #...work with JSON data (invoker trough "json module").
      #JSON objects have the same format as Python dictionaries.
  
  #JSON is plain text, but has the format of an object, and is well...
  #...known in the world of programming, including Pandas.

#Topic 8.0.7 - Pandas (Analyzing DataFrames):
  #Instead of print the entire dataset, we can see just a few first rows...
  #...and also a few last rows (the quantity of rows is decided by the...
  #...user or by default we are goint to watch only 5 rows).
      #To see just a few first rows we use the code "head()" 
      #To see just a few first rows we use the code "tail()" 
    
  #We can get general infoabout the data through the method "info()" like: 
      #Memory usage
      #data type of the database
      #number of columns and rows
      #name of the columns
      #data type of the columns
      #quantity of non-nullvalues in every column
      #range of the index
                                                
#Example 8.0.7.1:
    #In this case we are printing just the first 5 rows of the dataset.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
print(dfpokemon.head()) 

#Example 8.0.7.2:
    #In this case we are printing just the first 10 rows of the dataset.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
print(dfpokemon.head(10)) 

#Example 8.0.7.3:
    #In this case we are printing just the last 5 rows of the dataset.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
print(dfpokemon.tail()) 

#Example 8.0.7.4:
    #In this case we are printing just the last 10 rows of the dataset.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
print(dfpokemon.tail(10)) 

#Example 8.0.7.5:
    #In this case we are printing just the last 10 rows of the dataset.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
print(dfpokemon.info()) 

#Topic 8.0.8 - Pandas (Cleaning Data):
  #Data cleaning means fixing bad data in your data set. Bad data...
  #...could be:
      #Empty cells
      #Data in wrong format
      #Wrong data
      #Duplicates

#Topic 8.0.9 - Pandas (Cleaning Empty Cells):
  #The empty cells are called "NULL" values.
                      
  #If want to deal with empty cells we have two options (which can affect...
  #...the original dataframe using the argument "inplace = True" or....
  #...generate a new dataframe using the argument "inplace = False" or...
  #...doing nothing because by default the argument "inplace" is "False"):
      
      #Option 1: Remove rows that contain empty cells using the code...
      #..."dropna()": This is viable when we have a huge amount of data.
            #We can drop data instances through a conditional "if" if...
            #...the dataset is huge.
      
      #Option 2: Fill the empty cells using the code "fillna()": we have...
      #...the following options:
          #Fill all the empty cells with the same value.
          #Fill all the empty cells in a specific column with the...
          #...same value.
          #Fill all the empty cells in a specific column with the...
          #..."median()" value or "mean()" value or "mode()" value.
                     #Mean = the average value (the sum of all values...
                     #...divided by number of values).
                     #Median = the value in the middle, after you have...
                     #...sorted all values ascending.
                     #Mode = the value that appears most frequently.
#Example 8.0.9.1:
    #In this case we are interested in the deal with the column labeled...
    #..."Type 2" of the dataset, because it shows everal Null Values...
    #...according to the code info().
    
    #To be specific, we are going to remove all the rows that are Null...
    #...values in the original dataframe, generating as a consequence...
    #...a new dataframe.
import pandas as pd
dfpokemon = pd.read_csv("pokemondata.csv")
new_df = dfpokemon.dropna()
print(new_df) 
print(dfpokemon) 

#Example 8.0.9.2:
    #In this case we are interested in the deal with the column labeled...
    #..."Type 2" of the dataset, because it shows everal Null Values...
    #...according to the code info().
    
    #To be specific, we are going to remove all the rows that are Null...
    #...values in the original dataframe, generating a change...
    #...the original dataframe.
import pandas as pd
dfpokemon1 = pd.read_csv("pokemondata.csv")
dfpokemon1.dropna(inplace = True)
print(dfpokemon1) 

#Example 8.0.9.3:
    #In this case we are interested in the deal with the column labeled...
    #..."Type 2" of the dataset, because it shows everal Null Values...
    #...according to the code info().
    
    #To be specific, we are going to fill all the cells that are Null...
    #...values in the new original dataframe with a single unique value,...
    #...generating as a consequence a new dataframe. We can check that...
    #...fill al the values:
        #Seeing the dataframe
        #Applying the code info() and checking that there is no Null values.
import pandas as pd
dfpokemon2 = pd.read_csv("pokemondata.csv")
new_df2 = dfpokemon2.fillna(1000) 
print(new_df2)
print(new_df2.info())  

#Example 8.0.9.4:
    #In this case we are interested in the deal with the column labeled...
    #..."Type 2" of the dataset, because it shows everal Null Values...
    #...according to the code info().
    
    #To be specific, we are going to fill all the cells that are Null...
    #...values (in a specific column of the existing dataframe)...
    #...We can check that fill al the values:
        #Seeing the dataframe
        #Applying the code info() and checking that there is no Null values.
import pandas as pd
dfpokemon3 = pd.read_csv("pokemondata.csv")
dfpokemon3["Type 2"].fillna("ASTRA", inplace = True) 
print(dfpokemon3)
print(dfpokemon3.info())  

#Example 8.0.9.5: 
    #In this case we are interested in the deal with the column labeled...
    #..."Type 2" of the dataset, because it shows several Null Values...
    #...according to the code info().
    
    #To be specific, we are going to fill all the cells that are Null...
    #...values (in a specific column of the existing dataframe) with the...
    #...mean value of that column.
    #...We can check that fill al the values:
        #Seeing the dataframe
        #Applying the code info() and checking that there is no Null values.
import pandas as pd
dfpokemon4 = pd.read_csv('pokemondata2.csv')
W = dfpokemon4["HP"].mean()
print(W)
dfpokemon4["Type 2"].fillna(W, inplace = True) 
print(dfpokemon4)
print(dfpokemon4.info())  

#Example 8.0.9.6: 
    #In this case we are interested in the deal with the column labeled...
    #..."Type 2" of the dataset, because it shows everal Null Values...
    #...according to the code info().
    
    #To be specific, we are going to fill all the cells that are Null...
    #...values (in a specific column of the existing dataframe) with the...
    #...median value of that column.
    #...We can check that fill al the values:
        #Seeing the dataframe
        #Applying the code info() and checking that there is no Null values.
import pandas as pd
dfpokemon5 = pd.read_csv('pokemondata2.csv')
WW = dfpokemon5["HP"].median()
print(WW)
dfpokemon5["Type 2"].fillna(WW, inplace = True) 
print(dfpokemon5)
print(dfpokemon5.info()) 

#Example 8.0.9.7: 
    #In this case we are interested in the deal with the column labeled...
    #..."Type 2" of the dataset, because it shows everal Null Values...
    #...according to the code info().
    
    #To be specific, we are going to fill all the cells that are Null...
    #...values (in a specific column of the existing dataframe) with the...
    #...mode value of that column.
    
    #I am not sure why we need to put "[0]" after the code "mode()".
    
    #...We can check that fill al the values:
        #Seeing the dataframe
        #Applying the code info() and checking that there is no Null values.
import pandas as pd
dfpokemon6 = pd.read_csv('pokemondata2.csv')
W = dfpokemon6["HP"].mode()[0]
dfpokemon6["Type 2"].fillna(W, inplace = True) 
print(dfpokemon6)
print(dfpokemon6.info()) 

#Topic 8.0.10 - Pandas (Cleaning Data of Wrong Format):
  #The wrong format in some instances of the data can be a problem...
  #...when we try to analyze the data; therefore, we need to fix (if is...
  #...possible those errors in the format).
  
  #To be specific, in this case we are going to fix the following things:
      #Format of dates
      
#Example 8.0.10.1: 
    #In this case we are interested in the deal with the column labeled...
    #..."Date" of the dataset, because it shows one "Null Value" and one...
    #...date value with a wrong format. 
    
    #To fix the format of the date instance, we are going to use the...
    #...Panda method "to_datetime()".
        #We can see from the result, that "Null Value" (NaN) were...
        #...converted into value "NaT" (Not a Time) in other words...
        #...an empty value.
    
    #This changing in format, modify the original dataframe.                            
import pandas as pd
dfdirty1 = pd.read_csv('dirtydata.csv')
print(dfdirty1)
print(dfdirty1.info()) 
 
import pandas as pd
dfdirty2 = pd.read_csv('dirtydata.csv')
dfdirty2['Date'] = pd.to_datetime(dfdirty2['Date'])
print(dfdirty2)
print(dfdirty2.info())                        

#Topic 8.0.11 - Pandas (Fixing Wrong Data):
  #It is important to know that we can fix the wrong data (incorrect data...
  #...instances) in a dataset. We have two options:
      #We can fix specific value (replacing the wrong value manually).
      #We can fix many data instances (replacing the wrong value through...
      #...a conditional "if" and a "for loop" to iterate over every...
      #...value of the column) if the dataset is huge.
 
#Example 8.0.11.1: 
    #In this case we are interested in fix a wrong value of a specific...
    #...row and column of the dataset; therefore, we need to:
        #Use the loc() code, then specify the number of the row and the...
        #...the number of the column.
        #Finally we set the correct value that will replace the wrong value.
import pandas as pd
dfdirty3 = pd.read_csv('dirtydata.csv')
print(dfdirty3)  

import pandas as pd
dfdirty3 = pd.read_csv('dirtydata.csv')
dfdirty3.loc[7, "Duration"] = 45
print(dfdirty3)

#Example 8.0.11.2: 
    #In this case we are interested in fix a wrong value of a specific...
    #...row and column of the dataset; therefore, we need to:
        #Apply a "for loop" in the index of the dataframe.
        #Then apply a conditional "if".
        #Third, use the loc() code, then specify the random row (i.e. we...
        #...are applying the code to all the row elements of a specific colum)...
        #...and the number of the column.
import pandas as pd
dfdirty4 = pd.read_csv('dirtydata.csv')
print(dfdirty4)  

import pandas as pd
dfdirty4 = pd.read_csv('dirtydata.csv')
for x in dfdirty4.index:
    if dfdirty4.loc[x, "Duration"] > 120:
        dfdirty4.loc[x, "Duration"] = 99
print(dfdirty4)  

#Topic 8.0.12 - Pandas (Removing Duplicates):
  #We can figure out if there are duplicated rows in the data set through...
  #...the code "df.duplicated()" an get as an answer the rows of the...
  #...dataframe with the words "True" (if there is a duplicated) or...
  #..."False"(if there is not a duplicated).
  
  #Also, if we discover a duplicated, we can erase it with the code...
  #..."df.drop_duplicates()".
  
#Example 8.0.12.1: 
    #In this case we are interested in find a duplicated row.                         
import pandas as pd
dfdirty5 = pd.read_csv('dirtydata.csv')
print(dfdirty5)  

import pandas as pd
dfdirty5 = pd.read_csv('dirtydata.csv')
Dupli = dfdirty5.duplicated()
print(Dupli) 

#Example 8.0.12.2: 
    #In this case we are interested in find a duplicated row and then...
    #...erase it in the original dataframe. As a consequence, we can see...
    #...the original dataframe with a row less.
import pandas as pd
dfdirty6 = pd.read_csv('dirtydata.csv')
print(dfdirty6)  

import pandas as pd
dfdirty6 = pd.read_csv('dirtydata.csv')
dfdirty6.drop_duplicates(inplace=True)
print(dfdirty6) 

#Topic 8.0.13 - Pandas (Pandas - Data Correlations):
  #We can figure out if there correlations between each column in our...
  #...data set uaing the "corr()" method.
  
  #The corr() method ignores "not numeric" columns.  
  
  #The number of correlation varies from -1 to 1.
  
  #1 means that there is a 1 to 1 relationship (a perfect correlation),...
  
  #A good correlation: it is safe to say you have to have at least 0.6...
  #...(or -0.6) is a good correlation. 

#Example 8.0.13.1: 
    #In this case we are interested in find a correlations between...
    #...each column in our data set                 .
import pandas as pd
dfdata2 = pd.read_csv('data2.csv')
print(dfdata2)  

import pandas as pd
dfdata2 = pd.read_csv('data2.csv')
CorrelationColums = dfdata2.corr()
print(CorrelationColums)              

##############################################################################

##############################################################################

##############################################################################             

#TEST 1

#PROB EXAMPLE

# You should write your solution here, and return your result
def example_word_count(example_string):
    result = example_string.split(" ")
    print(len(result))
    print("\n")
    return len(result)

# This example question requires counting words in the example_string below.
example_string = "Amy is 5 years old"

example_word_count(example_string)


#IMPORTANT TOPICS:
    
#This topics are in some helpful because allow us to write codes that warn us...
#...if something goes wrong when we execute the code.

#Code "Raise"
    #We use code "raise" to raise an exception. Also we can define the type of...
    #...error to raise and the text to print to the user.
    
        #It is important to say that if the conditions is met, then we will...
        #...see that the printed result is a bunch of text (in underlined blue...
        #...and red color). At the end of that text will see a red color text...
        #....with the message that we create fo that "raise code". For...
        #...the following example:
#x = -1
#if x < 0:
#    raise Exception ("This number is below zero")
    
        #It is important to say that if the conditions is not met, then the code...
        #...will continue their work without problem.For the following example:
xx = 6
if xx < 0:
    raise Exception ("This number is below zero")

#There are 2 kinds of errors: syntax errors and exceptions.
    #Syntax errors (also known as parsing error)
        #Are perhaps the most common kind of complaint you get while you...
        #...are still learning Python.
        #The parser repeats the offending line and displays a little ‘vertical...
        #...arrow’ pointing at the earliest point in the line where the error was...
        #..detected. File name and line number are printed so you know where...
        #...to look in case the input came from a script.

    #Exceptions
    #Even if a statement or expression is syntactically correct, it may cause ...
    #...an error when an attempt is made to execute it. 
    #Errors detected during execution are called exceptions.
    #They are not unconditionally fatal.
    #The last line of the error message indicates what happened. 
    #Exceptions come in different types, and the type is printed as part of...
    #...the message.
    
        #An exception is an occasion, which happens during the execution of a...
        #...program that disturbs the ordinary progression of the program’s...
        #...directions. 
        
        # An exception is a Python object that speaks to a mistake. At the...
        #....point when a Python content raises an exception.
    
#Code "NotImplementedError"
    #It is one of the exceptions that are usually raised.
    #This kind of exceptions and errors can be handled by "try" and "except"...
    #...blocks. 

#Code "Assert"
    #It is a special debugging statements which helps for flexible execution..
    #...of the code. 
    #It is a form of "raise-if statement", when a expression ends false...
    #...then the assert statements will be raised. 
    #It acts as a sophisticated form of sanity check for the code.
    
    #It is important to say that if the conditions is not met, then we will...
        #...see that the printed result is a bunch of text (in underlined blue...
        #...and red color). At the end of that text will see a red color text...
        #....with the message that we create fo that "assert code".
        
Input_List = [1,2,3,4.56,9]
for element in Input_List:
    element = int(element)
    print(element)
    assert element > 0,"!!! Negative number is entered !!!"
    
#Code "Open with"
    #The is a built-in python function to open file and as a consequence get a...
    #..."file object".
    #The "file object" contain methods and attributes that can be used to...
    #...collect information about the file you opened. 
    
    #The "mode attribute" of a file object tells you which mode...
    #...a file was opened in. And the "name attribute" tells you the name of...
    #...the file that the file object has opened. 
        #[file_object  = open(“filename”, “mode”)]
    
     #The file and file object are two wholly separate – yet related – things.   

    #Including a mode argument is optional because a default value of ‘r’ will...
    #...be assumed if it is omitted.The modes are:

    #‘r’: Read mode which is used when the file is only being read
    #‘w’: Write mode which is used to edit and write new information to the...
    #...file (any existing files with the same name will be erased when this...
    #...mode is activated)
    #‘a’: Append mode, which is used to add new data to the end of the file;...
    #...that is new information is automatically amended to the end.
    #‘r+’: Special read and write mode, which is used to handle both actions...
    #...when working with a file.

#PROB #1    
def names(simple_string):
    NameFinder = re.findall("[A-Z][a-z]{1,100}",simple_string)
    print(NameFinder)
    print("\n") 
    return NameFinder

simple_string = "Amy is 5 years old, and her sister Mary is 2 years old. Ruth and Peter, their parents, have 3 kids"   
names(simple_string )
    
#PROB #2    
with open("assets-grades.txt","r") as file:
    gradesx = file.read()
    
def grades(gradesx):
    FindBNames = re.findall("[A-Z a-z]+(?=: B)",gradesx)
    print(FindBNames)
    print("\n") 
    return FindBNames

grades(gradesx)  


#PROB #3    
with open("assets-logdata.txt", "r") as file:
    logdata = file.read()    

my_dict = {"host":[],"user_name":[],"time":[],"request":[]}
my_list = []

def logs(logdata):
    
    "Extracting Host"
    HostList = re.findall("[\d.]+(?= - )",logdata)
    print(HostList)
    
    "Extracting User Name"
    UserNameList = re.findall("\- [\w-]*",logdata)
    print(UserNameList)
    

    #"Putting the extracted Host inside the dictionary"
    #HostList[0]
    #my_dict["host"].append(HostList[0])
    
    #"Putting the extracted User Name inside the dictionary"
    #UserNameList[0]
    #my_dict["user_name"].append(UserNameList[0])
    
    #"Dictionary"
   #my_list.append(my_dict)
   #print(my_list)
   #print("\n") 
   #return my_list

logs(logdata) 


#############################################################

#GreatDict = { }

#def logs(logdata):
#    CreateDictio1 = re.findall("[\d.]+(?= - )",logdata)
#    for HostNumber in CreateDictio1:
#        CreateDictio1000 = {"Host:":HostNumber}
#        GreatDict["Host:"] = CreateDictio100
#    print(GreatDict)
#    print("\n") 
#    return GreatDict

#logs(logdata) 

    #GreatDict["Host:"].append(CreateDictio1

#####################################################

#def logs(logdata):
#    HostList = re.findall("[\d.]+(?= - )",logdata)
    
#    lengthHostList = len(HostList)
#    XXX = 0
#    while XXX < lengthHostList:
#        HostList[XXX]
#        XXX += 1
#        my_dict11["host"].append(HostList[XXX])
#        print(my_dict11)
#        print("\n") 
#    return my_dict11

#logs(logdata) 

#####################################################

solution_length=[[15, 9, 26, 26],
 [14, 13, 26, 54],
 [15, 11, 26, 61],
 [13, 9, 26, 29],
 [14, 9, 26, 20],
 [14, 10, 26, 26],
 [13, 8, 26, 35]]

your_length = [[len(d[k]) for k in ["host", "user_name", "time", "request"]] for d in solution_length]

#assert len(solution_length)==len(your_length), "your list does not have the correct number of entries"

for j in range(len(solution_length)):
    if solution_length[j]!=your_length[j]:
        print("Index number    : {}".format(j))
        print("Solution length : {}".format(solution_length[j]))
        print("Your length     : {}".format(your_length[j]))




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    


    
    



