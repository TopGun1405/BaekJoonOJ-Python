def main():
    N = int(input())

    seats = {chr(n): ["." for _ in range(20)] for n in range(65, 75)}
    for _ in range(N):
        seat = input()
        r, c = seat[0], int(seat[1:])
        seats[r][c-1] = "o"

    for row in seats.values():
        print("".join(row))


if __name__ == "__main__":
    main()
