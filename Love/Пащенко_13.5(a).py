def twin(f_name):
    f = open(f_name)
    counter = 0
    for line in f:
        if int(line) % 2 == 0:
            counter += 1
    f.close()
    return counter


f_name = "file"
print(f"Кількість парних чисел серед компонентів:{twin(f_name)}")
