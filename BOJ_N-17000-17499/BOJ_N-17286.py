from itertools import permutations


def main():
    def distance(pos1, pos2):
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

    yu_x, yu_y = map(int, input().split())
    pos = [list(map(int, input().split())) for _ in range(3)]

    minDis = int(1e9)
    for pos_i in map(list, permutations(pos)):
        dis = distance([yu_x, yu_y], pos_i[0])
        dis += distance(pos_i[0], pos_i[1])
        dis += distance(pos_i[1], pos_i[2])
        minDis = min(minDis, dis)

    print(int(minDis))


if __name__ == "__main__":
    main()
