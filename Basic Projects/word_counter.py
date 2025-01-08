def word_count(text):
    words = text.split()
    return len(words)

text = input("Enter text: ")
print(f"Word count: {word_count(text)}")
