from collections import deque


def main():

    def death_game():
        queue = deque([0])
        M = 0
        for _ in range(N):
            num = queue.popleft()
            M += 1
            if nums[num] == K:
                return M
            queue.append(nums[num])
        return -1

    N, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    print(death_game())


if __name__ == "__main__":
    main()
