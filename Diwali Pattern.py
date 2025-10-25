#Rendering all the required characters using no libs, just pure python
#Created a dictionary to store all the characters
patterns = {
    "A": [
        "  *  ",
        " * * ",
        "*****",
        "*   *",
        "*   *"
    ],
    "D": [
        "**** ",
        "*   *",
        "*   *",
        "*   *",
        "**** "
    ],
    "F": [
        "*****",
        "*    ",
        "**** ",
        "*    ",
        "*    "
    ],
    "G": [
        " ****",
        "*    ",
        "* ***",
        "*   *",
        " ****"
    ],
    "H": [
        "*   *",
        "*   *",
        "*****",
        "*   *",
        "*   *"
    ],
    "I": [
        "*****",
        "  *  ",
        "  *  ",
        "  *  ",
        "*****"
    ],
    "L": [
        "*    ",
        "*    ",
        "*    ",
        "*    ",
        "*****"
    ],
    "P": [
        "**** ",
        "*   *",
        "**** ",
        "*    ",
        "*    "
    ],
    "V": [
        "*   *",
        "*   *",
        "*   *",
        " * * ",
        "  *  "
    ],
    "Y": [
        "*   *",
        " * * ",
        "  *  ",
        "  *  ",
        "  *  "
    ],
    " ": [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ],
    "W":[
        "*   *",
        "*   *",
        "*   *",
        "* * *",
        "*   *"
    ]
}
#Making the fucntion to use the keys and values in order to print the pattern
def pattern(text):
    #Making characters uppercase to effectively print (Didn't want to make ASCII patterns for lowercase chars too 😭)
    text = text.upper()
    #Range is taken 5 because every character has length and breadth of 5
    for r in range(5):
        line = ""
        for ch in text:
            part = patterns.get(ch)[r]
            #Double spacing because emojis take 2 space
            line += part.replace("*", "⭐").replace(" ", "  ") + "   "
        print(line)
    print()

pattern("  HAPPY")
pattern("  DIWALI")
pattern("  GFG")
