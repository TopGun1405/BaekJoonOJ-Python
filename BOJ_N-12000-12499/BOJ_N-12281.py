def main():
    T = int(input())
    # Alex : odd, increasing
    # Bob  : even, decreasing
    for X in range(1, T + 1):
        N = int(input())
        s = list(map(int, input().split()))

        alex = sorted(filter(lambda e: e % 2 == 1, s), reverse=True)
        bob = sorted(filter(lambda e: e % 2 == 0, s), reverse=False)

        t, i = [], 0
        while len(t) < N:
            if s[i] % 2 == 1:
                t.append(alex.pop())
            else:
                t.append(bob.pop())
            i += 1

        print(f"Case #{X}:", *t)


if __name__ == "__main__":
    main()
