#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

options = ["piedra", "papel", "tijeras"]
player_score = 0
team_score = 0

while True:
    player_choice = input("Elige una opción (piedra, papel, tijeras): ").lower()
    if player_choice not in options:
        print("Opción no válida. Inténtalo de nuevo.")
        continue

    team_choice = random.choice(options)
    print(f"El equipo IA eligió {team_choice}")

    if player_choice == team_choice:
        print("Es un empate!")
    elif (player_choice == "piedra" and team_choice == "tijeras") or \
         (player_choice == "papel" and team_choice == "piedra") or \
         (player_choice == "tijeras" and team_choice == "papel"):
        print("Ganaste esta ronda!")
        player_score += 1
    else:
        print("El equipo gana esta ronda!")
        team_score += 1

    print(f"Puntuación: Jugador - {player_score}, Equipo - {team_score}")

    play_again = input("¿Quieres jugar otra vez? (si/no): ").lower()
    if play_again != "si":
        break
