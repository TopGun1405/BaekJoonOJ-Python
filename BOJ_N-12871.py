def main():
    s = list(input())
    t = list(input())
    s_rep, t_rep = s[0], t[0]
    s_check, t_check = 0, 0
    i = 1
    while True:
        if s[i] == s[0]:
            print(s_rep)
            s_check = 1
        else:
            s_rep += s[i]
        if t[i] == t[0]:
            print(t_rep)
            t_check = 1
        else:
            t_rep += t[i]
        if s_check and t_check:
            print(1)
            break
        elif i == len(s) or i == len(t):
            print(0)
            break
        if i < len(s) and i < len(t):
            i += 1


if __name__ == "__main__":
    main()
