
#Dictionaries in python {key:value}

people = {
    'name': 'Luiz',
    'age': '28'
}

print(people['name'])

#Useful methods

#len
print(len(people))

#keys
print(people.keys())

#Values
print(people.values())

#items
print(people.items())

#setdefault
people = {
    'name': 'Luiz',
    'age': '28',
    #'city': 'sp'
}
people.setdefault('city')
print(people['city'])

#copy
second_people = people.copy()
print('Second people print: ', second_people['name'])

#get

#pop
people.pop('name')

print("pop", people)

#popitem

people.popitem()

print("pop", people)

#update

people.update(
   { 'color':'blue'}
)

print(people)