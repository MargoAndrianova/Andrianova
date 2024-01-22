def duo(file):
    with open(file, "r") as myFile:
        cnt = 0
        lst = [float(el) for el in myFile.read().split()]
        for line in lst:
            if int(line) % 2 == 0:
                cnt += 1
        return cnt

def square_of_odd(file):
    with open(file, "r") as myFile:
        cnt = 0
        lst = [float(el) for el in myFile.read().split()]
        for line in lst:
            if (line**0.5)**2 == line:
                if line**0.5 % 2 == 1:
                    cnt += 1
        return cnt

def difference(file):
    with open(file, "r") as myFile:
        lst = [float(el) for el in myFile.read().split()]
        even = [num for num in lst if num % 2 == 0]
        odd = [num for num in lst if num % 2 != 0]
        res = max(even) - min(odd)
    return res

def long(file):
    with open(file, 'r') as myFile:
        longest_string = []
        string_now = []
        lst = [int(num) for num in myFile.read().split() if num.isdigit()]
        for line in lst:
            if not string_now or line >= string_now[-1]:
                string_now.append(line)
            else:
                if len(string_now) > len(longest_string):
                    longest_string = string_now
                string_now = [line]
            if len(string_now) > len(longest_string):
                longest_string = string_now
    return len(longest_string)


if __name__ == "__main__":
    double = duo("input.txt")
    square = square_of_odd("input.txt")
    diff = int(difference("input.txt"))
    longest = long("input.txt")
    print(f"Кількість парних: {double}")
    print(f"Кількість квадратів непарних: {square}")
    print(f"Різниця між найбільшим і найменшим: {diff}")
    print(f"Довжина найдовшої послідовності: {longest}")