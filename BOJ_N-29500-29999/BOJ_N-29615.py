def main():
    N, M = map(int, input().split())
    wait = list(map(int, input().split()))
    friends = list(map(int, input().split()))

    cnt = 0
    for n in wait[:M]:
        if n not in friends:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
