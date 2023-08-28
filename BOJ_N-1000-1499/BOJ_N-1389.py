from collections import deque


def main():
    N, M = map(int, input().split())
    rels = {n: [] for n in range(1, N + 1)}

    for _ in range(M):
        A, B = map(int, input().split())
        rels[A].append(B)
        rels[B].append(A)

    bacon = []
    for num, rel in rels.items():
        nums = [0] * (N + 1)
        visited = [False] * (N + 1)
        queue = deque([num])
        while queue:
            currStu = queue.popleft()
            for student in rels[currStu]:
                if not visited[student]:
                    queue.append(student)
                    visited[student] = True
                    nums[student] = nums[currStu] + 1
        bacon.append(sum(nums))

    print(bacon.index(min(bacon)) + 1)


if __name__ == "__main__":
    main()
