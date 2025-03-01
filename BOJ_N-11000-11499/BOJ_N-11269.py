def main():
    S = input()

    C = [S[i:i+3] for i in range(0, len(S), 3)]
    cnt = 0
    for c in C:
        cnt += sum(c[i] != "PER"[i] for i in range(3))

    print(cnt)


if __name__ == "__main__":
    main()
