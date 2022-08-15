def fatorial(n):
    fatorial = 1
    i=n
    while(i>0):
        fatorial*=i
        i=i-1
    return fatorial


numero = int(input("digite um numero para saber seu fatorial: "))
print(fatorial(numero))
