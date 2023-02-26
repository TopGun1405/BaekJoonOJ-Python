def main():
    T = int(input())
    for _ in range(T):
        a, b, c = sorted(map(int, input().split()))
        print("Case #{}:".format(_ + 1), ["NO", "YES"][a**2 + b**2 == c**2])


if __name__ == "__main__":
    main()
