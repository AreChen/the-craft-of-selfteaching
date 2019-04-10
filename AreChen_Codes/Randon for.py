def is_JIOU(x):
    for i in range(2,3):
        if x % 2 == 0:
            print(x, '偶数')
        else:
            print(x, '奇数')
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if (n % i) == 0:
            return False
        else:
            return True
for i in range(10,50):
    if is_JIOU(i):
        print(is_JIOU(i))
    if is_prime(i):
        print(i)