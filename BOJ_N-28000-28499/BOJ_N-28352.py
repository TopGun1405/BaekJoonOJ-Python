def main():
    N = int(input())
    week = 7 * 24 * 60 * 60
    s = 1
    for n in range(1, N + 1):
        s *= n
    print(s // week)


if __name__ == "__main__":
    main()
