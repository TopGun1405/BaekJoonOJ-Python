def main():
    dice1 = {1: "Yakk", 2: "Doh", 3: "Seh", 4: "Ghar", 5: "Bang", 6: "Sheesh"}
    dice2 = {1: "Habb Yakk", 2: "Dobara", 3: "Dousa", 4: "Dorgy", 5: "Dabash", 6: "Dosh"}
    T = int(input())
    for t in range(T):
        a, b = map(int, input().split())
        s = ''
        if a == b:
            s += dice2[a]
        else:
            if (a == 6 and b == 5) or (a == 5 and b == 6):
                s += "Sheesh Beesh"
            else:
                s += dice1[max(a, b)] + ' ' + dice1[min(a, b)]
        print("Case {}: {}".format(t + 1, s))


if __name__ == "__main__":
    main()
