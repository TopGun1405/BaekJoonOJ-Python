def main():
    t = int(input())
    for _ in range(t):
        A, C = map(int, input().split())
        r, g, b = map(int, input().split())

        R = A * ((r+1)**2 + g**2 + b**2) + C * min(r+1, g, b)
        G = A * (r**2 + (g+1)**2 + b**2) + C * min(r, g+1, b)
        B = A * (r**2 + g**2 + (b+1)**2) + C * min(r, g, b+1)

        maxScore = max(R, G, B)
        if maxScore == R:
            print("RED")
        elif maxScore == G:
            print("GREEN")
        elif maxScore == B:
            print("BLUE")
        elif maxScore == R == G == B:
            print("RED")


if __name__ == "__main__":
    main()
