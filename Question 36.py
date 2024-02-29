def common_divisors(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    gcd_value = gcd(a, b)
    count = 0
    for i in range(1, int(gcd_value ** 0.5) + 1):
        if gcd_value % i == 0:
            count += 1
            if i != gcd_value // i:
                count += 1
                return count
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
result = common_divisors(a, b)
print(f"The number of integers that can divide both {a} and {b} is: {result}")
