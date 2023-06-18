from collections import deque


def main():
    Q = int(input())
    queue = {'A': deque(), 'B': deque()}
    for _ in range(Q):
        queries = input().split()
        if queries[0] == "add":
            queue[queries[1]].append(queries[2])
        elif queries[0] == "delete":
            queue[queries[1]].remove(queries[2])
        elif queries[0] == "find":
            case = 0
            for a in queue['A']:
                for b in queue['B']:
                    if a + b == queries[1]:
                        case += 1
            print(case)


if __name__ == "__main__":
    main()
