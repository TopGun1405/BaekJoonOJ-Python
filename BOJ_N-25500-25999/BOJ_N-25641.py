from collections import deque


def main():
    N = int(input())
    stst = deque(input())
    s = stst.count('s')
    while True:
        if s == len(stst) - s:
            break
        else:
            st = stst.popleft()
            s = s - 1 if st == 's' else s
    print(''.join(stst))


if __name__ == "__main__":
    main()
