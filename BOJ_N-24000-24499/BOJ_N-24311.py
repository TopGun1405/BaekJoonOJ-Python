def main():
    t1, t2 = map(int, input().split())
    t3 = int(input())
    t4, t5 = map(int, input().split())
    br = int(input())
    t6 = int(input())

    deadline = t1*60 + t2 - 10

    travelTime = t4*60 + t5
    hotelTime = (br+1) * t6
    totalTime = t3 + travelTime + hotelTime

    dep = deadline - totalTime

    print(f"{dep // 60:02d} {dep % 60:02d}")


if __name__ == "__main__":
    main()
