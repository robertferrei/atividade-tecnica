#1 quantidade minima de turnos
#2 probabilidade de o seguir o caminho otimo
#3 total de caminhos diferentes sem looping


from math import ceil
from fractions import Fraction


#Calcula quantas formas diferentes existem de se chegar exatamente à última casa do tabuleiro
def count_optimal_paths(number,min_turns):
   
    if number < 0 or min_turns < 0:
        return 0
    
    elif number == 0 and min_turns == 0:
        return 1 ##chegou na ultima casa e acabou os turnos
    
    total = 0

    for move in (1, 2, 3):
        total += count_optimal_paths(number - move, min_turns - 1) ##reduz  numero de casas e o número de turnos restantes
    return total


def total_without_loop(n):
    if n == 0:
        return 1
    total = 0
    for move in (1, 2, 3):
        if n - move >= 0: ##entra somente se o movimento não ultrapassar o número de casas
            total += total_without_loop(n - move)
    return total

def analyze(number):
    if number < 3:
        raise ValueError("O tabuleiro deve ter pelo menos 3 casas.")
    
    min_turns = ceil(number/3)

    optimal_path = count_optimal_paths(number, min_turns) ##caminho otimo
    total_possible = 3 ** min_turns
    probability = Fraction(optimal_path, total_possible)

    return {
        "mínimo_de_turnos": min_turns,
        "probabilidade_como_fração": str(probability),
        "total_caminhos_sem_looping": total_without_loop(number)
    }


print(analyze(10))
