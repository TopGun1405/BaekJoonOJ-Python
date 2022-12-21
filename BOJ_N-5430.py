from collections import deque


def main():
    T = int(input())
    for _ in range(T):
        p = list(input())
        n = int(input())
        if n == 0:
            num = deque(input()[1:-1])
        else:
            num = deque(map(int, input()[1:-1].split(',')))

        cmdR = 0
        for c in p:
            if c == 'R':
                cmdR = (cmdR + 1) % 2
            elif c == 'D':
                if not num:
                    print("error")
                    break
                elif cmdR == 1:
                    num.pop()
                elif cmdR == 0:
                    num.popleft()
        else:
            if cmdR == 1:
                num.reverse()
            print('[' + ','.join(map(str, num)) + ']')


if __name__ == "__main__":
    main()
