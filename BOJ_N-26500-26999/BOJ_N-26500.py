def main():
    n = int(input())
    for _ in range(n):
        a, b = map(float, input().split())
        print("{:0.1f}".format(abs(a - b)))


if __name__ == "__main__":
    main()
