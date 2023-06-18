def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        z = 0
        for n in range(N, M + 1):
            # z += str(n).count('0')
            if 0 <= n < 100:
                z = z + 1 if n % 10 == 0 else z
            
        print(z)


if __name__ == "__main__":
    main()
