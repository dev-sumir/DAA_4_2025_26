count=0
max_depth=0

def complexRec(n, depth=1):
    global count, max_depth

    if depth>max_depth:
        max_depth = depth

    if n<=2:
        count+=1
        return

    p=n
    count+=1

    while p>0:
        count+=1
        temp=[0]*n
        count+=n
        for i in range(n):
            count += 1
            temp[i]=i^p
        p>>=1
        count+=1

    small=[0]*n
    count+=n
    for i in range(n):
        count+=1
        small[i]=i*i

    small.reverse()
    count+=n

    complexRec(n // 2, depth + 1)
    complexRec(n // 2, depth + 1)
    complexRec(n // 2, depth + 1)

complexRec(3)
print("Max recursion depth:", max_depth)
print("Total operations:", count)

# T(n) = 3T(n/2) + n log n --> complexRec(n // 2) is called 3 times and while loop run logn times and inside for loop runs for n times, so f(n)=nlogn
# a = 3, b = 2
# n^(log₂ 3) = n^1.585
# f(n) = n log n
# By Master Theorem,
# T(n) = Θ(n^(log₂ 3))