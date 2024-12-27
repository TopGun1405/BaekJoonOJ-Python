def main():
    b, d, c, l = map(int, input().split())

    cnt = 0
    for b_i in range(l//b+1):
        for d_i in range(l//d+1):
            for c_i in range(l//c+1):
                if b_i*b + d_i*d + c_i*c > l:
                    break
                if b_i*b + d_i*d + c_i*c == l:
                    cnt += 1
                    print(b_i, d_i, c_i)

    if cnt == 0:
        print("impossible")


if __name__ == "__main__":
    main()
