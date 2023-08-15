import random


def main():
    n = int(input())
    sub = ["swimming", "bowling", "soccer"]
    passSub = [sub[random.randint(0, 2)] for _ in range(n)]
    print(*passSub)
    failSub = input().split()
    sub = set(sub)
    for p, f in zip(passSub, failSub):
        print(*(sub - {p, f}), end=' ')


if __name__ == "__main__":
    main()
