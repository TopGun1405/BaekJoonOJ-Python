def main():
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    calc = [0]
    for i in num:
        calc.append(calc[-1] + i)
    for _ in range(M):
        i, j = map(int, input().split())
        print(calc[j] - calc[i - 1])


if __name__ == "__main__":
    main()
