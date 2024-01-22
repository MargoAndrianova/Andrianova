def count_squares_of_odd_numbers(f_name):
    with open(f_name, 'r') as file:
        numbers = [int(num) for num in file.read().split() if num.isdigit()]
        squares_of_odd = sum(1 for num in numbers if num % 2 != 0 and int(num ** 0.5) ** 2 == num)
        return squares_of_odd



f_name = "file"
print(f"Кількость квадратів непарних чисел серед компонентів:{count_squares_of_odd_numbers(f_name)}")