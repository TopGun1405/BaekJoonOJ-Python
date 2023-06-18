def main():
    N = int(input())
    H = list(map(int, input().split()))
    push, Hi = 1, H[0]
    for h in H[1:]:
        if h >= Hi:
            push += 1
        Hi = h
    print(push)


if __name__ == "__main__":
    main()
