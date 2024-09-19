def odd (arr):
    res=0
    for i in arr:
        res=res^i
    return res
arr=[]
n=int(input("Enter total number of element: "))
for i in range (n):
    num = int (input("Enter element: "))
    arr.apend(num)
print("odd occuring", odd(arr)) 