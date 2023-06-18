def main():
    n = list(map(int, input().split()))
    m = [1, 2, 3, 4, 5, 6, 7, 8]
    print("ascending" if n == m else ("descending" if n == m[::-1] else "mixed"))


if __name__ == "__main__":
    main()
