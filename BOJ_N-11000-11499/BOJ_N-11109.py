def main():
    T = int(input())
    for _ in range(T):
        d, n, s, p = map(int, input().split())
        print("does not matter" if d + p * n == n * s
              else ("do not parallelize" if d + p * n > n * s
                    else "parallelize"))


if __name__ == "__main__":
    main()
