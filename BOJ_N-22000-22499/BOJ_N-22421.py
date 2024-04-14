def main():
    while True:
        D, E = map(int, input().split())
        
        if D == E == 0:
            break

        minDiff = 1e9
        for i in range(D+1):
            minDiff = min(abs((i**2 + (D-i)**2)**0.5 - E), minDiff)
        print(minDiff)


if __name__ == "__main__":
    main()
