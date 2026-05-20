string = "taco cat"

# First Method
def palindrome_one(x: type(str)):
    # Remove Whitespaces from String
    x = x.replace(" ", "")

    # Iterate Characters in String
    w = []
    for character in x:
        w.append(character)
    
    p = list(reversed(w))

    # Palindrome Condition
    if w == p:
        print("Palindrome.")
    else:
        print("Not a Palindrome.") 

def palindrome_two(x: type(str)):
    # Remove Whitespaces From String
    x = x.replace(" ", "")

    # Iterate Characters in String
    w = []
    for character in x:
        w.append(character)

    # Palindrome Condition
    if w == w[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

palindrome_one(string)
palindrome_two(string)