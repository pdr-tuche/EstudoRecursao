def fatorial(n):
  #caso base:
  if n <= 1:
    return 1
  #recursao esta aqui:
  else:
    return n * fatorial(n-1)

def exibir_fatorial(num):
  print(fatorial(num))

numero = int(input("digite um numero para saber seu fatorial: "))
exibir_fatorial(numero)
