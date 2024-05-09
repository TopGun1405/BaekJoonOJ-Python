from itertools import combinations


def main():
    l = sorted(map(int, input().split()))
    print(len(list(filter(lambda e: e[2] < e[1] + e[0], combinations(l, 3)))))


if __name__ == "__main__":
    main()
