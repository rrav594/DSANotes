https://www.codingninjas.com/studio/problems/missing-and-repeating-numbers_6828164?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Modifying the array
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    repeat, miss = 0, 0
    n = len(a)
    for i in range(n):
        index = abs(a[i])-1
        if a[index] < 0:
            repeat = index+1
            continue
        a[index] *= -1
    for i in range(n):
        if a[i] > 0:
            miss = i+1
    return [repeat, miss]

# Xor method
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    xor = 0
    n = len(a)
    for i in range(n):
        xor ^= a[i]
        xor ^= i+1
    setbit = xor&(-xor)
    zero, one = 0, 0
    for i in range(n):
        if a[i] & setbit:
            one ^= a[i]
        else:
            zero ^= a[i]
    for i in range(1, n+1):
        if i & setbit:
            one ^= i
        else:
            zero ^= i
    count = 0
    for i in range(n):
        if a[i] == zero:
            count += 1
    return [zero, one] if count == 2 else [one, zero]


# Summation method
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a)
    sum_ = (n*(n+1))//2
    total = 0
    for i in range(n):
        total += a[i]
    sum_squ = 0
    total_squ = 0
    for i in range(n):
        total_squ += a[i]*a[i]
    for i in range(1, n+1):
        sum_squ += i*i
    diff = total-sum_
    diff_squ = total_squ-sum_squ
    ele_sum = diff_squ//diff
    repeat = (diff+ele_sum)//2
    miss = ele_sum-repeat
    return [repeat, miss]


