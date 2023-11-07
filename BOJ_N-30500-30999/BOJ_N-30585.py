def main():
    h, w = map(int, input().split())
    up, down = 0, 0
    for _ in range(h):
        bubble = input()
        for s in bubble:
            if s == '1':
                up += 1
            else:
                down += 1
    print(min(up, down))


if __name__ == "__main__":
    main()
