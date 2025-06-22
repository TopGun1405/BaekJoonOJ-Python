def main():
    T = int(input())
    for _ in range(T):
        A, n = map(int, input().split())

        res = []
        while True:
            if A == 0:
                break
            res.append(A % n)
            A //= n

        for i in range(len(res)//2):
            if res[i] != res[-i-1]:
                print(0)
                break
        else:
            print(1)


if __name__ == "__main__":
    main()
