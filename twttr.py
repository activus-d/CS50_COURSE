"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""
def twttr():
    word = input("input any text...")
    new_word = ""
    vowels = {"a", "e", "i", "o", "u"}
    for i in range(len(word)):
        if word[i].lower() in vowels:
            pass
        else:
            new_word += word[i]
        
    print(new_word)

twttr()