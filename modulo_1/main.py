# Comparación de Strings
text1 = "Hello Python"
text2 = "Hello Python"
print(text1 == text2)  # True

# Métodos de String
name = "Elmer de la paz"
print(name.upper())       # MAYÚSCULAS
print(name.lower())       # minúsculas
print(name.capitalize())  # Primera letra en mayúscula
print(name.title())       # Cada palabra con mayúscula

# Eliminar espacios
text_with_spaces = "    Hola Andre    "
print(text_with_spaces.strip())   # ambos lados
print(text_with_spaces.lstrip())  # solo izquierda
print(text_with_spaces.rstrip())  # solo derecha

# Reemplazo de texto
message = "Hello Java"
print(message.replace("Hello", "Hola"))  # Hola Java

# Convertir texto a lista
people = "Andres, Elmer , Manuel,isabel"
people_list = people.split(",")
print(people_list)
print(people_list[2])

# Convertir lista a texto
names = ["Andres", "Elmer", "Manuel", "isabel"]
print(" ".join(names))

# Función para saludar
def greet(message):
    print(message)
    print(f"Hola {message}")

# Punto de entrada principal
if __name__ == "__main__":
    print("Hola como esta")
    greet("Im a boy")


file = "Hola como estas Isabel"
buscado = file.find("como")
print(buscado)
print(file.index("Isabel"))
primero =file.startswith("como")
ultimo = file.endswith("como")
print(ultimo)
print(primero)

numeros = "123456"
decimal = "123.456"
textoooo = "Python"
mix = "Python3"

print("-----------------")
print(numeros.isnumeric())
print(numeros.isdigit())
print(decimal.isdecimal())
print(mix.isalnum())
print(mix.isalpha())
print(textoooo.isalpha())

espacio = " ".isspace()
print(espacio)
print("ELMER".isupper())
cip ="49955".zfill(8)
print(cip)


fraseCompleta = "El amigo como esta en la vida"
print(fraseCompleta)
print(fraseCompleta[0::2])
print(fraseCompleta[7:])
print(fraseCompleta[:6])
print(fraseCompleta[::-1])

nuevoTexto = "Python"

precio = 60

valor = f"el precio {"CARO" if precio>50 else "BARATO"}"
print(valor)

valores = 5
print(f"MI valores es de {valores:.2f}")

madre ="Serfaina" 
edades=15

mensajes = "madre {} tiene edad {}".format(madre,edades)
print(mensajes)