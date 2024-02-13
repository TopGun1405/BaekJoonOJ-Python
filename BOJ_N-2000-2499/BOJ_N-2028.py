def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        i = len(str(N))
        print("YES" if str(N ** 2)[-i:] == str(N) else "NO")


if __name__ == "__main__":
    main()
