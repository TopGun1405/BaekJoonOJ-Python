def main():
    X, Y = map(int, input().split())
    N = int(input())
    val = [X / Y * 1000]
    for _ in range(N):
        Xi, Yi = map(int, input().split())
        val.append(Xi / Yi * 1000)
    print("{:0.2f}".format(min(val)))


if __name__ == "__main__":
    main()
