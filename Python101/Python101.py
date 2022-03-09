#Hello World!
print("Hello World!")

#Store a message in a variable named messages
messages="Hello python World!"
print(messages)

#String methods

#First letter of each word Upper Case
print(messages.title())

#All letters Upper Case
print(messages.upper())

#All letter Lower Case
print(messages.lower())

#Add Whitespace
print("Hola mundo\n")
print("\nHola mundo")

#Add Tab
print("\tHola mundo")

#Stripping Whitespace
print(" HolaMundo")

left_space=" HolaMundo"
print(left_space.lstrip())

print("HolaMundo ")
rigth_space="HolaMundo "
print(rigth_space.rstrip())

both_sides_space=" Hola mundo "
print(both_sides_space)

print(both_sides_space.strip())  

#Single and doble quotes
print("Hello It's great to meet you")
print('Hello It"s great to meet you')

print(round(0.2+0.1,9))

#Concatenation, Strings and Integers.
print(f'Hola {23} como estas {54}')

#Lists
new_list=[1,2,3,4,5,6]
new_list.append(7)
new_list.insert(0,11)

#del, pop(), remove()
del new_list[0]

#pop() delete element by index Return the value
new_list.pop()
new_list.pop(0)

#remove method delete element by value, only removes the first occurrence.
new_list.remove(6)
print(new_list)

#sort() method sort elemets permanently
alphabet_list=["c","b","a"]
alphabet_list.sort()
print(alphabet_list)

alphabet_list.sort(reverse=True)
print(alphabet_list)

#sorted() function sort elements not permanently
sorted_list=["uno","cinco","diez","cinco"]
print(sorted(sorted_list))
print(sorted_list)
new_sorted=sorted(sorted_list)
print(new_sorted)

alphabet=[5,6,47,8,1,9]
for elem in sorted(alphabet):
    print(elem)

#reverse() Method reverse permanently the original order of a list 
prueba=[1,2,3,4,5,6,7]
prueba.reverse()

print(prueba)

#len() function.
prueba=[1,2,3,4,5,6,7]
print(len(prueba))

#list() Function Convert to a list class
li_1=list(range(1,11))
print(li_1)

#Dictionaries 
dict1={
    "nombre":"john",
    "apellido":"Algreen"
}

name="Pedro"
empty={}
empty[name]="Díaz"
print(empty)

#for bucle estructure
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }

for key, value in favorite_languages.items():
    print(key,value)

dict1={
    "nombre":"john",
    "apellido":"Algreen"
}
for key in dict1:
    print(dict1[key])

#set() function, Show the unique elements of an iterable class 
repeticiones=[1,1,2,3,4,4,5,5,6,6,6,7]
unique=set(repeticiones)
print(unique)

#Unpacking, assign variables to elements of an iterable class 
repeticiones=[1,1,2,3,4,4,5,5,6,6,6,7]
var1,var2,var3,_,_,_,_,_,_,_,_,_ = repeticiones
print(var1)

# max, min, sum functions
repeticiones=[1,1,2,3,4,4,5,5,6,6,6,7]
print(max(repeticiones))
print(min(repeticiones))
print(sum(repeticiones))

#List comprehensions, allow conditional construction of list literals using for and if clauses. 
square=[elem**2 for elem in range(10) if elem%2 == 0]
print(square)

#Continue statement, moves control to the loop continuation portion of the statement.
for elem in range(1,20):
    if elem == 5:
        continue
    print(elem)

#Accesing key-value elements of a Dictionary
alien_0 = {
    'color': 'green', 'points': 5
    }

claves=alien_0.items()
print(claves)
claves_nueva=list(claves)
print(claves_nueva[0])
print(type(claves_nueva[0]))
print(alien_0.values())


favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }

for name, languages in favorite_languages.items():
    print(name.title()+":")
    for language in languages:
        print("\t-"+language.title())

#Functions
def animals(nombre,tipo="Dog"):
    print(nombre)
    print(tipo)
animals("Gibson")
animals("Felix","Gato")

def arbritary_arguments(*par):
    print(par)
arbritary_arguments(1,2,3,4,5,6,7,8,9)

