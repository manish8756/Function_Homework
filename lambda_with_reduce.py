#Multiply of two numbers lambda function wit reduce function

import functools
lis = [2,3,4,]
mult=functools.reduce(lambda a,b: a*b,lis)
print(mult)