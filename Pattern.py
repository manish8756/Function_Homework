# n = 7
# for i in range (0,n):
#     for j in range(1, i+1):
#         print ('*', end="")
#     print()

# n = 7
# for i in range (n,0,-1):
#     for j in range(1, i+1):
#         print ('*', end="")
#     print()


# n = 7
# for i in range (n,0,-1):
#     for k in range (1,8-i):
#         print(' ', end="")
#     for j in range(1, i+1):
#         print ('*', end="")
#     print()


# n = 9
# for i in range (0,n):
#     for k in range(0, 9-i):
#         print(' ', end="")
#     for j in range(1, i+1):
#         print('*', end="")
#     print()
    

    

# n = int(input("Enter the number"))
# for i in range  (n):
#     for j in range (i+1):
#         print(j+1, end=" ")
#     print()    


# n = int(input("Enter the number"))
# for i in range  (n):
#     for j in range (i,-1,-1):
#         print(j+1, end=" ")
#     print()    


# n = int(input("Enter the number"))
# for i in range  (n):
#     for j in range (i+1):
#         print(i+1, end=" ")
#     print()        


# n = 5
# for i in range  (n):
#     for j in range (i+1):
#         print(n-i, end=" ")
#     print()  


# n = 5
# for i in range  (n):
#     for j in range (i+1):
#         print(n-j, end=" ")
#     print()    




# import string


# string = input("Enter the word: ")
# length = len(string)
# for i in range(length):
#     for j in range(i+1):
#         print(string[j], end="")
#     print()    


# n = 6
# for i in range  (n):
#     k = ord("A")+i
#     for j in range (i+1):
#         print(chr(k), end=" ")
#         k = k+1
#     print()  

n = 7
for i in range (0,n):
    for k in range (1,8-i):
        print(' ', end="")
    for j in range(1,(2*i-1)+1):
        print ('*', end="")
    print()

n = 7
for i in range (n,0,-1):
    for k in range (1,8-i):
        print(' ', end="")
    for j in range(1,(2*i-1)+1):
        print ('*', end="")
    print()
