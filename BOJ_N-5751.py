def main():
    while True:
        N = int(input())
        if N == 0:
            break
        R = list(map(int, input().split()))
        J = R.count(1)
        print("Mary won {} times and John won {} times".format(N - J, J))


if __name__ == "__main__":
    main()
