def main():
    N = int(input())
    hills = list(map(int, input().split()))

    enemy, maxH, cnt = 0, 0, 0
    for hill in hills:
        if hill > maxH:
            maxH, cnt = hill, 0
        else:
            cnt += 1
        enemy = max(enemy, cnt)
    print(enemy)


if __name__ == "__main__":
    main()
