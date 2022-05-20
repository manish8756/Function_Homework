import functools
def fun(a, b):
    return a+b


lis = [1, 2, 3, 4, 5,6,9]
res = functools.reduce(fun,lis)
print(res)
