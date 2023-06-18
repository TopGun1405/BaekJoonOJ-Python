def main():
    N, F = input(), int(input())
    n = int(N[:-2] + "00")
    while True:
        if not n % F:
            break
        n += 1
    print(str(n)[-2:])


if __name__ == "__main__":
    main()
