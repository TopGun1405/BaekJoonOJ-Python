from collections import deque


def main():
    N = int(input())
    pizza = deque(map(list, enumerate(map(int, input().split()))))
    times = [0 for _ in range(N)]
    timer = 0
    while pizza:
        p = pizza.popleft()
        p[1], timer = p[1] - 1, timer + 1
        if p[1] != 0:
            pizza.append(p)
        else:
            times[p[0]] = timer
    print(*times)


if __name__ == "__main__":
    main()
