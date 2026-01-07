# Longest common subsequence in tow strings
a = input("Enter a String A: ")
b = input("Enter a String B: ")
count = 0
result = ""
output = ""
for i in a:
    for j in b:
        if i in j:
            result = result + i
for char in result:
    if char not in output:
        count += 1
        output += char
print(count)
print(output)