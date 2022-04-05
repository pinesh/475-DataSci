#!/usr/bin/env python
# coding: utf-8

# In[50]:


#QUESTION 1-----------------------------------------------------------------------------


# In[56]:


def sumSales(d): 
    newD = {}
    for _, sales in d.items():
        for day, num in sales.items():
            newD[day] = newD.setdefault(day, 0) + num
    return newD


# In[69]:


def sumSalesN(L):
    result = map(sumSales, L)
    return sumSales(mapHead(list(result)))


# In[70]:


def mapHead(l):
    newD = {}
    for i in range(len(l)):
         newD[i] = l[i]
    return newD


# In[ ]:


#QUESTION 2-----------------------------------------------------------------------------


# In[155]:


def searchDicts(L,k): 
    result = None
    for d in L:
        if k in d:
            result = d.get(k)
    return result


# In[153]:


def searchDicts2(L,k):
    return searchDicts2Recur(L,k,len(L)-1)


# In[149]:


def searchDicts2Recur(L,k,i):
    (n,d) = L[i]
    if k in d:
        return d.get(k)
    elif n == i:
        return None
    else:
        return searchDicts2Recur(L,k,n)


# In[ ]:


#QUESTION 3-----------------------------------------------------------------------------


# In[161]:


def busStops (buses,stop):
    return [i[0] for i in buses.items() if stop in i[1]]


# In[ ]:


#QUESTION 4-----------------------------------------------------------------------------


# In[202]:


def palindromes(S):
    s = list(set([i for i in getSubstrings(S) if i == i[::-1]])) # set required to get rid of duplicates.
    s.sort()
    return s


# In[199]:


def getSubstrings(s):
    return [s[i:j+1] for i in range(len(s)) for j in range(i+1,len(s))]


# In[ ]:


#QUESTION 5-----------------------------------------------------------------------------


# In[70]:


class interlaceIter():
    def __init__(self, a, b):
        self.iterables = merge(a,b)
    def __iter__(self):
        return self.iterables
    def __next__(self):
        return self.iterables.__next__()
# In[68]:

def merge(a, b):#Got help from web for the new ability of zip in python 3
        for i,j in zip(a,b):
            yield i
            yield j


def typeHistogram (it,n):
    d = {}
    for _ in range(n):
        try:
            s = type(it.__next__()).__name__
            d[s] = d.setdefault(s, 0) + 1
        except:
            return list(d.items())
    return list(d.items())

