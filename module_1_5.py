immutable_var=1,2,"a",True
print("immutable tuple: ",immutable_var)
immutable_var1=([1,2],"a",True)
print(immutable_var1)
immutable_var1[0][0]=3
print(immutable_var1)
# кортеж является неизменяемой коллекцией, но внутри он может содержать изменяемые объекты
mutable_list=([1,2,"a",True])
print("Mutable list: ",mutable_list)
mutable_list[3]="modified"
print(mutable_list)