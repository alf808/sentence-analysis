'''
Write a script that takes a sentence from the user and returns:

the number of lower case letters
the number of uppercase letters
the number of punctuations characters
the total number of characters
Use a dictionary to store the count of each of the above.

Note: ignore all spaces.
'''
temp = "I love to work with dictionaries!"
lower_count = 0
upper_count = 0
other_count = 0
trimmed_str = temp.replace(' ', '')

for character in trimmed_str:
    if character.isalpha() and character.islower():
        lower_count += 1
    elif character.isalpha() and character.isupper():
        upper_count += 1
    elif not character.isalpha():
        other_count += 1

print(f"Upper case: {upper_count}")
print(f"Lower case: {lower_count}")
print(f"Other: {other_count}")
print(f"Total chars: {len(trimmed_str)}")