def arbritary_key_value(**par):
    print(par)
arbritary_key_value(uno="1",dos="2")

liista=["uno","dos","tres"]
def prueba_lista(list):
    new_value=list.pop(0)
    return new_value
prueba_lista(liista)

#Empty strings equal to false
print(bool("")==False)


#Classes
class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def bark(self):
        print(self.name+" Wooow")

    def bark(self):
        print(str(self.age)+" Years old")


dog1= Dog("Gibson",10)

#Sub Classes and inheritance
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Cat(Animal):
    def __init__(self,name,age,type):
        super().__init__(name,age)
        self.type=type

cat1=Cat("Missifu",2,"Perssian")


'''
__dict__ ADN vars()
'''
print(dog1.__dict__)
print(vars(dog1))

'''
SYS AND SYS.PATH
Sys is a built-in Python module that contains parameters specific to the system i.e. 
it contains variables and methods that interact with the interpreter and are also governed by it. 

sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter 
will search in for the required module. When a module(a module is a python file) is imported within a Python file, 
the interpreter first searches for the specified module among its built-in modules.
'''
import sys
print(sys.path)

#sys.path.append("Module to be appended in python interpreter this allow us to import modules outside of our working directory")

'''
dir() METHOD Allow Us to see variables, classes, functions etc in our namespace
'''
print(dir())
print(__name__)
print(__name__)
 
''' 
ERROR HANDLING, EXCEPTIONS

'''
#1 Just Catching One type of Exception(ZeroDivision or any)
#try:
    #Block of code to try
#except Exception(or any E.g TypeError, ZeroDivision):
        #print("Error message")

#2 Catching all exceptions but raising especific
#try:
    #Block of code to try
#except:
    #raise Exception("Error message")

#3 Raising an excpetion on any Block of code
#raise Excpetion("Error message") 
#E.g:
    # x = -1
    # if x < 0:
    # raise Exception("Sorry, no numbers below zero")

#Expression or statemnt to evalauate
try:
    a=2
    b=23
    c=a+b
#Type of excpetion and block of code to execute when the error occurrs
except TypeError:
    print("Can not concatenate int type and string")
#In case no error happens execute this code
else:
    print(c)
#Always execute this block of code
finally:
    print("Thanks")

''' 
ERROR HANDLING, RAISE KEYWORD
'''
#x="Hola"
#if not type(x) is int:
  #raise TypeError("Only integers are allowed")

''' 
FRAMEWORK UNITTEST, ERROR HANDLING
'''
# #import the module for testing cases

import unittest

def mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class CajaNegra(unittest.TestCase):

    #Always start the name of the test with "test" (test_mayor, test_menor) otherwise won't work.
    def test_mayor(self):
        edad=20

        resultado=mayor_de_edad(edad)

        self.assertEqual(resultado,True)
    
    def test_menor(self):
        age=17

        resultado=mayor_de_edad(age)

        self.assertEqual(resultado,False)

unittest.main(argv=[''], verbosity=2, exit=False)


'''
"->" The Arrow is a functionallity that allow us to specify the retrun value as a comment then 
we can acces it with the property __annotations__ E.g: raise_puebla.__annotations_
Supplying a function with an annotation about its return type

-------------------------

Supplying annotations about a function parameter
A function parameter is annotated with a colon (:) followed by the annotation.
def F(num: 'A number',
      txt: 'A text'   ='Hello World'):
'''
def raise_prueba(lista) -> 'regresa' :
    if (type(lista) != list):
        raise Exception("Not a list, please insert a valid input")
    else:
        pass
    print("Hello Wolrd")

raise_prueba([1,2,3,4])
print(raise_prueba.__annotations__)

#Creating .txt file and writting elements on it.
lineas_archivo=['Esto es un archivo de ejemplo','Probando','Gracias']
#open() function Creates de .txt file the 'w' allows us to Write on the file .txt
archivo=open('datos.txt','w')
for lineas in lineas_archivo:
    #The write() method allow us to write elements on the .txt file
    archivo.write(lineas+'\n')
#The close() method allow us to close the .txt file in order to stop Writting on the document
archivo.close() 
