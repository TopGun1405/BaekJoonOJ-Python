def main():
    N = int(input())
    for _ in range(N):
        a, b, c = map(int, input().split())
        print("{} {} {} {}".format(a, b, c, "Seems OK" if a + b + c == 180 else "Check"))


if __name__ == "__main__":
    main()
