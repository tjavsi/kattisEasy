n = int(input())
output = 0

for i in range(n):
    temp = input()
    output += int(temp[:-1]) ** int(temp[-1])

print(output)

