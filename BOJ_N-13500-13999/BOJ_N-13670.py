def main():
    while True:
        H1, M1, H2, M2 = map(int, input().split())

        if H1 == M1 == H2 == M2 == 0:
            break

        if H2 < H1 or (H2 == H1 and M2 < M1):
            H2 += 24

        print((H2 * 60 + M2) - (H1 * 60 + M1))


if __name__ == "__main__":
    main()
