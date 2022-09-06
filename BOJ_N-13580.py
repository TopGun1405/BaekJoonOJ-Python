def main():
    trv = sorted(map(int, input().split()))
    if trv[0] == trv[1] or trv[1] == trv[2]:
        print('S')
    elif trv[0] + trv[1] == trv[2]:
        print('S')
    else:
        print('N')


if __name__ == "__main__":
    main()
