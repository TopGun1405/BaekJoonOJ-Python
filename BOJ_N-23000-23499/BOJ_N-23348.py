def main():
    A, B, C = map(int, input().split())
    N = int(input())
    score = 0
    for _ in range(N):
        temp = 0
        for _ in range(3):
            a, b, c = map(int, input().split())
            temp += A * a + B * b + C * c
        if temp > score:
            score = temp
    print(score)


if __name__ == "__main__":
    main()
