from func import fibo, iseven

arr = [1, 2]

while arr[-1] < 4000000:
    arr.append(fibo(arr[-2], arr[-1]))


if arr[-1] > 400000:
    arr.remove(arr[-1])


a = [i for i in arr if iseven(i)]
a = sum(a)


print a
print a == 4613732
