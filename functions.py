def call_numbers():
    for number in range(0,10):
        print(number)

def call_numbers_with_limit(limit):
    for number in range(limit):
        print(number)


def calculadora(x=10,y=5):
    return x + y


#parametros nomeados
print(calculadora(y=10,x=5))
print(calculadora(5))