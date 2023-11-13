# List of words
word_list = ["apple", "banana", "orange", "grape", "watermelon"]

# List comprehension to filter words with odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
