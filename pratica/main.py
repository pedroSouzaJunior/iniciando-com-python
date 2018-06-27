
print("***************************************************************")
print("************* Caixa Eletrônico ********************************")
print("***************************************************************")

conta = input('Digite sua conta: ')
senha = input('Digite sua senha: ')

contas = {
    '0001-02':{
        'senha':'1234',
        'nome':'Pedro Souza',
        'valor':0
    },
    '0002-03' :{
        'senha':'5678',
        'nome':'Souza Pedro',
        'valor':0
    }
}


if conta in contas and senha == contas[conta]['senha']:
    print('Bem vindo ' + contas[conta]['nome'])
    print(contas[conta])
else:
    print('Conta ou Senha Invalida')