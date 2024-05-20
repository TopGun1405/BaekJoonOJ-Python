from collections import deque


def main():
    N = int(input())
    cycled = []
    for _ in range(N):
        word = deque(input())
        for w in cycled:
            if "".join(word) in w:
                break
        else:
            words = []
            for _ in range(len(word)):
                word.rotate(1)
                words.append("".join(word))
            cycled.append(words)
        continue
    print(len(cycled))


if __name__ == "__main__":
    main()
