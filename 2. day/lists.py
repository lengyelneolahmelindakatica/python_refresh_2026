numbers = [45, 3, 112, 0, -12, 10000, 6, 99]

worlds = ["This", "now", "is", "another", "sentence"]

mixed = ["This", "is", "the", 3, -10, "mixed", True]

embedded_list = ["bogar", 34, [1, 2, 3]]

print("The numbers list length is"+ str(len(numbers)))
print(f'The text list lenght is: {len(numbers)}')
print(f"The mixed list lenght is {len(mixed)}")

print(type(numbers))
print(type(worlds))
print(type(mixed))
print(type(embedded_list))

print(embedded_list[3])
print(embedded_list[1][2])

#lists functions

sample_list = []

print(sample_list)

sample_list.append(15)
print(sample_list)

sample_list.append('hello')
print(sample_list)

numbers.sort()
print(numbers)

numbers.pop()
print(numbers)

paired_list = zip(numbers, worlds)
print(type(paired_list))
print(list(paired_list))

numbers.clear()
print(numbers)

