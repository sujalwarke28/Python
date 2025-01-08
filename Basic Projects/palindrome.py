def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ").lower()
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
