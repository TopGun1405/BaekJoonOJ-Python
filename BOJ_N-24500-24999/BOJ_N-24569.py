def main():
    N = int(input())

    over40 = 0
    for _ in range(N):
        P = int(input())
        F = int(input())

        if 5*P - 3*F > 40:
            over40 += 1

    print(f"{over40}{'+' if over40 == N else ''}")


if __name__ == "__main__":
    main()
