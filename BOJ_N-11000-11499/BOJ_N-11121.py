def main():
    T = int(input())
    for _ in range(T):
        cIn, cOut = input().split()
        print("OK" if cIn == cOut else "ERROR")


if __name__ == "__main__":
    main()
