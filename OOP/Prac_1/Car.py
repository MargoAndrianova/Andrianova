class Auto:

    def __init__(self, mark, color, speed):
        self.mark = mark
        self.color = color
        self.speed = speed

    def go(self):
        print(f"{self.mark}: go ...")

    def drift(self):
        print(f"{self.mark}: drift on speed {self.speed} km/h")


if __name__ == "__main__":
    mercedes = Auto("Mercedes", "Red", 200)
    mazda = Auto("Mazda", "Blue", 120)
    mercedes.go()
    mazda.go()
    mercedes.drift()

