from collections import deque


def main():
    N = int(input())
    students = deque(map(int, input().split()))
    stack, idx = [], 1
    while students:
        if students and students[0] == idx:
            idx += 1
            students.popleft()
        else:
            stack.append(students.popleft())

        while stack and stack[-1] == idx:
            idx += 1
            stack.pop()

    print(["Sad", "Nice"][not stack])


if __name__ == "__main__":
    main()
