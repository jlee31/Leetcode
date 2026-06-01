// BUG: this leaks memory on one of its code paths. Find it.
//   g++ -std=c++17 -g -fsanitize=address bug.cpp -o bug && ./bug
//   (ASan prints a leak report on exit.)
#include <iostream>

int* makeBuffer(int n) {
    return new int[n];   // raw owning pointer — who frees it?
}

bool process(int n) {
    int* buf = makeBuffer(n);

    if (n <= 0) {
        std::cout << "nothing to do\n";
        return false;        // <-- early return: buf is never deleted
    }

    for (int i = 0; i < n; ++i) buf[i] = i * i;
    std::cout << "last = " << buf[n - 1] << "\n";

    delete[] buf;            // only reached on the happy path
    return true;
}

int main() {
    process(5);
    process(0);              // leaks the buffer allocated for n=0
    return 0;
}
