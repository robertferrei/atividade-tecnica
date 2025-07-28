def check(string):
   if string.startswith('B') and string.endswith('a'):
      return print("String começa com a letra 'B' e termina com a letra 'a'")
   else:
      return False

name = input("Digite seu nome:")
check(name)