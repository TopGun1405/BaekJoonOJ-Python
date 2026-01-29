def main():
    x, y, z = map(int, input().split())

    final = 0.25*x + 0.25*y + 0.5*z
    if 90 <= final <= 100:
        print("A")
    elif 80 <= final < 90:
        print("B")
    elif 70 <= final < 80:
        print("C")
    elif 60 <= final < 70:
        print("D")
    elif 0 <= final < 60:
        print("F")


if __name__ == "__main__":
    main()
