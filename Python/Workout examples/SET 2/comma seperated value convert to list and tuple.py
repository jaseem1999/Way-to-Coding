string=input("comma seperated numbers : ")
list_ = string.split(',')
print(list_)
print(tuple(list_))
converted = list(map(int,list_))
print(converted)
