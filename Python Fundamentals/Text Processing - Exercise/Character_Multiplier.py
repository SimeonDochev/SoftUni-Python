first_string, second_string = input().split()

total_sum = 0

if len(first_string) == len(second_string):
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])

elif len(first_string) > len(second_string):
    for i in range(len(second_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    for char in first_string[len(second_string):]:
        total_sum += ord(char)
else:
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    for char in second_string[len(first_string):]:
        total_sum += ord(char)

print(total_sum)
