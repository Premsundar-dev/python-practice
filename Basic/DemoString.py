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