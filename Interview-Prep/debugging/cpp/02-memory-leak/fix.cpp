// FIX: use RAII (std::vector) so the buffer frees itself on every exit path.
//   g++ -std=c++17 -g -fsanitize=address fix.cpp -o fix && ./fix
#include <iostream>
#include <vector>

bool process(int n) {
    std::vector<int> buf(n > 0 ? n : 0);  // owns its storage

    if (n <= 0) {
        std::cout << "nothing to do\n";
        return false;        // vector's destructor frees memory here — no leak
    }

    for (int i = 0; i < n; ++i) buf[i] = i * i;
    std::cout << "last = " << buf[n - 1] << "\n";
    return true;             // ...and here too. One owner, all paths covered.
}

int main() {
    process(5);
    process(0);
    return 0;
}

// Takeaway: a raw `new` with manual `delete` is fragile — any early return or
// thrown exception between them leaks. RAII containers (vector, unique_ptr,
// string) free in their destructor, which runs on every scope exit.
