// UniquePtr — reference solution.
//   g++ -std=c++17 -Wall -Wextra -g solution.cpp -o solution && ./solution
//   Verify no leaks/double-free:
//   g++ -std=c++17 -g -fsanitize=address,undefined solution.cpp -o sol && ./sol
#include <iostream>
#include <utility>

template <typename T>
class UniquePtr {
public:
    explicit UniquePtr(T* p = nullptr) noexcept : ptr_(p) {}

    ~UniquePtr() { delete ptr_; }

    // Non-copyable: two owners would each delete the same pointer.
    UniquePtr(const UniquePtr&) = delete;
    UniquePtr& operator=(const UniquePtr&) = delete;

    // Movable: transfer ownership, leave source empty.
    UniquePtr(UniquePtr&& other) noexcept : ptr_(other.ptr_) {
        other.ptr_ = nullptr;
    }
    UniquePtr& operator=(UniquePtr&& other) noexcept {
        if (this != &other) {
            delete ptr_;              // free what we currently own
            ptr_ = other.ptr_;        // steal
            other.ptr_ = nullptr;     // source must not also delete it
        }
        return *this;
    }

    T& operator*() const { return *ptr_; }
    T* operator->() const { return ptr_; }
    T* get() const { return ptr_; }

    // Give up ownership without deleting; caller is now responsible.
    T* release() {
        T* tmp = ptr_;
        ptr_ = nullptr;
        return tmp;
    }

    // Replace the owned object, deleting the old one.
    void reset(T* p = nullptr) {
        delete ptr_;
        ptr_ = p;
    }

    // explicit: prevents surprising conversions like `int x = myPtr;`
    explicit operator bool() const { return ptr_ != nullptr; }

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

    UniquePtr<Widget> b = std::move(a);
    std::cout << "after move, a is " << (a ? "non-null" : "null") << "\n";
    std::cout << "b->id = " << b->id << "\n";
    return 0;
}

// Notes:
// - Rule of Five: dtor, copy ctor (=delete), copy assign (=delete),
//   move ctor, move assign. Declaring any of them suppresses implicit moves,
//   so for a resource-owning type you spell out all five.
// - A moved-from object must be in a valid, destructible state. Here that means
//   ptr_ == nullptr so its destructor's `delete nullptr` is a safe no-op.
// - shared_ptr allows MANY owners via a reference count; unique_ptr allows
//   exactly one and is zero-overhead vs a raw pointer.
