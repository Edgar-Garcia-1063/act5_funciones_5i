print("manejo de emociones v1")
def hola_mundo():
    print("hola aqui estoy dentro de la funcion")
def mensa(msg):
    print (msg)
def EscribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"tu nombre completo es {Nombre} {Apellido}")
def suma2numeros(n1,n2):
    s=n1+n2
    return s
    print(f"la suma de {n1} + {n2} es {s}")
#llamando la funcion
hola_mundo()
mensa("hola WhatsAPP")#llama a mensa con un parametro
mensa("el profe me sorprendio enviando mensajes")#llama a mensa con un parametro
EscribeNC("Edgar","Garcia")
print("funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))