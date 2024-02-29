def is_perfect_number(num):
    factors_sum = sum([i for i in range(1, num) if num % i == 0])
    return factors_sum == num

def find_factors(num, m):
    factors = [i for i in range(1, num+1) if num % i == 0]
    return factors[:m]

def print_perfect_numbers_with_factors(n, m):
    count = 0
    num = 1
    while count < n:
        if is_perfect_number(num):
            factors = find_factors(num, m)
            print(f"Perfect number {count+1}: {num}, Factors: {factors}")
            count += 1
        num += 1

# Example usage:
n = int(input("Enter the value of n (number of perfect numbers): "))
m = int(input("Enter the value of m (number of factors to display): "))
print(f"First {n} perfect numbers and their first {m} factors:")
print_perfect_numbers_with_factors(n, m)
