// UniquePtr — fill in the TODOs.
//   g++ -std=c++17 -Wall -Wextra -g starter.cpp -o starter && ./starter
#include <iostream>
#include <utility>

template <typename T>
class UniquePtr {
public:
    // TODO: explicit UniquePtr(T* p = nullptr)
    // TODO: ~UniquePtr()
    // TODO: delete copy ctor + copy assignment
    // TODO: move ctor (steal ptr, null out source)
    // TODO: move assignment (free current, steal, null out source)
    // TODO: T& operator*() const
    // TODO: T* operator->() const
    // TODO: T* get() const
    // TODO: T* release()
    // TODO: void reset(T* p = nullptr)
    // TODO: explicit operator bool() const

private:
    T* ptr_ = nullptr;
};

struct Widget {
    int id;
    explicit Widget(int i) : id(i) { std::cout << "Widget " << id << " ctor\n"; }
    ~Widget() { std::cout << "Widget " << id << " dtor\n"; }
};

int main() {
    UniquePtr<Widget> a{new Widget(1)};
    std::cout << "a->id = " << a->id << "\n";

    UniquePtr<Widget> b = std::move(a);   // ownership moves to b
    std::cout << "after move, a is " << (a ? "non-null" : "null") << "\n";
    std::cout << "b->id = " << b->id << "\n";
    // Widget 1 should be destroyed exactly once, at scope exit.
    return 0;
}
