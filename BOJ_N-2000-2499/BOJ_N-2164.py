from collections import deque


def main():
    N = int(input())
    card = deque(range(1, N + 1))

    while len(card) > 1:
        card.popleft()
        card.append(card.popleft())
    print(card[0])


if __name__ == "__main__":
    main()
