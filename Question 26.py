def is_perfect_square(n):
    return n == int(n*0.5)*2

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def perfect_squares_with_sum_less_than_10(lower, upper):
    result = []
    for number in range(lower, upper+1):
        if is_perfect_square(number) and sum_of_digits(number) < 10:
            result.append(number)
    return result

# Example usage:
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
result_list = perfect_squares_with_sum_less_than_10(lower, upper)
print("List of perfect squares with sum of digits less than 10:")
print(result_list)
