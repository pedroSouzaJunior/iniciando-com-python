cars = {}
cars['corola'] = "red"
cars['fit'] = "green"
cars['fonfon'] = "wite"

people = dict(Pedro='Eu', Dani='Danielli')


print(cars.keys())
print(cars.values())
print(people)

if 'Pedro' in people:
    print(people['Pedro'])

for key, value in cars.items():
    print(key + " = " + value)