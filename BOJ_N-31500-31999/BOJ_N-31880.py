def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    luck = sum(a)
    for b_i in b:
        if b_i == 0:
            continue
        luck *= b_i

    print(luck)


if __name__ == "__main__":
    main()
