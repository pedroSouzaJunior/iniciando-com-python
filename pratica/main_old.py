import os

contas = {
    '0001-02':{
        'senha':'1234',
        'nome':'Pedro Souza',
        'valor':10,
        'admin':False
    },
    '0002-03' :{
        'senha':'5678',
        'nome':'Souza Pedro',
        'valor':20,
        'admin':False
    },
    '1111-11' :{
        'senha':'123456',
        'nome':'ADMIN',
        'valor':1000,
        'admin':True
    }
}

cedulas = {
    '20':5,
    '50':5,
    '100':5
}

while True:
    print("***************************************************************")
    print("************* Caixa Eletrônico ********************************")
    print("***************************************************************")
    conta = input('Digite sua conta: ')
    senha = input('Digite sua senha: ')

    if conta in contas and senha == contas[conta]['senha']:
        print('Bem vindo ' + contas[conta]['nome'])
        print("1- saldo")
        print("2- saque")
        if contas[conta]['admin']:
            print("10- incluir cedula")
        opcao = input("escolha opcao: ")
        if opcao == '1':
            print('Seu saldo eh %s' % contas[conta]['valor'])
        elif opcao == '10' and contas[conta]['admin']:
            valor_digitado = input("digite a qnt de cedulas: ")
            cedula_dinheiro = input("digite a cedula a ser incluida: ")
            cedulas[cedula_dinheiro] +=  int(valor_digitado)
            print(cedulas)
        elif opcao == '2':
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
    else:
        print('Conta ou Senha Invalida')
    
    input('\nPressione <Enter> Para Continuar...')
    #os.system('cls' if os.nome == 'nt' else 'clear')
    os.system('cls')
    os.system('clear')
