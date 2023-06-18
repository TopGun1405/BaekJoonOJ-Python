def main():
    n = int(input())
    birth = [input().split() for _ in range(n)]
    birth.sort(key=lambda k: (int(k[3]), int(k[2]), int(k[1])))
    print("{}\n{}".format(birth[-1][0], birth[0][0]))


if __name__ == "__main__":
    main()
