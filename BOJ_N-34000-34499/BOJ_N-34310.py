def main():
    N = int(input())

    stu, fac, vis = 0, 0, 0
    for _ in range(N):
        t, d, num = input().split()
        num = int(num)

        if t == "STU":
            if d == "IN":
                stu += num
            else:
                stu -= num
        elif t == "FAC":
            if d == "IN":
                fac += num
            else:
                fac -= num
        else:
            if d == "IN":
                vis += num
            else:
                vis -= num

    tot = stu + fac + vis
    if tot == 0:
        print("NO STRAGGLERS")
    else:
        print(tot)


if __name__ == "__main__":
    main()
