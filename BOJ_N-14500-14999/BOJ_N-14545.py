def main():
    P = int(input())
    sq = [0, 1]
    for i in range(2, 1_000_000):
        sq += [sq[-1] + i**2]
    for _ in range(P):
        I = int(input())
        print(sq[I])


if __name__ == "__main__":
    main()
