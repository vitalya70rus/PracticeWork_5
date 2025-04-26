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