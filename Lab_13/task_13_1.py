with open("input.txt") as myFile:
    # content = myFile.read()
    # print(content)
    long = ""
    cnt = 0
    for line in myFile:
        stripped = line.rstrip()
        print(stripped)
        if len(stripped) > 60:
            print(line)
        elif len(line.rstrip()) == 0:
            cnt += 1
        if len(long) < len(line):
            long = ""
            long += line
    print(cnt)
    print(long.strip())
