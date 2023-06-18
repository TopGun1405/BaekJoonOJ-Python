def main():
    n = int(input())
    for i in range(n):
        tri = sorted(map(int, input().split()))
        print("Scenario #{}:".format(i + 1))
        print("yes" if tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2 else "no")
        print()


if __name__ == "__main__":
    main()
