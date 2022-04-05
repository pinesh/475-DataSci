#!/usr/bin/env python
# coding: utf-8

#-------------------------10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  

#assuming top of the stack is the end of the list# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    x = opstack.pop()
    return x

# opPop should return the popped value.
# The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)


#--------------------------20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations

dictstack = []  

#assuming top of the stack is the end of the list# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    if(len(dictstack) != 0):
        dictstack.pop()

# dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)

#dictPush pushes the dictionary ‘d’ to the dictstack. 
#Note that, your interpreter will call dictPush only when Postscript 
#“begin” operator is called. “begin” should pop the empty dictionary from #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if len(dictstack) == 0:
        x = {name: value}
    else:
        x = dictstack.pop()
        x.update({name:value})
    dictPush(x)
    
def redefine(name, value):
    for i in dictstack:
        try:
            i[name] = value
            break
        except:
            pass
#add name:value pair to the top dictionary in the dictionary stack. 
#Keep the '/' in the name constant. #Your psDef function should pop the name and value from operand stack and #call the “define” function.
def lookup(name):
    for i in reversed(dictstack):
        try:
            val = i[name]
            return val
        except:
            pass
    print("ERROR: name not in dict")
    return None
# return the value associated with name
# What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break,but should give an appropriate error message.

#---------------------------10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not # Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        if(op1.isnumeric() and op2.isnumeric()):
            opPush(op1+op2)
        else:
            print("Error: add -one of the operands is not a numerical value")
            opPush(x)
            opPush(y)             
    else:
        print("Error: add expects 2 operands")
        
def sub():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        if(op1.isnumeric() and op2.isnumeric()):
            opPush(op1-op2)
        else:
            print("Error: sub -one of the operands is not a numerical value")
            opPush(x)
            opPush(y)             
    else:
        print("Error: sub expects 2 operands")

def mul():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        if(op1.isnumeric() and op2.isnumeric()):
            opPush(op1*op2)
        else:
            print("Error: mul -one of the operands is not a numerical value")
            opPush(x)
            opPush(y)             
    else:
        print("Error: mul expects 2 operands")

def eq():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        opPush(bool(op1 == op2))
    else:
        print("Error: eq expects 2 operands")

def lt():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        opPush(bool(op1 < op2))            
    else:
        print("Error: lt expects 2 operands")
        
def gt():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        opPush(bool(op1 > op2))          
    else:
        print("Error: gt expects 2 operands")
        
def psAnd():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        if(isinstance(op1,bool) and isinstance(op2,bool)):
            opPush(op1 & op2)
        else:
            print("Error: and -one of the operands is not a boolean value")
            opPush(x)
            opPush(y)
    else:
        print("Error: and expects 2 operands")

def psOr():
    if len(opstack) > 1:
        y = opPop()
        x = opPop()
        op2 = extract(y)
        op1 = extract(x)
        if(isinstance(op1,bool) and isinstance(op2,bool)):
            opPush(op1 | op2)
        else:
            print("Error: or -one of the operands is not a boolean value")
            opPush(x)
            opPush(y)
    else:
        print("Error: or expects 2 operands")
        
def psNot():
    if len(opstack) > 0:
        y = opPop()
        op1 = extract(y)
        if(isinstance(op1,bool)):
            opPush(not op1)
        else:
            print("Error: not -the operand is not a boolean value")
            opPush(y)
    else:
        print("Error: not expects 1 operands")

def extract(x):
    copy = dictstack
    if(isinstance(x,int)):
        return x
    if(isinstance(x,str)):
        if(x[0] != '/'):
            x = '/' + x
        for i in dictstack:
            try:
                val = i[x]
                return val
            except:
                pass
        return x
    else:
        return x

#---------------------------25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    if len(opstack) > 0:
        x = opPop()
        op = extract(x)
        if(isinstance(op,list)):
            opPush(len(op))
        else:
            print("Error - Expected a list")
            opPush(x)
    else:
        print("Error - expected 1 operand")

def get():
    if len(opstack) > 1:
        index = opPop()
        op1 = extract(index)
        array = opPop()
        op2 = extract(array)
        if(isinstance(op1,int) and isinstance(op2,list)):
            opPush(op2[op1])
        else:
            print("Error - operands are not of correct type, expected [] int ")
            opPush(array)
            opPush(index)
    else:
        print("Error - expected 2 operands")
    

