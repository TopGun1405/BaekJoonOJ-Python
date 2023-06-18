def main():
    A = input()
    B = input()
    alp = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2,
           'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2, 'N': 2,
           'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1,
           'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}
    score = []
    # PyPy3
    a, b = 0, 0
    while a < len(A) and b < len(B):
        if a < len(A):
            score.append(alp[A[a]])
            a += 1
        if b < len(B):
            score.append(alp[B[b]])
            b += 1
    while len(score) > 2:
        for _ in range(len(score) - 1):
            score.append((score[1] + score.pop(0)) % 10)
        else:
            del score[0]
    print(''.join(map(str, score)))

    # A = list(input())
    # B = list(input())
    # C = []
    # cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    # minus = ord('A') - 1
    # length = len(A)
    # for i in range(length):
    #     C.append(cnt[ord(A[i]) - minus - 1])
    #     C.append(cnt[ord(B[i]) - minus - 1])
    # length *= 2
    # times = length
    # for i in range(times - 2):
    #     for j in range(length - 1):
    #         C[j] = (C[j] + C[j + 1]) % 10
    #     length -= 1
    # result = 10 * C[0] + C[1]
    # print("%02d" % result)


if __name__ == "__main__":
    main()
