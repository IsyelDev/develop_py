suma_lamda = lambda a,b : a+b
resta_lamda = lambda a,b : a-b
multiplicacion_lamda = lambda a,b : a*b
division_lamda = lambda a,b : a/b

print(suma_lamda(5,6))
print(resta_lamda(50,6))
print(multiplicacion_lamda(5,6))
print(division_lamda(5,6))

"""
lambda : argumentos : expresiones
doble : lambda x : x * 2:
   print(doble(4))

filter(funcion , iterable)
   """
numeros =[1,2,3,4,5,6,7,8]
filtrado = list(filter(lambda x: x%2==0, numeros))
print(filtrado)



numeros = [10, 15, 20, 25, 30, 35]
impares = list(filter(lambda x: x%2!=0,numeros))
print(impares)

palabras = ["gato", "elefante", "sol", "maravilla", "luz"]
letras = list(filter(lambda x : len(x) >5,palabras))
print(letras)

edades = [5, 12, 17, 18, 24, 32]
mayoresImpares = list(filter(lambda x : x>=18,edades))
print(mayoresImpares)

nombres = ["Ana", "Pedro", "Alberto", "María", "Andrés", "Luisa"]
letraA = list(filter(lambda x : x.startswith("A"),nombres))
print(letraA)

numeros = [3, 6, 9, 12, 15, 20, 21, 30]
multiplo3 = list(filter(lambda x : x%3==0 and x > 10,numeros))
print(multiplo3)


nombres = ["ana", "pedro", "maria"]
matuscula = list(map(lambda x:x.upper(),nombres))
print(matuscula)

palabras = ["sol", "maravilla", "luz", "elefante"]
ordenadas = sorted(palabras , key=lambda x: len(x))
print(ordenadas)


personas = [("Ana", 25), ("Pedro", 20), ("Luis", 30)]
ordenadasxdic = sorted(personas,key = lambda x : x [1])
print(ordenadasxdic)


evaluar = lambda x: "Aprobado" if x >= 60 else "Reprobado"
print(evaluar(75))

lista_estudiantes = [('Edward', 4.2),
                     ('Pepe', 2.5),
                     ('Maria', 3.1),
                     ('Carlos', 4.5)]

lista_ordenada = sorted(lista_estudiantes , key=lambda x: x[0] ,reverse=True)
print(lista_ordenada)

import random
nombres = ['Ana', 'Luis', 'Pedro', 'Carla']
aleatorio = random.choice(nombres)
print(aleatorio)

print(random.randint(10,15))
print(random.random()*10)
print(random.uniform(1.5,5.4))


cartas = ['A', 'K', 'Q', 'J']
random.shuffle(cartas)
print(cartas)

frutas = ['manzana', 'pera', 'uva', 'plátano']
seleccion = random.sample(frutas,2)
print(seleccion)

colores = ['rojo', 'azul', 'verde']
print(random.choices(colores, k=3))  # Puede repetir elementos
