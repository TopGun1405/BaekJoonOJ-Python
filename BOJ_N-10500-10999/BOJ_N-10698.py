def main():
    T = int(input())
    for t in range(T):
        eq = input().split()
        print("Case {}: ".format(t + 1), end='')
        if eq[1] == '+':
            print("YES" if int(eq[0]) + int(eq[2]) == int(eq[4]) else "NO")
        elif eq[1] == '-':
            print("YES" if int(eq[0]) - int(eq[2]) == int(eq[4]) else "NO")


if __name__ == "__main__":
    main()
