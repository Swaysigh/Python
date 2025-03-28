"""Dictionaries are ordered collection of data items. They store multiple items in a single variable.
 Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}."""

info = {'name':'Swayam', 'age':19, 'eligible':True}
print(info)

info = {'name':'Swayam', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

info = {'name':'Swayam', 'age':19, 'eligible':True}
print(info.values())

info = {'name':'Swayam', 'age':19, 'eligible':True}
print(info.keys())

info = {'name':'Swayam', 'age':19, 'eligible':True}
print(info.items())

for key,value in info.items():
    print(f"the value of {key} is {value}") #here fstring and for loop is used to access info.items().

