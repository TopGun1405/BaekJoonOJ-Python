def main():
    N = int(input())

    for _ in range(N):
        S = int(input())

        for i in range(2, 1_000_000):
            if S % i == 0:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
