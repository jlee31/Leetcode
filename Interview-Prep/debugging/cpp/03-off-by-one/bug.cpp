// BUG: this reads/writes one past the end of the array. Find it.
//   g++ -std=c++17 -g -fsanitize=address,undefined bug.cpp -o bug && ./bug
#include <iostream>

int sumArray(const int* a, int n) {
    int sum = 0;
    for (int i = 0; i <= n; ++i)   // <-- look very closely at the condition
        sum += a[i];
    return sum;
}

int main() {
    int data[5] = {1, 2, 3, 4, 5};
    std::cout << "sum = " << sumArray(data, 5) << "\n";  // expects 15
    return 0;
}
