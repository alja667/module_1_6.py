my_dict={'Alex': 1985, 'Tim': 1995, 'Alisa': 2012}
print(my_dict)
print(my_dict['Tim'])
my_dict['Alja']=1992
print(my_dict)
my_dict.update({'Ivan': 1986, 'Nastja': 1987})
print(my_dict)
a=my_dict.pop('Ivan')
print(my_dict)
print(a)
my_set={1,3,5,'@',5,3,22,1,1,'@','dog','dog'}
print(my_set)
my_set.add(9)
my_set.add('mmix')
print(my_set)
my_set.discard("@")
print(my_set)