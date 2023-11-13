def main():
    father = input().split()
    mother = input().split()

    child = []
    for c1 in set(father + mother):
        for c2 in set(father + mother):
            child.append(' '.join([c1, c2]))
    print(*sorted(child), sep='\n')


if __name__ == "__main__":
    main()
