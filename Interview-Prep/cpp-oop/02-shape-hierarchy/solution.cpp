// Shape hierarchy — reference solution.
//   g++ -std=c++17 -Wall -Wextra -g solution.cpp -o solution && ./solution
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Shape {
public:
    virtual ~Shape() = default;            // virtual: safe delete via Shape*
    virtual double area() const = 0;       // pure virtual -> abstract class
    virtual std::string name() const = 0;
};

class Circle : public Shape {
public:
    explicit Circle(double radius) : radius_(radius) {}
    double area() const override { return 3.14159265358979 * radius_ * radius_; }
    std::string name() const override { return "Circle"; }
private:
    double radius_;
};

class Rectangle : public Shape {
public:
    Rectangle(double width, double height) : w_(width), h_(height) {}
    double area() const override { return w_ * h_; }
    std::string name() const override { return "Rectangle"; }
private:
    double w_, h_;
};

double totalArea(const std::vector<std::unique_ptr<Shape>>& shapes) {
    double sum = 0.0;
    for (const auto& s : shapes) sum += s->area();  // virtual dispatch
    return sum;
}

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(2.0));
    shapes.push_back(std::make_unique<Rectangle>(3.0, 4.0));

    for (const auto& s : shapes)
        std::cout << s->name() << " area = " << s->area() << "\n";
    std::cout << "Total area = " << totalArea(shapes) << "\n";
    return 0;
}

// Notes:
// - Without `virtual ~Shape()`, `delete shapePtr;` (where shapePtr is Shape*
//   pointing at a Circle) only runs ~Shape(), not ~Circle() => UB / leaks.
// - Storing Shape by value in the vector would SLICE: only the Shape part is
//   copied and virtual dispatch is lost. unique_ptr keeps the dynamic type.
// - totalArea never changed when we conceptually add a Triangle: it depends
//   only on the Shape interface (Open/Closed Principle).
