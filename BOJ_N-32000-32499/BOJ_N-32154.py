def main():
    N = int(input())
    scoreboard = {
        1: [11, "A", "B", "C", "D", "E", "F", "G", "H", "J", "L", "M"],
        2: [9, "A", "C", "E", "F", "G", "H", "I", "L", "M"],
        3: [9, "A", "C", "E", "F", "G", "H", "I", "L", "M"],
        4: [9, "A", "B", "C", "E", "F", "G", "H", "L", "M"],
        5: [8, "A", "C", "E", "F", "G", "H", "L", "M"],
        6: [8, "A", "C", "E", "F", "G", "H", "L", "M"],
        7: [8, "A", "C", "E", "F", "G", "H", "L", "M"],
        8: [8, "A", "C", "E", "F", "G", "H", "L", "M"],
        9: [8, "A", "C", "E", "F", "G", "H", "L", "M"],
        10: [8, "A", "B", "C", "F", "G", "H", "L", "M"]
    }
    print(scoreboard[N][0])
    print(*scoreboard[N][1:])


if __name__ == "__main__":
    main()
