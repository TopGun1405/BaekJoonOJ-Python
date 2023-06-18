def main():
    weights = [2, 7, 6, 5, 4, 3, 2]
    mapping = {0: 'J', 1: 'A', 2: 'B', 3: 'C', 4: 'D',
               5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'Z'}
    NICE = list(map(int, input()))
    sumNICE = 0
    for i, nice in enumerate(NICE):
        sumNICE += weights[i] * nice
    print(mapping[sumNICE % 11])


if __name__ == "__main__":
    main()
