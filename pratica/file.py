import os
from variaveis import cedulas, contas
'''
print(BASE_PATH)
#file = open(BASE_PATH + '/_file_test.dat','a')
#file.writelines('aprendendo a escrever em arquivos\n')
#file.write('aprendendo a escrever em arquivos\n')
#file.writelines(['linha','\n','nova linha'])
#file.close()

file = open(BASE_PATH + '/_file_test.dat','r')
linha = file.readline()
while linha:
    print(linha)
    linha = file.readline()
file.close()
'''
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def open_file_bank(modo):
    return open(BASE_PATH + '/_bank_file.dat', modo)

#cedula=quantidade;
def write_money_slips(file):
    for cedula, quantidade in cedulas.items():
        file.write(cedula + '=' + str(quantidade) + ';')

def read_money_slips(file):
    linha = file.readline()
    while linha.find(';') != -1:
        posicao_ponto_virgula = linha.find(';')
        cedula_valor = linha[0:posicao_ponto_virgula]
        set_money_bill_value(cedula_valor)
        if posicao_ponto_virgula + 1 == len(linha):
            break
        else:
            linha = linha[posicao_ponto_virgula + 1 : len(linha)]

def set_money_bill_value(cedula_valor):
    posicao_igual = cedula_valor.find('=')
    cedula = cedula_valor[0:posicao_igual]
    count_cedula_valor = len(cedula_valor)
    quantidade = cedula_valor[posicao_igual + 1 : count_cedula_valor]
    cedulas[cedula] = int(quantidade)


def carregar_informacoes_banco():
    file = open_file_bank('r')