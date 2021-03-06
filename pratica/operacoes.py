from variaveis import cedulas, contas

def faca_operacao(opcao, contaAutenticada):
    if opcao == '1':
        mostrar_saldo(contaAutenticada)
    elif opcao == '10' and contas[contaAutenticada]['admin']:
        inserir_cedulas()
    elif opcao == '2':
        saque()


def autenticacao():
    conta = input('Digite sua conta: ')
    senha = input('Digite sua senha: ')

    if conta in contas and senha == contas[conta]['senha']:
        return conta
    else:
        return False


def mostrar_saldo(contaAutenticada):
    print('Seu saldo eh %s' % contas[contaAutenticada]['valor'])


def inserir_cedulas():
    valor_digitado = input("digite a qnt de cedulas: ")
    cedula_dinheiro = input("digite a cedula a ser incluida: ")
    cedulas[cedula_dinheiro] +=  int(valor_digitado)
    print(cedulas)


def saque():
    valor_saque = input("digite o valor a ser sacado: ")
    cedulas_usuario = {}
    saque = int(valor_saque)
    
    if saque // 100 > 0 and saque // 100 <= cedulas['100']:
        cedulas_usuario['100'] = saque // 100
        saque -= saque // 100 * 100

    if saque // 50 > 0 and saque // 50 <= cedulas['50']:
        cedulas_usuario['50'] = saque // 50
        saque -= saque // 50 * 50
    
    if saque // 20 > 0 and saque // 20 <= cedulas['20']:
        cedulas_usuario['20'] = saque // 20
        saque -= saque // 20 * 20

    if saque != 0:
        print("o caixa nao tem cedulas disponiveis para este valor")
    else:
        for cedula in cedulas_usuario:
            cedulas[cedula] -= cedulas_usuario[cedula]
        print("pegue as notas")
        print(cedulas_usuario)


def obter_opcao_digitada(contaAutenticada):
    print('Bem vindo ' + contas[contaAutenticada]['nome'])
    print("1- saldo")
    print("2- saque")
    if contas[contaAutenticada]['admin']:
        print("10- incluir cedula")
    return input("escolha opcao: ")


