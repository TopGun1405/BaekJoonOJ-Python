def main():
    T = int(input())
    for _ in range(T):
        s, p = input().split()
        c = s.count(p)
        print(c + (len(s) - len(p) * c))


if __name__ == "__main__":
    main()
