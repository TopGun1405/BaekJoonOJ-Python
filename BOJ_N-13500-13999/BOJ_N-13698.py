def main():
    change = input()
    cup = [1, 0, 0, 2]
    case = {'A': [0, 1], 'B': [0, 2], 'C': [0, 3],
            'D': [1, 2], 'E': [1, 3], 'F': [2, 3]}
    for c in change:
        cup[case[c][0]], cup[case[c][1]] = cup[case[c][1]], cup[case[c][0]]
    print(cup.index(1) + 1)
    print(cup.index(2) + 1)


if __name__ == "__main__":
    main()
