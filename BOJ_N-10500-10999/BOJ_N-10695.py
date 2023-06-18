def main():
    T = int(input())
    for t in range(1, T + 1):
        n, r1, c1, r2, c2 = map(int, input().split())
        able = [(r1-1, c1+2), (r1-1, c1-2), (r1+1, c1+2), (r1+1, c1-2),
                (r1-2, c1+1), (r1-2, c1-1), (r1+2, c1+1), (r1+2, c1-1)]
        print(f"Case {t}: {['NO', 'YES'][(r2, c2) in able]}")


if __name__ == "__main__":
    main()
