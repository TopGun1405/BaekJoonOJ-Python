def main():
    S = input()

    score_tot, score_prev, C_prev = 1, 1, S[0]
    for C in S[1:]:
        if ord(C) > ord(C_prev):
            score_prev += 1
            score_tot += score_prev
        else:
            score_prev = 1
            score_tot += score_prev
        C_prev = C

    print(score_tot)


if __name__ == "__main__":
    main()
