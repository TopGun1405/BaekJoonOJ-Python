def main():
    score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5,
             'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
    tot = 0
    grades_tot = 0
    for _ in range(20):
        n, g, s = input().split()
        if s != 'P':
            tot += float(g) * score[s]
            grades_tot += float(g)
    print("{:0.6f}".format(tot / grades_tot))


if __name__ == "__main__":
    main()
