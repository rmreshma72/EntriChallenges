
n = int(input())
A = input().split()
a = []
b = []
for i in A:
    a.append(int(i))

for i in a:
    if i < 10:
        b.append(i)
        continue
    while i >= 10:
        sum = 0
        while i > 0:
            sum = sum + (i % 10)
            i = i // 10
        if sum < 10:
            b.append(sum)
            break
        else:
            i = sum
print (b)
    
