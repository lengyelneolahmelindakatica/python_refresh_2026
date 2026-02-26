lastname = input("Please, say your last name: \n")
firstname = input("Please, say your first name: \n")
age = input("Please, say your age: \n")

# Concatenate
fullname = lastname + " " + firstname

datas = " Your name is " + fullname + ", your age is " + str(age)
print(datas, end=".")

print(datas, sep="\n")
print("apple", "banana", "orange", sep="\n")


text = "This is example text"

print(text[0])
print(text[18])

print(len(text))
print(text[len(text)-1])

print(text[-1])

print(text[7:12])
print(text[:7])
print(text[::2])

print(text[1::2])
print(text[2:10:3])

#string functions
print(text.upper())
print(text.lower())

other_text = "   This is other example text!        "
print(other_text.strip())

hello_world = "Hello World!"
print(hello_world.replace("l", "j"))
print(hello_world.replace("Hello", "Goodbye"))


print(text.split())
print(text.split(","))

#join method <string>.join(iterable)

print(hello_world.join("###"))
print("#".join(hello_world))

lists = ["This", "is", "a","new", "list"]
print("#".join(lists))

#contains, or inclusion

sentence = "This is a sentence."
print("This sentence is include the 'is' world", "is" in sentence)
