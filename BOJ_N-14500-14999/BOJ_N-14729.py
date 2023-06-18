def main():
    N = int(input())
    score = [float(input()) for _ in range(N)]
    score.sort()
    for i in range(7):
        print("{:0.3f}".format(score[i]))

# import sys
# z=sys.stdin.readline
# x=[100 for i in range(7)]
# a=int(z())
# for i in range(a):
#     t=float(z())
#     if x[6]>t:del x[6];x.append(t);x.sort()
# for i in range(7):print("{:.3f}".format(x[i]))


if __name__ == "__main__":
    main()
