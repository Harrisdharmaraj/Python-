def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def count_prime_and_composite():
    prime_count = 0
    composite_count = 0
    while True:
        try:
            num = int(input("Enter a number (enter 0 to quit): "))
            if num == 0:
                break
            if is_prime(num):
                prime_count += 1
            else:
                composite_count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("Total prime numbers entered:", prime_count)
    print("Total composite numbers entered:", composite_count)
# Function call
count_prime_and_composite()
