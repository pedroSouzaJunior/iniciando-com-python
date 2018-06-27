conta = input('Digite sua conta: ')
senha = input('Digite sua senha: ')

contas = {
    '0001-02':{
        'senha':'1234',
        'nome':'Pedro Souza',
        'valor':10
    },
    '0002-03' :{
        'senha':'5678',
        'nome':'Souza Pedro',
        'valor':20
    }
}

if conta in contas and senha == contas[conta]['senha']:
    print("***************************************************************")
    print("************* Caixa Eletrônico ********************************")
    print("***************************************************************")
    print("1- saldo")
    opcao = input("escolha opcao: ")
    if opcao == '1':
        print('Bem vindo ' + contas[conta]['nome'])
        print('Seu saldo eh %s' % contas[conta]['valor'])
else:
    print('Conta ou Senha Invalida')