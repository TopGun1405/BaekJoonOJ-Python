def main():
    A, B, C, N = map(int, input().split())
    room = [0] * 301
    room[A] = room[B] = room[C] = 1

    for i in range(A, N + 1):
        for j in [A, B, C]:
            if i >= j and room[i - j]:
                room[i] = 1
    print(room[N])


if __name__ == "__main__":
    main()
