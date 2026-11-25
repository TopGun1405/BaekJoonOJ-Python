def main():
    n, k = map(int, input().split())
    d, s = map(int, input().split())

    # total = n * d
    # solved = k * s
    us = n*d - k*s
    usr = us / (n-k)
    print(usr if 0 <= usr <= 100 else "impossible")


if __name__ == "__main__":
    main()
