def main():
    C, L = float(input()), int(input())
    S = 0
    for _ in range(L):
        w, l = map(float, input().split())
        S += w * l
    print("{:0.7f}".format(C * S))


if __name__ == "__main__":
    main()
