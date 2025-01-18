#Prompt the user for a string and build a dictionary that counts how many times each word appears.

# string = input("Enter a string: ")
# words = string.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print("Word count:", word_count)

text = input("Enter a string: ")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word count:", word_count)