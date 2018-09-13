import operacoes
import utils
from variaveis import cedulas
from file import carregar_informacoes_banco

def main():
    carregar_informacoes_banco()
    print(cedulas)
    utils.cabecalho()
    contaAutenticada = operacoes.autenticacao()

    if contaAutenticada:
        utils.clear()
        utils.cabecalho()
        opcao = operacoes.obter_opcao_digitada(contaAutenticada)
        operacoes.faca_operacao(opcao, contaAutenticada)
    else:
        print('Conta ou Senha Invalida')

while True:
    main()

    input('\nPressione <Enter> Para Continuar...')
    utils.clear()

    
