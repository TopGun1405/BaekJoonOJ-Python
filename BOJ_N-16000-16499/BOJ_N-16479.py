def main():
    K = int(input())
    D1, D2 = map(int, input().split())
    if D1 == D2:
        print(K ** 2)
    else:
        print(K ** 2 - (abs(D2 - D1) / 2) ** 2)


if __name__ == "__main__":
    main()
