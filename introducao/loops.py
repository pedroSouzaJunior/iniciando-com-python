list = [1,2,3,4,5]

for number in list:
    print(number)

nomes = ["Pedro", "Souza","Junior"]

for nome in nomes:
    if not nome == "Pedro":
        print(nome)

numero = 5
while numero < 10:
    print(numero)
    numero += 1
    # if numero == 8:
    #     print('Break!!')
    #     break
else:
    print("chegou no limite do laço")