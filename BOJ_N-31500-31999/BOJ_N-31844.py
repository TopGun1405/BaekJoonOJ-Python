def main():
    storage = input()

    robot, box, flag = storage.index("@"), storage.index("#"), storage.index("!")
    if robot < box < flag or robot > box > flag:
        print(abs(box - robot) + abs(flag - box) - 1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
