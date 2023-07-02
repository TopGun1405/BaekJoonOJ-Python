def main():
    A, B = map(int, input().split())
    N = int(input())

    click = abs(A - B)
    for _ in range(N):
        freq = int(input())
        if click > abs(freq - B):
            click = abs(freq - B) + 1
    print(click)


if __name__ == "__main__":
    main()
