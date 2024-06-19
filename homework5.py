immutable_var = 1,5,7, True, 'Снуп Догг'
print(immutable_var)
immutable_var[2]=3 # кортежи являются неизменяемыми списками данных. данная строка выдаст ошибку при запуске
mutable_list = [1,5,7,True,'Снуп Догг']
mutable_list[4]='Snoop Dogg'
print(mutable_list)
