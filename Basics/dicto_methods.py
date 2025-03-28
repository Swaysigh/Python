info = {'name':'Swayam', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

info = {'name':'Swayam', 'age':19, 'eligible':True}
info.clear()
print(info)

info = {'name':'Swayam', 'age':19, 'eligible':True}
info.pop('eligible')   #pop that value which key is provided.
print(info)

info = {'name':'Swayam', 'age':19, 'eligible':True, 'DOB':2005}
info.popitem()    #removes the last key value pair..
print(info)

info = {'name':'Swayam', 'age':19, 'eligible':True, 'DOB':2005}
del info['age']  #removes the item
print(info)

info = {'name':'Swayam', 'age':19, 'eligible':True, 'DOB':2005}
del info           #removes the whole dictonary as key is not provided..
print(info)
