def make_pi(dPoint):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(dPoint):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


def main():
    my_array = []

    for i in make_pi(1_000):
        my_array.append(str(i))

    # my_array = my_array[:1] + ['.'] + my_array[1:]
    big_string = "".join(my_array)
    print("here is a big string:\n %s" % big_string)
    # N = int(input())
    # for _ in range(N):
    #     # Q >= P이고 π의 Q번째 자리가 D인 최소 자리 Q
    #     # R > Q이고 π의 R번째 자리가 5인 최소 자리 R
    #     P, D = map(int, input().split())


if __name__ == "__main__":
    main()
