from itertools import permutations

def unique_permutations(num):
    # Generate all permutations
    perms = permutations(str(num))

    # Use a set to store unique permutations
    unique_perms = set()

    # Iterate over each permutation
    for perm in perms:
        # Join the digits of the permutation into a string
        perm_str = ''.join(perm)
        # Add the permutation to the set
        unique_perms.add(perm_str)

    # Print the unique permutations
    for perm in unique_perms:
        print(perm)

# Example usage:
num = int(input("Enter a number: "))
print("Unique permutations of", num, "are:")
unique_permutations(num)
