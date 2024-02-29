def count_sorted_vowel_strings(n: int) -> int:
    # Define the vowels
    vowels = "aeiou"

    # Initialize a count to keep track of valid strings
    count = 0

    # Helper function to generate strings recursively
    def generate_strings(curr_string, length):
        nonlocal count
        if length == 0:
            count += 1
            return
        for vowel in vowels:
            if not curr_string or curr_string[-1] <= vowel:
                generate_strings(curr_string + vowel, length - 1)

    # Start generating strings
    generate_strings("", n)
    return count

if _name_ == "_main_":
    n = int(input("Enter the length of strings (n): "))
    result = count_sorted_vowel_strings(n)
    print("The number of strings of length", n, "that consist only of vowels and are lexicographically sorted is:", result)

