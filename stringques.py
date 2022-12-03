x = str(input("Enter a Phrase: "))
count = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in x:
    if i in vowels:
        count += 1
print(count)