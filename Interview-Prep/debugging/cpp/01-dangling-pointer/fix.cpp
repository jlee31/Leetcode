// FIX: return by value, not by reference to a local.
//   g++ -std=c++17 -Wall -Wextra -g fix.cpp -o fix && ./fix
#include <iostream>
#include <string>

// `message` is a local; it's destroyed when greeting() returns. Returning a
// reference to it leaves a dangling reference -> undefined behavior.
// Returning by value is correct AND cheap: the compiler elides the copy (NRVO)
// or moves the string out.
std::string greeting(const std::string& name) {
    std::string message = "Hello, " + name + "!";
    return message;
}

int main() {
    std::string g = greeting("Joseph");
    std::cout << g << "\n";   // Hello, Joseph!
    return 0;
}
