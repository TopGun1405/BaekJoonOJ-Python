def main():
    S = input()

    grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0
    }

    tot_grade, cnt = 0, 0
    for i in range(len(S)):
        if S[i] == "+":
            continue

        cnt += 1
        if i < len(S)-1 and S[i+1] == "+":
            tot_grade += grades[S[i]] + 0.5
        else:
            tot_grade += grades[S[i]]

    print(tot_grade / cnt)


if __name__ == "__main__":
    main()
