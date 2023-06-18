def main():
    n = int(input())
    c = list(map(int, input().split()))
    k = int(input())
    p = list(map(int, input().split()))
    for pj in p:
        c[pj-1] -= 1
    for ci in c:
        print(["yes", "no"][ci >= 0])


if __name__ == "__main__":
    main()
