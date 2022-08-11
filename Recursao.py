def fatorial(n):
  #caso base:
  if (n <= 1):
    return 1
  #recursao esta aqui:
  else:
    return n * fatorial(n-1)


numero = int(input("digite um numero para saber seu fatorial: "))
fatorial = fatorial(numero)
print(fatorial)