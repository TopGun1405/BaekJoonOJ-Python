def main():
    T = int(input())
    for _ in range(T):
        A, B = input().split()

        # a, b = {c: 0 for c in list(A)}, {c: 0 for c in list(B)}
        # for c in A:
        #     a[c] += 1
        # for c in B:
        #     b[c] += 1

        # print(f"{A} & {B} are {'' if a == b else 'NOT '}anagrams.")
        print("{} & {} are {}anagrams.".format(
            A, B, "" if sorted(A) == sorted(B) else "NOT "
        ))


if __name__ == "__main__":
    main()
