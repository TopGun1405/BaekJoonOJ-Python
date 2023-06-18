def main():
    N = int(input())
    for _ in range(N):
        n = int(input())
        print("even" if n % 2 == 0 else "odd")


if __name__ == "__main__":
    main()
