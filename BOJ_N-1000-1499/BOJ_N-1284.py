def main():
    number = {0: 4, 1: 2, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3}
    while True:
        n = list(map(int, list(str(input()))))
        if n[0] == 0:
            break
        w = 0
        for i in n:
            w += number[i]
        print(len(n) + 1 + w)


if __name__ == "__main__":
    main()
