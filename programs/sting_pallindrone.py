# Python program to check whether a string is palindrome or not

def palidrome_string():
    word = input("Enter a word")
    reversed_word = word[::-1]

    if (word.lower() == reversed_word.lower()):
        print("it is palindrome")
    else:
        print("it in not palindrome")


palidrome_string()
