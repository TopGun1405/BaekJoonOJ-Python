def main():
    N = list(input())
    card = {i: 0 for i in range(10)}

    i = 0
    print(N)
    while i < len(N):
        if int(N[i]) == 6 and card[6] > card[9]:
            card[9] += 1
        elif int(N[i]) == 9 and card[9] > card[6]:
            card[6] += 1
        else:
            card[int(N[i])] += 1
        i += 1
    print(card)
    print(max(card.values()))


if __name__ == "__main__":
    main()
