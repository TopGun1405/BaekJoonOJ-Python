def main():
    cnt, right, obtuse, acute = 0, 0, 0, 0
    while True:
        a, b, c = map(int, input().split())
        a, b, c = sorted([a, b, c])
        if a + b > c and a + c > b and b + c > a:
            cnt += 1

            if a ** 2 + b ** 2 == c ** 2:
                right += 1
            elif a ** 2 + b ** 2 < c ** 2:
                acute += 1
            elif a ** 2 + b ** 2 > c ** 2:
                obtuse += 1
        else:
            print(cnt, right, obtuse, acute)
            break


if __name__ == "__main__":
    main()
