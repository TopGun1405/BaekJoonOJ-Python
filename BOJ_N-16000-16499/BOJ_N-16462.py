import math


def main():
    N = int(input())
    tot = 0
    for _ in range(N):
        Q_i = input()

        s = ""
        for q in Q_i:
            s += "9" if q in ["0", "6", "9"] else q

        s = 100 if 100 < int(s) else int(s)
        tot += s

    avg = tot / N
    print(math.floor(avg) if avg - int(avg) < 0.5 else math.ceil(avg))


if __name__ == "__main__":
    main()
