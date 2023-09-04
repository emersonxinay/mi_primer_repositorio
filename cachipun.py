# logica de cachipun 
import random as r 

def cachipun(jugador):
    # validar los datos 
    if jugador == "piedra" or jugador == "papel"  :
        print("Jugaste correctamente ")
        # jugada del computador 
        pc = r.choice(["piedra", "papel"])
        # mostrar las dos jugadas
        print(f"humano: {jugador}, computador:   ") 
        # todas las opciones para que gane 
        if ((jugador == "piedra" and pc == "tijera" )or (jugador == "papel" and pc == "piedra" ) or () ):
            print("Ganaste")
        # todas las opciones para empatar
        elif pc == jugador:
            print("Empataste")
        # todas las opciones para perder
        else:
            print("Perdiste 😒 ")

    else:
        print("Solo piedra, papel o tijera ")

# bloques de prueba 
if __name__ == "__main__":
    # datos de entrada 
    humano = input("ingrese piedra, papel o tijera: ")
    # invocando a la función
    cachipun(humano)