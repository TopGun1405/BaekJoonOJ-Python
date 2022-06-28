def main():
    a, b, c, = int(input()), int(input()), int(input())
    if a + b + c != 180:
        print("Error")
    else:
        if a == b == 60:
            print("Equilateral")
        elif a == b or b == c or c == a:
            print("Isosceles")
        else:
            print("Scalene")


if __name__ == "__main__":
    main()
