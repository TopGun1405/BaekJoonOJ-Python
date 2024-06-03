import math


def main():
    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def angle(v1, v2):
        dot_prod = sum(v1[i] * v2[i] for i in range(2))
        mag_v1 = math.sqrt(sum(v1[i]**2 for i in range(2)))
        mag_v2 = math.sqrt(sum(v2[i]**2 for i in range(2)))
        return math.acos(dot_prod / (mag_v1 * mag_v2))

    def triangle(p1, p2, p3):
        v1 = (p2[0]-p1[0], p2[1]-p1[1])
        v2 = (p3[0]-p2[0], p3[1]-p2[1])
        v3 = (p1[0]-p3[0], p1[1]-p3[1])

        angle1 = angle(v1, (-v3[0], -v3[1]))
        angle2 = angle(v2, (-v1[0], -v1[1]))
        angle3 = angle(v3, (-v2[0], -v2[1]))

        angles = [angle1, angle2, angle3]

        if any(math.isclose(a_n, math.pi/2, rel_tol=1e-9) for a_n in angles):
            return "Jikkak"
        elif any(a_n > math.pi/2 for a_n in angles):
            return "Dunkak"
        else:
            return "Yeahkak"

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    d1 = distance(A, B)
    d2 = distance(B, C)
    d3 = distance(C, A)
    if (B[1]-A[1]) * (C[0]-B[0]) == (B[0]-A[0]) * (C[1]-B[1]):
        print("X")
    elif d1 == d2 == d3:
        print("JungTriangle")
    elif (d1 == d2) or (d2 == d3) or (d3 == d1):
        print(triangle(A, B, C) + "2Triangle")
    else:
        print(triangle(A, B, C) + "Triangle")


if __name__ == "__main__":
    main()
