def main():
    T = int(input())

    for _ in range(T):
        n = int(input())

        if n <= 2:
            print(1)
        else:
            print(3)


if __name__ == "__main__":
    main()
