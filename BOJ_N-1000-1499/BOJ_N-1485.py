from itertools import combinations


def main():

    def length(A, B):
        return (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2

    T = int(input())
    for _ in range(T):
        pos = sorted([list(map(int, input().split())) for _ in range(4)])

        case = sorted([length(a, b) for a, b in list(combinations(pos, 2))])

        print(1 if len(set(case)) == case.count(case[-1]) == 2 and case.count(case[0]) == 4 else 0)


if __name__ == "__main__":
    main()
