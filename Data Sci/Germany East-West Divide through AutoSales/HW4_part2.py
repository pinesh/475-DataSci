#!/usr/bin/env python
# coding: utf-8

# In[21]:


#!/usr/bin/env python
# coding: utf-8

#HARRY PINES CPTS 355 ID:11578059

#-------------------------10% -------------------------------------
# The operand stack: define the operand stack and its operations

opstack = []

#assuming top of the stack is the end of the list# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    global opstack
    if(len(opstack) > 0):
        x = opstack.pop()
        return x
    else:
        pass

# opPop should return the popped value.
# The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    global opstack
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
    if(name[0] != '/'):
        name = '/' + name
    for i in reversed(dictstack):
        try:
            val = i[name]
            return val
        except:
            pass
    #print("ERROR: name not in dict")
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
        if(isinstance(op1, (int, float, complex)) and not isinstance(op1, bool) and isinstance(op2, (int, float, complex)) and not isinstance(op2, bool)):
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
        if(isinstance(op1, (int, float, complex)) and not isinstance(op1, bool) and isinstance(op2, (int, float, complex)) and not isinstance(op2, bool)):
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
        if(isinstance(op1, (int, float, complex)) and not isinstance(op1, bool) and isinstance(op2, (int, float, complex)) and not isinstance(op2, bool)):
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
    if(isinstance(x,int) or isinstance(x,float)):
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
    global opstack
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
            for _ in range (0,x):
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
    global opstack
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
    global opstack
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
        _ = opPop()
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
            opPush(x)
            print("Error: top of stack was not a dictionary.")
    else:
        print("Error: begin expected 1 operand")
        
#pop a dictionary
def end():
    if len(dictstack) > 0:
        dictPop()
    else:
        pass
    
def psDef():
    if len(opstack) > 1:
        val = opPop()   
        name = opPop()
        if(not (isinstance(name,str))):
            print("Error - name must be a string")
        else:
            if name[0] == '/':
                define(name,val)
            else:
                define('/'+name,val)
    else:
        print("Error: psDef expects 2 operands")

        
