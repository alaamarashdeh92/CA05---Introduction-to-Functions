# Q 9
# ******
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
def fun2 ():
    list1=[]
    for i in range(lower,upper+1):
        if(i % 2 == 0):
            list1.append(i)  
    return list1

print(fun2()) 





