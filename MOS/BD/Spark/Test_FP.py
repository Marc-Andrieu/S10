print("Fonction map(…)")

print("Question 1")

def mkimpair(i):
    return 2*i+1

print("Question 2")

a = map(mkimpair, range(0, 10))
print(list(a))

def est_voyelle(c: str):
    return c in 'aeiouyAEIOUY'

def bool_to_int(b):
    return 1 if b else 0

def nb_voyelles(mot01):
    return sum(mot01)

mot = 'bonjour'
print(nb_voyelles(map(bool_to_int, map(est_voyelle, mot))))


# def nb_voyelles(s):
#     voyelles = 'aeiouyAEIOUY'
#     return sum(1 for c in s if c in voyelles)

print("Question 3")

def multiply(x):
    return(x*x)
def add(x):
    return(x+x)

funcs=[multiply, add]
for i in range(2,5):
    print(list(map(lambda x: x(i), funcs)))

print("Question 4")

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print(list(map(lambda x,y:   x+y,   a,b)))
print(list(map(lambda x,y,z: x+y-z, a,b,c)))

print("Fonction filter(…)")

print("Question 1")

print(list(filter(lambda x: x < 0, range(-5, 5))))

print("Question 2")

def est_pair(n):
    return n%2 == 0

print(list(filter(lambda x: x % 2 == 0, map(lambda x: x*x, range(1, 20)))))

print("Question 3")

print(list(filter(None, [1, 2, None, 4])))

print("Fonction reduce(…)")

from functools import reduce  # noqa: E402, F401
import numpy as np  # noqa: E402, F401

print("Question 1")

def factorielle(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(factorielle(5))

print("Question 2")

def moyenne(a, b):
    return 0.5*a+0.5*b

nombres = [2, 3, 4]
print(reduce(moyenne, nombres), ' != ', np.mean(nombres))

print("----")

def moyenne_poids(tuple1, tuple2):
    v1, p1 = tuple1
    v2, p2 = tuple2
    return ( (v1*p1+v2*p2) / (p1+p2), p1+p2)

nombres = [2, 3, 4]
print(reduce(moyenne_poids, zip(nombres, [1.0]*len(nombres))), ' == ', np.mean(nombres))

print("Combinaison de plusieurs fonctions")

print("Question 1")

def heure_vers_secondes(s: str) -> int:
    h, m, s = s.split(':')
    return 3600*int(h) + 60*int(m) + int(s)

print(heure_vers_secondes("8:19:22"))

print("Question 2")

from operator import add  # noqa: E402
people=[
    {'name':'Mary','height':160},
    {'name':'Isla','height':80},
    {'name':'Sam'}
]

heights=list(map(lambda x: x['height'], filter(lambda x: 'height' in x, people)))
print(reduce(add, heights)/len(heights))

print("Question 3")

def pdt(tupleab):
    return tupleab[0]*tupleab[1]

isbn10 = [0, 3, 8, 7, 7, 1, 6, 7, 5, 0]
print(list(enumerate(isbn10)))
print(list(map(pdt, enumerate(isbn10))))
print(reduce(add, map(pdt, enumerate(isbn10))) % 11)
# le reste de la division entière par 11 valant 0, le code est bien de type ISBN10

print("Question 4")

def poids13(tupleiv):
    i, v = tupleiv
    return v if i%2 == 0 else v*3

isbn13 = [9, 7, 8, 2, 8, 2, 2, 7, 0, 1, 6, 2, 4]
print(list(enumerate(isbn13)))
print(list(map(poids13, enumerate(isbn13))))
print(reduce(add, map(poids13, enumerate(isbn13))) % 10)
# le reste de la division entière par 10 valant 0, le code est bien de type ISBN13