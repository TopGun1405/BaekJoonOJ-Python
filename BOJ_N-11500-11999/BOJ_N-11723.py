def main():
    M = int(input())
    # set -> list
    S = set()
    for _ in range(M):
        cmd = input().split()
        if cmd[0] == "add":
            if cmd[1] in S:
                continue
            else:
                S.add(cmd[1])
        elif cmd[0] == "remove":
            if cmd[1] in S:
                S.remove(cmd[1])
        elif cmd[0] == "check":
            print(1 if cmd[1] in S else 0)
        elif cmd[0] == "toggle":
            if cmd[1] in S:
                S.remove(cmd[1])
            else:
                S.add(cmd[1])
        elif cmd[0] == "all":
            S = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"}
        elif cmd[0] == "empty":
            S = set()


if __name__ == "__main__":
    main()
