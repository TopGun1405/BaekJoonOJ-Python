def main():
    T = int(input())
    for _ in range(T):
        x = input()
        print("YES" if sum(map(int, x)) % 9 == 0 else "NO")


if __name__ == "__main__":
    main()
