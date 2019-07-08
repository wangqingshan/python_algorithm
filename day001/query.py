import os

def query_method(num,item):
    low=0
    high=(len(item)-1)

    while(low<high):
        mid=int((low+high)/2)
        guess=item[mid]
        if guess==num:
            return guess
        elif guess<num:
            low=mid+1
        else:
            high=mid-1
    return None

array=[1,2,3,4,5,6,7,8,9]
print(query_method(12,array))
print(query_method(2,array))