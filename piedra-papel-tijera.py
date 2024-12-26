nombre1 = input("Como se llamara el jugador1?: ")
nombre2 = input("Como se llamara el jugador2?: ")



turno = 1
while turno <= 5:
    print("\nTurno " + str(turno))

    jugador1 = input("Hola " + nombre1 + " que eliges? Piedra, Papel o Tijera: ").lower()
    jugador2 = input("Hola " + nombre2 + " que eliges? Piedra, Papel o Tijera: ").lower()

    condicion1 = (jugador1 == "piedra" and jugador2 == "tijera")
    condicion2 = (jugador1 == "papel" and jugador2 == "piedra")
    condicion3 = (jugador1 == "tijera" and jugador2 == "papel")

    if jugador1 == jugador2:
        print("Empate")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado:", nombre1)
    else:
        print ("Ha ganado:", nombre2)

    turno += 1
    