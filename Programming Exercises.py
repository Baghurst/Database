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
#???

#h
print("")
print("*H*")
print("")
car = dict({
    
    'make': "Audi",
    'model': "A6",
    'year' : 2013,
    'kms' :52739,
    'colour': "Silver",
    'diesel': True,
    'reg':"131 CN 6439",
    })

print(car['make'])
print(car['model'])
print(car['kms'])
print(car['colour'][0])
print(car['diesel'])
print(car['reg'][4:5])
currentYear = 2018
print(car['kms'] / (currentYear - car['year']))

#2
print("")
print("*2*")
print("")
#a
print("a")
colours = dict({
    'white': "ban",
    'red': "dearg",
    'green': "gorm",
    'blue': "glas",
    'black': "dubh",
    })
colours['yellow'] = 'bui'
print("")
#c
print("c")
# Prompt the user to enter a colour
colour = input("Enter a colour: ")
# Look up the translation of colour
translation = colours{colour}
