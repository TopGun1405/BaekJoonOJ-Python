def main():
    P, N = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    acc = 0
    while P < 200 and A:
        P, acc = P + A.pop(), acc + 1
    print(acc)


if __name__ == "__main__":
    main()
