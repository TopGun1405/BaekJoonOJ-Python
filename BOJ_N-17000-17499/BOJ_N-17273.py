def main():
    N, M = map(int, input().split())
    front, back = [], []
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        front.append(A_i)
        back.append(B_i)
    K = [int(input()) for _ in range(M)]

    cards = front[::]
    for i in range(M):
        for j in range(N):
            if cards[j] > K[i]:
                continue
            cards[j] = back[j] if cards[j] == front[j] else front[j]

    print(sum(cards))


if __name__ == "__main__":
    main()
