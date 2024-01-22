def new_file(string, file):
    with open(file, 'w') as file:
        index = 0
        while index < len(string):
            file.write(string[index:index + 40] + '\n')
            index += 40

character_string = input()
file = 'output.txt'

new_file(character_string, file)