# task1
n = int(input())

for i in range(1, n + 1):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")  

# task2
n = int(input())
num_str = str(n)
power = len(num_str)
total = 0
for digit in num_str:
    total += int(digit) ** power
print(total == n)

# task3
s = input()
result = ""
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1
result = result + s[-1] + str(count)
print(result)

# task4
text = input()
cleaned = text.lower().replace(" ", "")
print(cleaned == cleaned[::-1])

# task5
s = input()
k = int(input())
if len(s) == 0:
    print("")
else:
    k = k % len(s)
    shifted = s[-k:] + s[:-k]
    print(shifted)