def main():
    T = int(input())
    for _ in range(T):
        DNA = input()
        seq = []
        for _ in range(len(DNA)):
            seq.append(DNA)
            DNA = DNA[1:] + DNA[0]
        print(sorted(seq)[0])


if __name__ == "__main__":
    main()
