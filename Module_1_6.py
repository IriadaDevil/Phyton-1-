my_dict={'Susan':1999,'Max':1998,'Scott':2001,'Tony':1987}
print("Dictionary: ",my_dict)
print("Existing value: ",my_dict['Scott'])
print("Not existing value: ",my_dict.get('Aqua', 'Not exist'))
my_dict['Lux']=2003
my_dict.update({'Alex':1997,
                'Robert':2002})
a=my_dict.pop('Max')
print("Deleted value: ", a)
print("Modified dictionary: ",my_dict)

my_set={1,3,3,6.33,1,6.33,True,'cat','mouse','cat'}
print("My set: ",my_set)
my_set.discard('mouse')
my_set.add('rose')
my_set.add(13)
print("Updated set: ",my_set)