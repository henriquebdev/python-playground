#Lambda Function

def sum(n1,n2):
    return n1+n2


print(sum(2,3))

#Format to lambda


sum1 = lambda a,b: sum(a,b+2)
    
print(sum1(4,2))