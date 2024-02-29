def count_characters():
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0

    while True:
        char = input("Enter any character: ")
        if char == '*':
            break
        elif char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1

    print("Total count of lower case:", lowercase_count)
    print("Total count of upper case:", uppercase_count)
    print("Total count of numbers:", number_count)

# Function call
count_characters()
