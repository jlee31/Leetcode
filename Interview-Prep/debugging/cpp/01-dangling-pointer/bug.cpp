// BUG: this program prints garbage (or crashes). Find out why.
//   g++ -std=c++17 -Wall -Wextra -g bug.cpp -o bug && ./bug
// Hint: build with -fsanitize=address and read the report.
#include <iostream>
#include <string>

const std::string& greeting(const std::string& name) {
    std::string message = "Hello, " + name + "!";
    return message;   // <-- returns a reference to WHAT, exactly?
}

int main() {
    const std::string& g = greeting("Joseph");
    std::cout << g << "\n";
    return 0;
}
