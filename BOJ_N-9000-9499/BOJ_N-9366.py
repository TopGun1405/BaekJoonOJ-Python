def main():
    T = int(input())
    for i in range(T):
        tri = sorted(map(int, input().split()))
        print("Case #{}: ".format(i + 1), end='')
        print("invalid!" if tri[2] >= tri[1] + tri[0]
              else ("equilateral" if tri[2] == tri[1] == tri[0]
                    else ("isosceles" if tri[2] == tri[1] or tri[1] == tri[0] or tri[0] == tri[2]
                          else "scalene")))


if __name__ == "__main__":
    main()
