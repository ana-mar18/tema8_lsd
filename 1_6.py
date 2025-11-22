#1

import functools
def invers(dict):
    def f(acc,elem):
        acc[elem[1]]=elem[0]
        return acc
    return functools.reduce(f,dict.items(),{})
print(invers({"red": 1, "green": 2, "blue": 3}))

#2

def cursuri(student):
    def f(acc,elem):
        if(elem[1]!=[]):
            acc.add(elem[0])
        return acc
    return functools.reduce(f,student.items(),set())
st={
    "Ana": ["PA", "SD"],
    "Mihai": [],
    "Ioana": ["AL"]
}
print(cursuri(st))

#3

def mai_mare(str):
    def f(acc,elem):
        if(elem[1]>0):
            acc.add(elem[0])
        return acc
    return functools.reduce(f,str.items(),set())
print(mai_mare({"a": 3, "b": -1, "c": 0, "d": 8}))

#4

def patrat(lista):
    def f(acc,elem):
        acc[elem]=elem**2
        return acc
    return functools.reduce(f,lista,{})
print(patrat([1, 2, 3, 4]))

#5

def toate(dict):
    def f(acc,elem):
        key,lista=elem
        def g(multime,elem_lis):
            multime.add(elem_lis)
            return multime
        unire=acc|functools.reduce(g,lista,set())
        return unire
    return functools.reduce(f,dict.items(),set())
print(toate({"A": [1, 2], "B": [2, 3], "C": [3, 4]}))

#6

def nr_ap(lista):
    def f(acc,elem):
        if(elem[0] in acc):
            acc[elem[0]]=acc[elem[0]]+1
        else:
            acc[elem[0]]=1
        return acc
    return functools.reduce(f,lista,{})