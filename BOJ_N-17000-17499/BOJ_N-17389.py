def main():
    N, S = input(), input()
    score, bonus = 0, 0
    for idx, val in enumerate(S):
        if val == 'O':
            score, bonus = score + idx + 1 + bonus, bonus + 1
        else:
            bonus = 0
    print(score)


if __name__ == "__main__":
    main()
