def main():
    N = int(input())
    for n in range(N):
        print("Case {}:".format(n + 1))
        M = int(input())
        for m in range(M):
            num = int(input())
            if num < 6:
                print(num + 1)


if __name__ == "__main__":
    main()
