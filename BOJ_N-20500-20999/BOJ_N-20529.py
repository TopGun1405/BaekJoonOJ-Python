from itertools import combinations


def main():

    def psycDistance(MBTI_1: str, MBTI_2: str) -> int:
        dis = 0
        for t1, t2 in zip(MBTI_1, MBTI_2):
            if t1 != t2:
                dis += 1
        return dis

    T = int(input())
    for _ in range(T):
        N = int(input())
        MBTI = input().split()

        minDis = 8
        if N > 32:
            minDis = 0
        else:
            ABC = list(combinations(MBTI, 3))
            for a, b, c in ABC:
                ab = psycDistance(a, b)
                bc = psycDistance(b, c)
                ca = psycDistance(c, a)
                minDis = min(minDis, ab + bc + ca)

        print(minDis)


if __name__ == "__main__":
    main()
