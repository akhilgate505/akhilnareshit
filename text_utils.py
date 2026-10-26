# Program 3: String operations
# All data and operations are inside this file.

sentence = "python is easy to learn"
word = "python"

print("TEXT OPERATIONS")
print("Original sentence:", sentence)
print("Uppercase:", sentence.upper())
print("Title case:", sentence.title())
print("Word count:", len(sentence.split()))
print("Reversed word:", word[::-1])
print("Characters as a list:", list(word))
print("Words as a list:", sentence.split())
