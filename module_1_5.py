immutable_var = 1,2,'a','b','song'
print(immutable_var)
#immutable_var[0] =3# в данной команде есть ошибка, т.к. элемент не является списком
mutable_list = [1,2,'a','b','song']
mutable_list[0] =3
print(mutable_list)