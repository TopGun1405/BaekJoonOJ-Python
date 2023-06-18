def main():
    T = int(input())
    for t in range(T):
        g = list(map(int, input().split()))
        s = list(map(int, input().split()))
        gc = g[0] + g[1] * 2 + g[2] * 3 + g[3] * 3 + g[4] * 4 + g[5] * 10
        sc = s[0] + s[1] * 2 + s[2] * 2 + s[3] * 2 + s[4] * 3 + s[5] * 5 + s[6] * 10
        print("Battle {}: Good triumphs over Evil".format(t + 1) if gc > sc
              else ("Battle {}: Evil eradicates all trace of Good".format(t + 1) if gc < sc
                    else "Battle {}: No victor on this battle field".format(t + 1)))


if __name__ == "__main__":
    main()
