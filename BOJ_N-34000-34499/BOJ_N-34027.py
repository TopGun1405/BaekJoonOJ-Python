def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(1 if int(N ** 0.5) == N ** 0.5 else 0)


if __name__ == "__main__":
    main()
