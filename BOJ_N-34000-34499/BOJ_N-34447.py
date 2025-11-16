def main():
    t = int(input())
    for _ in range(t):
        k, n = input().split()
        k = int(k)

        print("".join(str((int(digit) + k) % 10) for digit in n))


if __name__ == "__main__":
    main()
