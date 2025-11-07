def main():
    JLPT = {1: 100, 2: 90}
    fail = {1: 18, 2: 18}

    Q = int(input())
    for _ in range(Q):
        info = list(map(int, input().split()))
        s, k, r, l = info
        if (s == 1 or s == 2) and l >= 50:
            check1 = [k*3 < JLPT[s], r*3 < JLPT[s]]
            check2 = [k - fail[s] <= 3, r - fail[s] <= 3]
            if check1.count(True) >= 2 or check2.count(True) >= 1:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


if __name__ == "__main__":
    main()
