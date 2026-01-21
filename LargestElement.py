#  Largest Element in array
a = int(input("Enter a Size: "))
arr = list(map(int,input("Enter a array size: ").split()))
first_ele = arr[0]
for i in range(1 , a):
    if(arr[i] > first_ele):
        first_ele = arr[i]
print(f"Largest Element in array is: {first_ele}")


# Second Largest Element in array
a = int(input("Enter a Size: "))
arr = list(map(int,input("Enter a array size: ").split()))
result = []
for i in range(a):
    for j in range(i + 1, a):
        if arr[i] > arr[j]:
            temp = arr[i]                  #sorting array
            arr[i] = arr[j]
            arr[j] = temp 
print(arr[-2])



    