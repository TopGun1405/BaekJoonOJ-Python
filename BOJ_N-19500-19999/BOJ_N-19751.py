from itertools import permutations


def main():
    nums = list(map(int, input().split()))
    fraction = list(map(lambda e: [e[0]/e[1] + e[2]/e[3]] + list(e), permutations(nums, 4)))
    fraction.sort(key=lambda k: k[0])

    print(*fraction[0][1:])


if __name__ == "__main__":
    main()
