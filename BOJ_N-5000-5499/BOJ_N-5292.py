def main():
    N = int(input())
    for n in range(1, N + 1):
        if n % 15 == 0:
            print("DeadMan")
        elif n % 3 == 0:
            print("Dead")
        elif n % 5 == 0:
            print("Man")
        else:
            print(n, end=' ')


if __name__ == "__main__":
    main()
