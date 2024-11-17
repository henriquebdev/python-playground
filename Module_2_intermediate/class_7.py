#Unpack Dictionary


people = {
    'name': 'Louis',
    'state': 'single'
}

personal_data = {
    'age': 28,
    'height': 1.80
}

dictionary_merge = {**people, **personal_data}

print(dictionary_merge)