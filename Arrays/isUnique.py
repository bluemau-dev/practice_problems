s1 = "Daog"

def isUnique(s1: type(str)):
    
    # Iterate String
    myList = []
    for x in s1:
        if x in myList:
           print("Not Unique.")
           return
        else:
            myList.append(x)
    print("Is Unique.")

isUnique(s1)
