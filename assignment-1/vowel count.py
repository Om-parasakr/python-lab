text = input("enter a sentence:")
vowelcount = 0
for letter in text :
    if letter in "aeiouAEIOU":
        vowelcount = vowelcount + 1
print("number of vowels:",vowelcount)
