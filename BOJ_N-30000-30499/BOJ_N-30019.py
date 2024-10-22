def main():
    N, M = map(int, input().split())

    room = {}
    for _ in range(M):
        k_i, s_i, e_i = map(int, input().split())

        if k_i not in room:
            room[k_i] = [s_i, e_i]
            print("YES")

        else:
            if room[k_i][1] > s_i:
                print("NO")
            else:
                room[k_i] = [s_i, e_i]
                print("YES")


if __name__ == "__main__":
    main()
