# multiple var input assign
# not for a row of numbers
x, y, z, n = (int(input()) for _ in range(4))

# a string and a string list in a row
var1, *lis = input().split()

# limit input &  to list
i = int(input())
lis = list(map(str, input().strip().split()))[:i]  # to string list
lis = list(map(int, input().strip().split()))[:i]  # to int list
lis = list(map(int, input().strip().split()))  # no limit
lis = list(set(map(int, input().strip().split())))  # uniq list

# loop list
for x in lis:
    print(x)  # x = item
for i in range(len(lis)):
    print(i)  # i = index

# slice
s = "You are learning Python"
print(s[:])  # outputs "You are learning Python"
print(s[1:6])  # outputs "ou ar"
print(s[10:])  # outputs "arning Python"
print(s[:10])  # outputs "You are le"
