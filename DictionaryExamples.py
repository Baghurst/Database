counts={} # create a dictionary
counts2 = dict({}) #create a dictionary
counts3 = dict()
print(counts)
print(counts2)
#to add a key value pair
counts['games'] = 24
print(counts)
counts['players'] = 200
print(counts)
#To ding the number of items in a dictionary
print(len(counts))
#To check if a kay is in a dictionary
if 'players' in counts: #Boolean check
    print('players found')
if 'managers' not in counts: #returns true or false
    print ('managers not found')
#To print a value
print(counts['games']) # returns games value - error
print(counts)
print(counts.get('games')) # returns games value - re
print(counts)
print(counts.pop('games')) #Returns games value - rem
print(counts)

for key in counts.keys():
    print(key)
for key in counts:#will print the keys in the diction
    print(key)
for values in counts.values():#will print the values
    print(values)
for key,value in counts.items(): #will return key-val
    print(f'{key} -- {value}')
