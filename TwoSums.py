a = int(input("Enter a Size: "))
target = int(input("Enter a Target: "))
arr = list(map(int,input("Enter a Array: ").split()))
for i in range(0, a):
            for j in range(i + 1, a):
                if(arr[i] + arr[j] == target):
                    print([i , j])               #printing the indexes of the target value.
                    break
                