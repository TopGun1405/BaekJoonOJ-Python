def main():
    N = int(input())

    pair = []
    for a in range(1, int(N**0.5)+1):
        if N % a == 0:
            pair.append((a, N//a))
            pair.append((N//a, a))

    print(len(set(pair)))


if __name__ == "__main__":
    main()
