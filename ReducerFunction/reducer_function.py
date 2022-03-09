#Reducer_Function 
def reduce(num):
    
    list1=[]
    for number in range(0,num+1):
        list1.append(number)
    results=sum(list1)
    return results
    
print(reduce(5))
#Results 15