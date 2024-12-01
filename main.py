immutable_var = tuple_=1,2,'Alli',True
print(immutable_var)
#immutable_var [0]=1 Ошибка. Составные части кортежа не меняются.
mutable_list = [1,2,3,4]
print(mutable_list)
mutable_list.append ('пять')
print(mutable_list)
mutable_list.extend ('5' '6')
print(mutable_list)
mutable_list.remove('пять')
print(mutable_list)
mutable_list[1]=0
print(mutable_list)
