import math


def main():
    N = int(input())
    for _ in range(N):
        data = input().split(" = ")

        res = -math.log10(float(data[1]))
        if data[0] == "H":
            print(f"{res:.02f}")
        else:
            print(f"{14 - res:.02f}")


if __name__ == "__main__":
    main()
