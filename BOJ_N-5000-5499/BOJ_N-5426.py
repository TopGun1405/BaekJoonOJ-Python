def main():
    T = int(input())
    for _ in range(T):
        msg = input()
        k = int(len(msg) ** 0.5)

        decoded = []
        for i in range(k, 0, -1):
            for j in range(i, k ** 2 + 1, k):
                decoded.append(msg[j - 1])
        print(''.join(decoded))


if __name__ == "__main__":
    main()
