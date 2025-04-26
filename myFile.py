# задание 1
N = 5
sequence = list(range(1, N + 1))

sum = 0
for num in sequence:
    sum += num

print(sum)

# задание 2
def sum_and_multiplie_with_arr(numbers, sum, highest_num, minimal_num, multiplie):
    for num in numbers:
        if num > 0:
            sum += num
    print("Сумма положительных элементов:", sum)

    for num in numbers:
        if num > highest_num:
            highest_num = num
    number_of_highest_num = numbers.index(highest_num)

    for num in numbers:
        if num < minimal_num:
            minimal_num = num
    number_of_minimal_num = numbers.index(minimal_num)

    if number_of_minimal_num < number_of_highest_num:
        between_numbers = numbers[number_of_minimal_num + 1:number_of_highest_num]
        for num in between_numbers:
            multiplie *= num
        print(f"Произведение чисел {between_numbers}: {multiplie}")

    elif number_of_minimal_num > number_of_highest_num:
        between_numbers = numbers[number_of_highest_num + 1:number_of_minimal_num]
        for num in between_numbers:
            multiplie *= num
        print(f"Произведение чисел {between_numbers}: {multiplie}")

numbers = [5, 6, 8, -2, 3, 1, -5]
print("Набор чисел:", numbers)

sum = 0
highest_num = numbers[0]
minimal_num = numbers[0]
multiplie = 1

sum_and_multiplie_with_arr(numbers, sum, highest_num, minimal_num, multiplie)

# задание 3
import random

random_list = [random.randint(1,10) for i in range(5)]
print("Исходный список:", random_list)

temp = 0

for i in range(0, len(random_list)):
    for j in range(i+1, len(random_list)):
        if random_list[i] > random_list[j]:
            temp = random_list[i]
            random_list[i] = random_list[j]
            random_list[j] = temp

print("В упорядоченном виде:", random_list)

# задание 4
str = "abcdef"

if str[:3] == 'abc':
    str = 'www' + str[3:]
    print(str)
else:
    str += 'zzz'
    print(str)

# задание 5
def solve_the_example(a, b):
    result = (a + 4 * b) * (a - 3 * b) + (2 * a)  # 10 * (-4) + 4
    print(result)

a = 2
b = 2
solve_the_example(a, b)

# задание 6
numbers = [1, -5, 0, 3, -4]
print(numbers)

new_numbers = []
for num in numbers:
    num *= -1
    new_numbers.append(num)

print(new_numbers)

# задание 7
a1 = -3
a2 = 2

R = 5

if -R <= a1 <= R and -R <= a2 <= R:
    print("точка принадлежит кругу")
else:
    print("точка не принадлежит кругу")