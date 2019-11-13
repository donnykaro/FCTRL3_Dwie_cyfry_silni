import sys

max_range = 1000000000
max_number_of_cases = 30

number_of_cases = int(input())
if number_of_cases < 1 or number_of_cases > max_number_of_cases:
    sys.exit(0)

user_numbers = []

for i in range(0, number_of_cases):
    counter = 2
    result = 1

    user_number = int(input())
    if user_number > max_range:
        sys.exit(0)

    for x in range(1, user_number):
        result *= counter
        counter += 1

    if len(str(result)) == 1:
        user_numbers.append(['0', str(result)[-1]])
        continue
    else:
        user_numbers.append([str(result)[-2], str(result)[-1]])
        continue

for strong in user_numbers:
    print(f'{strong[0]} {strong[1]}')
