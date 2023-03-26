def main():
    N = int(input())
    if N < 99:
        print(99)
    else:
        i = 1
        while True:
            if (N + i) % 100 == 99:
                print(N + i)
                break
            if (N - i) % 100 == 99:
                print(N - i)
                break
            i += 1


if __name__ == "__main__":
    main()
