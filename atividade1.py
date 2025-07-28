def check(string):
   if string.startswith('B'):
    return print("String começa com a letra 'B'")
   elif string.endswith('A'):
    return print("String começa com a letra 'A'")

   return print("String não começa com 'B' nem termina com 'A'")


name = input("Digite seu nome:")
check(name)