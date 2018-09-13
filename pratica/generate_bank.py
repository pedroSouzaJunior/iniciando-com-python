from utils import cabecalho
from variaveis import cedulas
from file import open_file_bank, write_money_slips,carregar_informacoes_banco

def main():
    cabecalho()
    make_money_slips()

def make_money_slips():
    file = open_file_bank('w')
    write_money_slips(file)
    file.close()

main()