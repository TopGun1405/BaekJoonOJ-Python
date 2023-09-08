def main():
    N = int(input())
    balls = sorted(map(int, input().split()))
    # print(sum(map(lambda n: n[1] - n[0], zip(balls[:-1], balls[1:]))) + balls[-1] - balls[0])
    print(2 * (max(balls) - min(balls)))


if __name__ == "__main__":
    main()
