'''
The Python range() function generates a sequence of numbers, which is commonly used in for loops
to iterate over a specific set of values.
It can take one, two, or three arguments: range(stop), range(start, stop), or range(start, stop, step).
The sequence includes the start value (default 0 if omitted) and increments by the step value (default 1),
but excludes the stop value.

How range() Works in Loops
range(stop): Generates numbers from 0 up to but not including stop.

range(start, stop): Generates numbers from start up to but not including stop.

range(start, stop, step): Generates numbers from start to stop incrementing by step
'''


for i in range(6):
    print(i)
    print(f"Hi {i}")

print("----------XXX----------")

for i in range(2, 6):
    print(i)
print("----------XXX----------")

for i in range(2, 12, 3):
    print(i)
print("----------XXX----------")

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i + 1, fruits[i])

