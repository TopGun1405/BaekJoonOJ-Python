def main():
    N = int(input())
    D, P = 0, 0
    for _ in range(N):
        winner = input()
        if D - P < 2 and P - D < 2:
            if winner == 'D':
                D += 1
            else:
                P += 1
    print("{}:{}".format(D, P))


if __name__ == "__main__":
    main()
