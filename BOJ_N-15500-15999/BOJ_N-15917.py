def main():
    Q = int(input())
    two = [2 ** i for i in range(32)]
    for _ in range(Q):
        a = int(input())
        print(1 if a in two else 0)
        # print(1 if a & (-a) == a else 0)


if __name__ == "__main__":
    main()
