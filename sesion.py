import cachipun 

def login(usuario, password):
    if usuario == "emerson" and password == "123456":
        print("Igresaste correctamente")
        jugar= input("ingrese piedra, papel o tijera: ")
        cachipun.cachipun(jugar)

