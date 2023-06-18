def main():
    n = int(input())
    events = input()
    rooms = [0] * 10
    for event in events:
        if event == 'L':
            for i in range(10):
                if rooms[i] == 0:
                    rooms[i] = 1
                    break
        elif event == 'R':
            for i in range(10):
                if rooms[-i-1] == 0:
                    rooms[-i-1] = 1
                    break
        else:
            rooms[int(event)] = 0
    print(*rooms, sep='')


if __name__ == "__main__":
    main()
