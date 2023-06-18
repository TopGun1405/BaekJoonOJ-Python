def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        while True:
            for N in range(2, int(n ** 0.5) + 1):
                if n % N == 0:
                    n += 1
                    break
            else:
                print(2 if n == 0 or n == 1 else n)
                break


if __name__ == "__main__":
    main()
