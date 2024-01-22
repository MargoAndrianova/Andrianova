def getSum(file):
    with open(file, "r") as myFile:
        # for line in myFile:
        #     print(line.rstrip())
        lst = [float(el) for el in myFile.read().split()]
        # print(lst)
        return sum(lst)

def getMinus(file):
    cnt = 0
    with open(file, "r") as myFile:
        # for line in myFile:
        #     print(line.rstrip())
        lst = [float(el) for el in myFile.read().split()]
        # print(lst)
        for i in lst:
            if i < 0:
                cnt += 1
    return cnt

def MinMax(file):
    res = 0
    with open(file, "r") as myFile:
        # for line in myFile:
        #     print(line.rstrip())
        lst = [float(el) for el in myFile.read().split()]
        # print(lst)
        res += max(lst)
        res += min(lst)
    return res

def Difference(file):
    res = 0
    with open(file, "r") as myFile:
        # for line in myFile:
        #     print(line.rstrip())
        lst = [float(el) for el in myFile.read().split()]
        # print(lst)
        res += lst[0]
        res += lst[len(lst)-1]
    return abs(res)

if __name__ == "__main__":
    suma = getSum("input02.txt")
    cnt = getMinus("input02.txt")
    res = MinMax("input02.txt")
    difference = Difference("input02.txt")
    print(suma)
    print(cnt)
    print(res)
    print(difference)