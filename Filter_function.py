#Finding prime number using filter function
def prime(n):
    for i in range (2,n//2+1):
        if n%i == 0:
            return False
    return True


lis= [23,12,34,45,56,78,67]    
value = filter(prime,lis) 
print(list(value))       