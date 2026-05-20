string = "taco cat"

def palindrome(x: type(String)):
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

palindrome(string)
