def main():
    n, m = map(int, input().split())
    print(n*(m-1) + m*(n-1) + 2*(n*m-(n+m-1)))


if __name__ == "__main__":
    main()
