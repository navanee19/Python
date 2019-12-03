def factorial(n,result):
    if (n==1):
        return result
    else:
        result = result*n
        return factorial(n-1,result)
start=1
print(factorial(3,start))


    
