def main():
    grades = {
        'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
        'F': 0.0
    }

    N = int(input())
    tot, tot_g = 0, 0
    for _ in range(N):
        subs, n, grade = map(lambda e: int(e) if e.isdigit() else e, input().split())
        tot += n * grades[grade]
        tot_g += n

    GPA = tot / tot_g
    print("%.2f" % (round(GPA + 10 ** -10, 2)))


if __name__ == "__main__":
    main()
