def return_position(number):
   if not isinstance(number, int) or number < 1:
    raise ValueError("A posição deve ser um número inteiro maior ou igual a 1.")
   
   first = 11
   value = first +(number - 1) * 7
   
   return value


try:
    number_position = int(input("Digite um número inteiro maior ou igual a 1: "))
    result = return_position(number_position)
    print(f"O valor na posição {number_position} é: {result}")
except ValueError as e:
    print(f"Erro: {e}")
