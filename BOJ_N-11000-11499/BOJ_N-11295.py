def main():
    i = 1
    while True:
        L = int(input())
        if L == 0:
            break
        N = int(input())
        print("User", i)
        for _ in range(N):
            print("{:0.5f}".format(L * int(input()) / 100_000))
        i += 1


if __name__ == "__main__":
    main()
