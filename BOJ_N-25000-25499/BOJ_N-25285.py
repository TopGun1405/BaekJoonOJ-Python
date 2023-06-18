def main():
    T = int(input())
    for _ in range(T):
        h, w = map(int, input().split())
        BMI = w / ((h / 100) ** 2)
        if h < 140.1:
            print(6)
        elif 140.1 <= h < 146:
            print(5)
        elif 146 <= h < 159:
            print(4)
        elif 159 <= h < 161:
            if 16 <= BMI < 35:
                print(3)
            else:
                print(4)
        elif 161 <= h < 204:
            if 20 <= BMI < 25:
                print(1)
            elif 18.5 <= BMI < 20 or 25 <= BMI < 30:
                print(2)
            elif 16 <= BMI < 18.5 or 30 <= BMI < 35:
                print(3)
            else:
                print(4)
        elif h >= 204:
            print(4)


if __name__ == "__main__":
    main()
