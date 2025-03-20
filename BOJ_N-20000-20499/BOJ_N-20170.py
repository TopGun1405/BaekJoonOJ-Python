from fractions import Fraction


def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    tot = 0
    for A_i in A:
        tot += len(list(filter(lambda e: e < A_i, B)))

    fr = Fraction(tot, len(A)**2)
    print(fr.numerator, "/", fr.denominator, sep="")


if __name__ == "__main__":
    main()
