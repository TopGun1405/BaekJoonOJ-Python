def main():
    ax, ay, az = map(int, input().split())
    cx, cy, cz = map(int, input().split())

    print(cx - az, cy // ay, cz - ax)


if __name__ == "__main__":
    main()
