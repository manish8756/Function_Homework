#Printing numbers which is more than 50 using lambda function with filter function

lis = [12, 23, 34, 45, 56, 78, 89, 123]
value= (list(filter(lambda x: x>50,lis)))
print(value)