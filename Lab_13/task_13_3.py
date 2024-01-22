def createDigitalTriangle(n):
    with open("out03.txt", "w") as f:
        for i in range(1, n+1):
            print(str(i) * i, file=f)

if __name__ == "__main__":
    createDigitalTriangle(9)