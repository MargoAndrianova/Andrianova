def create_text_file(sequence, file):
    with open(file, 'w') as file:
        index = 0
        while index < len(sequence):
            file.write(sequence[index:index + 40] + '\n')
            index += 40

sequence_of_chars = input()
file = 'output.txt'

create_text_file(sequence_of_chars, file)
