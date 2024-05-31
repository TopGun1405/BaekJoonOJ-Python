def main():
    K = int(input())
    flag = ["G...", ".I.T", "..S."]

    for p in flag:
        for _ in range(K):
            print("".join(map(lambda c: c*K, p)))


if __name__ == "__main__":
    main()
