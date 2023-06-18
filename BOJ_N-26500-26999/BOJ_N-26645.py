def main():
    N = int(input())
    potion = [0] * 5
    potion[1] = 0 if N > 209 else (210 if N + 8 > 210 else N + 8)
    potion[2] = 0 if N > 219 else (220 if N + 4 > 220 else N + 4)
    potion[3] = 0 if N > 229 else (230 if N + 2 > 230 else N + 2)
    potion[4] = N + 1
    p = max(potion)
    for i in range(4, 0, -1):
        if potion[i] == p:
            print(i)
            break


if __name__ == "__main__":
    main()
