def main():
    N = int(input())
    for _ in range(N):
        a, b, c = map(int, input().split())
        print(["IMPOSSIBLE", "POSSIBLE"][a + b == c or abs(a - b) == c or a * b == c or a / b == c or b / a == c])


if __name__ == "__main__":
    main()
