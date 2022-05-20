# sum of number using map function
def sum(n):
    s = 0
    for i in range (0, n+1):
       s = s+i
    return s

l1 = [2, 3, 4, 5, 6, 7, 8, 9]    
result = map(sum,l1)
print(list(result))






#factorial of number using map function

#creating function using def keyword
def fac(n):
    f = 1
    for i in range (1, n+1):
       f = f*i
    return f

l1 = [1, 2, 3, 4, 5,]    
result = map(fac,l1)
print(list(result))