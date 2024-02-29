def count_vowels_consonants(statement):
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vowels=sum(1 for char in statement if char in vowels)
    num_consonants=sum(1 for char in statement if char in consonants)
    return num_vowels,num_consonants
def find_maximum(count):
    max_count=max(count)
    max_index=count.index(max_count)
    if max_index==0:
        return "vowels"
    else:
        return "consonants"
statement=input("entre the given stemt:")
vowels_count, consonants_count=count_vowels_consonants(statement)
maximum_type=find_maximum([vowels_count,consonants_count])
print(f"no.of vowels:{vowels_count}")
print(f"no.of consonants:{consonants_count}")
print(f"the maximum is in:{maximum_type}")
print("it is a program")
