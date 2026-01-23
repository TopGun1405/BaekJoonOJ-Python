def main():
    n = int(input())
    for _ in range(n):
        x, k, h = map(int, input().split())

        print(format(h*(2*x) + min(k-h, 140)*x + max(k-h-140, 0)*int(1.5*x), ",d"))


if __name__ == "__main__":
    main()
