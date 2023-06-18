import math


def main():
    i = 1
    while True:
        d, r, t = map(float, input().split())
        if r == 0:
            break
        dis = d / 63360 * math.pi * r
        mph = dis / t * 3600
        print("Trip #{}: {:0.2f} {:0.2f}".format(i, dis, mph))
        i += 1


if __name__ == "__main__":
    main()
