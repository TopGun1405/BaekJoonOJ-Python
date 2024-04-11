def main():
    N, C = map(int, input().split())

    fireWork = [0] * (C + 1)
    for _ in range(N):
        n = int(input())
        
        if n == 1:
            print(C)
            break

        for i in range(n, C + 1, n):
            fireWork[i] = 1
    else:
        print(sum(fireWork))


if __name__ == "__main__":
    main()
