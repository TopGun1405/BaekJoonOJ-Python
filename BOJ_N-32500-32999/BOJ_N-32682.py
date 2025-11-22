def main():
    T = int(input())
    for _ in range(T):
        N = int(input())

        if int(N**0.5) == N**0.5 and N % 2:
            print("OS")
        elif int(N**0.5) == N**0.5:
            print("S")
        elif N % 2:
            print("O")
        else:
            print("EMPTY")


if __name__ == "__main__":
    main()
