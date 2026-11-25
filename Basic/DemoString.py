first = "Hello"
second = "World"

result = first + " " + second
print(result)


text = "Prem"
print("First character:", text[0])
print("Last character:", text[-1])


text = "I am learning Python"
if "Python" in text:
    print("Word found")
else:
    print("Word not found")
     

text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)


text = "I am learning Python"
count = text.count(" ")
print("Total spaces:", count)


text = "i am learning python"
result = text.title()
print(result)


text = "   Hello Python   "
result = text.strip()
print("Original:", text)
print("After removing spaces:", result)


text = "Python is easy to learn"
if text.startswith("Python"):
    print("The string starts with Python")
else:
    print("The string does not start with Python")


text = "Hello Python"
position = text.find("P")
print("Character position:", position)


text = "Python"
reverse = ""

for ch in text:
    reverse = ch + reverse
print("Original string:", text)
print("Reversed string:", reverse)


text = "programming"
count = text.count("m")
print("Character m appears:", count, "times")


text = "12345"
if text.isdigit():
    print("String contains only digits")
else:
    print("String contains other characters")


text = "HELLO PYTHON"
if text.isupper():
    print("String is in uppercase")
else:
    print("String is not in uppercase")


text = "python programming"
result = text.capitalize()
print("Original string:", text)
print("Updated string:", result)


text = "Hello Python"
result = text.replace("o", "")
print("Original string:", text)
print("Updated string:", result)


text = "I love learning Python"
words = text.split()
print(words)


text = "I am learning Python"
if text.endswith("Python"):
    print("String ends with Python")
else:
    print("String does not end with Python")


text = "I am learning Python programming"
words = text.split()
print("Total number of words:", len(words))


text = "Hello Python"
result = text.swapcase()
print("Original string:", text)
print("Updated string:", result)


text = "Python"
result = text[1:]
print("Original string:", text)
print("Updated string:", result)


text = "Programming"
result = text[:-1]
print("Original string:", text)
print("Updated string:", result)


text = "banana"
letter = "a"
frequency = text.count(letter)
print("Letter:", letter)
print("Frequency:", frequency)


text = "Python"
for ch in text:
    print(ch)


sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total words:", len(words))