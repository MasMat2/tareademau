# Preguntarle al usuario con cuantos palillos quiere jugar y quien jugara primero
n = int(input('Write the number of matches the game will have:\n'))
player = str(input('Would you like to go first? (Y/N)\n')).upper() == 'Y'

# Palillos que sobran
matches_left = n

while matches_left>0:
    print()

    # Turno del jugador
    if player:
        # Preguntar por el numero de palillos que se recogeran
        # Seguir preguntando hasta que se entre un valor correcto
        pick = n+1
        while (pick > matches_left) or (pick>3):
            pick = int(input('Cuantos palillos quieres recoger 1-3?\n'))

        # Recoger palillos
        matches_left = matches_left - pick
        print(f'Quedan {matches_left} palillos\n')

        # Revisar si el usuario recogio el ultimo palillo
        if matches_left == 0:
            print('Gana la computadora')

        player = not player

    # Turno de la computadora
    else:
        # Recoger 1, 2 o 3 palillos y verificar si se recogio hasta el k-esimo termino
        for i in range(1,4):
            try_matches = matches_left
            try_matches = try_matches - i

            # Revisar si se recogio el k-esimo termino
            while try_matches > 5:
                try_matches = try_matches - 4

            # Recoger el k-esimo termino, si no es posible recoger 3 palillos
            if (try_matches == 5) or (i==3) or (try_matches == 1):
                matches_left = matches_left - i
                print(f'La computadora recogio {i} palillos')
                print(f'Quedan {matches_left} palillos\n')
                # Revisar si la computadora recogio el ultimo palillos
                if matches_left < 0:
                    print('Ganaste')
                break
        player = not player
