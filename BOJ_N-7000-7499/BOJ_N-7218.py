def main():
    N = int(input())
    s = input()

    r = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6,
         'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12}
    num = []
    for key in r:
        if key in s:
            num.append(r[key])

    print(*num)


if __name__ == "__main__":
    main()
