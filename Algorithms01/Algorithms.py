# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

from sqlalchemy import null
import math


def ListaEnteros(inicio, tamanio):
    '''
    Esta función devuelve una lista de números enteros
    Recibe dos argumentos:
        inicio: Numero entero donde inicia la lista
        tamanio: Cantidad de números enteros consecutivos
    Ej:
        ListaEnteros(10,5) debe retornar [10,11,12,13,14]
    '''
    lista = list(range(inicio,(inicio+tamanio)))
    #Tu código aca:
    return lista


def DividirDosNumeros(dividendo, divisor):
    '''
    Esta función devuelve dos valores, la parte entera de la división y su resto
    Recibe dos argumentos:
        dividendo: El número que va a ser dividido
        divisor: El número que va a dividir
    Ej:
        DividirDosNumeros(10,3) debe retornar 3, 1
    '''
    parte_entera = None
    resto = None
    #Tu código aca:
    parte_entera=dividendo/divisor
    resto=dividendo%divisor
    return math.floor(parte_entera), resto
print(DividirDosNumeros(13,3))

def NumeroCapicua(numero):
    '''
    En matemáticas, la palabra capicúa (del catalán cap i cua, 'cabeza y cola')​ 
    se refiere a cualquier número que se lee igual de izquierda a derecha que 
    de derecha a izquierda. Se denominan también números palíndromos.
    Esta función devuelve el valor booleano True si el número es capicúa, de lo contrario
    devuelve el valor booleano False 
    En caso de que el parámetro no sea de tipo entero, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se evaluará si es capicúa o no lo es.
    Ej:
        NumeroCapicua(787) debe retornar True
        NumeroCapicua(108) debe retornar False
    '''
    #Tu código aca:
    if type(numero) != int:
        return None
    numero=str(numero)
    list=[]
    for i in numero:
        list.append(i)
    list.reverse()
    string="".join(list)
    string=int(string)

    if int(numero) == string:
        return True
    else:
        return False

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if (numero < 1 or type(numero)!= int):
        return None
    else:
        return(math.factorial(numero))


def ProximoPrimo(actual_primo):
    '''
    Esta función devuelve el número primo siguiente al enviado como parámetro.
    En caso de que el parámetro no sea de tipo entero y/o no sea un número primo, debe retornar nulo.
    Recibe un argumento:
        actual_primo: Será el número primo a partir del cual debo buscar el siguiente
    Ej:
        ProximoPrimo(7) debe retornar 11
        ProximoPrimo(8) debe retornar nulo
    '''
    #Tu código aca:
    list3=[]
    for num in range(2,200):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            list3.append(num)
    if actual_primo in list3 and type(actual_primo)==int:
        print(list3)
        index_primo=list3.index(actual_primo)
        return list3[index_primo+1]
    else:
        return None

def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class ClaseAnimal:
        def __init__(self,especie,color):
            self.edad=0
            self.especie=especie
            self.color=color

        def CumplirAnios(self):
            self.edad=self.edad+1
            return self.edad

    return ClaseAnimal(especie,color)

def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    #Tu código aca:
    if type(numero) != int or numero <  0:
        return None
    else:
        dart = "{0:b}".format(numero)
        binario=int(dart)
        print(type(binario))

        return binario

'''
Algorithms
Sum of all numbers of a number, E.g 3, 3+2+1 = 6
'''
number=3
acc=0
i=0
flag=True
while flag:
    if i < number:
        i=i+1
        print(i)
        acc=acc+i
    else:
        flag=False
print(acc)

'''
Algorithms
Pyramid of Numbers
'''

#With Numbers
num=1 
for i in range(0,5):
    for j in range(0,i+1):
        print(num, end=" ")
        num=num+1
    print("")

#With Asterisks
num=1 
for i in range(0,5):
    for j in range(0,i+1):
        print("*", end=" ")
        num=num+1
    print("")

#Mutual numbers Algorithm
friends1=[1,2,3,4,5]
friends2=[3,4,5,6,7]
mutual=[]

for x in friends1:
    for y in friends2:
        if x == y:
            mutual.append(x)
print(mutual)

#Print elements of a list in the same line
list99=[1,2,3,4,5,6,7,8,9]
for elem in list99:
    if elem == list99[-1]:
        print(elem)
    else:
        #end="" parameter allow us to change the next line predefined within the print() function.
        print(elem, end=", ") 

#Removes repeated Keys from two dictionaries and returns a list with Unique keys from both Dictionaries.
def inetrsection(obj1,obj2):
    list1=[]
    list2=[]
    for key in obj1:
        list1.append(key)
    for key in obj2:
        list2.append(key)
    z=list(set(list1+list2))
    for x in list1:
        for y in list2:
            if x==y:
                print(x,y)
                z.remove(x)
    return print(z)


inetrsection({"prop1":1,"prop2":2,"prop4":4},{"prop1":1,"prop3":3,"prop2":2,"prop5":5})