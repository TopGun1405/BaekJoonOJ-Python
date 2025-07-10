def main():
    N = int(input())
    for t in range(1, N + 1):
        A1, A2 = [0] * 26, [0] * 26
        W1 = input()
        W2 = input()

        for i in range(len(W1)):
            A1[ord(W1[i]) - 97] += 1
        for i in range(len(W2)):
            A2[ord(W2[i]) - 97] += 1

        dis = 0
        for i in range(26):
            dis += abs(A1[i] - A2[i])

        print(f"Case #{t}: {dis}")


if __name__ == "__main__":
    main()
