def main():
    P = int(input())
    for _ in range(P):
        patterns = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
        game = input()
        for i in range(38):
            patterns[game[i:i+3]] += 1
        print(*patterns.values())


if __name__ == "__main__":
    main()
