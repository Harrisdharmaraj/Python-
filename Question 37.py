def are_isomorphic(s, t):
    if len(s) != len(t):
        return False

    # Mapping of characters from s to t
    s_to_t = {}
    # Mapping of characters from t to s
    t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        # If s_to_t does not contain char_s and t_to_s does not contain char_t
        if char_s not in s_to_t and char_t not in t_to_s:
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        # If s_to_t does not contain char_s or t_to_s does not contain char_t
        elif char_s not in s_to_t or char_t not in t_to_s:
            return False
        # If the mappings are not consistent
        elif s_to_t[char_s] != char_t or t_to_s[char_t] != char_s:
            return False

    return True

# Input strings
s = input("Enter the first string: ")
t = input("Enter the second string: ")

# Check if the strings are isomorphic
if are_isomorphic(s, t):
    print(f"The strings '{s}' and '{t}' are isomorphic.")
else:
    print(f"The strings '{s}' and '{t}' are not isomorphic.")
