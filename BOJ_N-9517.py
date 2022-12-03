def main():
    K = int(input())
    N = int(input())
    bombTimer = 210
    for _ in range(N):
        T, Z = input().split()
        bombTimer -= int(T)
        if Z == 'T' and bombTimer > 0:
            K = (K + 1) % 8 if K + 1 != 8 else 8
    print(K)


if __name__ == "__main__":
    main()