def getinterval():
    if len(opstack) > 2:
        count = opPop()
        index = opPop()
        array = opPop()
        opcount = extract(count)
        opindex = extract(index)
        oparray = extract(array)
        if(isinstance(opindex,int) and isinstance(oparray,list) and isinstance(opcount,int)):
            index2 = opindex + opcount
            opPush(oparray[opindex:index2])
        else:
            print("Error - operands are not of correct type, expected [] int int")
            opPush(array)
            opPush(index)
            opPush(count)
    else:
        print("Error - expected 3 operands")
        
def put():
    if len(opstack) > 2:
        value = opPop()
        index = opPop()
        array = opPop()
        opindex = extract(index)
        #if we are working with a variable array instead of a reference to an array
        if(extract(array) != array):
            if(isinstance(extract(array),list) and isinstance(opindex,int)):
                templist = extract(array)
                templist[opindex] = value
                define(array,templist)
            else:
                print("Error - operands are not of correct type, expected [] int var")
        else:
            if(isinstance(array,list) and isinstance(opindex,int)):
                array[opindex] = value
            else:
                print("Error - operands are not of correct type, expected [] int var")
    else:
        print("Error - expected 3 operands")

def putinterval():
    #replaces the section of <array1> with <array2> starting at  <index>
    if len(opstack) > 2:
        array2 = extract(opPop())
        index = opPop()
        array = opPop()
        opindex = extract(index)
        #if we are working with a variable array instead of a reference to an array
        if(extract(array) != array):
            if(isinstance(extract(array),list) and isinstance(opindex,int) and isinstance(array2,list)):
                newlist = extract(array)[:opindex] + array2
                if(len(extract(array)) >= len(array2) + opindex):
                    newlist = newlist + extract(array)[(opindex+len(array2)):]
                redefine(array,newlist)
            else:
                print("Error - operands are not of correct type, expected [] int []")
        else:
            if(isinstance(array,list) and isinstance(opindex,int) and isinstance(array2,list)):
                newEnd = []
                if(len(array) >= len(array2) + opindex):
                    newEnd = array[(opindex+len(array2)):]
                slic(array,opindex)
                for i in array2:
                    array.append(i)
                for i in newEnd:
                    array.append(i)
            else:
                print("Error - operands are not of correct type, expected [] int []")
    else:
        print("Error - expected 3 operands")
        
        
def slic(ls,itera):
    ls[:] = ls[:itera]

#---------------------------15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    x = opPop()
    opPush(x)
    opPush(x)

def copy():
    if (len(opstack) > 0):
        templist = []
        x = opPop()
        if(isinstance(x,int)):
            for i in range (0,x):
                if (len(opstack) != 0): 
                    templist.append(opPop())  
            stackcopy = templist[::-1] +templist[::-1]
            for y in stackcopy:
                opPush(y)
        else:
            opPush(x)
            print("Error: copy expected an int")
    else:
        print("Error: copy expected at least 1 operand")

def count():
    opPush(len(opstack))

def pop():
    if(len(opstack) > 0):
        opPop()

def clear():
    opstack.clear()

def exch():
    if(len(opstack) > 0):
        if(len(opstack) > 1):
            #swap
            x = opPop()
            y = opPop()
            opPush(x)
            opPush(y)
    else:
        print("Error, expected at least 1 operands")

        
def mark():
    opPush("-mark-")

def cleartomark():
    found = False
    while found == False:
        if(len(opstack) == 0):
            break
        if(opPop() == "-mark-"):
            found = True

def counttomark():
    count = 0
    for i in opstack[::-1]:
        if(i == "-mark-"):
            break
        else:
            count = count + 1
    opPush(count)

def stack():
    for i in opstack[::-1]:
        print(extract(i))

#---------------------------20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    if len(opstack) > 0:
        #IGNORE THE SIZE THATS PASSED
        new_dict = dict()
        opPush(new_dict)
    else:
        print("Error: dict expects 1 operands")
    
# add a new dictionary to dictionary stack
def begin():
    if len(opstack) > 0:
        x = opPop()
        if isinstance(x,dict):
            dictPush(x)
        else:
            print("Error: top of stack was not a dictionary.")
    else:
        print("Error: begin expected 1 operand")
        
#pop a dictionary
def end():
    if len(dictstack) > 0:
        dictPop()
    else:
        print("Error: no dict to end")
    
def psDef():
    if len(opstack) > 1:
        val = opPop()   
        name = opPop()
        if name[0] == '/':
            define(name,val)
        else:
            print("Error: psDef-The variable name didn't start with a '/'")
    else:
        print("Error: psDef expects 2 operands")
