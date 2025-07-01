from itertools import permutations


def main():
    n = int(input())
    A = list(map(int, input().split()))

    for A_i, A_j, A_k in list(permutations(A, 3)):
        if (A_i - A_j) / A_k != (A_i - A_j) // A_k:
            print("no")
            break
    else:
        print("yes")


if __name__ == "__main__":
    main()
