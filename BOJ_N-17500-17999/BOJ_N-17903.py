def main():
    m, n = map(int, input().split())
    for _ in range(m):
        val = map(int, input().split())
    print("satisfactory" if m >= 8 else "unsatisfactory")


if __name__ == "__main__":
    main()
