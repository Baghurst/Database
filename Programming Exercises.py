car = dict({
    'reg':"131 CN 6439",
    'make': "Audi",
    'model': "A6",
    'year' : 2013,
    'kms' :52739,
    'colour': "Silver",
    'diesel': True,
    })
#e
print(car['make'])
#print(car[model])
#print(car['miles'])
print(car['colour'][0])
#print(car['diesel'][0])
print(car['reg'][4:5])

#f
currentYear = 2018
print(car['kms']/(currentYear - car['year']))

#g
