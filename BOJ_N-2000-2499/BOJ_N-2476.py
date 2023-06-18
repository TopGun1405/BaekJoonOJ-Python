def main():
    N = int(input())
    p = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        temp = 0
        if a == b == c:
            temp += 10000 + a * 1000
        else:
            if a == b and b != c:
                temp += 1000 + a * 100
            elif b == c and c != a:
                temp += 1000 + b * 100
            elif c == a and a != b:
                temp += 1000 + c * 100
            else:
                temp += max(a, b, c) * 100
        if temp > p:
            p = temp
    print(p)


if __name__ == "__main__":
    main()