#-------------------------------------------HOMEWORK PART 2-----------------------------------------------------------
import re
def tokenize(s):
    return re.findall(r"/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)



def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(c)
    return False

def parseType(value):
    val , failed = intTryParse(value)
    if(failed):
        return val
    else:
        val , failed = boolTryParse(value)
        if(failed):
            return val
    return value

def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def boolTryParse(value):
    if(value.lower() in ['true', 'false']):
        if(value.lower() == 'false'):
            return False,True
        else:
            return True,True
    else:
        return False,False
     
def listTryParse(_list):
    res = []
    for item in _list:
        if(len(item) > 2):
            if(item[0] == ']'):
                return False
            elif(item[0] == '['):
                if(item[len(item)-1] == ']'):
                    res.append(listTryParse(item[1:-1].split()))
                else:
                    return False
            else:
                res.append(parseType(item))   
        else:
            res.append(parseType(item))
    return res

# THE ONLY EDIT MADE WAS TRYING TO PARSE AS A LIST FIRST, THAT FUNCTION HANDLES OTHER TYPES.
def parse(L):
    values = listTryParse(L)
    res = []
    it = iter(values)
    for c in it:
        if c=='}':
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(c)
    return {'codearray':res}

def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []
    
#Handling the if and ifele operators  (write the Python methods psIf and psIfelse)
def psIf():
    global opstack
    if len(opstack) > 1:
        codeArray = opPop()
        _bool = opPop()
        if(isinstance(_bool,bool)):
            if(_bool == True):
                if(isinstance(codeArray,dict)):
                    interpretSPS(codeArray,False)
                else:
                    interpretSPS([codeArray],False)
            else:
                pass
        else:
            print("Error bool is not of type bool")
    else:
        print("Error: psIf expects 2 operands")
        
def psIfelse():
    global opstack
    if len(opstack) > 1:
        codeArray_case2 = opPop()
        codeArray_case1 = opPop()
        _bool = opPop()
        if(isinstance(_bool,bool)):
            if(_bool == True):
                if(isinstance(codeArray_case1,dict)):
                    interpretSPS(codeArray_case1,False)
                else:
                    interpretSPS([codeArray_case1],False)    
            else:
                if(isinstance(codeArray_case2,dict)):
                    interpretSPS(codeArray_case2,False)
                else:
                    interpretSPS([codeArray_case2],False)
        else:
            print("Error bool is not of type bool")
    else:
        print("Error: psIfelse expects 3 operands")
    
#4.Handling the repeat and foralloperators  (write the Python method psRepeat and forall)
#<N> <code array> repeat 
#Pops two items: “N” and  “code array”. • Nis an integer value, representing the repeat count of the loop.
#– repeat executes the code in “code array” “N”times. 
def psRepeat():
    global opstack
    if len(opstack) > 1:
        codeArray = opPop()
        n = opPop()
        if(isinstance(n,int) and isinstance(codeArray,dict)):
            for _ in range(n):
                interpretSPS(codeArray,False)
        else:
            print("Error n is not of type int or codeArray was not of type dict")
    else:
        print("Error: psRepeat expects 2 operands")
        
        
#<array> <codearray> forall 
#Postscript defines a forall operator that takes an array and a procedure as operands. 
#The procedure is performed on each member of the array
def forall():
    global opstack
    if len(opstack) > 1:
        codeArray = opPop()
        array = opPop()
        if(isinstance(array,list) and isinstance(codeArray,dict)):
            for i in array:
                interpretSPS([i,codeArray],False)
        else:
            print("Error array is not of type list or codeArray was not of type dict")
    else:
        print("Error: forall expects 2 operands")
    

# this dictionary contains all of our user unctions
function_dispatcher = {'add': add, 'sub': sub,'mul' : mul,'eq':eq,'lt':lt,'gt':gt,'and':psAnd,'or':psOr,'not':psNot,'length':length,
                       'get':get,'getinterval':getinterval,'put':put,'putinterval':putinterval,'dup':dup,'copy':copy,'count':count,
                       'pop':pop,'clear':clear,'exch':exch,'mark':mark,'cleartomark':cleartomark,'counttomark':counttomark,
                      'stack':stack,'dict':psDict,'begin':begin,'end':end,'def':psDef,'if':psIf,'ifelse':psIfelse,'repeat':psRepeat,'forall':forall}
     # COMPLETED FUNCTION
# This will probably be the largest function of the whole project, 
# CodeArray is our input and our stac variable determines how we should look at codearrays dicts
def interpretSPS(codeArray,static = True): 
    global opstack
    if(isinstance(codeArray,dict)):
        codeArray = list(codeArray.values())[0]
    for token in codeArray:
        #if it's a variabe
        if isinstance(token, bool) or isinstance(token, float) or isinstance(token, int):
            opPush(token)
        else: 
            #if it's something we can define with a dict
            if  isinstance(token,str) and '/' in token: 
                    opPush(token)
            #if it's an array we mark it and push it all to the stack where we evaluate it then we pull it back out and reinsert as a reference
            elif isinstance(token,list):
                opPush('[')
                for i in token:
                    interpretSPS([i])
                res = opstack[opstack.index('[')+ 1:]
                opstack = opstack[0:opstack.index('[')]
                opPush(res)
            #if it's a dictionary then we are working with a code array, if we are pushing it in, we just emplace it, otherwise we interpret it
            elif isinstance(token,dict):
                if(static == True):
                    opPush(token)
                else:
                    interpretSPS(token,False)
            #we either have a function or an  variable at this point so we try to interpret it as either.
            else:
                action = function_dispatcher.get(token.lower(), None)
                if action is not None:
                    action()
                else:
                    temp_token = lookup(token)
                    if(temp_token != None):
                        if(isinstance(temp_token,dict)):
                            interpretSPS(temp_token)
                        else:
                            interpretSPS([temp_token])
                    else:
                           opPush(token)
