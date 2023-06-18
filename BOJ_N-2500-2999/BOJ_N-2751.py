def main():
    N = int(input())
    num = [int(input()) for _ in range(N)]

    # Time Complexity : O(n^2)
    # selection sort, bubble sort, improvement_bubble_sort, insertion_sort
    # Time Complexity : O(nlog(n))
    # merge_sort, quick_sort, heap_sort

    ##############
    # solution 1 #
    ##############

    # pypy3
    # merge_sort(num, 0, N - 1)
    # print(*num, end='\n')

    ##############
    # solution 2 #
    ##############

    print(*sorted(num), sep='\n')

    ##############
    # solution 3 #
    ##############

    quick_sort()

    ##############
    # solution 4 #
    ##############


def merge_sort(s, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(s, low, mid)
        merge_sort(s, mid + 1, high)
        merge(s, low, mid, high)


def merge(s, low, mid, high):
    tmp = [0] * (high - low + 1)
    i, j, t = low, mid + 1, 0
    while i <= mid and j <= high:
        if s[i] <= s[j]:
            tmp[t] = s[i]
            t, i = t + 1, i + 1
        else:
            tmp[t] = s[j]
            t, j = t + 1, j + 1
    while True:
        if i <= mid:
            tmp[t] = s[i]
            t, i = t + 1, i + 1
        elif j <= high:
            tmp[t] = s[j]
            t, j = t + 1, j + 1
        else:
            break
    i, t = low, 0
    while i <= high:
        s[i] = tmp[t]
        i, t = i + 1, t + 1


def quick_sort(s, ):
    pass


def partition(s, ):
    pass


def heap_sort():
    pass


def build_heap(s, ):
    pass


def heapify(s, ):
    pass


if __name__ == "__main__":
    main()
