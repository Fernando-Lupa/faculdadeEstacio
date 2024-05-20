saida = 'N'

def adicao(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    if n2 == 0:
        return 'Não foi possível realizar a divisão por 0'
    return n1/n2

def calculadora(n1,n2,op):
    op = op.lower()

    if op == 'adição' or op == '+':
        return adicao(n1,n2)
    elif op == 'subtração' or op == '-':
        return subtracao(n1,n2)
    elif op == 'divisão' or op == '/':
        return divisao(n1,n2)
    elif op == 'multiplicação' or op == '*':
        return multiplicacao(n1,n2)
    else:
        return 'Operação não encontrada'
    

while saida == 'N':

    N = int(input('Escolha o primeiro valor: '))

    n = int(input('Escolha o segundo valor: '))

    op = input('Digite a operação desejada: ')

    print(calculadora(N,n,op))

    saida = input('Deseja parar? ("S"/"N")')