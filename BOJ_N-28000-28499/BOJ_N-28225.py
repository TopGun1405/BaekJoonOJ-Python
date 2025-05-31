def main():
    n, f = map(int, input().split())
    s = []
    for i in range(1, n+1):
        x_i, v_i = map(int, input().split())
        s.append([i, (f - x_i) / v_i])
    s.sort(key=lambda k: k[1])

    print(s[0][0])


if __name__ == "__main__":
    main()
