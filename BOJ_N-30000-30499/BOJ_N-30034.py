def main():
    N = int(input())
    # 구분자
    seps = input().split()
    M = int(input())
    # 숫자 구분자
    nums = input().split()
    K = int(input())
    # 병합자
    comb = input().split()
    S = int(input())
    text = input()

    seperator = list(set(seps).union(set(nums)) - set(comb))

    for c in seperator:
        text = text.replace(c, " ")

    print(*text.split(), sep="\n")


if __name__ == "__main__":
    main()
