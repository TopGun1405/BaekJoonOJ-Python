# C++
# #include "aplusb.h"
# #include <vector>
#
# std::vector<int> A_global;
# std::vector<int> B_global;
#
# void initialize(std::vector<int> A, std::vector<int> B) {
#     A_global = A;
#     B_global = B;
# }
#
# int answer_question(int i, int j) {
#     return A_global[i] + B_global[j];
# }

A_global = []
B_global = []


def initialize(A, B):
    global A_global, B_global
    A_global = A
    B_global = B


def answer_question(i, j):
    return A_global[i] + B_global[j]


def main():
    pass


if __name__ == "__main__":
    main()
