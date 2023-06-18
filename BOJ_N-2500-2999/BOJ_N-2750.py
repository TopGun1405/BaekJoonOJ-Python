def main():
    N = int(input())
    num_arr = [int(input()) for _ in range(N)]

    # Time Complexity : O(n^2)
    # selection sort, bubble sort, improvement_bubble_sort, insertion_sort
    # Time Complexity : O(nlog(n))
    # merge_sort, quick_sort, heap_sort

    ##############
    # solution 1 #
    ##############

    # num_arr.sort()

    ##############
    # solution 2 #
    ##############

    # insertion_sort(num_arr)

    ##############
    # solution 3 #
    ##############

    # bubble_sort(num_arr)

    ##############
    # solution 4 #
    ##############

    improvement_bubble_sort(num_arr)

    print(*num_arr, sep='\n')


def selection_sort(arr):
    pass


def insertion_sort(arr):
    # from index 1
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    # return arr


def bubble_sort(arr):
    for n in range(len(arr), 1, -1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def improvement_bubble_sort(arr):
    for n in range(len(arr), 1, -1):
        arr_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                arr_sorted = False
        if arr_sorted:
            return


if __name__ == "__main__":
    main()
