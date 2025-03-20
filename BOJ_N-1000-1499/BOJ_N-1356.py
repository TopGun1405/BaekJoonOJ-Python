from functools import reduce


def main():
    N = input()

    for i in range(1, len(N)):
        front = reduce(lambda a, b: a * b, map(int, list(N[:i])))
        back = reduce(lambda a, b: a * b, map(int, list(N[i:])))
        if front == back:
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    main()
