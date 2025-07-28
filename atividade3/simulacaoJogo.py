import random

def simulate_duel(house_numbers):
    players = {
        "Player 1": {"position": 0, "turns": 0},
        "Player 2": {"position": 0, "turns": 0}
    }

    order = ["Player 1", "Player 2"]
    winner = None

    while not winner:
        for name in order:
            player = players[name]
            pos = player["position"]
            remaining = house_numbers - pos

            draw = random.randint(1, 3)
            player["turns"] += 1

            print(f"{name} | Turno {player['turns']}: roleta sorteou {draw} | posição atual: {pos}")
            if draw > remaining:
                print('sorteio:',draw, 'faltam:',remaining)
                print(f"!!!! {name} ultrapassou o limite! Reiniciando do início...")

                player["position"] = draw - remaining
            else:
                player["position"] += draw

            print(f"{name} nova posição: {player['position']}\n")
            if player["position"] == house_numbers:
                winner = name
                break
    
    
    print(f"VENCEDOR: {winner} venceu o jogo em {players[winner]['turns']} turnos!")
    print(f"Player 1: {players['Player 1']['turns']} turns")
    print(f"Player 2: {players['Player 2']['turns']} turns")

simulate_duel(11)

    
    
