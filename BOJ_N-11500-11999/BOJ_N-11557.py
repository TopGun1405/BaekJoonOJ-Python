def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        alc, name = 0, ''
        for _ in range(N):
            univ, n = input().split()
            if int(n) > alc:
                alc, name = int(n), univ
        print(name)


if __name__ == "__main__":
    main()
