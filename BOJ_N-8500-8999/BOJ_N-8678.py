def main():
    z = int(input())
    for _ in range(z):
        a, b = map(int, input().split())

        print("TAK" if b % a == 0 else "NIE")


if __name__ == "__main__":
    main()
