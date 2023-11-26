from itertools import permutations


def main():
    n = int(input())
    k = int(input())
    cards = [input() for _ in range(n)]
    print(len(set(''.join(num) for num in permutations(cards, k))))


if __name__ == "__main__":
    main()
