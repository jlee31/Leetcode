// Shape hierarchy — fill in the TODOs.
//   g++ -std=c++17 -Wall -Wextra -g starter.cpp -o starter && ./starter
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Shape {
public:
    // TODO: virtual destructor
    // TODO: pure virtual double area() const
    // TODO: pure virtual std::string name() const
};

// TODO: class Circle : public Shape { ... }
// TODO: class Rectangle : public Shape { ... }

// TODO: double totalArea(const std::vector<std::unique_ptr<Shape>>& shapes)

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    // TODO: shapes.push_back(std::make_unique<Circle>(2.0)); etc.

    // TODO: print each shape's name + area, then total
    return 0;
}
