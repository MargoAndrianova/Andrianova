def longest(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(num) for num in file.read().split() if num.isdigit()]

        longest_sequence = []
        current_sequence = []

        for num in numbers:
            if not current_sequence or num >= current_sequence[-1]:
                current_sequence.append(num)
            else:
                if len(current_sequence) > len(longest_sequence):
                    longest_sequence = current_sequence
                current_sequence = [num]

            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence

    return longest_sequence

file_name = "file"

print(f"Кількость компонентів у найдовшій зростаючій послідовності компонент файла:{len(longest(file_name))}")