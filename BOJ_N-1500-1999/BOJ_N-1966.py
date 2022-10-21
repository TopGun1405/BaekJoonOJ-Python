from collections import deque


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        imp = list(map(int, input().split()))

        for i in range(len(imp)):
            imp[i] = [i, imp[i]]
        sorted_imp = sorted(imp, key=lambda k: k[1])
        imp = deque(imp)

        t = 1
        while True:
            if imp[0][0] == M and imp[0][1] == sorted_imp[-1][1]:
                print(t)
                break
            elif imp[0][1] < sorted_imp[-1][1]:
                imp.append(imp.popleft())
            elif imp[0][1] == sorted_imp[-1][1]:
                sorted_imp.pop()
                imp.popleft()
                t += 1


if __name__ == "__main__":
    main()
