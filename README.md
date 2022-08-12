# EstudoRecursao
📚 Minha visão sobre a técnica de recursividade na progamação

### Minha Definição:

Uma função recursiva é uma função que chama a si própia 🤝

### tipos de recursividade:
A função recursiva pode se auto chamar dentro do própio escopo. Esse tipo de método é chamado de **Recursividade direta**.
utilizando o exemplo de calculo de fatorial, é possivel ver a recursividade direta na seguinte função:

~~~Python
  def fatorial(n):
    if n <= 1:
      return 1
    else:
      return n * fatorial(n-1)
~~~
Note que na estrutura de condição `else` da função `fatorial` é passada a própia função. [Clique aqui para entender este funcionamento](#como-funciona)

O outro tipo de função recursiva é a **recursividade indireta**, onde, a função recursiva é chamada a partir de outra função. Exemplo:
~~~Python
def exibir_fatorial(num):
  print(fatorial(num))
~~~
A função `exibir_fatorial` exibe na tela o resultado da função recursiva `fatorial`.

### Como Funciona?

