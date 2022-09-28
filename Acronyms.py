# Ask for phrase

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
Acronyms = " "
for i in text:
    Acronyms = Acronyms+str(i[0]).upper()
print(Acronyms)

# Output:
# Enter a Phrase: I Don't Know
# IDK
