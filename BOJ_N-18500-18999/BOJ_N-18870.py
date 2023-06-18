def main():
    # 만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면,
    # 모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다.
    N = int(input())
    coord = list(map(int, input().split()))
    rank = sorted(set(coord))
    dic = {rank[i]: i for i in range(len(rank))}

    for i in coord:
        print(dic[i], end=' ')


if __name__ == "__main__":
    main()
