// FIX: half-open range [0, n) — stop at n-1.
//   g++ -std=c++17 -g -fsanitize=address,undefined fix.cpp -o fix && ./fix
#include <iostream>

int sumArray(const int* a, int n) {
    int sum = 0;
    for (int i = 0; i < n; ++i)   // was: i <= n
        sum += a[i];
    return sum;
}

int main() {
    int data[5] = {1, 2, 3, 4, 5};
    std::cout << "sum = " << sumArray(data, 5) << "\n";  // 15
    return 0;
}

// Takeaway: prefer range-based loops when you can — `for (int x : data)` can't
// run off the end. When you must index, the half-open `[0, n)` convention
// (`i < n`) is the safe default.
