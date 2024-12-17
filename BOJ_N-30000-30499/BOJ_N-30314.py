def main():
    n = int(input())
    prev_winner = input()
    own_initial = input()

    total_move = 0
    for s1, s2 in zip(prev_winner, own_initial):
        S1, S2, A, Z = ord(s1), ord(s2), ord("A"), ord("Z")
        total_move += min(abs(S2-S1), S1-A+Z-S2+1, Z-S1+S2-A+1)

    print(total_move)


if __name__ == "__main__":
    main()
