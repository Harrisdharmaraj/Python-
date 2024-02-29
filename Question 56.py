def count_special_characters(statement):
    special_characters= "!@#$%^&*()_-=+[]{}\|:;',.<>?/"
    count=0
    for char in statement:
        if char in special_characters:
            count+=1

    return count
given_statement="modi Birthday @ spetember 17,#&amp;$% is the wishes code for him."
result=count_special_characters(given_statement)
print(f"the no.of special cahracters in the statement is:{result}")
