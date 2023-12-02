from collections import deque


def main():
    N = int(input())
    router = deque()

    while True:
        info = int(input())

        if info == -1:
            break
        elif info == 0:
            router.popleft()
        else:
            if len(router) < N:
                router.append(info)

    print(" ".join(map(str, router)) if router else "empty")


if __name__ == "__main__":
    main()
