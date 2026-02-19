lastname = input("Please, say your last name: \n")
firstname = input("Please, say your first name: \n")
age = input("Please, say your age: \n")

# Concatenate
fullname = lastname + " " + firstname

datas = " Your name is " + fullname + ", your age is " + str(age)
print(datas, end=".")

print(datas, sep="\n")
print("apple", "banana", "orange", sep="\n")
