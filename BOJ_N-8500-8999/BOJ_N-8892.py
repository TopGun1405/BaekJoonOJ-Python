from itertools import combinations


def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        words = [input() for _ in range(k)]

        for s1, s2 in combinations(words, 2):
            w1 = s1 + s2
            w2 = s2 + s1
            if w1 == w1[::-1]:
                print(w1)
                break
            if w2 == w2[::-1]:
                print(w2)
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
