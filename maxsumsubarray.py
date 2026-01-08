# Maxsum Sub array    -2 1 -3 4 -1 2 1 -5 4          size:9
a = int(input("Enter a Size: "))
arr = list(map(int,input("Enter a Array: ").split()))
sub_arr = []
for i in range(a):
    sub_arr_sum = arr[i]
    for j in range(i+1 , a):
        sub_arr_sum += arr[j]
        sub_arr.append(sub_arr_sum)
print(max(sub_arr))
print(sub_arr)