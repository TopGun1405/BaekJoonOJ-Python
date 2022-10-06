def main():
    T = int(input())
    for _ in range(T):
        VPS = []
        brk = input()
        for b in brk:
            if b == '(':
                VPS.append(b)
            elif b == ')':
                if len(VPS) > 0:
                    VPS.pop()
                else:
                    print("NO")
                    break
        else:
            print("YES" if len(VPS) == 0 else "NO")


if __name__ == "__main__":
    main()
