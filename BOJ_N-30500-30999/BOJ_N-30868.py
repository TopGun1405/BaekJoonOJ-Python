def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(" ".join(["++++" for _ in range(n // 5)] + ["|" * (n % 5)]))


if __name__ == "__main__":
    main()
