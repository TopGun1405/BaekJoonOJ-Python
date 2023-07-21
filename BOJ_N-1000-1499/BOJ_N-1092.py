def main():
    N = int(input())
    cranes = sorted(map(int, input().split()), reverse=True)
    M = int(input())
    boxes = sorted(map(int, input().split()), reverse=True)

    if boxes[0] > cranes[0]:
        print(-1)
    else:
        time = 0
        while boxes:
            for crane in cranes:
                if boxes and crane < boxes[-1]:
                    continue
                for box in boxes:
                    if crane >= box:
                        boxes.remove(box)
                        break
            time += 1
        print(time)


if __name__ == "__main__":
    main()
