def main():
    N = int(input())
    words = {}
    for _ in range(N):
        x, y = input().split(" = ")
        words[x] = y

    T = int(input())
    for _ in range(T):
        K = int(input())
        sentence = input().split()
        print(" ".join(map(lambda c: words[c], sentence)))


if __name__ == "__main__":
    main()
