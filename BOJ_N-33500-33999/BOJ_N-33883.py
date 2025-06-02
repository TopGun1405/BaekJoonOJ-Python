def main():
    S = input()

    idx = -1
    vowel = ["a", "e", "i", "o", "u"]
    if S[-1] not in vowel and S[-1] not in ["n", "s"]:
        for i in range(len(S)-1, -1, -1):
            if S[i] in vowel:
                idx = i + 1
                break
    else:
        cnt = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] in vowel:
                cnt += 1
            if cnt == 2:
                idx = i + 1
                break

    print(idx)


if __name__ == "__main__":
    main()
