def main():
    A, B = map(int, input().split())
    num, cnt = 0, 0
    for i in range(1, 1001):
        for j in range(i):
            cnt += 1
            if A <= cnt <= B:
                num += i
            elif cnt > B:
                break
        else:
            continue
    print(num)


if __name__ == "__main__":
    main()
